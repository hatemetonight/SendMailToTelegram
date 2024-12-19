from telebot import types

back_keyboard = ["↩️ Вернуться назад"]
start_keyboard = ["📧 Подключить почту"]
menu_keyboard = ["📬 Проверить почту", "⚙️ Настройки"]
settings_keyboard = ["✏️ Поменять почту", "❌ Удалить почту", "↩️ Вернуться назад"]
admin_keyboard = ["🗓️ Расписание задач", "🚫 Блокировка пользователей", "➕ Управление чатами", "↩️ Вернуться назад"]
tasks_keyboard =  ["🗓️ Cписок задач","🕚 Вкл/выкл задач", "↩️ Вернуться назад"]
block_users_keyboard = ["🔒 Заблокировать пользователя", "🔓 Разблокировать пользователя", "↩️ Вернуться назад"]
chat_manage = ["➕ Добавить чат","❌ Удалить чат"]

def create_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        keyboard.add(types.KeyboardButton(button))
    return keyboard

