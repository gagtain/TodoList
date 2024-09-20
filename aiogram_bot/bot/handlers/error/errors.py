import sys

from aiogram import Router
from aiogram.exceptions import DetailedAiogramError
from aiogram.types.error_event import ErrorEvent

from aiohttp import ContentTypeError
from loguru import logger

import setup
from config.settings import Settings
from keyboards.base.start import get_start_keyboard
from main import bot

on = Router(name=__name__)


@on.errors()
async def error_handler(event: ErrorEvent):
    text = ("Произошла ошибка.\n"
            "Сообщение об ошибке:\n"
            "{}".format(event.exception))


    exception = event.exception
    if isinstance(exception, (DetailedAiogramError, ContentTypeError)):
        _type, _, tb = sys.exc_info()
        logger.opt(exception=(_type, None, tb)).error(exception.message)
    else:
        logger.exception(exception)
    for admin in Settings().admins.split(','):
        try:
            await bot.send_message(admin, text, parse_mode=None)
        except:
            pass
    text = "error"

    if str(event.exception) == "429":
        text = "max_count_send"
    if event.update.callback_query:
        await event.update.callback_query.answer()
        message = event.update.callback_query.message
        user = event.update.callback_query.from_user
    else:
        message = event.update.message
        user = event.update.message.from_user
    translator_hub = setup.init_translator_hub()
    await message.answer(translator_hub.get_translator_by_locale(user.language_code).get(text),
        reply_markup=await get_start_keyboard(
            translator_hub.get_translator_by_locale(user.language_code)
                                              )
                         )
