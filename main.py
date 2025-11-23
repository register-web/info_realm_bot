import os
from aiohttp import web
from bot import bot, dp
from webhook import handle_webhook
import handlers.basic  # подключаем хендлеры


async def on_startup(app: web.Application) -> None:
    webhook_base = os.getenv("WEBHOOK_BASE")
    if not webhook_base:
        raise RuntimeError("WEBHOOK_BASE is not set")

    webhook_url = f"{webhook_base.rstrip('/')}/webhook"

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(webhook_url)


async def on_cleanup(app: web.Application) -> None:
    await bot.session.close()


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)
    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)
    return app


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    web.run_app(create_app(), host="0.0.0.0", port=port)
