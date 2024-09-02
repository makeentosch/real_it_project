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

