import asyncio
from aiogram import Bot, Dispatcher

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.reminder import remind

import logging

from bot_token import BOT_TOKEN
from app.handlers import router

from app.database.models import run_db

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await run_db()
    dp.include_router(router)

    scheduler = AsyncIOScheduler()
    scheduler.start()
    scheduler.add_job(remind, IntervalTrigger(seconds=30), (bot,))

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())