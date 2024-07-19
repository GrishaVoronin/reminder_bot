from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

import app.text as tx

greeting_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=tx.create_reminder)]
],
    resize_keyboard=True,
    input_field_placeholder=tx.greeting_placeholder
)