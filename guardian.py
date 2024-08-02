import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [ {
        "question": "What is the primary goal of a security simulation exercise?",
        "options": ["To test an organization's security measures and incident response capabilities", "To deploy new software patches", "To block all network traffic", "To encrypt sensitive data"],
        "correct_answer": "To test an organization's security measures and incident response capabilities",
    },
    {
        "question": "What is a 'red team' in security simulation?",
        "options": ["A group of skilled professionals who simulate cyberattacks on an organization", "A type of malware", "A method for data recovery", "A type of encryption method"],
        "correct_answer": "A group of skilled professionals who simulate cyberattacks on an organization",
    },
    {
        "question": "What is a 'blue team' in security simulation?",
        "options": ["A group responsible for defending against simulated cyberattacks", "A type of network protocol", "A method for blocking network traffic", "A type of firewall rule"],
        "correct_answer": "A group responsible for defending against simulated cyberattacks",
    },
    {
        "question": "What is the purpose of a 'penetration test' in security simulation?",
        "options": ["To identify vulnerabilities and weaknesses in a system or network", "To encrypt sensitive data", "To analyze encryption keys", "To develop antivirus software"],
        "correct_answer": "To identify vulnerabilities and weaknesses in a system or network",
    },
    {
        "question": "What is 'vulnerability assessment' in security simulation?",
        "options": ["A process of identifying and prioritizing vulnerabilities in a system", "A type of password", "A method for deleting data", "A type of network firewall rule"],
        "correct_answer": "A process of identifying and prioritizing vulnerabilities in a system",
    },
    {
        "question": "What is 'ethical hacking' in the context of security simulation?",
        "options": ["A practice of testing systems for security vulnerabilities with the owner's consent", "A type of network protocol", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "A practice of testing systems for security vulnerabilities with the owner's consent",
    },
    {
        "question": "What is 'spear phishing' in security simulation?",
        "options": ["A targeted form of phishing, usually directed at specific individuals or organizations", "A type of malware", "A method for data recovery", "A type of password"],
        "correct_answer": "A targeted form of phishing, usually directed at specific individuals or organizations",
    },
    {
        "question": "What does 'SQL injection' simulate in security testing?",
        "options": ["A method of exploiting a vulnerability in database security", "A type of firewall rule", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "A method of exploiting a vulnerability in database security",
    },
    {
        "question": "What is a 'capture the flag' (CTF) competition in security simulation?",
        "options": ["A game-like cybersecurity challenge to test participants' skills in finding and exploiting vulnerabilities", "A type of encryption method", "A method for blocking network traffic", "A method for data recovery"],
        "correct_answer": "A game-like cybersecurity challenge to test participants' skills in finding and exploiting vulnerabilities",
    },
    {
        "question": "What is the primary goal of a 'security tabletop exercise'?",
        "options": ["To simulate a security incident and test how an organization's response plan works", "To test network protocols", "To develop antivirus software", "To block all network traffic"],
        "correct_answer": "To simulate a security incident and test how an organization's response plan works",
    },
    {
        "question": "What is 'sandboxing' in security simulation?",
        "options": ["Running untrusted or potentially malicious code in an isolated environment for analysis", "A type of network protocol", "A method for deleting data", "A type of password"],
        "correct_answer": "Running untrusted or potentially malicious code in an isolated environment for analysis",
    },
    {
        "question": "What is 'war dialing' in security simulation?",
        "options": ["The process of dialing phone numbers to identify open modem connections", "A type of malware", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "The process of dialing phone numbers to identify open modem connections",
    },
    {
        "question": "What is 'security training and awareness' in the context of security simulation?",
        "options": ["Educating employees about security threats and best practices", "A method for data recovery", "A type of encryption method", "A type of network firewall rule"],
        "correct_answer": "Educating employees about security threats and best practices",
    },
    {
        "question": "What is 'honeynet' in security simulation?",
        "options": ["A network of intentionally vulnerable systems designed to attract and trap attackers", "A type of password", "A type of network protocol", "A method for analyzing encryption keys"],
        "correct_answer": "A network of intentionally vulnerable systems designed to attract and trap attackers",
    },
    {
        "question": "What is 'social engineering' in the context of security simulation?",
        "options": ["Manipulating individuals to disclose sensitive information or perform actions that compromise security", "A type of encryption method", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "Manipulating individuals to disclose sensitive information or perform actions that compromise security",
    },
    {
        "question": "What is 'incident response testing' in security simulation?",
        "options": ["Testing an organization's ability to respond to simulated security incidents", "A type of firewall", "A method for deleting data", "A type of encryption method"],
        "correct_answer": "Testing an organization's ability to respond to simulated security incidents",
    },
    {
        "question": "What is 'purple teaming' in security simulation?",
        "options": ["A combined approach that involves both red and blue teams working together", "A type of malware", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "A combined approach that involves both red and blue teams working together",
    },
    {
        "question": "What is 'disaster recovery testing' in security simulation?",
        "options": ["Testing an organization's ability to recover from various types of disasters or incidents", "A type of password", "A method for blocking network traffic", "A type of network firewall rule"],
        "correct_answer": "Testing an organization's ability to recover from various types of disasters or incidents",
    },
    {
        "question": "What is 'cyber range' in security simulation?",
        "options": ["A controlled environment for simulating cyberattacks and defenses", "A method for data recovery", "A type of encryption method", "A type of network protocol"],
        "correct_answer": "A controlled environment for simulating cyberattacks and defenses",
    },
    {
        "question": "What is 'fuzz testing' in security simulation?",
        "options": ["Testing software applications with random or unexpected input to uncover vulnerabilities", "A type of network protocol", "A method for deleting data", "A type of encryption method"],
        "correct_answer": "Testing software applications with random or unexpected input to uncover vulnerabilities",
    },
    {
        "question": "What is a 'honeypot' in security simulation?",
        "options": ["A decoy system used to lure potential attackers away from critical systems", "A type of network firewall rule", "A type of password", "A method for analyzing encryption keys"],
        "correct_answer": "A decoy system used to lure potential attackers away from critical systems",
    },
    {
        "question": "What is 'zero-day vulnerability testing' in security simulation?",
        "options": ["Identifying and testing vulnerabilities that are not yet known or patched", "A type of malware", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Identifying and testing vulnerabilities that are not yet known or patched",
    },
    {
        "question": "What is 'simulated phishing' in security simulation?",
        "options": ["Sending fake phishing emails to test how employees respond", "A type of network protocol", "A method for data recovery", "A type of network protocol"],
        "correct_answer": "Sending fake phishing emails to test how employees respond",
    },
    {
        "question": "What is 'malware analysis' in security simulation?",
        "options": ["Studying and analyzing malicious software to understand its behavior and purpose", "A type of encryption method", "A method for blocking network traffic", "A type of password"],
        "correct_answer": "Studying and analyzing malicious software to understand its behavior and purpose",
    },
    {
        "question": "What is 'security awareness training' in security simulation?",
        "options": ["Educating employees about security best practices and threats", "A type of password", "A type of network protocol", "A method for deleting data"],
        "correct_answer": "Educating employees about security best practices and threats",
    },
    {
        "question": "What is 'war gaming' in security simulation?",
        "options": ["Simulating large-scale security scenarios to prepare organizations for potential threats", "A type of malware", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "Simulating large-scale security scenarios to prepare organizations for potential threats",
    },
    {
        "question": "What is 'tabletop cyber exercise' in security simulation?",
        "options": ["A discussion-based exercise to simulate cyber incidents and responses", "A type of network protocol", "A type of encryption method", "A method for blocking network traffic"],
        "correct_answer": "A discussion-based exercise to simulate cyber incidents and responses",
    },
    {
        "question": "What is 'sandbox escape' in security simulation?",
        "options": ["A scenario where an attacker breaks out of a restricted environment", "A type of firewall rule", "A method for data recovery", "A type of encryption method"],
        "correct_answer": "A scenario where an attacker breaks out of a restricted environment",
    },
    {
        "question": "What is 'security incident simulation' in security testing?",
        "options": ["Simulating various security incidents to evaluate an organization's response and preparedness", "A type of network firewall rule", "A type of password", "A method for analyzing encryption keys"],
        "correct_answer": "Simulating various security incidents to evaluate an organization's response and preparedness",
    },
    {
        "question": "What is 'threat emulation' in security simulation?",
        "options": ["Imitating the behavior of specific threats or adversaries to test defenses", "A method for blocking network traffic", "A type of encryption method", "A type of password"],
        "correct_answer": "Imitating the behavior of specific threats or adversaries to test defenses",
    },
    {
        "question": "What is a 'honeymoon phase' in a security simulation scenario?",
        "options": ["A period when security measures are less stringent to allow the testing of defenses", "A type of malware", "A type of network protocol", "A method for data recovery"],
        "correct_answer": "A period when security measures are less stringent to allow the testing of defenses",
    },
    {
        "question": "What is a 'security control assessment' in security simulation?",
        "options": ["Evaluating the effectiveness of security controls and safeguards", "A type of network protocol", "A type of firewall", "A method for deleting data"],
        "correct_answer": "Evaluating the effectiveness of security controls and safeguards",
    },
    {
        "question": "What is 'live-fire exercise' in security simulation?",
        "options": ["A high-intensity simulation that tests security measures in a real-world scenario", "A type of password", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "A high-intensity simulation that tests security measures in a real-world scenario",
    },
    {
        "question": "What is a 'purple team assessment' in security simulation?",
        "options": ["Collaborative testing where both red and blue teams work together", "A type of encryption method", "A type of password", "A method for analyzing encryption keys"],
        "correct_answer": "Collaborative testing where both red and blue teams work together",
    },
    {
        "question": "What is a 'malware sandbox' in security simulation?",
        "options": ["An isolated environment for analyzing and containing malware samples", "A type of network firewall rule", "A type of network protocol", "A method for data recovery"],
        "correct_answer": "An isolated environment for analyzing and containing malware samples",
    },
    {
        "question": "What is 'continuous security testing' in security simulation?",
        "options": ["Regular, ongoing testing of security controls and systems", "A type of malware", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "Regular, ongoing testing of security controls and systems",
    },
    {
        "question": "What is 'zero-trust security testing' in security simulation?",
        "options": ["Testing security assumptions by assuming that threats are already inside the network", "A type of password", "A type of encryption method", "A method for blocking network traffic"],
        "correct_answer": "Testing security assumptions by assuming that threats are already inside the network",
    },
    {
        "question": "What is 'man-in-the-middle attack simulation' in security testing?",
        "options": ["Simulating an attacker intercepting communications between two parties", "A type of network protocol", "A method for deleting data", "A type of firewall rule"],
        "correct_answer": "Simulating an attacker intercepting communications between two parties",
    },
    {
        "question": "What is 'resilience testing' in security simulation?",
        "options": ["Testing an organization's ability to withstand and recover from cyberattacks", "A type of encryption method", "A method for analyzing encryption keys", "A type of password"],
        "correct_answer": "Testing an organization's ability to withstand and recover from cyberattacks",
    },
    {
        "question": "What is 'adversarial simulation' in security testing?",
        "options": ["Simulating adversarial tactics to test an organization's defenses", "A type of firewall", "A type of network protocol", "A method for blocking network traffic"],
        "correct_answer": "Simulating adversarial tactics to test an organization's defenses",
    },
    {
        "question": "What is 'tiger team testing' in security simulation?",
        "options": ["Engaging a skilled team to assess an organization's security from an attacker's perspective", "A type of network firewall rule", "A type of password", "A method for analyzing encryption keys"],
        "correct_answer": "Engaging a skilled team to assess an organization's security from an attacker's perspective",
    },
    {
        "question": "What is 'security posture assessment' in security simulation?",
        "options": ["Evaluating the overall security posture of an organization", "A type of password", "A type of network protocol", "A method for deleting data"],
        "correct_answer": "Evaluating the overall security posture of an organization",
    },
    {
        "question": "What is a 'black box test' in security simulation?",
        "options": ["A test where the tester has no prior knowledge of the system being tested", "A type of malware", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "A test where the tester has no prior knowledge of the system being tested",
    },
    {
        "question": "What is a 'red team assessment' in security simulation?",
        "options": ["An offensive approach where a team attempts to exploit vulnerabilities", "A type of network protocol", "A method for analyzing encryption keys", "A type of network firewall rule"],
        "correct_answer": "An offensive approach where a team attempts to exploit vulnerabilities",
    },
    {
        "question": "What is a 'blue team assessment' in security simulation?",
        "options": ["A defensive approach where a team protects against red team attacks", "A type of encryption method", "A type of password", "A method for data recovery"],
        "correct_answer": "A defensive approach where a team protects against red team attacks",
    },
    {
        "question": "What is 'threat intelligence simulation' in security testing?",
        "options": ["Simulating various cyber threats based on threat intelligence data", "A type of firewall rule", "A type of network protocol", "A method for deleting data"],
        "correct_answer": "Simulating various cyber threats based on threat intelligence data",
    },
    {
        "question": "What is a 'mock phishing campaign' in security simulation?",
        "options": ["A controlled phishing test to assess employee awareness", "A type of password", "A type of network protocol", "A method for blocking network traffic"],
        "correct_answer": "A controlled phishing test to assess employee awareness",
    },
    {
        "question": "What is 'virtual patching' in security simulation?",
        "options": ["Applying temporary security fixes to mitigate vulnerabilities", "A type of malware", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "Applying temporary security fixes to mitigate vulnerabilities",
    },
    {
        "question": "What is 'chaos engineering' in security simulation?",
        "options": ["Deliberately introducing system failures to test resiliency", "A type of network protocol", "A method for data recovery", "A type of encryption method"],
        "correct_answer": "Deliberately introducing system failures to test resiliency",
    },
    {
        "question": "What is 'business continuity testing' in security simulation?",
        "options": ["Testing an organization's ability to maintain critical operations during disruptions", "A type of network firewall rule", "A type of password", "A method for deleting data"],
        "correct_answer": "Testing an organization's ability to maintain critical operations during disruptions",
    },
    {
        "question": "What is 'rogue device testing' in security simulation?",
        "options": ["Testing for unauthorized devices connected to the network", "A type of encryption method", "A method for blocking network traffic", "A type of password"],
        "correct_answer": "Testing for unauthorized devices connected to the network",
    },
    {
        "question": "What is 'authentication bypass testing' in security simulation?",
        "options": ["Testing for vulnerabilities that allow unauthorized access without proper authentication", "A type of malware", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Testing for vulnerabilities that allow unauthorized access without proper authentication",
    },
    {
        "question": "What is 'countermeasure assessment' in security simulation?",
        "options": ["Evaluating the effectiveness of security countermeasures", "A type of network protocol", "A type of firewall rule", "A method for analyzing encryption keys"],
        "correct_answer": "Evaluating the effectiveness of security countermeasures",
    },
    {
        "question": "What is a 'virtual security assessment' in security simulation?",
        "options": ["Assessing the security of virtualized environments", "A type of encryption method", "A type of password", "A method for data recovery"],
        "correct_answer": "Assessing the security of virtualized environments",
    },
    {
        "question": "What is 'active directory penetration testing' in security simulation?",
        "options": ["Testing the security of an organization's active directory infrastructure", "A type of password", "A type of network protocol", "A method for deleting data"],
        "correct_answer": "Testing the security of an organization's active directory infrastructure",
    },
    {
        "question": "What is 'log analysis testing' in security simulation?",
        "options": ["Analyzing system logs to detect security incidents and anomalies", "A type of network protocol", "A type of firewall", "A method for blocking network traffic"],
        "correct_answer": "Analyzing system logs to detect security incidents and anomalies",
    },
    {
        "question": "What is a 'container security assessment' in security simulation?",
        "options": ["Assessing the security of containerized applications and environments", "A type of malware", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "Assessing the security of containerized applications and environments",
    },
]
# Initialize variables
current_question = 0
score = 0
used_questions = []
quiz_started = False

# Function to shuffle the options for a given question
def shuffle_options(question):
    options = question["options"]
    random.shuffle(options)
    return options

# Function to select 10 random questions from the pool
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
root.title("Guardian of world")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="GUARDIAN OF WORLD", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
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