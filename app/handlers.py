from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from app.keyboards import greeting_kb

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await message.answer('Hi', reply_markup=greeting_kb)