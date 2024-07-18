from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.text import greeting_button, greeting_placeholder

greeting_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=greeting_button)]
],
    resize_keyboard=True,
    input_field_placeholder=greeting_placeholder
)