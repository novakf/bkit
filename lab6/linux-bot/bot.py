from subprocess import check_output
import telebot
from telebot import types
import time

API_TOKEN = "5988847313:AAGTPwkaWliNHySNqxhSuZdmfmARxn8Jgik"

bot = telebot.TeleBot(API_TOKEN)
user_id = 1513374550

@bot.message_handler(content_types=["text"])
def main(message):
   if (user_id == message.chat.id):
      comand = message.text
      markup = types.InlineKeyboardMarkup() 
      button = types.InlineKeyboardButton(text="Повторить", callback_data=comand)
      markup.add(button)
      try:
         bot.send_message(user_id, check_output(comand, shell = True),  reply_markup = markup)
      except:
         bot.send_message(user_id, "Invalid input / no output")
   else:
      bot.send_message(user_id, "Invalid USER id")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  comand = call.data
  try:
     markup = types.InlineKeyboardMarkup()
     button = types.InlineKeyboardButton(text="Повторить", callback_data=comand)
     markup.add(button) 
     bot.send_message(user_id, check_output(comand, shell = True), reply_markup = markup)
  except:
     bot.send_message(user_id, "Invalid input / no output")

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)#в случае падения