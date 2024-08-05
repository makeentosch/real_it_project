context = dict()
question_num = 0
answer_num = 0


def make_answer(answer):
    global answer_num
    answer_num += 1
    context[f"Ответ {answer_num}"] = answer


def make_question(question):
    global question_num
    question_num += 1
    context[f"Вопрос {question_num}"] = question


# Нет нейросети для использования этого метода
def make_prompt(text):
    prompt = "Ты опрератор на сайте школы программирования, общающийся с клиентами. Веди диалог дружелюбно. Проанализируй контекст диалога: " + "\n"
    for key, value in context.items():
        prompt += f"{key} {value}" + "\n"
    prompt += "Сформируй очередной ответ на основе последнего вопроса, используя следующую информацию: " + text
    return prompt
