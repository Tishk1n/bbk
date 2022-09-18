import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp.web import run_app, Application

from app import handlers
from app.database import init as database_init
from app.routers import register_router_app


async def on_startup(bot: Bot, base_url):
    await bot.delete_webhook()
    await bot.set_webhook(f"{base_url}/webhook")
    asyncio.create_task(_asyncio_database_init())


def main(token: str) -> None:
    bot: Bot = Bot(token=token)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(DeletedMiddleware())
    dp['base_url'] = getenv('BASE_URL')
    dp.startup.register(on_startup)
    for router in handlers.routers:
        dp.include_router(router)
    dp.run_polling(bot)
    #app = Application()
    #app['bot'] = bot
    #register_router_app(app)
    #SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
    #setup_application(app, dp, bot=bot)
    #run_app(app, host="0.0.0.0", port=7621)


async def _asyncio_database_init() -> None:
    db_url = f'mysql://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_HOST")}/{getenv("MYSQL_DATABASE")}'
    await database_init(db_url=db_url)
