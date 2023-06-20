#This is the main file that helps to run the bot properly.

from pyrogram import Client, filters
import os

bot=Client(
    "My_path_Bot",
    api_id = 26636840,
    api_hash = "1c1e44c655ad55989989671c912d1a17",
    bot_token = "6294637176:AAH0fKes1oIPlPVGNUcFrJHVsXCvHUPwLhY"
)

@bot.on_message(filters.command("start"))
async def start(client, message):
  await bot.send_message(message.chat.id, "Hello user, This is a very simple bot.")
  
bot.run()  
  
  
