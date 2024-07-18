from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from app.keyboards import greeting_kb

import app.database.requests as rq

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await rq.add_user(message.from_user.id, message.from_user.first_name)
    await message.answer('Hi', reply_markup=greeting_kb)