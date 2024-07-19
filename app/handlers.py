from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router

from datetime import datetime

import app.database.requests as rq

import app.text as tx

from app.states import Reminder
from aiogram.fsm.context import FSMContext

from app.validator import check_time

from app.keyboards import greeting_kb

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    await rq.add_user(message.from_user.id, message.from_user.first_name)
    await message.answer('Hi', reply_markup=greeting_kb)

@router.message(F.text == tx.create_reminder)
async def create_reminder(message: Message, state: FSMContext):
    await state.set_state(Reminder.year)
    await message.answer('Введите год')

@router.message(Reminder.year)
async def get_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(Reminder.month)
    await message.answer('Введите месяц')

@router.message(Reminder.month)
async def get_month(message: Message, state: FSMContext):
    await state.update_data(month=message.text)
    await state.set_state(Reminder.day)
    await message.answer('Введите день')

@router.message(Reminder.day)
async def get_day(message: Message, state: FSMContext):
    await state.update_data(day=message.text)
    await state.set_state(Reminder.hour)
    await message.answer('Введите час')

@router.message(Reminder.hour)
async def get_hour(message: Message, state: FSMContext):
    await state.update_data(hour=message.text)
    await state.set_state(Reminder.minute)
    await message.answer('Введите минуту')

@router.message(Reminder.minute)
async def get_minute(message: Message, state: FSMContext):
    await state.update_data(minute=message.text)
    await state.set_state(Reminder.description)
    await message.answer('Введите напоминание')

@router.message(Reminder.description)
async def get_remind(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    if await check_time(state):
        reminder = await state.get_data()
        await state.clear()
        time = datetime(int(reminder['year']), int(reminder['month']),
                        int(reminder['day']), int(reminder['hour']), int(reminder['minute']))
        await rq.add_reminder(message.from_user.id, reminder["description"], time)
        await message.answer('Напоминание успешно создано')
    else:
        await message.answer('Невалидное время, попробуйте еще раз')
        await state.clear()