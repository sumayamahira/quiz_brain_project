from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(text=item["question"], answer=item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.new_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
