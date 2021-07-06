from flask import Flask
from flask import request
from threading import Thread
from check_item import is_item_in_stock

app = Flask('')

@app.route('/')
def main():
  return "Bot Is Alive"

@app.route('/check')
def check():
  url = request.args.get('url')
  tag = request.args.get('tag')
  attr_key = request.args.get('attr_key')
  attr_val = request.args.get('attr_val')
  sold_out_label = request.args.get('sold_out_label')

  return str(is_item_in_stock(url, tag, attr_key, attr_val, sold_out_label))

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()