import requests

# WhatsApp Business API endpoint URL
api_url = "https://api.whatsapp.com/send?phone=9730551007&text=test"

# Replace PHONE_NUMBER with the recipient's phone number (including country code)
# Replace YOUR_MESSAGE with the message you want to send

# Make the API call
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
        print("API call successful!")
else:
            print(f"API call failed with status code: {response.status_code}")

