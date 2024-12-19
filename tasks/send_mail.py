import asyncio
from telebot.async_telebot import AsyncTeleBot
from misc.config_loader import config


async def periodic_sender(bot: AsyncTeleBot):
    CHAT_IDS = config["CHAT_IDS"]
    while True:
        for chat_id in CHAT_IDS:
            try:
                await bot.send_message(chat_id, "Это периодическое сообщение!")
            except Exception as e:
                print(f"Ошибка отправки сообщения в чат {chat_id}: {e}")
                continue
        await asyncio.sleep(config["TIME_SEND"])
