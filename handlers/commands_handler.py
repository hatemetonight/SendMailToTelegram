from telebot.async_telebot import AsyncTeleBot
from data.messages import MAIL_NOT_FOUND_MSG, MENU_MSG
from misc.keyboards import create_keyboard, start_keyboard, menu_keyboard


def register_handlers(bot: AsyncTeleBot):
    @bot.message_handler(commands=['help', 'start'])
    async def send_welcome(message):
        await bot.send_message(message.chat.id, MAIL_NOT_FOUND_MSG, reply_markup=create_keyboard(start_keyboard))
        await bot.send_message(message.chat.id, MENU_MSG, reply_markup=create_keyboard(menu_keyboard))

