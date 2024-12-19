from telebot.async_telebot import AsyncTeleBot
from misc.keyboards import create_keyboard, menu_keyboard, settings_keyboard
from data.messages import BACK_MSG, SETTINGS_MSG

def other_handlers(bot: AsyncTeleBot):
    # @bot.message_handler(func=lambda message: True)
    # async def echo_message(message):
    #     try:
    #         await bot.delete_message(message.chat.id, message.message_id)
    #     except Exception as e:
    #         print(f"Ошибка при удалении сообщения: {e}")

    @bot.message_handler(func=lambda message: message.text == "↩️ Вернуться назад")
    async def back_handler(message):
        try:
            await bot.delete_state(chat_id=message.chat.id, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, BACK_MSG, reply_markup=create_keyboard(menu_keyboard))
        except Exception as e:
            print(f"Ошибка при сбросе состояния: {e}")


    @bot.message_handler(func=lambda message: message.text == "⚙️ Настройки")
    async def settings_handler(message):
        try:
            await bot.send_message(message.chat.id, SETTINGS_MSG, reply_markup=create_keyboard(settings_keyboard))
        except Exception as e:
            print(f"Ошибка {e}")