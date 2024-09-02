import sqlite3
from extract_keywords import *

# Подключение к базе данных
conn = sqlite3.connect("real_it.db")
c = conn.cursor()


def get_city(question):
    """Метод, который извлекает информацию о городе, в котором живет клиент
    :param question: вопрос клиента
    :return: None, если город неопределен, и название города, если город
    """
    query = "SELECT DISTINCT City FROM Branches"
    c.execute(query)
    cities = []
    for city in c.fetchall():
        cities.append(city[0].lower())
    for word in question:
        if word in cities:
            return word.capitalize()
    return None


def get_course_info(keyword):
    query = f"SELECT * FROM Courses WHERE Keywords LIKE '%{keyword}%'"
    c.execute(query)
    return c.fetchall()


def get_branches_info(city):
    query = f"SELECT DISTINCT City FROM Branches WHERE City = '{city}'"
    c.execute(query)
    data = c.fetchall()
    data = list(data[0])
    data = data[0].split("; ")
    result = []
    for branch in data:
        result.append(extract_keywords(branch))
    return result


def get_subscription_info(city):
    query = f"SELECT Title, FullPrice, LessonPrice FROM Prices WHERE City = '{city}' AND CourseType = 'Основной'"
    c.execute(query)
    data = c.fetchall()
    return data


def answer_about_course_availability(question):
    data = tuple()
    for word in question:
        temp_data = get_course_info(word)
        if temp_data != []:
            data = temp_data
    if len(data) == 0:
        return False
    return True


def answer_about_course_price(question, city):
    data = tuple()
    for word in question:
        temp_data = get_subscription_info(city)
        if temp_data != []:
            data = temp_data
            break
    return data


def answer_about_course_periodicity(city):
    query = f"SELECT DISTINCT Periodicity FROM Courses WHERE City = '{city}'"
    c.execute(query)
    data = c.fetchall()[0]
    return data[0]


def answer_about_course_format(city):
    query = f"SELECT DISTINCT Format FROM Courses WHERE City = '{city}'"
    c.execute(query)
    data = c.fetchall()[0]
    return data[0]