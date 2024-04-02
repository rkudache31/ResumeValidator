#!/usr/bin/env python
import fitz
import openai
# Import necessary modules
import fitz
from docx import Document
from flask import Flask, request, jsonify
from openai import OpenAI
import os
import requests
import json
import mysql.connector

# Initialize Flask application
app = Flask(__name__)

# OpenAI API key
openai.api_key = "mytestravsk-TtN2pd19WpnAokeULuBpT3BlbkFJaimaN0siwQTK0i2bS64R"

def download_file(url, local_filename):
    with requests.get(url, stream=True) as response:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

# Function to get OpenAI completion
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = OpenAI().chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    raw_input = response.choices[0].message
    return raw_input.content

# Function to read log file content
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        log_content = file.read()
    return log_content

# Function to convert docx to string
def docx_to_string(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

# Function to convert pdf to string
def pdf_to_string(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    num_pages = pdf_document.page_count
    for page_num in range(num_pages):
        page = pdf_document[page_num]
        text += page.get_text()
    pdf_document.close()
    return text

# Function to check if file is a pdf
def is_pdf_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.pdf'



def extract_info(rwdata):
    #raw_data = rwdata.text
#    rawinfo=rwdata.data.decode('utf-8')
    #data = json.loads(rwdata)
    #data = rwdata["candidate_info"]
    #candidate_info = data.get("candidate_info", "")

    # Split the data by newline delimiter
    lines = rwdata.split('\n')

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
            score = line.split(': ')[1]

    return candidate_name, email, contact_number, experience, score


# Flask route to handle GET requests
@app.route('/analyze', methods=['GET'])
def analyze_resume():
    # Get URLs from query parameters

    arg1_log_url = request.args.get('log_url')
    arg2_jd_url = request.args.get('jd_url')

    if not arg1_log_url or not arg2_jd_url:
        return jsonify({"error": "Missing log_url or jd_url parameters"}), 400

    # Extract filenames from URLs
    log_filename = os.path.basename(arg1_log_url)
    jd_filename = os.path.basename(arg2_jd_url)

    # Download the files
    download_file(arg1_log_url, log_filename)
    download_file(arg2_jd_url, jd_filename)
    cv=log_filename
    jd=jd_filename

    # Reading log file content
    jd_content = read_log_file(jd)

    if is_pdf_file(cv):
        log_content = pdf_to_string(cv)
    else:
        log_content = docx_to_string(cv)

    prompt = f"Score provided resume on provided Job decription {jd_content}  and : please check given resume \n{log_content}\n Score the resume and also overall score outof 10 explain more experince from resume\n{log_content}\n, give sepreatly to upload excel."
    response_data = get_completion(prompt)
    prompt = f" candidate name,email id , contactnumber,total experince,overall score,  from resume\n{log_content}\n, give sepreatly to upload excel."
    response_info = get_completion(prompt)
    #print(response_info)
    #data=jsonify({"data": response_data,"candidate_info":response_info})
    candidate_name,email,contact_number,experience,score = extract_info(response_info)
#    return type(jsonify({"candidate_info":response_info}))
    #print(jsonify({"candidate_info":response_info}))
    candidate_data=response_data
#    return jsonify({"candidate_name": candidate_name, "email": email, "contact_number": contact_number, "experience": experience, "score": score})

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
            data_insert = (candidate_name,1,'Devops',candidate_data,email,contact_number,score,arg1_log_url )

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

    #return(candidate_name,email,contact_number,experience,score)
    return jsonify(response_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


