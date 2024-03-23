import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.methods import DeleteWebhook
from utils.commands import set_commands
from config_reader import bot_token
from handlers import get_find_tyres, user_commands

async def main():
    default_bot_properties = DefaultBotProperties(parse_mode="HTML")
    bot = Bot(token=bot_token, default=default_bot_properties)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        get_find_tyres.router
    )

    await set_commands(bot)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
