import asyncio
from aiogram import Bot, Dispatcher

import logging

from bot_token import BOT_TOKEN
from app.handlers import router

from app.database.models import run_db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    await run_db()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())