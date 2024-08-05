from dialog_context import *
from extract_keywords import *
from extract_question_info import *

if __name__ == "__main__":
    # Получение вопроса от клиента
    question = "Здравствуйте! Есть ли у вас филиал в Екатеринбурге?"
    make_question(question)
    keywords = extract_keywords(question)

    # Выясняем город
    city = get_city(keywords)
    if city is None:
        make_answer("Укажите, пожалуйста, из какого вы города? Наша школа представлена в Екатеринбурге, Перьми, Тюмени и Первоуральске")

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
