import telebot
import sys
sys.path.append("/home/dave/PYrojects/TableStation/TableStation/")
import importlib.util
from main_token import token
import logging
from app.models import Base, DHT11Table
from app import app,session
from logging.config import fileConfig


fileConfig('logging.conf')
logger = logging.getLogger()
logger.debug('launching ButlerBot')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there """)

@bot.message_handler(commands=["temperature"])
def get_sensor_data(message):
    humid = session.query(DHT11Table).order_by(DHT11Table.id.desc()).limit(1)
    temp = session.query(DHT11Table).order_by(DHT11Table.id.desc()).limit(1)
    responce = humid.getHumidity + " " + temp.getTemperature

    bot.send_message(message.chat.id, responce)
"""
def send_temperature(message):
    with open('/home/dave/PYrojects/Temperature_log/cpu_current_temp.csv', 'r') as temperature_file:
        responce = temperature_file.read()
    bot.send_message(message.chat.id, responce)
"""


if __name__ == '__main__':
    bot.polling(none_stop=True)

