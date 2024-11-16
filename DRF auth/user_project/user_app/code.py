import requests


url = 'http://127.0.0.1:8000/api/logout/'  # Replace with your actual logout URL


token = 'db13c6d0c0a93d591baf39197b32374c404f4b94'  # Replace with the user's actual token

headers = {
    'Authorization': f'Token {token}'
}


response = requests.post(url, headers=headers)


if response.status_code == 200:
    print("Successfully logged out.")
else:
    print("Logout failed.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())  # Display the error message if any