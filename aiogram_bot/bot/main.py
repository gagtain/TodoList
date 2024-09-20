import asyncio
from pprint import pformat

from aiogram import Bot, F, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from loguru import logger

import setup
from config.settings import Settings
from setup.opts import SetupOpts


async def on_startup(settings: Settings, bot: Bot):
    pass


async def on_shutdown(bot: Bot):
    pass


settings = Settings()
bot = Bot(
    token=settings.token,
    default=DefaultBotProperties(
        parse_mode="html"
    )
)


async def main():
    # Initialize settings
    logger.info(f"Settings:\n{pformat(settings.model_dump())}")

    storage = MemoryStorage()

    translator_hub = setup.init_translator_hub()
    base_l10n = translator_hub.get_translator_by_locale("ru")

    opts = SetupOpts(
        bot=bot,
        settings=settings,
        l10n=base_l10n,
    )

    dp = Dispatcher(
        storage=storage,
        settings=settings,
        translator_hub=translator_hub,
        fsm_strategy=FSMStrategy.GLOBAL_USER
    )

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)


    dp.message.filter(F.chat.type == "private")


    await setup.setup_routers(dp, settings)



    setup.setup_middlewares(dp)

    scheduler = await setup.setup_scheduler()


    logger.info("Start bot in polling mode")
    await bot.delete_webhook()
    await dp.start_polling(
        bot,
        skip_updates=True,
        allowed_updates=dp.resolve_used_update_types(),
        scheduler=scheduler,
    )

    await bot.session.close()
    await dp.storage.close()


def start_runner():
    try:
        import uvloop
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    except ImportError:
        logger.warning("uvloop is not installed")
        asyncio.run(main())


if __name__ == "__main__":

    try:
        start_runner()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
