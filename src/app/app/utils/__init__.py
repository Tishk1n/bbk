from os import getenv

from aiogram import Bot

bot: Bot = Bot(token=getenv('token'))
