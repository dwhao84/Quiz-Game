from main import question


class Quiz_brain:
    # TODO: Asking the questions
    def __init__(self, question_number, question_list):
        self.question_number = 0

    # TODO: Checking if the answer was correct
    def check_answer(self):
        print("Active the check answer")

    # TODO: Checking if we're the end of the quiz.
    def next_question(self, question_number):
        question_number += 1
        print(question_number)