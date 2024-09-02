context = dict()
question_num = 0
answer_num = 0


def make_answer(prompt):
    global answer_num
    answer_num += 1
    context[f"Ответ {answer_num}"] = prompt
    print(prompt) # Промпт должен поступать на вход нейросети, а она бы сформировала ответ на его основе. Сейчас такой функциональности нет, поэтому возвращаю обычный промпт


def make_question(question):
    global question_num
    question_num += 1
    context[f"Вопрос {question_num}"] = question


def make_prompt(text):
    prompt = "Ты опрератор на сайте школы программирования, общающийся с клиентами. Веди диалог дружелюбно. Проанализируй контекст диалога: " + "\n"
    for key, value in context.items():
        prompt += f"{key} {value}" + "\n"
    prompt += "Сформируй очередной ответ на основе последнего вопроса, используя следующую информацию: " + text
    return make_answer(prompt)
