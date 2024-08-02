import random

# Function to present a social engineering scenario.
def social_engineering_scenario():
    scenarios = [
        {
            "scenario": "You receive a phone call from someone claiming to be from your bank. They ask for your account number and password to verify your identity. What do you do?",
            "choices": ["Provide the information", "Hang up and call your bank's official number"],
            "correct_choice": 1,
            "response": "You made the right choice. It's important not to give sensitive information over the phone. Hang up and call your bank's official number."
        },
        {
            "scenario": "You receive an email with a link that claims to be from a friend. The link asks you to download an attachment. What do you do?",
            "choices": ["Click the link and download the attachment", "Contact your friend to verify the email"],
            "correct_choice": 2,
            "response": "Good job! Always verify unexpected emails or links with the sender before taking any action to prevent malware or phishing attempts."
        }
    ]

    scenario = random.choice(scenarios)
    print(scenario["scenario"])
    for i, choice in enumerate(scenario["choices"], start=1):
        print(f"{i}. {choice}")

    choice = int(input("Enter the number of your choice: "))

    if choice == scenario["correct_choice"]:
        print(scenario["response"])
    else:
        print("That's not the best choice. Remember to stay cautious and verify before sharing information.")

# Main game loop.
while True:
    social_engineering_scenario()
    play_again = input("Play another scenario? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
