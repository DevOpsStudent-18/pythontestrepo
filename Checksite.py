
import requests

def check_website_status(url):
    try:
        response = requests.get(url )
        if response.status_code == 200:
            print(f" The website '{url}' is up and running!")
        else:
            print(f" The website '{url}' returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" The website '{url}' is down or unreachable. Error: {e}")


check_website_status("https://www.google.com/")
