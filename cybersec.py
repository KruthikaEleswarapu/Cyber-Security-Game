import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [
    {
        "question": "What does 'SSL' stand for?",
        "options": ["Secure Socket Layer", "Super Secure Layer", "Simple Security Layer", "Safe Socket Layer"],
        "correct_answer": "Secure Socket Layer",
    },
    {
        "question": "What is a common method of social engineering?",
        "options": ["Phishing", "Firewall", "Antivirus", "Malware"],
        "correct_answer": "Phishing",
    },
    {
        "question": "Which of the following is a strong password?",
        "options": ["password123", "P@ssw0rd!", "hunter2", "CorrectHorseBatteryStaple"],
        "correct_answer": "CorrectHorseBatteryStaple",
    },
    {
        "question": "What is a firewall used for in cybersecurity?",
        "options": ["Attacking computers", "Filtering network traffic", "Sending spam emails", "Hacking passwords"],
        "correct_answer": "Filtering network traffic",
    },
    {
        "question": "What is the most common encryption algorithm used in HTTPS?",
        "options": ["AES", "MD5", "SHA-256", "RSA"],
        "correct_answer": "RSA",
    },
    {
        "question": "Which of the following is a common two-factor authentication method?",
        "options": ["Username and password", "Fingerprint recognition", "Social media login", "QR code"],
        "correct_answer": "Fingerprint recognition",
    },
    {
        "question": "What is the primary purpose of a VPN?",
        "options": ["Encrypting emails", "Hiding your IP address", "Blocking ads", "Finding Wi-Fi networks"],
        "correct_answer": "Hiding your IP address",
    },
    {
        "question": "What does 'DDoS' stand for in cybersecurity?",
        "options": ["Data Download over Secure System", "Distributed Denial of Service", "Digital Defense of Systems", "Deep Data Scanning"],
        "correct_answer": "Distributed Denial of Service",
    },
    {
        "question": "What is the first step in a typical cybersecurity incident response plan?",
        "options": ["Identify the attacker", "Contain the incident", "Eradicate the threat", "Recover from the incident"],
        "correct_answer": "Identify the attacker",
    },
    {
        "question": "What is the primary purpose of a firewall in network security?",
        "options": ["Blocking all network traffic", "Allowing all network traffic", "Filtering and controlling network traffic", "Encrypting network traffic"],
        "correct_answer": "Filtering and controlling network traffic",
    },
    {
        "question": "What is the main goal of penetration testing?",
        "options": ["To secure a network", "To find vulnerabilities", "To develop software", "To manage incidents"],
        "correct_answer": "To find vulnerabilities",
    },
    {
        "question": "Which of the following is not a common encryption algorithm?",
        "options": ["AES", "MD5", "SHA-256", "TCP/IP"],
        "correct_answer": "TCP/IP",
    },
    {
        "question": "What does 'IoT' stand for in the context of cybersecurity?",
        "options": ["Internet of Things", "Input/Output Technology", "Intrusion of Things", "Information over Transport"],
        "correct_answer": "Internet of Things",
    },
    {
        "question": "What is a honeypot in cybersecurity?",
        "options": ["A sweet treat for hackers", "A type of firewall", "A deceptive system to attract attackers", "A hardware security module"],
        "correct_answer": "A deceptive system to attract attackers",
    },
    {
        "question": "What does 'CIA' stand for in the context of cybersecurity?",
        "options": ["Central Intelligence Agency", "Computer Information Assurance", "Confidentiality, Integrity, Availability", "Cybersecurity Investigation Agency"],
        "correct_answer": "Confidentiality, Integrity, Availability",
    },
    {
        "question": "What is the purpose of an intrusion detection system (IDS) in cybersecurity?",
        "options": ["To create strong passwords", "To prevent all network traffic", "To detect and alert on suspicious activities", "To generate encryption keys"],
        "correct_answer": "To detect and alert on suspicious activities",
    },
    {
        "question": "What is a common method for protecting data in transit over the internet?",
        "options": ["Putting data in a drawer", "Using HTTPS with SSL/TLS encryption", "Printing it out and sending it by mail", "Shouting the data across the room"],
        "correct_answer": "Using HTTPS with SSL/TLS encryption",
    },
    {
        "question": "What is the concept of 'least privilege' in cybersecurity?",
        "options": ["Everyone should have full access", "Everyone should have no access", "Users should have the minimum access needed", "Only administrators should have access"],
        "correct_answer": "Users should have the minimum access needed",
    },
    {
        "question": "What is a 'zero-day vulnerability' in cybersecurity?",
        "options": ["A software bug that's been around for zero days", "A vulnerability that's been fixed for zero days", "A vulnerability that's known and actively exploited", "A vulnerability that's not yet known or patched"],
        "correct_answer": "A vulnerability that's not yet known or patched",
    },
    {
        "question": "What is a 'firewall rule' in network security?",
        "options": ["A set of instructions for building a physical wall", "A rule for blocking all network traffic", "A rule for allowing all network traffic", "A rule for controlling network traffic based on defined criteria"],
        "correct_answer": "A rule for controlling network traffic based on defined criteria",
    },
    {
        "question": "What is 'two-factor authentication' in cybersecurity?",
        "options": ["Using two different computers for authentication", "Using two different passwords for authentication", "Using two different networks for authentication", "Using two different methods for authentication"],
        "correct_answer": "Using two different methods for authentication",
    },
    {
        "question": "What is the primary goal of cryptography in cybersecurity?",
        "options": ["To make information easy to access", "To ensure confidentiality and data integrity", "To create complex passwords", "To hide data from users"],
        "correct_answer": "To ensure confidentiality and data integrity",
    },
    {
        "question": "What is 'phishing' in cybersecurity?",
        "options": ["A type of fishing technique", "A way to block spam emails", "A method of luring users to reveal sensitive information", "A type of firewall"],
        "correct_answer": "A method of luring users to reveal sensitive information",
    },
    {
        "question": "What is 'malware' in cybersecurity?",
        "options": ["Malicious hardware components", "Malfunctioning software", "Malicious software designed to harm or steal data", "Malicious web browsers"],
        "correct_answer": "Malicious software designed to harm or steal data",
    },
    {
        "question": "What does 'VPN' stand for in the context of cybersecurity?",
        "options": ["Virtual Personal Network", "Virtual Private Network", "Very Private Network", "Virtual Public Network"],
        "correct_answer": "Virtual Private Network",
    },
    {
        "question": "What is the main purpose of a 'proxy server' in network security?",
        "options": ["To block all internet traffic", "To intercept and forward network requests", "To act as a firewall", "To provide free internet access"],
        "correct_answer": "To intercept and forward network requests",
    },
    {
        "question": "What is 'encryption' in cybersecurity?",
        "options": ["The process of hiding data", "The process of generating passwords", "The process of obfuscating code", "The process of encoding data to make it unreadable without a decryption key"],
        "correct_answer": "The process of encoding data to make it unreadable without a decryption key",
    },
    {
        "question": "What is the primary goal of 'access control' in cybersecurity?",
        "options": ["To allow everyone access to all data", "To restrict access to authorized users", "To delete all data", "To generate passwords"],
        "correct_answer": "To restrict access to authorized users",
    },
    {
        "question": "What is a 'keylogger' in cybersecurity?",
        "options": ["A device for logging keys on a piano", "A type of keyboard", "A software or hardware tool for capturing keystrokes", "A tool for analyzing encryption keys"],
        "correct_answer": "A software or hardware tool for capturing keystrokes",
    },
    {
        "question": "What is the primary purpose of 'antivirus software' in cybersecurity?",
        "options": ["To create viruses", "To block all network traffic", "To remove dust from the computer", "To detect and remove malicious software"],
        "correct_answer": "To detect and remove malicious software",
    },
    {
        "question": "What is 'social engineering' in cybersecurity?",
        "options": ["A type of social event for engineers", "A method for hacking social media accounts", "A technique for manipulating individuals to reveal sensitive information", "A type of programming language"],
        "correct_answer": "A technique for manipulating individuals to reveal sensitive information",
    },
    {
        "question": "What is 'cybersecurity'?",
        "options": ["The study of cyberspace", "A type of cyber warfare", "The practice of protecting systems, networks, and data from digital attacks", "A virtual currency"],
        "correct_answer": "The practice of protecting systems, networks, and data from digital attacks",
    },
    {
        "question": "What is 'ransomware' in cybersecurity?",
        "options": ["A type of payment for online services", "A type of password", "A type of firewall", "Malicious software that encrypts data and demands a ransom for decryption"],
        "correct_answer": "Malicious software that encrypts data and demands a ransom for decryption",
    },
    {
        "question": "What is 'zero-day vulnerability' in cybersecurity?",
        "options": ["A software bug that's been around for zero days", "A vulnerability that's been fixed for zero days", "A vulnerability that's known and actively exploited", "A vulnerability that's not yet known or patched"],
        "correct_answer": "A vulnerability that's not yet known or patched",
    },
    {
        "question": "What is a 'DMZ' in network security?",
        "options": ["A De-Militarized Zone", "A type of malware", "A zone with no data", "A network segment that separates a private network from the public internet"],
        "correct_answer": "A network segment that separates a private network from the public internet",
    },
    {
        "question": "What is 'brute force' in cybersecurity?",
        "options": ["A physical attack on a computer", "A method for guessing passwords through trial and error", "A type of firewall", "A type of encryption"],
        "correct_answer": "A method for guessing passwords through trial and error",
    },
    {
        "question": "What is 'pharming' in cybersecurity?",
        "options": ["A type of gardening", "A method for harvesting user data", "A type of malware", "A method for filtering web traffic"],
        "correct_answer": "A method for harvesting user data",
    },
    {
        "question": "What is a 'data breach'?",
        "options": ["A physical break in a computer", "A type of password", "An unauthorized release of sensitive data", "A type of malware"],
        "correct_answer": "An unauthorized release of sensitive data",
    },
    {
        "question": "What is the primary purpose of a 'security policy' in cybersecurity?",
        "options": ["To make security fun", "To create complex passwords", "To define rules and procedures for protecting data and systems", "To block all network traffic"],
        "correct_answer": "To define rules and procedures for protecting data and systems",
    },
    {
        "question": "What is a 'key pair' in encryption?",
        "options": ["A set of car keys and house keys", "A pair of identical keys", "A public key and a private key used in asymmetric encryption", "A type of password"],
        "correct_answer": "A public key and a private key used in asymmetric encryption",
    },
    {
        "question": "What is a 'data center' in the context of cybersecurity?",
        "options": ["A place where data is stored", "A type of malware", "A type of firewall", "A computer that generates data"],
        "correct_answer": "A place where data is stored",
    },
    {
        "question": "What is a 'rootkit' in cybersecurity?",
        "options": ["A type of tree", "A software tool for managing files", "A type of malware that provides unauthorized access to a computer", "A type of encryption"],
        "correct_answer": "A type of malware that provides unauthorized access to a computer",
    },
    {
        "question": "What is 'multi-factor authentication' (MFA) in cybersecurity?",
        "options": ["A type of math formula", "A type of malware", "A type of password", "A security method that requires two or more forms of authentication before granting access"],
        "correct_answer": "A security method that requires two or more forms of authentication before granting access",
    },
    {
        "question": "What is the purpose of a 'security assessment' in cybersecurity?",
        "options": ["To assess the physical security of a building", "To evaluate and test the security of an organization's systems and networks", "To assess an employee's security knowledge", "To block all network traffic"],
        "correct_answer": "To evaluate and test the security of an organization's systems and networks",
    },
    {
        "question": "What is 'malware analysis' in cybersecurity?",
        "options": ["Analyzing the behavior of malicious software", "Studying malware in a laboratory setting", "A type of encryption method", "A method for blocking malware"],
        "correct_answer": "Analyzing the behavior of malicious software",
    },
    {
        "question": "What is the purpose of a 'security incident response plan' in cybersecurity?",
        "options": ["To create security incidents", "To identify security incidents", "To define procedures for responding to and mitigating security incidents", "To block all network traffic"],
        "correct_answer": "To define procedures for responding to and mitigating security incidents",
    },
    {
        "question": "What is 'SQL injection' in cybersecurity?",
        "options": ["Injecting structured query language into a database", "A type of programming language", "A method for encrypting data", "A type of network firewall"],
        "correct_answer": "Injecting structured query language into a database",
    },
    {
        "question": "What is the purpose of 'network segmentation' in cybersecurity?",
        "options": ["To create secure networks", "To divide a network into isolated segments for security and performance reasons", "To encrypt all network traffic", "To block all network traffic"],
        "correct_answer": "To divide a network into isolated segments for security and performance reasons",
    },
    {
        "question": "What is 'cyber threat intelligence' in cybersecurity?",
        "options": ["Intelligence about cyber warfare", "A type of antivirus software", "Information about potential and current cyber threats and attacks", "A way to generate passwords"],
        "correct_answer": "Information about potential and current cyber threats and attacks",
    },
    {
        "question": "What is a 'security audit' in cybersecurity?",
        "options": ["An audit of financial records", "A type of password", "A review of an organization's security policies and procedures", "A type of firewall"],
        "correct_answer": "A review of an organization's security policies and procedures",
    },
    {
        "question": "What is 'penetration testing' in cybersecurity?",
        "options": ["Testing pens and pencils", "A type of keyboard", "A method for testing an organization's security defenses by simulating attacks", "A type of network protocol"],
        "correct_answer": "A method for testing an organization's security defenses by simulating attacks",
    },
    {
        "question": "What is a 'security token' in cybersecurity?",
        "options": ["A physical object used for security", "A type of password", "A type of malware", "A type of encryption method"],
        "correct_answer": "A physical object used for security",
    },
    {
        "question": "What is 'end-to-end encryption' in cybersecurity?",
        "options": ["Encryption that covers only the middle part of a data transmission", "Encryption that covers the beginning and end of a data transmission", "A type of firewall", "A type of malware"],
        "correct_answer": "Encryption that covers the beginning and end of a data transmission",
    },
    {
        "question": "What is 'cyber hygiene' in cybersecurity?",
        "options": ["A method for cleaning computers", "Practices and habits for maintaining good digital health and security", "A type of encryption", "A type of gardening"],
        "correct_answer": "Practices and habits for maintaining good digital health and security",
    },
    {
        "question": "What is a 'honeynet' in cybersecurity?",
        "options": ["A network of honeypots", "A type of internet service", "A type of encryption method", "A type of malware"],
        "correct_answer": "A network of honeypots",
    },
]

# Initialize variables
current_question = 0
score = 0
used_questions = []
quiz_started = False
# Function to select a random question that hasn't been used yet
def select_random_question():
    unused_questions = [q for q in quiz_data if q not in used_questions]
    if unused_questions:
        return random.choice(unused_questions)
    return None

# Function to shuffle the options for a given question
def shuffle_options(question):
    options = question["options"]
    random.shuffle(options)
    return options

# Function to start a new quiz session
def start_new_quiz():
    global current_question, score, quiz_started
    if not quiz_started:
        quiz_started = True
        start_button.destroy()  # Remove the "Start Quiz" button
        load_question()
        next_button.pack(pady=20)
        for option in option_buttons:
            option.pack(pady=10)

# Function to check the answer and update the score
def check_answer(selected_option):
    global score
    if quiz_data[current_question]["correct_answer"] == selected_option:
        score += 1
        option_buttons[quiz_data[current_question]["options"].index(selected_option)].config(bg="green")
    else:
        option_buttons[quiz_data[current_question]["options"].index(selected_option)].config(bg="red")
    next_button.config(state=tk.NORMAL)
    for option in option_buttons:
        option.config(state=tk.DISABLED)

# Function to load the next question
def load_question():
    result_label.config(text="")
    question_label.pack(pady=20)
    for option in option_buttons:
        option.config(bg="SystemButtonFace", state=tk.NORMAL)
        option.pack(pady=10)
    current_quiz = select_random_question()
    if current_quiz:
        used_questions.append(current_quiz)
        current_quiz["options"] = shuffle_options(current_quiz)  # Shuffle the options
        question_label.config(text=current_quiz["question"])
        for i, option in enumerate(option_buttons):
            option.config(text=current_quiz["options"][i])
    else:
        show_score()

# Function to handle moving to the next question or show the final score
def next_question():
    global current_question
    current_question += 1
    if current_question <= 10:  # 10 questions per session
        load_question()
        next_button.config(state=tk.DISABLED)
    else:
        show_score()

# Function to display the final score
def show_score():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the current frame
    # Create a new frame for the scoreboard
    scoreboard_frame = tk.Frame(root, bg="lightblue")
    scoreboard_frame.pack(pady=20)
    # Create and display the scoreboard label
    score_label = tk.Label(scoreboard_frame, text="Your Score: {}/10".format(score), font=("Helvetica", 16, "bold"), bg="lightblue")
    score_label.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Cyber Smarts Challenge")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="CYBER SMARTS CHALLENGE", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
title_label.pack(pady=20)

# Create Start New Quiz button
start_button = tk.Button(root, text="Start Quiz", font=("Helvetica", 12), command=start_new_quiz)
start_button.pack(pady=10)
start_button.config(state=tk.NORMAL)

# Create question label
question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="lightblue")

# Create result label
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="lightblue")

# Create option buttons
option_buttons = []
for i in range(4):
    option = tk.Button(root, text="", font=("Helvetica", 14), command=lambda i=i: check_answer(quiz_data[current_question]["options"][i]))
    option_buttons.append(option)

# Create Next button
next_button = tk.Button(root, text="Next", font=("Helvetica", 12), command=next_question)

# Start the GUI main loop
root.mainloop()