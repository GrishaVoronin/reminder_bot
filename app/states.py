from aiogram.fsm.state import StatesGroup, State

class Reminder(StatesGroup):
    year = State()
    month = State()
    day = State()
    hour = State()
    minute = State()
    description = State()