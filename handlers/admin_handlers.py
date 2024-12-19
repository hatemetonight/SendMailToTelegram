from telebot.async_telebot import AsyncTeleBot
from data.messages import NO_ADMIN_MSG, ADMIN_MSG
from misc.keyboards import create_keyboard, admin_keyboard
from filters.user_filters import is_admin
from handlers.commands_handler import register_handlers


def admin_menu_handlers(bot: AsyncTeleBot):
    @bot.message_handler(commands=['admin'])
    async def send_welcome(message):
        if not is_admin(message.from_user.id):
            await bot.send_message(message.chat.id, NO_ADMIN_MSG)
            return register_handlers(bot)
        else:
            await bot.send_message(message.chat.id, ADMIN_MSG, reply_markup=create_keyboard(admin_keyboard))
