from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from art import tprint as t
# Dastuchi : @MrGayartov
# Manba : @KingsOfPy
# kod manba bilan tarqatilsin...
async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    #
    # # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    t('KingsOfPy')
    print("Dasturchi: @MrGayratov Manba : @KingsOfPy")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
