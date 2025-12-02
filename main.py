from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question banks by difficulty
question_banks = {
    "easy": [],
    "medium": [],
    "hard": []
}

# Create Question objects and sort them into the banks
for item in question_data:
    difficulty = item["difficulty"].lower()
    if difficulty in question_banks:
        question = Question(
            text=item["question"],
            answer=item["correct_answer"],
            difficulty=difficulty
        )
        question_banks[difficulty].append(question)

# Main quiz loop
while True:
    difficulty_level = input(
        "\nWhich difficulty level would you like?\n"
        "[ Easy | Medium | Hard ] or [ Exit to quit ]: "
    ).strip().lower()

    if difficulty_level in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    if difficulty_level not in question_banks:
        print("Please choose a valid difficulty level.")
        continue

    selected_bank = question_banks[difficulty_level]

    if not selected_bank:
        print(f"No questions available for '{difficulty_level}'.")
        continue

    print(f"\nStarting a {difficulty_level.capitalize()} Quiz!")
    print(f"There will be {len(selected_bank)} questions.\n")

    quiz = QuizBrain(selected_bank)

    # Run the quiz
    while quiz.still_has_question():
        quiz.new_question()

    print("\nYou've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")

    # Replay option
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("\nGoodbye!")
        break
