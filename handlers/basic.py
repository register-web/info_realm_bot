from aiogram.filters import Command
from aiogram.types import Message
from bot import dp


@dp.message(Command("start"))
async def start_cmd(msg: Message) -> None:
    await msg.answer("Бот работает через Render Webhook!")
