# Define a list of cybersecurity quiz questions and answers.
quiz_questions = [
    {
        "question": "What is the first line of defense against unauthorized access to a computer or network?",
        "options": ["Antivirus software", "Firewall", "Encryption", "Two-Factor Authentication"],
        "correct_answer": 1,
    },
    {
        "question": "What does the term 'Phishing' refer to in cybersecurity?",
        "options": ["A method to prevent data breaches", "A social engineering attack that tricks users into revealing information", "A type of malware", "A network security protocol"],
        "correct_answer": 1,
    },
    {
        "question": "Which of the following is not considered a strong password practice?",
        "options": ["Using a combination of uppercase and lowercase letters", "Using a single-word password", "Incorporating special characters", "Creating a long password"],
        "correct_answer": 1,
    },
]

# Function to present a quiz question and check the answer.
def present_quiz_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    user_answer = int(input("Enter the number of your answer: ") - 1)

    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {options[correct_answer]}\n")
        return 0

# Main quiz loop.
score = 0
for question in quiz_questions:
    score += present_quiz_question(question["question"], question["options"], question["correct_answer"])

print(f"You scored {score}/{len(quiz_questions)}. Thanks for taking the cybersecurity quiz!")
