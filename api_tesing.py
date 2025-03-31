import json
import os
import requests
from dotenv import load_dotenv

# 88 Doc link: https://docs.browserless.io/baas/http-apis/content


# def run_test(website):
#     import requests

#     TOKEN = "*****************************************"
#     url = f"https://production-sfo.browserless.io/content?token={TOKEN}"
#     headers = {
#         "Cache-Control": "no-cache",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "url": "https://igrmaharashtra.gov.in/"
#     }

#     response = requests.post(url, headers=headers, json=data)
#     print(response.text) 



if __name__ == "__main__":
    website= "https://docs.browserless.io/baas/http-apis/"
    # website= "https://www.makemytrip.com/tripideas/places/"
    load_dotenv()
    browserless_api = os.getenv("BROWSERLESS_API_KEY")
    url = f"https://chrome.browserless.io/content?token={browserless_api}"
    payload = json.dumps({"url": website})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)