from aiogram import types
from fluentogram import TranslatorRunner


async def get_start_keyboard(l10n: TranslatorRunner):


    return types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(text=l10n.get('task_list')),
            types.KeyboardButton(text=l10n.get('create_task'))
        ]]
    )