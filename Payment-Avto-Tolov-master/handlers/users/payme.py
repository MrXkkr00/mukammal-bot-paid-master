import logging
from aiogram import types
from data import config
from keyboards.default.menu import DATAS
from loader import dp, bot

photo_url = "https://t.me/SearchBook_Robot/221"
caption = """📄 Nomi: ⌚️ Apple Watch
💰 Narxi: 850000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🔸iWatch
🔸Ishlashlari tez
🔸Qotmaydi"""


@dp.message_handler(text="⌚️ Apple Watch")
async def bot_echo(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url, caption=caption, reply_markup=DATAS)


@dp.callback_query_handler(text="savdo")
async def product(call: types.CallbackQuery):
    logging.basicConfig(level=logging.INFO)
    PRICE = types.LabeledPrice(label="Mahsulot Narxi", amount=5000 * 100)
    # if config.PAYMENT_TOKEN.split(':')[1] == 'TEST':
    await bot.send_invoice(chat_id=call.message.chat.id,
                           title="⌚️ Apple Watch Qol soati",
                           description="Payment tolov tizimi",
                           provider_token=config.PAYMENT_TOKEN[0],
                           currency="UZS",
                           photo_url="https://c0.klipartz.com/pngpicture/838/816/gratis-png-apple-watch-series-3-apple-watch-series-2-apple-watch-edition-apple.png",
                           photo_width=1280,
                           photo_height=600,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscripyion",
                           payload="test-invoice-payload")


# Dastuchi : @MrGayartov
# Manba : @KingsOfPy
# kod manba bilan tarqatilsin...
@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(message: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(message.id, ok=True)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def sddd(message: types.Message):
    payment_info = message.successful_payment.to_python()
    for k, x in payment_info.items():
        print(k, x)
        await bot.send_message(message.chat.id, f"Shunchaki foidanaluvchi uchun tolandi qismi...")
        await bot.send_message(config.ADMINS[0], f"To'langandan so'ng adminga habar yuborish uchun...")

    # Dastuchi : @MrGayartov
    # Manba : @KingsOfPy
    # kod manba bilan tarqatilsin...
