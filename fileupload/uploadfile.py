from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient
from urllib.parse import quote

import os

app = Flask(__name__)

# Azure Storage Account details
account_name = "myserverstg"
account_key = "+mipruK1Bg7VJupMMh8hP0cPZzmfNBXZKgFXkwKlOcYcsOiwNXz51oq2RGd4YAhkj13+mGTXHL1E+AStbvwa5Q=="
container_name = "invoice"

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
                # Check if files are present in the request
        if 'file' not in request.files:
              return jsonify({"status": "error", "message": "No files provided"}), 400

        # Get the files from the request
        files = request.files.getlist('file')

        for file in files:
            blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
        
            data = file.stream.read()
            blob_client.upload_blob(data, blob_type="BlockBlob")        
            return jsonify({"status": "success", "message": "File uploaded successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
