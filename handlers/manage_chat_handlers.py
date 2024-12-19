from telebot.async_telebot import AsyncTeleBot
from misc.config_loader import add_value_to_config, remove_value_from_config, config
from misc.keyboards import create_keyboard, back_keyboard, admin_keyboard


def manage_chat_handlers(bot: AsyncTeleBot):
    @bot.message_handler(func=lambda message: message.text == "➕ Добавить чат")
    async def add_chat(message):
        await bot.send_message(message.chat.id, "Введите ID чата для добавления:"
                               , reply_markup=create_keyboard(back_keyboard))
        
        @bot.message_handler(func=lambda msg: msg.text.isdigit())
        async def process_chat_id(msg):
            chat_id = int(msg.text)
            add_value_to_config("CHAT_IDS", chat_id)
            await bot.send_message(msg.chat.id, f"Чат с ID {chat_id} добавлен.", reply_markup=create_keyboard(admin_keyboard))


    @bot.message_handler(func=lambda message: message.text == "❌ Удалить чат")
    async def remove_chat(message):
        await bot.send_message(message.chat.id, "Введите ID чата для удаления:"
                               , reply_markup=create_keyboard(back_keyboard))
        
        @bot.message_handler(func=lambda msg: msg.text.isdigit())
        async def process_remove_chat_id(msg):
            chat_id = int(msg.text)
            
            if chat_id in config.get("CHAT_IDS", []):
                remove_value_from_config("CHAT_IDS", chat_id)
                await bot.send_message(msg.chat.id, f"Чат с ID {chat_id} удален.", reply_markup=create_keyboard(admin_keyboard))
            else:
                await bot.send_message(msg.chat.id, f"Чат с ID {chat_id} не найден.")