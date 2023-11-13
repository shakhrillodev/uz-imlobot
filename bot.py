"""
This is a echo bot.
It echoes any incoming text messages.
"""

from transliterate import to_latin, to_cyrillic
from aiogram import Bot, Dispatcher, executor, types
from checker import word_check
import logging

API_TOKEN = 'YOUR BOT TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nKrill-lotin botga xush kelibsiz!!!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Gap yuboring!!!")

@dp.message_handler()
async def kr2lt(message: types.Message):
    msg = message.text
    islatin = msg.isascii()
    krl = to_cyrillic(msg) if islatin else msg
    response = word_check(krl)
    text = ("✅"+msg if response["available"] else f"❌{msg}\n✅"+(to_latin("\n✅".join(response["matches"])) if islatin else f"❌{msg}\n✅"+"\n✅".join(response["matches"])))
    await message.reply(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
