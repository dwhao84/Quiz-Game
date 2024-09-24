from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    question_text = question["text"]     # 找到 question["text"]的dict
    question_answer = question["answer"] # 找到 question["answer"]的dict
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
    
print(question_bank)

