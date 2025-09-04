def welcome():
    print("="*50)
    print("🎯 Welcome to the Python Quiz App!")
    print("="*50)
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start the quiz...\n")
    return name

def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer == correct_answer
            else:
                print("⚠️ Please enter a number between 1 and 4.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def main():
    name = welcome()

    questions = [
        {
            "question": "Which language is used for web apps?",
            "options": ["Python", "Java", "PHP", "All of the above"],
            "answer": 4
        },
        {
            "question": "Who developed Python?",
            "options": ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"],
            "answer": 2
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Trainer Marking Language", "HyperText Markup Language", "HyperText Marketing Language", "HyperText Mark Language"],
            "answer": 2
        },
        {
            "question": "Which of these is not a programming language?",
            "options": ["Python", "HTML", "Java", "C++"],
            "answer": 2
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".pt", ".pyt", ".py", ".p"],
            "answer": 3
        }
    ]

    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!\n")

    print("="*50)
    print(f"🎉 Quiz Completed! {name}, Your Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You got all questions right.")
    elif score >= len(questions)//2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📘 Keep learning and try again!")
    print("="*50)

if __name__ == "__main__":
    main()
