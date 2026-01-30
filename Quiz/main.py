import json

def read_file():
    try:
        with open('questions.json', 'r', encoding='utf-8') as file:
            quiz_data = json.load(file)
            print(f"Loaded {len(quiz_data)} questions")
            return quiz_data
    except FileNotFoundError: 
        print("File not loaded!")
    except json.JSONDecodeError:
        print("Error in JSON file! Chek it!")

def main():
    try:
        quiz_data = read_file()
        num_of_questions = len(quiz_data)
        score = 0
        for i, section in enumerate(quiz_data):
            print(f"Question {i + 1} of {num_of_questions}")
            print(f"\n{section['question']}\n")
            for j, option in enumerate(section["options"]):
                print(f"{j + 1}. {option}")
            while True:
                try:
                    user_input = input("\nYour answer (1-4): ")
                    answer = int(user_input) - 1
                    if 0 <= answer < len(section["options"]):
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(section['options'])}")
                except ValueError:
                    print("Please enter a number!")
            correct_answer = section["correctAnswer"]
            if answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {section['options'][correct_answer]}\n")
            if "explanation" in section:
                print(f"{section['explanation']}\n")
        print(f"QUIZ COMPLETED!")
        print(f"Your score: {score}/{num_of_questions}")
        print(f"Percentage: {(score/num_of_questions)*100:.1f}%")
    except KeyboardInterrupt: print("\nThe program completed correctly.")

if __name__ == "__main__":
    main()