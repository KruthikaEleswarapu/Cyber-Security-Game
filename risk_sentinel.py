import tkinter as tk
import random

# Define a pool of 50 cybersecurity-related quiz questions and answers
quiz_data = [
    {
        "question": "What is the primary goal of risk assessment in cybersecurity?",
        "options": ["To create secure passwords", "To detect and remove malware", "To identify and mitigate security risks", "To encrypt data"],
        "correct_answer": "To identify and mitigate security risks",
    },
    {
        "question": "What is a 'threat' in the context of risk assessment?",
        "options": ["A potential harm or danger to an asset", "A software tool for cybersecurity", "A secure network segment", "A type of encryption method"],
        "correct_answer": "A potential harm or danger to an asset",
    },
    {
        "question": "What is 'vulnerability' in risk assessment?",
        "options": ["The strength of a security measure", "A known weakness that could be exploited", "A type of encryption key", "A type of network protocol"],
        "correct_answer": "A known weakness that could be exploited",
    },
    {
        "question": "What is 'likelihood' in risk assessment?",
        "options": ["The impact of a threat", "The probability of a threat occurring", "A type of password", "The cost of risk mitigation"],
        "correct_answer": "The probability of a threat occurring",
    },
    {
        "question": "What is 'impact' in risk assessment?",
        "options": ["The likelihood of a threat occurring", "The cost of risk mitigation", "The effect or harm caused by a threat", "The strength of a security measure"],
        "correct_answer": "The effect or harm caused by a threat",
    },
    {
        "question": "What is a 'risk assessment matrix' used for in cybersecurity?",
        "options": ["To encrypt data", "To visualize and prioritize risks based on likelihood and impact", "To remove malware", "To create strong passwords"],
        "correct_answer": "To visualize and prioritize risks based on likelihood and impact",
    },
    {
        "question": "What is 'risk mitigation' in risk assessment?",
        "options": ["A method for identifying threats", "A strategy for reducing the impact of risks", "A type of firewall", "A type of encryption method"],
        "correct_answer": "A strategy for reducing the impact of risks",
    },
    {
        "question": "What is 'residual risk' in risk assessment?",
        "options": ["The initial risk before any mitigation", "The risk that remains after mitigation efforts", "The risk of password breaches", "The likelihood of a threat occurring"],
        "correct_answer": "The risk that remains after mitigation efforts",
    },
    {
        "question": "What is 'risk acceptance' in risk assessment?",
        "options": ["A method for removing risks", "A decision to tolerate a certain level of risk without mitigation", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "A decision to tolerate a certain level of risk without mitigation",
    },
    {
        "question": "What is 'risk avoidance' in risk assessment?",
        "options": ["A method for identifying threats", "A strategy for reducing the impact of risks", "A decision to eliminate a risk by avoiding the associated activity or asset", "A type of password"],
        "correct_answer": "A decision to eliminate a risk by avoiding the associated activity or asset",
    },
    {
        "question": "What is 'risk transfer' in risk assessment?",
        "options": ["A method for removing risks", "A strategy for reducing the impact of risks", "A decision to shift the responsibility for a risk to a third party", "A type of encryption key"],
        "correct_answer": "A decision to shift the responsibility for a risk to a third party",
    },
    {
        "question": "What is a 'risk assessment framework' used for in cybersecurity?",
        "options": ["To create secure passwords", "To provide a structured approach to assess and manage risks", "To encrypt data", "To detect and remove malware"],
        "correct_answer": "To provide a structured approach to assess and manage risks",
    },
    {
        "question": "What is 'asset valuation' in risk assessment?",
        "options": ["A method for removing risks", "The process of assigning a value to an asset based on its importance", "A type of firewall", "A type of encryption method"],
        "correct_answer": "The process of assigning a value to an asset based on its importance",
    },
    {
        "question": "What is 'risk appetite' in risk assessment?",
        "options": ["The level of risk that is acceptable to an organization", "A method for identifying threats", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "The level of risk that is acceptable to an organization",
    },
    {
        "question": "What is 'risk register' in risk assessment?",
        "options": ["A list of all the risks in an organization", "A type of antivirus software", "A way to generate passwords", "A secure network segment"],
        "correct_answer": "A list of all the risks in an organization",
    },
    {
        "question": "What is 'risk communication' in risk assessment?",
        "options": ["A method for cleaning computers", "The process of sharing risk information with stakeholders", "A type of encryption", "A type of gardening"],
        "correct_answer": "The process of sharing risk information with stakeholders",
    },
    {
        "question": "What is a 'risk assessment report' used for in cybersecurity?",
        "options": ["To make security fun", "To communicate the results of a risk assessment, including identified risks and mitigation strategies", "To create complex passwords", "To block all network traffic"],
        "correct_answer": "To communicate the results of a risk assessment, including identified risks and mitigation strategies",
    },
    {
        "question": "What is 'threat modeling' in risk assessment?",
        "options": ["A method for identifying threats", "A process for evaluating and managing security threats and vulnerabilities", "A type of password", "A type of network protocol"],
        "correct_answer": "A process for evaluating and managing security threats and vulnerabilities",
    },
    {
        "question": "What is 'business impact analysis' in risk assessment?",
        "options": ["A type of financial analysis", "A method for removing risks", "The process of identifying critical business functions and their dependencies", "A type of encryption method"],
        "correct_answer": "The process of identifying critical business functions and their dependencies",
    },
    {
        "question": "What is 'risk assessment software' used for in cybersecurity?",
        "options": ["A tool for cleaning computers", "To identify and manage risks more efficiently", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "To identify and manage risks more efficiently",
    },
    {
        "question": "What is 'quantitative risk assessment' in cybersecurity?",
        "options": ["A method for removing risks", "An approach that uses data and metrics to assess and quantify risks", "A type of encryption key", "A type of malware"],
        "correct_answer": "An approach that uses data and metrics to assess and quantify risks",
    },
    {
        "question": "What is 'qualitative risk assessment' in cybersecurity?",
        "options": ["A process for evaluating risks", "An approach that uses data and metrics to assess and quantify risks", "A method for cleaning computers", "A type of network protocol"],
        "correct_answer": "A process for evaluating risks",
    },
    {
        "question": "What is 'risk treatment' in risk assessment?",
        "options": ["A method for removing risks", "The process of selecting and implementing risk mitigation measures", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "The process of selecting and implementing risk mitigation measures",
    },
    {
        "question": "What is a 'risk assessment checklist' used for in cybersecurity?",
        "options": ["To create secure passwords", "To provide a structured list of items to consider during a risk assessment", "To encrypt data", "To detect and remove malware"],
        "correct_answer": "To provide a structured list of items to consider during a risk assessment",
    },
    {
        "question": "What is a 'risk assessment team' in cybersecurity?",
        "options": ["A group of hackers", "A team of experts responsible for conducting risk assessments", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "A team of experts responsible for conducting risk assessments",
    },
    {
        "question": "What is 'risk monitoring' in risk assessment?",
        "options": ["A method for removing risks", "The ongoing process of tracking and assessing risks", "A strategy for reducing the impact of risks", "A type of encryption key"],
        "correct_answer": "The ongoing process of tracking and assessing risks",
    },
    {
        "question": "What is 'likelihood assessment' in risk assessment?",
        "options": ["A method for removing risks", "The evaluation of the probability of a threat occurring", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "The evaluation of the probability of a threat occurring",
    },
    {
        "question": "What is 'risk assessment methodology' used for in cybersecurity?",
        "options": ["To encrypt data", "A structured approach for conducting risk assessments", "To remove malware", "To create strong passwords"],
        "correct_answer": "A structured approach for conducting risk assessments",
    },
    {
        "question": "What is 'inherent risk' in risk assessment?",
        "options": ["The initial risk before any mitigation", "The risk that remains after mitigation efforts", "The risk of password breaches", "The likelihood of a threat occurring"],
        "correct_answer": "The initial risk before any mitigation",
    },
    {
        "question": "What is 'risk assessment policy' in cybersecurity?",
        "options": ["A type of password policy", "A documented set of guidelines and procedures for conducting risk assessments", "A type of network protocol", "A type of encryption method"],
        "correct_answer": "A documented set of guidelines and procedures for conducting risk assessments",
    },
    {
        "question": "What is 'risk assessment training' used for in cybersecurity?",
        "options": ["To train hackers", "To educate individuals on how to conduct risk assessments", "To create secure passwords", "To detect and remove malware"],
        "correct_answer": "To educate individuals on how to conduct risk assessments",
    },
    {
        "question": "What is 'risk assessment framework' in cybersecurity?",
        "options": ["A way to assess the risk of frameworks", "A structured approach for assessing and managing risks", "A type of firewall", "A type of encryption key"],
        "correct_answer": "A structured approach for assessing and managing risks",
    },
    {
        "question": "What is 'risk analysis' in risk assessment?",
        "options": ["A method for removing risks", "The process of identifying and evaluating risks", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "The process of identifying and evaluating risks",
    },
    {
        "question": "What is 'risk assessment process' in cybersecurity?",
        "options": ["To encrypt data", "A series of steps and activities to identify, assess, and manage risks", "To remove malware", "To create strong passwords"],
        "correct_answer": "A series of steps and activities to identify, assess, and manage risks",
    },
    {
        "question": "What is 'risk assessment tool' used for in cybersecurity?",
        "options": ["To create secure passwords", "Software or applications designed to assist in risk assessment processes", "To encrypt data", "To detect and remove malware"],
        "correct_answer": "Software or applications designed to assist in risk assessment processes",
    },
    {
        "question": "What is 'risk register template' in risk assessment?",
        "options": ["A template for creating a list of risks", "A type of network protocol", "A type of encryption method", "A secure network segment"],
        "correct_answer": "A template for creating a list of risks",
    },
    {
        "question": "What is 'risk assessment standard' in cybersecurity?",
        "options": ["A type of password standard", "A set of guidelines and principles for conducting risk assessments", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "A set of guidelines and principles for conducting risk assessments",
    },
    {
        "question": "What is 'security risk assessment' in cybersecurity?",
        "options": ["The process of assessing and managing risks to an organization's information security", "A type of encryption key", "A method for removing risks", "A type of malware"],
        "correct_answer": "The process of assessing and managing risks to an organization's information security",
    },
    {
        "question": "What is 'security risk assessment methodology' used for in cybersecurity?",
        "options": ["A method for removing risks", "A structured approach for conducting security risk assessments", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "A structured approach for conducting security risk assessments",
    },
    {
        "question": "What is 'risk identification' in risk assessment?",
        "options": ["A method for removing risks", "The process of identifying and documenting potential risks", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "The process of identifying and documenting potential risks",
    },
    {
        "question": "What is 'risk evaluation' in risk assessment?",
        "options": ["A method for removing risks", "The process of comparing identified risks against established criteria", "A type of firewall", "A type of encryption key"],
        "correct_answer": "The process of comparing identified risks against established criteria",
    },
    {
        "question": "What is 'risk control' in risk assessment?",
        "options": ["A method for removing risks", "The process of selecting and implementing risk mitigation measures", "A type of password", "A type of malware"],
        "correct_answer": "The process of selecting and implementing risk mitigation measures",
    },
    {
        "question": "What is 'risk assessment report' in cybersecurity?",
        "options": ["A type of password report", "A document that summarizes the results of a risk assessment", "A type of network protocol", "A type of encryption method"],
        "correct_answer": "A document that summarizes the results of a risk assessment",
    },
    {
        "question": "What is 'residual risk' in risk assessment?",
        "options": ["The initial risk before any mitigation", "The risk that remains after mitigation efforts", "The risk of password breaches", "The likelihood of a threat occurring"],
        "correct_answer": "The risk that remains after mitigation efforts",
    },
    {
        "question": "What is 'risk assessment software' used for in cybersecurity?",
        "options": ["To create secure passwords", "Software tools designed to assist in conducting risk assessments", "To encrypt data", "To remove malware"],
        "correct_answer": "Software tools designed to assist in conducting risk assessments",
    },
    {
        "question": "What is 'risk assessment template' in risk assessment?",
        "options": ["A template for assessing risks", "A type of firewall", "A type of encryption key", "A secure network segment"],
        "correct_answer": "A template for assessing risks",
    },
    {
        "question": "What is 'risk assessment matrix' in cybersecurity?",
        "options": ["A type of network matrix", "A visual tool used to assess and prioritize risks", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "A visual tool used to assess and prioritize risks",
    },
    {
        "question": "What is 'risk assessment workshop' in risk assessment?",
        "options": ["A method for removing risks", "A collaborative session involving stakeholders to identify and assess risks", "A type of password", "A type of malware"],
        "correct_answer": "A collaborative session involving stakeholders to identify and assess risks",
    },
    {
        "question": "What is 'threat and risk assessment' in cybersecurity?",
        "options": ["A type of encryption key", "The process of identifying and assessing threats and associated risks", "A method for removing risks", "A type of network protocol"],
        "correct_answer": "The process of identifying and assessing threats and associated risks",
    },
    {
        "question": "What is 'vulnerability assessment' in risk assessment?",
        "options": ["A method for removing vulnerabilities", "The process of identifying and assessing vulnerabilities in a system or network", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "The process of identifying and assessing vulnerabilities in a system or network",
    },
    {
        "question": "What is 'asset-based risk assessment' in cybersecurity?",
        "options": ["A method for assessing assets", "An approach that focuses on identifying and assessing risks to specific assets", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "An approach that focuses on identifying and assessing risks to specific assets",
    },
    {
        "question": "What is 'quantitative risk assessment' in risk assessment?",
        "options": ["A process for evaluating risks", "An approach that uses data and metrics to assess and quantify risks", "A method for cleaning computers", "A type of network protocol"],
        "correct_answer": "An approach that uses data and metrics to assess and quantify risks",
    },
    {
        "question": "What is 'qualitative risk assessment' in cybersecurity?",
        "options": ["A process for evaluating risks", "An approach that uses data and metrics to assess and quantify risks", "A method for cleaning computers", "A type of network protocol"],
        "correct_answer": "A process for evaluating risks",
    },
    {
        "question": "What is 'risk treatment' in risk assessment?",
        "options": ["A method for removing risks", "The process of selecting and implementing risk mitigation measures", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "The process of selecting and implementing risk mitigation measures",
    },
    {
        "question": "What is a 'risk assessment checklist' used for in cybersecurity?",
        "options": ["To create secure passwords", "To provide a structured list of items to consider during a risk assessment", "To encrypt data", "To detect and remove malware"],
        "correct_answer": "To provide a structured list of items to consider during a risk assessment",
    },
    {
        "question": "What is a 'risk assessment team' in cybersecurity?",
        "options": ["A group of hackers", "A team of experts responsible for conducting risk assessments", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "A team of experts responsible for conducting risk assessments",
    },
    {
        "question": "What is 'risk monitoring' in risk assessment?",
        "options": ["A method for removing risks", "The ongoing process of tracking and assessing risks", "A strategy for reducing the impact of risks", "A type of encryption key"],
        "correct_answer": "The ongoing process of tracking and assessing risks",
    },
    {
        "question": "What is 'likelihood assessment' in risk assessment?",
        "options": ["A method for removing risks", "The evaluation of the probability of a threat occurring", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "The evaluation of the probability of a threat occurring",
    },
    {
        "question": "What is 'risk assessment methodology' used for in cybersecurity?",
        "options": ["To encrypt data", "A structured approach for conducting risk assessments", "To remove malware", "To create strong passwords"],
        "correct_answer": "A structured approach for conducting risk assessments",
    },
    {
        "question": "What is 'inherent risk' in risk assessment?",
        "options": ["The initial risk before any mitigation", "The risk that remains after mitigation efforts", "The risk of password breaches", "The likelihood of a threat occurring"],
        "correct_answer": "The initial risk before any mitigation",
    },
    {
        "question": "What is 'risk assessment policy' in cybersecurity?",
        "options": ["A type of password policy", "A documented set of guidelines and procedures for conducting risk assessments", "A type of network protocol", "A type of encryption method"],
        "correct_answer": "A documented set of guidelines and procedures for conducting risk assessments",
    },
    {
        "question": "What is 'risk assessment training' used for in cybersecurity?",
        "options": ["To train hackers", "To educate individuals on how to conduct risk assessments", "To create secure passwords", "To detect and remove malware"],
        "correct_answer": "To educate individuals on how to conduct risk assessments",
    },
    {
        "question": "What is 'risk assessment framework' in cybersecurity?",
        "options": ["A way to assess the risk of frameworks", "A structured approach for assessing and managing risks", "A type of firewall", "A type of encryption key"],
        "correct_answer": "A structured approach for assessing and managing risks",
    },
    {
        "question": "What is 'risk analysis' in risk assessment?",
        "options": ["A method for removing risks", "The process of identifying and evaluating risks", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "The process of identifying and evaluating risks",
    },
    {
        "question": "What is 'risk assessment process' in cybersecurity?",
        "options": ["To encrypt data", "A series of steps and activities to identify, assess, and manage risks", "To remove malware", "To create strong passwords"],
        "correct_answer": "A series of steps and activities to identify, assess, and manage risks",
    },
    {
        "question": "What is 'risk assessment tool' used for in cybersecurity?",
        "options": ["To create secure passwords", "Software or applications designed to assist in risk assessment processes", "To encrypt data", "To detect and remove malware"],
        "correct_answer": "Software or applications designed to assist in risk assessment processes",
    },
    {
        "question": "What is 'risk register template' in risk assessment?",
        "options": ["A template for creating a list of risks", "A type of network protocol", "A type of encryption method", "A secure network segment"],
        "correct_answer": "A template for creating a list of risks",
    },
    {
        "question": "What is 'risk assessment standard' in cybersecurity?",
        "options": ["A type of password standard", "A set of guidelines and principles for conducting risk assessments", "A way to generate passwords", "A type of firewall"],
        "correct_answer": "A set of guidelines and principles for conducting risk assessments",
    },
    {
        "question": "What is 'security risk assessment' in cybersecurity?",
        "options": ["The process of assessing and managing risks to an organization's information security", "A type of encryption key", "A method for removing risks", "A type of malware"],
        "correct_answer": "The process of assessing and managing risks to an organization's information security",
    },
    {
        "question": "What is 'security risk assessment methodology' used for in cybersecurity?",
        "options": ["A method for removing risks", "A structured approach for conducting security risk assessments", "A type of antivirus software", "A type of encryption method"],
        "correct_answer": "A structured approach for conducting security risk assessments",
    },
    {
        "question": "What is 'risk identification' in risk assessment?",
        "options": ["A method for removing risks", "The process of identifying and documenting potential risks", "A strategy for reducing the impact of risks", "A type of network protocol"],
        "correct_answer": "The process of identifying and documenting potential risks",
    },
    {
        "question": "What is 'risk evaluation' in risk assessment?",
        "options": ["A method for removing risks", "The process of comparing identified risks against established criteria", "A type of firewall", "A type of encryption key"],
        "correct_answer": "The process of comparing identified risks against established criteria",
    },
    {
        "question": "What is 'risk control' in risk assessment?",
        "options": ["A method for removing risks", "The process of selecting and implementing risk mitigation measures", "A type of password", "A type of malware"],
        "correct_answer": "The process of selecting and implementing risk mitigation measures",
    },
    {
        "question": "What is 'risk assessment report' in cybersecurity?",
        "options": ["A type of password report", "A document that summarizes the results of a risk assessment", "A type of network protocol", "A type of encryption method"],
        "correct_answer": "A document that summarizes the results of a risk assessment",
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
root.title("Risk Sentinel")
root.configure(bg="lightblue")

# Create title label
title_label = tk.Label(root, text="RISK SENTINEL", font=("Helvetica", 24, "bold"), bg="lightblue", fg="blue")
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