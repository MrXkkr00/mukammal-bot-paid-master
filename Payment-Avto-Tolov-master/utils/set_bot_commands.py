from aiogram import types
# Dastuchi : @MrGayartov
# Manba : @KingsOfPy
# kod manba bilan tarqatilsin...

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
        ]
    )
