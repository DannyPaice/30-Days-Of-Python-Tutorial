
def extract_from_emails(file="Day_19-Modules/Exercises_level_2/email_exchange_big.txt"):
    with open(file, "r") as f:
        lines = f.readlines()
    
    emails = []
    for line in lines:
        if line[:4] == "From":
            email = line.strip().split()
            if email[1] not in emails:
                emails.append(email[1])
    
    return emails

print(extract_from_emails())