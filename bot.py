"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from wikitest import sendWikiUz

API_TOKEN = '5994723715:AAEQNqCOeatSspLj-qvGoXDhAojcThC8Lo0'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Wikipedia botiga xush kelibsiz!")



@dp.message_handler()
async def echo(message: types.Message):
    summury = sendWikiUz(message.text)
    await message.reply(summury)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)