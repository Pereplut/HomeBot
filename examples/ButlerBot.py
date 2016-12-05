#!/usr/bin/python3.4
import telebot

from main_token import token

#API_TOKEN = '231105610:AAGnsQ2EX4nm3fuDTYlJC1e-43oIzGN4E3c'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there """)

@bot.message_handler(commands=["temperature"])
def send_temperature(message):
    with open('/home/dave/PYrojects/Temperature_log/cpu_current_temp.csv','r') as temperature_file:
        responce=temperature_file.read()
    bot.send_message(message.chat.id, responce)

if __name__ == '__main__':
    bot.polling(none_stop=True)

