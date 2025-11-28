from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(text=item["question"], answer= item["correct_answer"])
    question_bank.append(question)











brain = QuizBrain(question_bank)

first_question = brain.next_question()
print(first_question)

