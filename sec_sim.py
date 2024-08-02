# Define a list of security scenarios.
security_scenarios = [
    {
        "scenario": "You notice a suspicious email in your inbox with an attachment. What do you do?",
        "options": [
            "Open the attachment to see what it contains",
            "Delete the email immediately",
            "Forward the email to your IT department for analysis",
        ],
        "correct_option": 2,
        "response": "Good choice! You forwarded the email to your IT department for analysis, which is the right thing to do to prevent potential malware.",
    },
    {
        "scenario": "You receive a call from someone claiming to be from your bank asking for your account information. What's your response?",
        "options": [
            "Provide the requested information",
            "Hang up and call your bank's official number to verify the call",
            "Engage in a lengthy conversation to gather more information about the caller",
        ],
        "correct_option": 2,
        "response": "Excellent! You hung up and called your bank's official number to verify the call, avoiding a potential phishing attempt.",
    },
    {
        "scenario": "You receive an email from a coworker with a link to a website. What's your next step?",
        "options": [
            "Click the link without hesitation",
            "Hover over the link to inspect the URL before clicking",
            "Delete the email and report it as spam",
        ],
        "correct_option": 2,
        "response": "Smart move! You hovered over the link to inspect the URL, ensuring it's not a phishing attempt.",
    },
]

# Function to present a security scenario and get the user's response.
def simulate_security_scenario(scenario, options, correct_option):
    print(scenario)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_choice = int(input("Enter the number of your choice: "))

    if user_choice == correct_option:
        print("Correct! ")
        return True
    else:
        print("Incorrect. The correct response is: " + options[correct_option - 1])
        return False

# Main security challenge loop.
score = 0
for scenario in security_scenarios:
    if simulate_security_scenario(scenario["scenario"], scenario["options"], scenario["correct_option"]):
        score += 1

print("You scored {}/{} in the security simulation challenges. Great job!".format(score, len(security_scenarios)))
