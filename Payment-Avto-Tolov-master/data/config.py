from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
PAYMENT_TOKEN = env.list("PAYMENT_TOKEN")  # Payment Token
IP = env.str("ip")  # Xosting ip manzili

# Dastuchi : @MrGayartov
# Manba : @KingsOfPy
# kod manba bilan tarqatilsin...
