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

# Initialize Flask application
app = Flask(__name__)

# OpenAI API key
openai.api_key = "<<---APIKey------------>>"

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

    prompt = f"Score provided resume on provided Job decription {jd_content}  and : please check given resume \n{log_content}\n Score the resume and also overall score outof 10 give sepreatly to upload excel."
    response = get_completion(prompt)

    return jsonify({"result": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

