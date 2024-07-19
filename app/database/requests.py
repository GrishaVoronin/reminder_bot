from app.database.models import async_session
from app.database.models import User, Reminder

from sqlalchemy import select

async def add_user(tg_id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, name=name))
            await session.commit()

async def add_reminder(tg_id, description, time):
    async with async_session() as session:
        session.add(Reminder(tg_id=tg_id, description=description, time=time))
        await session.commit()

async def get_reminders(tg_id):
    async with async_session() as session:
        return await session.scalars(select(Reminder).where(Reminder.tg_id == tg_id))

async def get_reminder(id):
    async with async_session() as session:
        return await session.scalar(select(Reminder).where(Reminder.id == id))

async def delete_reminder(id):
    async with async_session() as session:
        reminder = await session.scalar(select(Reminder).where(Reminder.id == id))
        await session.delete(reminder)
        await session.commit()