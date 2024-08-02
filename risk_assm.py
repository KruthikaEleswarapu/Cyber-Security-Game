# Define a list of risk factors for the project.
risk_factors = [
    {
        "name": "Resource Constraints",
        "description": "Limited budget and staff resources.",
        "impact": "High impact on project success.",
        "likelihood": "Moderate likelihood of occurring.",
    },
    {
        "name": "Technology Dependency",
        "description": "Dependent on a critical but potentially unreliable technology.",
        "impact": "High impact on project success.",
        "likelihood": "Low likelihood of occurring.",
    },
    {
        "name": "Scope Creep",
        "description": "Constantly changing project requirements.",
        "impact": "Moderate impact on project success.",
        "likelihood": "High likelihood of occurring.",
    },
]

# Function to assess and manage risks.
def assess_and_manage_risks():
    print("Welcome to the Risk Assessment Game!")
    print("You are managing a project, and you need to assess and manage potential risks.")
    
    total_score = 0

    for risk in risk_factors:
        print("\nRisk Factor:", risk["name"])
        print("Description:", risk["description"])
        print("Impact:", risk["impact"])
        print("Likelihood:", risk["likelihood"])

        choice = input("Do you want to (a) Accept, (m) Mitigate, or (i) Ignore this risk? ").lower()

        if choice == "a":
            print("You accepted the risk.")
            score = 0
        elif choice == "m":
            print("You decided to mitigate the risk.")
            score = 1
        elif choice == "i":
            print("You ignored the risk.")
            score = -1
        else:
            print("Invalid choice. The risk has been ignored.")
            score = -1

        total_score += score

    print("\nRisk Assessment Completed!")
    print("Total Risk Score:", total_score)

    if total_score < 0:
        print("You have unmanaged risks. The project is at high risk.")
    elif total_score == 0:
        print("You have accepted all risks. The project has moderate risk.")
    else:
        print("You have successfully mitigated all risks. The project is at low risk.")

# Run the risk assessment game.
assess_and_manage_risks()
