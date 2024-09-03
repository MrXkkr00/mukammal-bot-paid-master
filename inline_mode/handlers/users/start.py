from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.courses import aiogram_keys, python_keys
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=aiogram_keys)


@dp.message_handler(text = "2")
async def bot_start(message: types.Message):
    await message.answer(f"Som, {message.from_user.full_name}!", reply_markup=python_keys)
