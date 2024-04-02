# server.py

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/analyze')
def analyze_resume():
    log_url = request.args.get('log_url')
    jd_url = request.args.get('jd_url')

    # Make requests to log_url and jd_url
    log_response = requests.get(log_url)
    jd_response = requests.get(jd_url)

    # Perform analysis

    # Example: Just return the contents of log_url and jd_url
    result = f"Log URL content: {log_response.text}<br />JD URL content: {jd_response.text}"

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

