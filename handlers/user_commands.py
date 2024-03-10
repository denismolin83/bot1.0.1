from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def get_start(message: Message):
    # await bot.send_message(message.from_user.id, f"Привет, это бот для Форточек", reply_markup=reply.main_kb)
    await message.answer(f"Привет, это бот для Форточек", reply_markup=reply.main_kb)