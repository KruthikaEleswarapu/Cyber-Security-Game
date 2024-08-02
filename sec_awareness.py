# Define a list of security awareness challenges.
security_challenges = [
    {
        "challenge": "You receive an email with a link from an unknown sender. What do you do?",
        "options": [
            "Click the link without hesitation.",
            "Hover over the link to inspect the URL before clicking.",
            "Delete the email immediately."
        ],
        "correct_option": 1,
        "response": "Well done! Hovering over the link to inspect the URL is a safe practice to avoid phishing attacks."
    },
    {
        "challenge": "You are asked to create a password for an online account. What's a strong password?",
        "options": [
            "123456",
            "password",
            "P@ssw0rd!"
        ],
        "correct_option": 2,
        "response": "Excellent choice! A strong password should include a mix of uppercase, lowercase, numbers, and special characters."
    },
    {
        "challenge": "You receive a call from someone claiming to be a tech support agent. They request access to your computer. What do you do?",
        "options": [
            "Grant them access without question.",
            "Ask for their name and company, then verify their identity.",
            "Hang up immediately."
        ],
        "correct_option": 2,
        "response": "Great decision! Always verify the identity of callers, especially those requesting access to your computer."
    }
]

# Function to present a security awareness challenge and check the response.
def security_awareness_challenge(challenge, options, correct_option, response):
    print(challenge)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    user_choice = int(input("Enter the number of your choice: "))

    if user_choice == correct_option:
        print("Correct! " + response)
        return True
    else:
        print("Incorrect. The correct response is: " + options[correct_option - 1])
        return False

# Main security awareness challenge loop.
score = 0
for challenge in security_challenges:
    if security_awareness_challenge(challenge["challenge"], challenge["options"], challenge["correct_option"], challenge["response"]):
        score += 1

print("You scored {}/{} in the security awareness challenges. Great job!".format(score, len(security_challenges)))
