from aiogram import types, Dispatcher
from create_bot import bot

async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Даня лох')



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)