import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def is_item_in_stock(product_url, tag, attr_key, attr_val, sold_out_label):
    current_time = f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}]'

    try:
        page = requests.get(product_url, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        print(current_time, "Connection error occured")
        return False
    except Exception as e:
        print(current_time, e)
        return False

    soup = BeautifulSoup(page.content, 'html.parser')
    buy_text = soup.find(tag, attrs={attr_key:attr_val}).getText().strip()
    
    status_code = f'[{page.status_code}]'

    print(current_time, status_code, product_url, buy_text)

    return sold_out_label not in buy_text