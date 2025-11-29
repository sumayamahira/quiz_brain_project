from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank_easy = []
question_bank_medium = []
question_bank_hard = []

for item in question_data:
    question = Question(text=item["question"], answer=item["correct_answer"], difficulty=item["difficulty"])
    if question.difficulty == "easy":
        question_bank_easy.append(question)

    elif question.difficulty == "medium":
        question_bank_medium.append(question)

    elif question.difficulty == "hard":
        question_bank_hard.append(question)

    else:
        pass

while True:

    difficulty_level = input("Which Type of difficulty level you may like? \nEasy | Medium | Hard: ").strip().lower()

    if difficulty_level == "easy":
        quiz = QuizBrain(question_bank_easy)
        print(f"There will be {len(question_bank_easy)} questions.")

    elif difficulty_level == "medium":
        quiz = QuizBrain(question_bank_medium)
        print(f"There will be {len(question_bank_medium)} questions.")

    elif difficulty_level == "hard":
        quiz = QuizBrain(question_bank_hard)
        print(f"There will be {len(question_bank_hard)} questions.")

    else:
        print("Type the difficulty level properly as mentioned.")
        continue

    while quiz.still_has_question():
        quiz.new_question()

    print("You have completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number} \n\n")

