from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from sqlalchemy import BigInteger, String, ForeignKey, DateTime

from datetime import datetime

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

class Reminder(Base):
    __tablename__ = 'reminders'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id'))
    description: Mapped[str] = mapped_column(String(50))
    time: Mapped[datetime] = mapped_column(DateTime)

async def run_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)