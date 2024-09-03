from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⌚️ Apple Watch")
        ]
    ],
    resize_keyboard=True
)

DATAS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "🛒 Sotib olish", callback_data="savdo"),
        ]
    ],
    row_width=1
)


# Dastuchi : @MrGayartov
# Manba : @KingsOfPy
# kod manba bilan tarqatilsin...
