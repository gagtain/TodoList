from aiogram import Dispatcher
from loguru import logger

from handlers import common, error
from dialogs import on as dialogs_on
from config.settings import Settings


async def setup_routers(
        dp: Dispatcher,
        settings: Settings,
):
    # Handling errors
    dp.include_router(error.on)


    # Common handlers
    dp.include_router(common.on)
    dp.include_router(dialogs_on)
    # common.on.include_router(admin.stats.on)
    logger.info("Routers setup complete")