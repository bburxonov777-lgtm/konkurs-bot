import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Bot tokeningizni shu yerga yozing
TOKEN = "8840889023:AAEYDcKQLSg150xQD0uFvBdBobOS2mVTvKI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Salom! Konkurs boti ishga tushdi.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
