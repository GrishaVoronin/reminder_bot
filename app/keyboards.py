from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import app.database.requests as rq

import app.text as tx

greeting_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=tx.create_reminder)]
],
    resize_keyboard=True,
    input_field_placeholder=tx.greeting_placeholder
)

empty_kb = ReplyKeyboardRemove()

default_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=tx.create_reminder)],
    [KeyboardButton(text=tx.delete_reminder)],
    [KeyboardButton(text=tx.reminders_list)],
],
    resize_keyboard=True,
    input_field_placeholder=tx.greeting_placeholder
)

async def inline_reminders(tg_id):
    keyboard = InlineKeyboardBuilder()
    reminders = await rq.get_reminders(tg_id)
    for reminder in reminders:
        keyboard.add(InlineKeyboardButton(text=f"{reminder.description}\n"
                     f"{reminder.time}", callback_data=f'reminder{reminder.id}'))
    return keyboard.adjust(1).as_markup()