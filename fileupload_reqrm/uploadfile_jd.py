from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient
from urllib.parse import quote

import os

app = Flask(__name__)

# Azure Storage Account details
account_name = "myserverstg"
account_key = "+mipruK1Bg7VJupMMh8hP0cPZzmfNBXZKgFXkwKlOcYcsOiwNXz51oq2RGd4YAhkj13+mGTXHL1E+AStbvwa5Q=="
container_name = "unprocecedresume"
connection_string = "DefaultEndpointsProtocol=https;AccountName=myserverstg;AccountKey=+mipruK1Bg7VJupMMh8hP0cPZzmfNBXZKgFXkwKlOcYcsOiwNXz51oq2RGd4YAhkj13+mGTXHL1E+AStbvwa5Q==;EndpointSuffix=core.windows.net"
@app.route('/uploadresume', methods=['POST'])
def upload_file():
    try:
        request_num_nm = request.args.get('requestid')
        request_num = request_num_nm.lower()

        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # List blobs in the container
        blobs = container_client.walk_blobs(name_starts_with=request_num)
        # Check if the folder exists
        folder_exists = any(blob.name.startswith(request_num) for blob in blobs)
        
        if  folder_exists:

                # Check if files are present in the request
            if 'file' not in request.files:
                  return jsonify({"status": "error", "message": "No files provided"}), 400

                 # Get the files from the request
            files = request.files.getlist('file')

            for file in files:
                file_blob_name = f"{request_num}/{request_num}_{file.filename}"
                blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_blob_name)
        
                data = file.stream.read()
                blob_client.upload_blob(data, blob_type="BlockBlob")        
                return jsonify({"status": "success", "message": "File uploaded successfully"})
        else :

                # Check if files are present in the request
            if 'file' not in request.files:
                  return jsonify({"status": "error", "message": "No files provided"}), 400

                 # Get the files from the request
            files = request.files.getlist('file')

            for file in files:
                file_blob_name = f"{request_num}/{request_num}_{file.filename}"
                blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_blob_name)

                data = file.stream.read()
                blob_client.upload_blob(data, blob_type="BlockBlob")
                return jsonify({"status": "success", "message": "File uploaded successfully"})

    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
