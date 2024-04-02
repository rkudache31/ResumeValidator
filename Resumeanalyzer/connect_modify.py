import requests
import re
import json
import mysql.connector

url = "http://52.147.172.204:5000/analyze"
payload = {
    "log_url": "https://myserverstg.blob.core.windows.net/resumestore/sampleresume_ai.pdf",
    "jd_url": "https://myserverstg.blob.core.windows.net/resumestore/jd.txt"
}
headers = {}

response = requests.get(url, params=payload, headers=headers, verify=False)  # Setting verify=False to ignore SSL verification (use with caution)
data = response.text
print(data)

#rwdata="raw_data =" + data + "\n"

#def extract_info(data):
    # Extracting email using regex
    #email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', input_json)
    #email = email.group(0) if email else None


    # Extracting contact number using regex
    #contact_number = re.search(r'(\d{10})', input_json)
    #contact_number = contact_number.group(0) if contact_number else None

    # Extracting total experience using regex
    #experience = re.search(r'(\d+ year[s]?)', input_json)
    #experience = experience.group(0) if experience else None

    #score = re.search(r'Resume Score: (\d+/\d+)', input_json['result']).group(1)
    #candidate_name = re.search(r'The resume of (.+?) can', input_json['result']).group(1)
    

    # Constructing the result JSON
#    result = {
#        "result": f"Email: {email}\nContact Number: {contact_number}\nTotal Experience: {experience}\n\nPlease upload the resume separately for further review."
#    }

# Define regular expressions to extract information
#    name_pattern = r"Candidate Name: ([^\n]+)"
#    email_pattern = r"Email(?: ID)?: ([^\n]+)"
#    contact_pattern = r"Contact Number: ([^\n]+)"
#    experience_pattern = r"Total Experience: ([^\n]+)"
#    score_pattern = r"Overall Score: ([^\n]+)"

# Extract information using regular expressions
#    candidate_name = re.search(name_pattern, data).group(1)
#    email = re.search(email_pattern, data).group(1)
#    contact_number = re.search(contact_pattern, data).group(1)
#    experience = re.search(experience_pattern, data).group(1)
#    score = re.search(score_pattern, data).group(1)
    #print("updated info "+ email,contact_number,experience,score,candidate_name)
#    return(candidate_name,email,contact_number,experience,score)

def extract_info(rwdata):
    rawinfo=json.loads(rwdata)
    data = rawinfo.get("candidate_info", "")

    # Split the data by newline delimiter
    lines = data.split('\n')

    # Initialize variables
    candidate_name = None
    email = None
    contact_number = None
    experience = None
    overall_score = None

    # Iterate over each line to extract information
    for line in lines:
        if line.startswith('Candidate Name:'):
            candidate_name = line.split(': ')[1]
        elif line.startswith('Email:'):
            email = line.split(': ')[1]
        elif line.startswith('Contact Number:'):
            contact_number = line.split(': ')[1]
        elif line.startswith('Total Experience:'):
            experience = line.split(': ')[1]
        elif line.startswith('Overall Score:'):
            overall_score = line.split(': ')[1]

    return candidate_name, email, contact_number, experience, overall_score




candidate_name,email,contact_number,experience,score = extract_info(data)
print("\n candidate  "+ candidate_name +" \n")
print("email "+ str(email) +"\n")
print("contact  "+ contact_number +" \n")
print("iexp  "+ experience +" \n")
print("score  "+ score +" \n")




