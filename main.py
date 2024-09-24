from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]     # 找到 question["text"]的value，從dict裡面找
    question_answer = question["answer"] # 找到 question["answer"]的value，從dict裡面找
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
    
# 命名一個叫quiz的變數，用來找到QuizBrain裡面的question_bank。
quiz = QuizBrain(question_bank)
quiz.next_question()

# 當仍然繼續問答時，產生下一個問答題。
while quiz.still_has_questions():
    quiz.next_question()

# 印出 答題分數、總共達了幾題。
print("You've completed the quiz")
print(f"Your final score was { quiz.score } / { quiz.question_bank }")