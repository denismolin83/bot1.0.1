from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запустить Бота'
        ),
        BotCommand(
            command='help',
            description='Справка по боту'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
