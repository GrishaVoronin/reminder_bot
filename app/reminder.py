from app.database.models import async_session
from aiogram import Bot
from app.database.models import Reminder

from sqlalchemy import select

from datetime import datetime

from app.database.requests import delete_reminder

async def remind(bot: Bot):
    async with async_session() as session:
        reminders = await session.scalars(select(Reminder).where(Reminder.time <= datetime.now()))
        for reminder in reminders:
            await bot.send_message(reminder.tg_id, reminder.description)
            await delete_reminder(reminder.id)