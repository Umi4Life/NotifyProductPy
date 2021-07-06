import asyncio
import os
from check_item import is_item_in_stock
import discord
from keep_alive import keep_alive
import pandas as pd

BOT_TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

async def background_task():
   await client.wait_until_ready()
   channel = client.get_channel(861933719748476948)
   while not client.is_closed():
      items = pd.read_csv('notify/items.csv', header=0).to_dict('index')
      for i in items:
        item = items[i]
        if is_item_in_stock(
            item['url'], 
            item['tag'], 
            item['attr_key'], 
            item['attr_val'], 
            item['sold_out_label']):
          await channel.send("ITEM IS AVAILABLE" + '\n' + item['url'])
      await asyncio.sleep(600)

keep_alive()
client.loop.create_task(background_task())
client.run(BOT_TOKEN)