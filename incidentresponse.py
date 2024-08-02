import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [
    {
        "question": "What is the first step in the incident response process after a security incident is identified?",
        "options": ["Contain the incident", "Eradicate the threat", "Recover from the incident", "Notify stakeholders"],
        "correct_answer": "Contain the incident",
    },
    {
        "question": "What is the purpose of a tabletop exercise in incident response?",
        "options": ["Simulate a security incident and test the response plan", "Erase sensitive data", "Develop new incident response tools", "Create a physical table for incident responders"],
        "correct_answer": "Simulate a security incident and test the response plan",
    },
    {
        "question": "What does 'CSIRT' stand for in the context of incident response?",
        "options": ["Computer System Incident Response Team", "Cyber Security Investigation and Response Team", "Centralized Security Incident Response Team", "Cyber Security Incident Reporting Tool"],
        "correct_answer": "Computer System Incident Response Team",
    },
    {
        "question": "What is 'forensics' in the context of incident response?",
        "options": ["The science of analyzing digital evidence", "A type of firewall", "A method for blocking network traffic", "A type of encryption"],
        "correct_answer": "The science of analyzing digital evidence",
    },
    {
        "question": "What is a 'chain of custody' in digital forensics?",
        "options": ["A documented record of who has had possession of evidence", "A type of encryption method", "A type of malware", "A physical chain used to secure evidence"],
        "correct_answer": "A documented record of who has had possession of evidence",
    },
    {
        "question": "What is 'data exfiltration' in the context of incident response?",
        "options": ["Transferring data from an internal network to an external location", "The process of deleting data", "A method for blocking network traffic", "A type of network firewall"],
        "correct_answer": "Transferring data from an internal network to an external location",
    },
    {
        "question": "What is 'threat hunting' in incident response?",
        "options": ["The practice of actively searching for security threats within an organization", "A type of hunting game", "A type of encryption method", "A method for preventing data breaches"],
        "correct_answer": "The practice of actively searching for security threats within an organization",
    },
    {
        "question": "In an incident response plan, what is the role of a 'communications coordinator'?",
        "options": ["To handle all external and internal communications during an incident", "To make coffee for the team", "To eradicate threats", "To recover lost data"],
        "correct_answer": "To handle all external and internal communications during an incident",
    },
    {
        "question": "What is the primary goal of 'digital evidence preservation' in incident response?",
        "options": ["To ensure that digital evidence remains intact and unaltered", "To make evidence available for public access", "To prevent evidence from being used in court", "To erase digital evidence"],
        "correct_answer": "To ensure that digital evidence remains intact and unaltered",
    },
    {
        "question": "What is the role of a 'first responder' in incident response?",
        "options": ["To contain the incident", "To investigate the incident", "To recover lost data", "To handle external communications"],
        "correct_answer": "To contain the incident",
    },
    {
        "question": "When conducting digital forensics, what is the purpose of creating a forensic image of a device?",
        "options": ["To preserve the state of the device for analysis", "To erase all data on the device", "To speed up the analysis process", "To hide evidence from attackers"],
        "correct_answer": "To preserve the state of the device for analysis",
    },
    {
        "question": "What is the role of 'legal counsel' in incident response?",
        "options": ["To provide legal guidance and ensure compliance with laws and regulations", "To handle communications with the media", "To provide technical expertise during investigations", "To recover lost data"],
        "correct_answer": "To provide legal guidance and ensure compliance with laws and regulations",
    },
    {
        "question": "What is 'threat intelligence' in incident response?",
        "options": ["Information about potential and current cyber threats and attacks", "A type of encryption method", "A method for blocking network traffic", "A type of malware"],
        "correct_answer": "Information about potential and current cyber threats and attacks",
    },
    {
        "question": "What is the role of a 'digital evidence custodian' in incident response?",
        "options": ["To preserve and manage digital evidence", "To investigate security incidents", "To handle external communications", "To make coffee for the team"],
        "correct_answer": "To preserve and manage digital evidence",
    },
    {
        "question": "What is a 'root cause analysis' in incident response?",
        "options": ["A process for identifying and addressing the underlying causes of incidents", "A type of malware", "A type of encryption method", "A method for preventing data breaches"],
        "correct_answer": "A process for identifying and addressing the underlying causes of incidents",
    },
    {
        "question": "What is 'incident classification' in incident response?",
        "options": ["Categorizing incidents based on their severity and impact", "A type of network firewall", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Categorizing incidents based on their severity and impact",
    },
    {
        "question": "What is the purpose of 'lessons learned' in incident response?",
        "options": ["To improve future incident response efforts based on past experiences", "To block all network traffic", "To recover lost data", "To investigate security incidents"],
        "correct_answer": "To improve future incident response efforts based on past experiences",
    },
    {
        "question": "What is a 'security incident' in incident response?",
        "options": ["A violation or imminent threat of violation of security policies, acceptable use policies, or standard security practices", "A type of keyboard", "A method for analyzing encryption keys", "A type of firewall rule"],
        "correct_answer": "A violation or imminent threat of violation of security policies, acceptable use policies, or standard security practices",
    },
    {
        "question": "What is 'continuous monitoring' in incident response?",
        "options": ["The ongoing process of monitoring an organization's security controls and systems", "A type of antivirus software", "A type of password", "A type of encryption method"],
        "correct_answer": "The ongoing process of monitoring an organization's security controls and systems",
    },
    {
        "question": "What is a 'SIEM' in incident response?",
        "options": ["Security Information and Event Management system", "A type of network protocol", "A type of network firewall", "A type of keyboard"],
        "correct_answer": "Security Information and Event Management system",
    },
    {
        "question": "What is the 'detection phase' in the incident response process?",
        "options": ["The phase where security incidents are identified and assessed", "A type of malware", "A type of encryption method", "The phase where incidents are eradicated"],
        "correct_answer": "The phase where security incidents are identified and assessed",
    },
    {
        "question": "What is 'incident response automation'?",
        "options": ["The use of automated tools and processes to respond to security incidents", "A method for preventing incidents", "A type of firewall", "A type of encryption method"],
        "correct_answer": "The use of automated tools and processes to respond to security incidents",
    },
    {
        "question": "What is 'RTO' in incident response?",
        "options": ["Recovery Time Objective", "A type of encryption method", "A type of network protocol", "A type of firewall rule"],
        "correct_answer": "Recovery Time Objective",
    },
    {
        "question": "What is the 'identification phase' in the incident response process?",
        "options": ["The phase where an incident is discovered and reported", "A type of antivirus software", "A type of keyboard", "The phase where incidents are eradicated"],
        "correct_answer": "The phase where an incident is discovered and reported",
    },
    {
        "question": "What is the 'CSIRT playbook' in incident response?",
        "options": ["A predefined set of procedures and guidelines for responding to specific incidents", "A type of network protocol", "A type of firewall", "A type of encryption method"],
        "correct_answer": "A predefined set of procedures and guidelines for responding to specific incidents",
    },
    {
        "question": "What is a 'false positive' in incident response?",
        "options": ["An alert or alarm generated by a security tool that is not indicative of an actual security incident", "A type of firewall rule", "A type of malware", "A type of network protocol"],
        "correct_answer": "An alert or alarm generated by a security tool that is not indicative of an actual security incident",
    },
    {
        "question": "What is 'NIST' in incident response?",
        "options": ["National Institute of Standards and Technology", "A type of network firewall", "A type of network protocol", "A type of keyboard"],
        "correct_answer": "National Institute of Standards and Technology",
    },
    {
        "question": "What is the 'containment phase' in the incident response process?",
        "options": ["The phase where immediate actions are taken to prevent the incident from spreading", "A type of malware", "A type of encryption method", "The phase where incidents are eradicated"],
        "correct_answer": "The phase where immediate actions are taken to prevent the incident from spreading",
    },
    {
        "question": "What is 'two-factor authentication' in incident response?",
        "options": ["A security process in which a user provides two different authentication factors to verify their identity", "A type of antivirus software", "A type of firewall rule", "A type of encryption method"],
        "correct_answer": "A security process in which a user provides two different authentication factors to verify their identity",
    },
    {
        "question": "What is 'phishing' in incident response?",
        "options": ["A type of social engineering attack aimed at tricking individuals into revealing confidential information", "A type of encryption method", "A method for preventing data breaches", "A type of network protocol"],
        "correct_answer": "A type of social engineering attack aimed at tricking individuals into revealing confidential information",
    },
    {
        "question": "What is 'evidence spoliation' in digital forensics?",
        "options": ["The intentional or unintentional destruction, alteration, or contamination of evidence", "A type of network firewall", "A method for blocking network traffic", "A type of antivirus software"],
        "correct_answer": "The intentional or unintentional destruction, alteration, or contamination of evidence",
    },
    {
        "question": "What is 'SOC' in incident response?",
        "options": ["Security Operations Center", "A type of network protocol", "A type of malware", "A type of firewall rule"],
        "correct_answer": "Security Operations Center",
    },
    {
        "question": "What is 'data classification' in incident response?",
        "options": ["Categorizing data based on its sensitivity and importance", "A type of network firewall", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Categorizing data based on its sensitivity and importance",
    },
    {
        "question": "What is 'data loss prevention' (DLP) in incident response?",
        "options": ["A strategy and tools to prevent unauthorized data access, sharing, or leakage", "A type of encryption method", "A type of keyboard", "A method for analyzing encryption keys"],
        "correct_answer": "A strategy and tools to prevent unauthorized data access, sharing, or leakage",
    },
    {
        "question": "What is 'zero-day vulnerability' in incident response?",
        "options": ["A previously unknown software vulnerability that is actively exploited by attackers", "A type of network protocol", "A type of firewall rule", "A type of antivirus software"],
        "correct_answer": "A previously unknown software vulnerability that is actively exploited by attackers",
    },
    {
        "question": "What is a 'firewall' in incident response?",
        "options": ["A network security device that monitors and filters incoming and outgoing network traffic", "A type of encryption method", "A type of network protocol", "A type of malware"],
        "correct_answer": "A network security device that monitors and filters incoming and outgoing network traffic",
    },
    {
        "question": "What is the 'communication and coordination' phase in incident response?",
        "options": ["The phase where communication with stakeholders and relevant parties is established", "A type of keyboard", "A method for analyzing encryption keys", "The phase where incidents are eradicated"],
        "correct_answer": "The phase where communication with stakeholders and relevant parties is established",
    },
    {
        "question": "What is 'business continuity planning' in incident response?",
        "options": ["The process of creating a plan to ensure essential business functions can continue during and after a disaster", "A type of network firewall", "A type of network protocol", "A type of encryption method"],
        "correct_answer": "The process of creating a plan to ensure essential business functions can continue during and after a disaster",
    },
    {
        "question": "What is 'multi-factor authentication' (MFA) in incident response?",
        "options": ["A security process in which a user provides multiple authentication factors to verify their identity", "A type of malware", "A method for preventing data breaches", "A type of antivirus software"],
        "correct_answer": "A security process in which a user provides multiple authentication factors to verify their identity",
    },
    {
        "question": "What is 'vulnerability scanning' in incident response?",
        "options": ["The process of identifying and assessing security vulnerabilities in a network or system", "A type of firewall rule", "A type of encryption method", "A type of network protocol"],
        "correct_answer": "The process of identifying and assessing security vulnerabilities in a network or system",
    },
    {
        "question": "What is 'incident reporting' in incident response?",
        "options": ["The process of documenting and notifying appropriate parties about a security incident", "A type of keyboard", "A type of network protocol", "A type of network firewall"],
        "correct_answer": "The process of documenting and notifying appropriate parties about a security incident",
    },
    {
        "question": "What is the 'analysis phase' in the incident response process?",
        "options": ["The phase where collected evidence and data are analyzed to determine the scope and impact of the incident", "A type of encryption method", "A method for blocking network traffic", "The phase where incidents are contained"],
        "correct_answer": "The phase where collected evidence and data are analyzed to determine the scope and impact of the incident",
    },
    {
        "question": "What is a 'honeypot' in incident response?",
        "options": ["A decoy system designed to attract and analyze malicious activity", "A type of malware", "A type of firewall rule", "A type of keyboard"],
        "correct_answer": "A decoy system designed to attract and analyze malicious activity",
    },
    {
        "question": "What is 'fuzzing' in incident response?",
        "options": ["A testing technique that involves sending random or unexpected data inputs to software to find vulnerabilities", "A type of network protocol", "A method for analyzing encryption keys", "A method for preventing data breaches"],
        "correct_answer": "A testing technique that involves sending random or unexpected data inputs to software to find vulnerabilities",
    },
    {
        "question": "What is the 'eradication phase' in the incident response process?",
        "options": ["The phase where the root cause of the incident is identified and removed", "A type of encryption method", "A type of network firewall", "The phase where incidents are contained"],
        "correct_answer": "The phase where the root cause of the incident is identified and removed",
    },
    {
        "question": "What is 'cryptography' in incident response?",
        "options": ["The practice of secure communication techniques using codes and ciphers", "A type of keyboard", "A type of network protocol", "A type of antivirus software"],
        "correct_answer": "The practice of secure communication techniques using codes and ciphers",
    },
    {
        "question": "What is 'BIA' in incident response?",
        "options": ["Business Impact Analysis", "A type of network firewall", "A type of malware", "A type of firewall rule"],
        "correct_answer": "Business Impact Analysis",
    },
    {
        "question": "What is 'threat modeling' in incident response?",
        "options": ["A practice of identifying potential threats and vulnerabilities to an organization", "A method for analyzing encryption keys", "A method for preventing data breaches", "A type of network protocol"],
        "correct_answer": "A practice of identifying potential threats and vulnerabilities to an organization",
    },
    {
        "question": "What is 'data breach' in incident response?",
        "options": ["Unauthorized access, use, or disclosure of sensitive or confidential data", "A type of encryption method", "A type of network protocol", "A type of keyboard"],
        "correct_answer": "Unauthorized access, use, or disclosure of sensitive or confidential data",
    },
    {
        "question": "What is a 'CSIRT manager' in incident response?",
        "options": ["The individual responsible for leading the incident response team", "A type of firewall rule", "A method for blocking network traffic", "A type of network firewall"],
        "correct_answer": "The individual responsible for leading the incident response team",
    },
    {
        "question": "What is a 'security incident log' in incident response?",
        "options": ["A record of security incidents and related details", "A type of network protocol", "A type of malware", "A type of keyboard"],
        "correct_answer": "A record of security incidents and related details",
    },
    {
        "question": "What is 'payload' in incident response?",
        "options": ["The malicious content or code delivered by an attacker", "A type of antivirus software", "A type of firewall rule", "A method for analyzing encryption keys"],
        "correct_answer": "The malicious content or code delivered by an attacker",
    },
    {
        "question": "What is 'security awareness training' in incident response?",
        "options": ["Educational programs designed to raise awareness about security threats and best practices", "A type of encryption method", "A method for preventing data breaches", "A type of network protocol"],
        "correct_answer": "Educational programs designed to raise awareness about security threats and best practices",
    },
    {
        "question": "What is a 'chain of command' in incident response?",
        "options": ["A structured order of authority and responsibility within an organization", "A type of network firewall", "A type of network protocol", "A type of malware"],
        "correct_answer": "A structured order of authority and responsibility within an organization",
    },
    {
        "question": "What is 'IR plan testing' in incident response?",
        "options": ["The process of evaluating and validating the incident response plan through testing and simulations", "A type of keyboard", "A method for analyzing encryption keys", "A type of firewall rule"],
        "correct_answer": "The process of evaluating and validating the incident response plan through testing and simulations",
    },
    {
        "question": "What is 'social engineering' in incident response?",
        "options": ["Manipulating individuals to reveal confidential information or perform actions", "A type of network protocol", "A type of malware", "A method for preventing data breaches"],
        "correct_answer": "Manipulating individuals to reveal confidential information or perform actions",
    },
    {
        "question": "What is 'data encryption' in incident response?",
        "options": ["The process of converting data into a code to prevent unauthorized access", "A type of network firewall", "A type of network protocol", "A type of keyboard"],
        "correct_answer": "The process of converting data into a code to prevent unauthorized access",
    },
    {
        "question": "What is 'cybersecurity framework' in incident response?",
        "options": ["A structured set of cybersecurity standards and best practices", "A type of antivirus software", "A type of firewall rule", "A type of encryption method"],
        "correct_answer": "A structured set of cybersecurity standards and best practices",
    },
    {
        "question": "What is 'data backup' in incident response?",
        "options": ["Creating copies of data to restore it in case of data loss or damage", "A type of malware", "A type of encryption method", "A method for blocking network traffic"],
        "correct_answer": "Creating copies of data to restore it in case of data loss or damage",
    },
    {
        "question": "What is an 'incident response policy' in incident response?",
        "options": ["A documented set of guidelines for handling security incidents", "A type of network protocol", "A type of network firewall", "A type of keyboard"],
        "correct_answer": "A documented set of guidelines for handling security incidents",
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
root.title("Incident Commander")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="INCIDENT COMMANDER", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
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