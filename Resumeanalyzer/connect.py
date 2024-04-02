import requests
import re
import json
import mysql.connector

#url = "http://172.210.90.153/validate/analyze"
url = "http://52.147.172.204:5000/analyze"
payload = {
    "log_url": "https://myserverstg.blob.core.windows.net/resumestore/sampleresume_ai.pdf",
    "jd_url": "https://myserverstg.blob.core.windows.net/resumestore/jd.txt"
}
headers = {}

candidate_name = requests.get(url, params=payload, headers=headers, verify=False)  # Setting verify=False to ignore SSL verification (use with caution)
#data = response.text

print(candidate_name)
'''
def extract_info(input_json):
    # Extracting email using regex
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', input_json)
    email = email.group(0) if email else None

    # Extracting contact number using regex
    contact_number = re.search(r'(\d{10})', input_json)
    contact_number = contact_number.group(0) if contact_number else None

    # Extracting total experience using regex
    experience = re.search(r'(\d+ year[s]?)', input_json)
    experience = experience.group(0) if experience else None

    #score = re.search(r'Resume Score: (\d+/\d+)', input_json['result']).group(1)
    #candidate_name = re.search(r'The resume of (.+?) can', input_json['result']).group(1)


    # Constructing the result JSON
    result = {
        "result": f"Email: {email}\nContact Number: {contact_number}\nTotal Experience: {experience}\n\nPlease upload the resume separately for further review."
    }
    return(email,contact_number,experience)


email,contact_number,experience = extract_info(data)
#print(output_json)



# Establishing a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host="57.151.34.90",
        user="hr",
        password="hr123",
        database="resumedetails"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Creating a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example insert command
        insert_query = "INSERT INTO candidate (candidate_name, jobid,job,score_details,email,contactnumber,score,resumelink) VALUES (%s,%s, %s,%s, %s,%s, %s,%s)"
        # Example data to be inserted
        data_insert = ('Ravi k',1,'Devops',data,email,contact_number,'8','https://myserverstg.blob.core.windows.net/resumestore/sampleresume_ai.pdf' )

        # Executing the insert command
        print("Insert comman running")
        cursor.execute(insert_query, data_insert)

        # Committing the transaction
        connection.commit()

        print("Insert command executed successfully")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

finally:
    # Closing the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
'''
