# Define a list of cybersecurity trivia questions and answers.
questions = [
    {
        "question": "What does 'HTTPS' stand for?",
        "options": ["HyperText Transfer Protocol Secure", "Highly Technical Encryption Protocol for Security", "Home to Email Transfer System"],
        "correct_answer": 0,
    },
    {
        "question": "Which of the following is not a common type of malware?",
        "options": ["Virus", "Firewall", "Trojan", "Worm"],
        "correct_answer": 1,
    },
    {
        "question": "What is the primary purpose of a firewall?",
        "options": ["To prevent unauthorized access to or from a private network", "To speed up internet connection", "To encrypt data during transmission"],
        "correct_answer": 0,
    },
]

# Function to present a question and check the answer.
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    user_answer = int(input("Enter the number of your answer: ")) - 1

    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print("Incorrect. The correct answer is: " + options[correct_answer] + "\n")
        return False

# Main trivia game loop.
score = 0
for question in questions:
    if ask_question(question["question"], question["options"], question["correct_answer"]):
        score += 1

print(f"You scored {score}/{len(questions)}. Thanks for playing!")
