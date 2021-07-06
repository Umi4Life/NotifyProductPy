import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
PRODUCT_URL = os.getenv("PRODUCT_URL")
BUTTON_TAG_ID = os.getenv("BUTTON_TAG_ID")
TELEGRAM_API_ENDPOINT = os.getenv("TELEGRAM_API_ENDPOINT")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
TELEGRAM_API_ENDPOINT_PARAMS = {
    'chat_id': TELEGRAM_CHAT_ID, 
    'text': PRODUCT_URL + " is in stock!"
}

def isItemInStock():
    currentTime = f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}]'

    try:
        page = requests.get(PRODUCT_URL, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        print(currentTime, "Connection error occured")
        return False
    except Exception as e:
        print(currentTime, e)
        return False


    soup = BeautifulSoup(page.content, 'html.parser')
    buyButtonText = soup.find(id=BUTTON_TAG_ID).getText().strip()
    
    statusCode = f'[{page.status_code}]'

    print(currentTime, statusCode, PRODUCT_URL, buyButtonText)

    return "Sold Out" not in buyButtonText

def notify():
    requests.post(url = TELEGRAM_API_ENDPOINT, params=TELEGRAM_API_ENDPOINT_PARAMS) 

while 1:
    if isItemInStock():
        notify()
    time.sleep(5) 