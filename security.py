def handle_security_incident(incident_type):
    if incident_type == "malware":
        print("Isolate affected system, run antivirus scan, and report the incident to IT.")
    elif incident_type == "data_breach":
        print("Identify and contain the breach, report it to data protection authorities, and notify affected parties.")
    else:
        print("Handle the incident according to the established incident response plan.")

incident_type = input("Enter the type of security incident (malware, data_breach, other): ")
handle_security_incident(incident_type)
