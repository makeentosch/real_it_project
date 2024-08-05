import sqlite3

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


def get_question_subject(question):
    # Вспомогательный словарь с ключевыми словами
    subjects_kw = {
      "курс": ["курс", "обучение", "занятие", "урок"],
      "филиал": ["адрес", "расположение", "находиться", "располагаться", "филиал"],
      "абонемент": ["абонемент", "скидка"]
    }

    for word in question:
        for key, value in subjects_kw.items():
            if word in value:
                return key
    return None


def get_question_essence(question, subjects, question_subject):
    # Вспомогательный словарь с ключевыми словами
    essence_kw = {
      "наличие": ["есть", "иметься", "присутствовать"],
      "цена": ["стоить", "цена", "прайс", "рубль", "стоимость", "оплата", "платить", "оплатить"],
      "формат": ["форма", "очно", "онлайн", "дистант", "дистанционный"],
      "периодичность": ["периодичность", "раз", "неделя"],
      "адрес": ["адрес", "расположение", "находиться", "располагаться"]
    }

    for word in question:
        for key, value in essence_kw.items():
            if word in value and key in subjects[question_subject].keys():
                subjects[question_subject][key] = True
                return key
    return None

