from aiohttp import web
from aiogram.types import Update
from bot import bot, dp


async def handle_webhook(request: web.Request) -> web.Response:
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return web.Response()
