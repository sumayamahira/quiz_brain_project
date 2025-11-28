class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

        for _ in q_list:
            self.question_number += 1

    def next_question(self):
        import random
        cq = random.choice(self.question_list)
        current_question = cq["question"]
        return current_question

    def next(self):
        import random
        cr = random.choice(self.question_list)
