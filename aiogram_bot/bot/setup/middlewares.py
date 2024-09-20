from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from loguru import logger

from aiogram_dialog import setup_dialogs
from config.middlewares import (
    TranslatorRunnerMiddleware
)


def setup_middlewares(dp: Dispatcher):
    translator_runner_middleware = TranslatorRunnerMiddleware()
    dp.message.middleware(translator_runner_middleware)
    dp.callback_query.middleware(translator_runner_middleware)

    setup_dialogs(dp)

    # Callback answer middleware
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    logger.info("Middlewares setup completed")