import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [ {
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
        "options": ["Security Information and Event Management system", "A type of network protocol", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Security Information and Event Management system",
    },
    {
        "question": "What is 'security awareness training' in incident response?",
        "options": ["Educating employees about security risks and best practices", "A type of malware", "A type of firewall rule", "A type of encryption method"],
        "correct_answer": "Educating employees about security risks and best practices",
    },
    {
        "question": "What is 'data breach notification' in incident response?",
        "options": ["Informing affected individuals and authorities about a data breach", "A method for blocking network traffic", "A type of encryption method", "A type of network protocol"],
        "correct_answer": "Informing affected individuals and authorities about a data breach",
    },
    {
        "question": "What is 'honeypot' in incident response?",
        "options": ["A decoy system used to lure attackers and study their behavior", "A type of encryption method", "A method for deleting data", "A type of password"],
        "correct_answer": "A decoy system used to lure attackers and study their behavior",
    },
    {
        "question": "What does 'IRP' stand for in the context of incident response?",
        "options": ["Incident Response Plan", "Internet Routing Protocol", "Incident Reporting Procedure", "Internal Recovery Process"],
        "correct_answer": "Incident Response Plan",
    },
    {
        "question": "What is the role of a 'public relations coordinator' in incident response?",
        "options": ["To manage communications with the media and the public", "To investigate incidents", "To recover lost data", "To develop encryption tools"],
        "correct_answer": "To manage communications with the media and the public",
    },
    {
        "question": "What is 'patch management' in incident response?",
        "options": ["The process of applying software updates and patches to address security vulnerabilities", "A type of network firewall", "A method for deleting data", "A type of encryption method"],
        "correct_answer": "The process of applying software updates and patches to address security vulnerabilities",
    },
    {
        "question": "What is the 'principle of least privilege' in incident response?",
        "options": ["Providing users with the minimum levels of access necessary to perform their job functions", "Providing users with unlimited access to all systems", "Blocking all network traffic", "Encrypting all data"],
        "correct_answer": "Providing users with the minimum levels of access necessary to perform their job functions",
    },
    {
        "question": "What is the role of a 'security incident manager' in incident response?",
        "options": ["To oversee and coordinate the response to a security incident", "To conduct digital forensics", "To recover lost data", "To manage the organization's social media accounts"],
        "correct_answer": "To oversee and coordinate the response to a security incident",
    },
    {
        "question": "What is 'zero-day vulnerability' in incident response?",
        "options": ["A previously unknown and unpatched software vulnerability", "A type of password", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "A previously unknown and unpatched software vulnerability",
    },
    {
        "question": "What is 'incident prioritization' in incident response?",
        "options": ["Assigning a priority level to incidents based on their potential impact and severity", "A type of malware", "A type of encryption method", "A type of network protocol"],
        "correct_answer": "Assigning a priority level to incidents based on their potential impact and severity",
    },
    {
        "question": "What is the purpose of 'digital chain of custody' in incident response?",
        "options": ["To maintain the integrity of digital evidence during legal proceedings", "To block all network traffic", "To recover lost data", "To create encrypted chains"],
        "correct_answer": "To maintain the integrity of digital evidence during legal proceedings",
    },
    {
        "question": "What is 'anomaly detection' in incident response?",
        "options": ["Identifying unusual patterns or behaviors that may indicate a security threat", "A type of antivirus software", "A type of firewall rule", "A method for blocking network traffic"],
        "correct_answer": "Identifying unusual patterns or behaviors that may indicate a security threat",
    },
    {
        "question": "What is 'social engineering' in incident response?",
        "options": ["Manipulating individuals to divulge confidential information or perform actions that compromise security", "A type of encryption method", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "Manipulating individuals to divulge confidential information or perform actions that compromise security",
    },
    {
        "question": "What is 'malware analysis' in incident response?",
        "options": ["The process of examining and understanding malicious software", "A type of password", "A method for deleting data", "A type of encryption method"],
        "correct_answer": "The process of examining and understanding malicious software",
    },
    {
        "question": "What is a 'digital signature' in incident response?",
        "options": ["A cryptographic method used to verify the authenticity and integrity of digital documents or messages", "A type of malware", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "A cryptographic method used to verify the authenticity and integrity of digital documents or messages",
    },
    {
        "question": "What is 'incident reporting' in incident response?",
        "options": ["The process of notifying appropriate parties about a security incident", "A method for analyzing encryption keys", "A type of firewall rule", "A type of encryption method"],
        "correct_answer": "The process of notifying appropriate parties about a security incident",
    },
    {
        "question": "What is 'incident response automation'?",
        "options": ["Using technology to streamline and automate incident response tasks", "A type of antivirus software", "A type of password", "A method for deleting data"],
        "correct_answer": "Using technology to streamline and automate incident response tasks",
    },
    {
        "question": "What is 'threat actor' in incident response?",
        "options": ["An individual or group responsible for carrying out a cyberattack", "A type of firewall", "A type of encryption method", "A method for blocking network traffic"],
        "correct_answer": "An individual or group responsible for carrying out a cyberattack",
    },
    {
        "question": "What is 'steganography' in incident response?",
        "options": ["Hiding data within other data to conceal its existence", "A type of network protocol", "A method for blocking network traffic", "A type of password"],
        "correct_answer": "Hiding data within other data to conceal its existence",
    },
    {
        "question": "What is 'data loss prevention' (DLP) in incident response?",
        "options": ["A strategy for preventing the unauthorized sharing of sensitive data", "A type of encryption method", "A method for deleting data", "A method for blocking network traffic"],
        "correct_answer": "A strategy for preventing the unauthorized sharing of sensitive data",
    },
    {
        "question": "What is 'security information sharing' in incident response?",
        "options": ["The exchange of security information and threat intelligence between organizations", "A type of malware", "A type of password", "A type of network protocol"],
        "correct_answer": "The exchange of security information and threat intelligence between organizations",
    },
    {
        "question": "What is 'virtualization' in incident response?",
        "options": ["Creating virtual instances of hardware or software for various purposes", "A type of encryption method", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "Creating virtual instances of hardware or software for various purposes",
    },
    {
        "question": "What is 'data classification' in incident response?",
        "options": ["Categorizing data based on its sensitivity and value", "A type of firewall rule", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Categorizing data based on its sensitivity and value",
    },
    {
        "question": "What is 'security token' in incident response?",
        "options": ["A physical or digital device used for authentication and access control", "A type of malware", "A method for blocking network traffic", "A type of password"],
        "correct_answer": "A physical or digital device used for authentication and access control",
    },
    {
        "question": "What is 'incident documentation' in incident response?",
        "options": ["The process of recording all actions and findings during an incident", "A type of encryption method", "A method for deleting data", "A type of network protocol"],
        "correct_answer": "The process of recording all actions and findings during an incident",
    },
     {
        "question": "What is the primary goal of an incident response plan?",
        "options": ["To minimize damage and reduce recovery time", "To maximize damage and create chaos", "To provide detailed descriptions of security incidents", "To increase the risk of data breaches"],
        "correct_answer": "To minimize damage and reduce recovery time",
    },
    {
        "question": "What is the 'detection phase' in incident response?",
        "options": ["Identifying signs of a security incident", "A type of encryption method", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "Identifying signs of a security incident",
    },
    {
        "question": "What is the 'response phase' in incident response?",
        "options": ["Taking action to contain and mitigate the impact of a security incident", "A type of malware", "A type of password", "A method for deleting data"],
        "correct_answer": "Taking action to contain and mitigate the impact of a security incident",
    },
    {
        "question": "What is 'post-incident analysis' in incident response?",
        "options": ["Evaluating the incident response effort and identifying areas for improvement", "A type of network firewall", "A method for analyzing encryption keys", "A type of network protocol"],
        "correct_answer": "Evaluating the incident response effort and identifying areas for improvement",
    },
    {
        "question": "What is 'evidence collection' in digital forensics?",
        "options": ["Gathering digital evidence from various sources", "A method for blocking network traffic", "A type of password", "A type of encryption method"],
        "correct_answer": "Gathering digital evidence from various sources",
    },
    {
        "question": "What is 'incident escalation' in incident response?",
        "options": ["Increasing the severity level of an incident based on its impact", "A type of firewall rule", "A type of encryption method", "A method for preventing data breaches"],
        "correct_answer": "Increasing the severity level of an incident based on its impact",
    },
    {
        "question": "What is 'business continuity planning' in incident response?",
        "options": ["Developing a strategy to ensure essential business functions can continue in the event of a disaster or incident", "A type of malware", "A type of password", "A method for analyzing encryption keys"],
        "correct_answer": "Developing a strategy to ensure essential business functions can continue in the event of a disaster or incident",
    },
    {
        "question": "What is 'de-escalation' in incident response?",
        "options": ["Reducing the severity level of an incident after containment", "A type of network protocol", "A method for blocking network traffic", "A type of encryption method"],
        "correct_answer": "Reducing the severity level of an incident after containment",
    },
    {
        "question": "What is a 'security audit' in incident response?",
        "options": ["A systematic evaluation of an organization's security practices and controls", "A type of firewall", "A method for deleting data", "A type of network firewall rule"],
        "correct_answer": "A systematic evaluation of an organization's security practices and controls",
    },
    {
        "question": "What is 'volatility analysis' in digital forensics?",
        "options": ["Analyzing a computer's RAM to gather evidence", "A type of password", "A method for blocking network traffic", "A type of network protocol"],
        "correct_answer": "Analyzing a computer's RAM to gather evidence",
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
root.title("Security Savvy")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="SECURITY SAVVY SHUTDOWN", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
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