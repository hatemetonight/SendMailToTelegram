import asyncio
from telebot.async_telebot import AsyncTeleBot
from misc.config_loader import config
from tasks.send_mail import periodic_sender
from misc.notifications import startup_notification
from handlers.commands_handler import register_handlers
from handlers.manage_chat_handlers import manage_chat_handlers
from handlers.utils_handlers import other_handlers
from handlers.admin_handlers import admin_menu_handlers

bot = AsyncTeleBot(config["BOT_TOKEN"])

async def main():
    register_handlers(bot)
    manage_chat_handlers(bot)
    admin_menu_handlers(bot)
    other_handlers(bot)
    await startup_notification(bot)
    if config["TIME_SEND"] != 0:
        asyncio.create_task(periodic_sender(bot))
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())

