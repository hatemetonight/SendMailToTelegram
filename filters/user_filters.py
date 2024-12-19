from misc.config_loader import config


def is_admin(telegram_id: int) -> bool:
    for admin_id in config.get("ADMIN_LIST"):
        if admin_id == telegram_id:
            return True  
    return False

