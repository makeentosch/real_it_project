from dialog_context import *
from extract_keywords import *
from extract_question_info import *
from get_prompt import *

if __name__ == "__main__":
    question = input("Задайте вопрос (для завершения введите дефис): ")  # "Здравствуйте! Есть ли у вас филиал в Екатеринбурге?"
    while question != "-":
        make_question(question)
        keywords = extract_keywords(question)

        # Выясняем город
        city = get_city(keywords)
        if city is None:
            make_answer("Выясни город. Уведоми, что школа представлена в Екатеринбурге, Перьми, Тюмени и Первоуральске")
            question = input("Задайте вопрос (для завершения введите дефис): ")
            continue

        # Предметы и сути вопросов
        subjects = {
            "курс": {
                "наличие": False,
                "периодичность": False,
                "формат": False,
                "цена": False,
                "длительность": False
            },
            "филиал": {
                "наличие": False,
                "адрес": False
            },
            "абонемент": {
                "наличие": False,
                "цена": False
            }
        }

        # Определяем предмет и суть вопроса
        question_subject = get_question_subject(keywords)
        question_essence = get_question_essence(keywords, subjects, question_subject)
        print(question_subject, question_essence)
        print(context)

        data = tuple()

        match question_subject:
            case "курс":
                match question_essence:
                    case "наличие":
                        if answer_about_course_availability(keywords):
                            make_prompt("Сообщи клиент, что курс имеется")
                        else:
                            make_prompt("Сообщи клиенту, что такого курса нет")
                    case "цена":
                        data = []
                        prices = answer_about_course_price(keywords, city)
                        for price in prices:
                            data.append(f"{price[0]}, полная цена: {price[1]}, цена за одно занятие: {price[2]}")
                        make_prompt(data)
                    case "периодичность":
                        data = answer_about_course_periodicity(city)
                        if data is None:
                            make_prompt("Нет информации. Переведи клиента на оператора")
                        else:
                            make_prompt(data)
                    case "формат":
                        data = answer_about_course_format(city)
                        if data is None:
                            make_prompt("Нет информации. Переведи клиента на оператора")
                        else:
                            make_prompt(data)

            # case "лагерь":
            #   pass

            case "филиал":
                match question_essence:
                    case "наличие":
                        flag = True
                        data = get_branches_info(city)
                        for word in keywords:
                            for branch in data:
                                if word in branch:
                                    make_prompt("Сообщи клиенту, что филиал по данному адресу имеется")
                                    flag = False
                        if flag:
                            make_prompt("Сообщи клиенту, что филиала по данному адресу нет")

            case "абонемент":
                pass

            case _:
                make_prompt("Нет информации. Переведи клиента на оператора")

        question = input("Задайте вопрос (для завершения введите дефис): ")