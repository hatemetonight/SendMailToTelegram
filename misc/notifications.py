from telebot.async_telebot import AsyncTeleBot
from data.messages import STARTUP_MSG
from misc.config_loader import config


async def startup_notification(bot: AsyncTeleBot):
    for admin_id in config.get("ADMIN_LIST", []):
        try:
            await bot.send_message(admin_id, STARTUP_MSG)
        except Exception as e:
            print(f"Не удалось отправить сообщение администратору {admin_id}: {e}")
            continue 
