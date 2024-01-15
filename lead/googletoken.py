import requests
import json
from rest_framework.response import Response
from rest_framework import status


def verify_not_robot_func(token):
    captcha_data = {
        'secret': '6LcBrkkpAAAAAB_RHKQ5Cw-4YxJn_FxtE00Msb-l',
        'response': token
    }

    # Send a POST request to Google's reCAPTCHA verification endpoint
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=captcha_data)
    
    # Parse the response as JSON
    result = json.loads(response.text)
    
    # Check if the verification was successful
    if result['success']:
        return "humman"
    else:
        # If verification fails, return a response with an error message
        return Response({"error": "You are not a human"}, status=status.HTTP_400_BAD_REQUEST)
