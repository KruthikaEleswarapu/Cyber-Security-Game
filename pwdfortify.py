import tkinter as tk
import string

# Function to check the strength of a password and provide best practice guidelines
def check_password_strength():
    password = password_entry.get()
    score = 0
    feedback = []

    # Check for lowercase characters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Check for uppercase characters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add digits")

    # Check for special characters
    if any(char in "!@#$%^&*()_+=-[]{}|:;<>,.?/~" for char in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Check the overall score and provide feedback
    if score == 1:
        strength_label.config(text=f"Strength: Weak - {', '.join(feedback)}")
    elif score == 2:
        strength_label.config(text=f"Strength: Moderate - {', '.join(feedback)}")
    elif score >= 3:
        strength_label.config(text="Strength: Strong")
    else:
        strength_label.config(text="Strength: N/A")

    # Display best practice guidelines
    best_practice_label.config(text="Best Practice: A strong password should be at least 12 characters long and include a mix of lowercase and uppercase letters, digits, and special characters.")

# Create the main window
root = tk.Tk()
root.title("Password fortifier")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="PASSWORD FORTIFIER", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
title_label.pack(pady=20)

# Create an entry for password input
password_label = tk.Label(root, text="Enter Password:", font=("Helvetica", 12))
password_label.pack(pady=20)
password_entry = tk.Entry(root, font=("Helvetica", 12))
password_entry.pack()

# Create a button to check password strength
check_button = tk.Button(root, text="Check Strength", font=("Helvetica", 12), command=check_password_strength)
check_button.pack(pady=20)

# Create a label to display password strength
strength_label = tk.Label(root, text="Strength: N/A", font=("Helvetica", 14))
strength_label.pack()

# Create a label to display best practice guidelines
best_practice_label = tk.Label(root, text="Best Practice: A strong password should be at least 12 characters long and include a mix of lowercase and uppercase letters, digits, and special characters.", font=("Helvetica", 12))
best_practice_label.pack(pady=20)

# Start the GUI main loop
root.mainloop()
