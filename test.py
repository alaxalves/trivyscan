import requests
from requests.auth import HTTPBasicAuth

def docker_login():
    try:
        response = requests.get(
            f"https://{NEXUS_REGISTRY}/v2/", 
            auth=HTTPBasicAuth(NEXUS_USERNAME, NEXUS_PASSWORD)
        )
        
        if response.status_code == 200:
            print("Login successful")
        else:
            print(f"Failed to login, status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error during Docker login: {e}")

docker_login()
