import asyncio

from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from utils.commands import set_commands
from config_reader import config
from handlers import get_find_tyres, user_commands


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode='HTML')
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
