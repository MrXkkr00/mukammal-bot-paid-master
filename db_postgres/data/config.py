from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "6780604386:AAEEy1q2Nvp8WjqCranyizWNDwAcModvho4"  # Bot toekn
ADMINS = ["984568970"]  # adminlar ro'yxati
IP = env.str("DB_HOST")  # Xosting ip manzili

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
