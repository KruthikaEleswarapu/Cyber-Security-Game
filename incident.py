import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [{
        "question": "What is the first step in the incident response process?",
        "options": ["Preparation", "Identification", "Containment", "Eradication"],
        "correct_answer": "Identification",
    },
    {
        "question": "What does the 'C' stand for in the 'CIA' triad in the context of security incidents?",
        "options": ["Confidentiality", "Control", "Continuity", "Capture"],
        "correct_answer": "Confidentiality",
    },
    {
        "question": "Which phase of incident response involves minimizing the impact of an incident?",
        "options": ["Containment", "Preparation", "Identification", "Recovery"],
        "correct_answer": "Containment",
    },
    {
        "question": "What is the primary goal of the 'Recovery' phase in incident response?",
        "options": ["Restore normal operations as quickly as possible", "Analyze the incident's root cause", "Contain and isolate the incident", "Prepare for future incidents"],
        "correct_answer": "Restore normal operations as quickly as possible",
    },
    {
        "question": "What is a 'false positive' in the context of security incident detection?",
        "options": ["An alert that incorrectly identifies a non-existent incident", "An incident that goes undetected", "A security incident caused by an insider threat", "A minor security incident"],
        "correct_answer": "An alert that incorrectly identifies a non-existent incident",
    },
    {
        "question": "What is 'digital forensics' in the context of incident response?",
        "options": ["The process of collecting, preserving, and analyzing electronic data for legal purposes", "Recovering lost data from backups", "Restoring affected systems to their original state", "Documenting incident details"],
        "correct_answer": "The process of collecting, preserving, and analyzing electronic data for legal purposes",
    },
    {
        "question": "What is 'incident severity' used for in incident response?",
        "options": ["To prioritize and classify incidents based on their impact", "To assess the skills of incident responders", "To measure the cost of incident response", "To determine the root cause of incidents"],
        "correct_answer": "To prioritize and classify incidents based on their impact",
    },
    {
        "question": "What is the 'chain of custody' in digital forensics?",
        "options": ["A documented record of evidence handling to maintain its integrity", "The order in which incidents are resolved", "A security incident's impact on business operations", "A chronological record of incident events"],
        "correct_answer": "A documented record of evidence handling to maintain its integrity",
    },
    {
        "question": "What is 'volatile data' in digital forensics?",
        "options": ["Data that is lost when a system is powered off", "Data stored on cloud servers", "Data that remains unchanged during an incident", "Data that is publicly accessible"],
        "correct_answer": "Data that is lost when a system is powered off",
    },
    {
        "question": "What is 'root cause analysis' in incident response?",
        "options": ["The process of identifying the underlying cause of an incident", "Determining the financial impact of an incident", "An analysis of privileged user activity", "Assessing the incident's severity"],
        "correct_answer": "The process of identifying the underlying cause of an incident",
    },
    {
        "question": "What is a 'security incident report' used for in incident response?",
        "options": ["To document incident details, response actions, and findings", "To generate new encryption keys", "To identify vulnerabilities in a system", "To perform threat modeling"],
        "correct_answer": "To document incident details, response actions, and findings",
    },
    {
        "question": "What is 'business impact analysis' (BIA) in incident response?",
        "options": ["Assessing the potential impact of an incident on business operations", "A technique for data recovery", "Evaluating the effectiveness of security controls", "Documenting incident timelines"],
        "correct_answer": "Assessing the potential impact of an incident on business operations",
    },
    {
        "question": "What is a 'security breach' in the context of security incidents?",
        "options": ["An unauthorized access or disclosure of sensitive data", "A penetration test", "A firewall rule", "A recovery plan"],
        "correct_answer": "An unauthorized access or disclosure of sensitive data",
    },
    {
        "question": "What is 'data exfiltration' in incident response?",
        "options": ["Unauthorized transfer of data from an organization's network", "A network protocol", "A cybersecurity certification", "A method for securing data at rest"],
        "correct_answer": "Unauthorized transfer of data from an organization's network",
    },
    {
        "question": "What is an 'incident handling team' responsible for in incident response?",
        "options": ["Coordinating and responding to security incidents", "Developing software patches", "Managing network traffic", "Creating encryption keys"],
        "correct_answer": "Coordinating and responding to security incidents",
    },
    {
        "question": "What is the purpose of 'lessons learned' in incident response?",
        "options": ["To improve incident response processes based on previous experiences", "To classify incidents based on their severity", "To recover encrypted data", "To analyze firewall rules"],
        "correct_answer": "To improve incident response processes based on previous experiences",
    },
    {
        "question": "What is 'threat hunting' in the context of incident response?",
        "options": ["Proactively searching for signs of security threats and incidents", "Developing antivirus software", "Encrypting sensitive data", "Testing network protocols"],
        "correct_answer": "Proactively searching for signs of security threats and incidents",
    },
    {
        "question": "What is the 'lead incident responder' responsible for in incident response?",
        "options": ["Overseeing the entire incident response process", "Implementing firewall rules", "Encrypting data", "Performing threat modeling"],
        "correct_answer": "Overseeing the entire incident response process",
    },
    {
        "question": "What is 'legal compliance' in incident response?",
        "options": ["Adhering to laws and regulations in incident handling", "A network protocol", "A type of password", "A cybersecurity certification"],
        "correct_answer": "Adhering to laws and regulations in incident handling",
    },
    {
        "question": "What is 'continuous improvement' in incident response?",
        "options": ["Ongoing enhancement of incident response capabilities based on feedback", "Blocking network traffic", "Recovering lost data", "Assessing security controls"],
        "correct_answer": "Ongoing enhancement of incident response capabilities based on feedback",
    },
    {
        "question": "What is 'evidence preservation' in digital forensics?",
        "options": ["Ensuring that electronic evidence remains intact and unaltered", "A method for data recovery", "A type of network firewall rule", "An incident response protocol"],
        "correct_answer": "Ensuring that electronic evidence remains intact and unaltered",
    },
    {
        "question": "What is a 'threat actor' in the context of security incidents?",
        "options": ["An individual or entity that carries out malicious activities", "A type of antivirus software", "A firewall configuration", "A cybersecurity certification"],
        "correct_answer": "An individual or entity that carries out malicious activities",
    },
    {
        "question": "What does 'IRP' stand for in incident response?",
        "options": ["Incident Response Plan", "Internet Recovery Protocol", "Initial Recovery Procedure", "Integrated Reporting Process"],
        "correct_answer": "Incident Response Plan",
    },
    {
        "question": "What is 'malware analysis' in incident response?",
        "options": ["The process of studying malicious software to understand its behavior and impact", "Securing network traffic", "Developing encryption keys", "Managing firewall configurations"],
        "correct_answer": "The process of studying malicious software to understand its behavior and impact",
    },
    {
        "question": "What is a 'SOC' in the context of incident response?",
        "options": ["Security Operations Center", "System of Communication", "Security Order Checklist", "Server Operations Command"],
        "correct_answer": "Security Operations Center",
    },
    {
        "question": "What is 'incident containment' in incident response?",
        "options": ["The process of limiting the spread and impact of an incident", "Managing backups", "Creating antivirus software", "Documenting incident timelines"],
        "correct_answer": "The process of limiting the spread and impact of an incident",
    },
    {
        "question": "What is a 'RTO' in the context of incident response?",
        "options": ["Recovery Time Objective", "Root Cause Analysis", "Response to an Incident", "Risk Tolerance Order"],
        "correct_answer": "Recovery Time Objective",
    },
    {
        "question": "What is a 'security incident notification' used for in incident response?",
        "options": ["To inform stakeholders and appropriate authorities of a security incident", "To update antivirus definitions", "To test network protocols", "To perform incident classification"],
        "correct_answer": "To inform stakeholders and appropriate authorities of a security incident",
    },
    {
        "question": "What is 'penetration testing' in incident response?",
        "options": ["Evaluating system security by simulating an attack", "An incident response protocol", "A type of firewall", "A method for data recovery"],
        "correct_answer": "Evaluating system security by simulating an attack",
    },
    {
        "question": "What is a 'security vulnerability' in the context of incident response?",
        "options": ["A weakness in a system or process that could be exploited", "An incident response plan", "A cybersecurity certification", "A type of backup strategy"],
        "correct_answer": "A weakness in a system or process that could be exploited",
    },
    {
        "question": "What is 'security awareness training' in incident response?",
        "options": ["Educating employees about security threats and best practices", "Implementing a firewall", "Recovering encrypted data", "Incident response classification"],
        "correct_answer": "Educating employees about security threats and best practices",
    },
    {
        "question": "What is 'evidence admissibility' in digital forensics?",
        "options": ["Ensuring that digital evidence is legally accepted in court", "An antivirus definition", "A recovery plan", "A network protocol"],
        "correct_answer": "Ensuring that digital evidence is legally accepted in court",
    },
    {
        "question": "What is 'phishing' in the context of security incidents?",
        "options": ["A type of social engineering attack that tricks individuals into revealing sensitive information", "A network protocol", "A cybersecurity certification", "A firewall rule"],
        "correct_answer": "A type of social engineering attack that tricks individuals into revealing sensitive information",
    },
    {
        "question": "What is 'PII' in the context of incident response?",
        "options": ["Personally Identifiable Information", "Preventing Incidents Instantly", "Public Internet Infrastructure", "Protecting Information Internationally"],
        "correct_answer": "Personally Identifiable Information",
    },
    {
        "question": "What is 'access control' in incident response?",
        "options": ["A security measure that restricts access to authorized users", "A type of firewall", "A response to an incident", "A security certification"],
        "correct_answer": "A security measure that restricts access to authorized users",
    },
    {
        "question": "What is 'forensic imaging' in digital forensics?",
        "options": ["Creating an exact copy of a digital device or storage medium for analysis", "A method for data recovery", "Testing network protocols", "Security response planning"],
        "correct_answer": "Creating an exact copy of a digital device or storage medium for analysis",
    },
    {
        "question": "What is an 'incident evidence log' used for in incident response?",
        "options": ["Documenting all actions taken during an incident", "Managing encryption keys", "Assessing system vulnerabilities", "Classifying incidents based on their impact"],
        "correct_answer": "Documenting all actions taken during an incident",
    },
    {
        "question": "What is 'DDoS' in the context of security incidents?",
        "options": ["Distributed Denial of Service", "Digital Data Security", "Direct Disk Storage", "Database Design and Optimization"],
        "correct_answer": "Distributed Denial of Service",
    },
    {
        "question": "What is 'intrusion detection' in the context of security incidents?",
        "options": ["Monitoring and identifying unauthorized access or malicious activity", "A response to an incident", "A type of backup", "A security certification"],
        "correct_answer": "Monitoring and identifying unauthorized access or malicious activity",
    },
    {
        "question": "What is 'chain of evidence' in digital forensics?",
        "options": ["A complete and unbroken trail of evidence handling", "A method for data recovery", "Incident response planning", "A type of encryption"],
        "correct_answer": "A complete and unbroken trail of evidence handling",
    },
    {
        "question": "What is a 'security incident response team' (SIRT) responsible for in incident response?",
        "options": ["Coordinating and managing the response to security incidents", "Developing antivirus software", "Creating firewall rules", "Testing network protocols"],
        "correct_answer": "Coordinating and managing the response to security incidents",
    },
    {
        "question": "What is 'security triage' in incident response?",
        "options": ["The initial assessment of an incident to determine its severity and response", "A data recovery process", "A method for securing data", "Incident documentation"],
        "correct_answer": "The initial assessment of an incident to determine its severity and response",
    },
    {
        "question": "What is 'zero-day vulnerability' in the context of security incidents?",
        "options": ["A previously unknown software vulnerability", "A security certificate", "An antivirus update", "A backup strategy"],
        "correct_answer": "A previously unknown software vulnerability",
    },
    {
        "question": "What is 'cybersecurity hygiene' in incident response?",
        "options": ["Best practices for maintaining security, including regular updates and patches", "A response to a security incident", "A firewall configuration", "Incident documentation"],
        "correct_answer": "Best practices for maintaining security, including regular updates and patches",
    },
    {
        "question": "What is a 'honeypot' in the context of security incidents?",
        "options": ["A deceptive system used to attract and monitor attackers", "A network protocol", "A type of encryption", "An incident response protocol"],
        "correct_answer": "A deceptive system used to attract and monitor attackers",
    },
    {
        "question": "What is 'incident escalation' in incident response?",
        "options": ["The process of involving higher-level authorities or experts when necessary", "Recovering encrypted data", "Testing network protocols", "Classifying incidents based on their impact"],
        "correct_answer": "The process of involving higher-level authorities or experts when necessary",
    },
    {
        "question": "What is a 'security risk assessment' used for in incident response?",
        "options": ["Evaluating and identifying potential security threats and vulnerabilities", "Implementing antivirus software", "Documenting incident timelines", "Creating firewall rules"],
        "correct_answer": "Evaluating and identifying potential security threats and vulnerabilities",
    },
    {
        "question": "What is 'two-factor authentication' (2FA) in incident response?",
        "options": ["A security method requiring two forms of identification to access a system", "A backup strategy", "A response to a security incident", "An incident classification process"],
        "correct_answer": "A security method requiring two forms of identification to access a system",
    },
    {
        "question": "What is 'social engineering' in the context of security incidents?",
        "options": ["Manipulating individuals to disclose sensitive information or perform actions", "A network protocol", "A type of backup strategy", "Incident classification"],
        "correct_answer": "Manipulating individuals to disclose sensitive information or perform actions",
    },
    {
        "question": "What is 'vulnerability scanning' in incident response?",
        "options": ["The process of identifying weaknesses in systems or networks", "Incident response planning", "Recovering lost data", "A type of antivirus software"],
        "correct_answer": "The process of identifying weaknesses in systems or networks",
    },
    {
        "question": "What is a 'security patch' used for in incident response?",
        "options": ["A software update that fixes security vulnerabilities", "Managing backups", "A firewall rule", "An incident documentation process"],
        "correct_answer": "A software update that fixes security vulnerabilities",
    },
    {
        "question": "What is 'third-party risk management' in incident response?",
        "options": ["Evaluating and mitigating security risks associated with external vendors or partners", "A data recovery process", "A network protocol", "A security certification"],
        "correct_answer": "Evaluating and mitigating security risks associated with external vendors or partners",
    },
    {
        "question": "What is 'file integrity monitoring' (FIM) in incident response?",
        "options": ["A security practice that checks for unauthorized changes to files", "A method for data recovery", "A response to a security incident", "A type of encryption"],
        "correct_answer": "A security practice that checks for unauthorized changes to files",
    },
    {
        "question": "What is 'SIEM' in the context of security incidents?",
        "options": ["Security Information and Event Management", "System Incident Escalation Measure", "Security Identity and Encryption Module", "Secure Internet Evaluation Method"],
        "correct_answer": "Security Information and Event Management",
    },
    {
        "question": "What is 'forensic chain of custody' in digital forensics?",
        "options": ["The documentation of evidence handling to ensure its integrity and admissibility", "An incident response plan", "A method for securing data", "A cybersecurity certification"],
        "correct_answer": "The documentation of evidence handling to ensure its integrity and admissibility",
    },
    {
        "question": "What is a 'ROE' in the context of incident response?",
        "options": ["Rules of Engagement", "Recovery of Evidence", "Root Cause Examination", "Response to an Event"],
        "correct_answer": "Rules of Engagement",
    }
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
root.title("Password Fortify")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="PASSWORD FORTIFY" ,font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
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