from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти шины в Форточках"),
            KeyboardButton(text="Найти шины у нас")
        ]
    ],
    resize_keyboard=True
)


exit_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Exit")
        ]
    ],
    resize_keyboard=True
)