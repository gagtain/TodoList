from aiogram import types
from aiogram_dialog import DialogProtocol, DialogManager

from api.comment_api import comment_api
from states.bot import BotMenu


async def on_comment_text_create(
        message: types.Message, dialog: DialogProtocol, manager: DialogManager,
):
    data = manager.dialog_data
    await comment_api.create_comment(message.from_user.id, task_id=data['task_id'], text=message.text,
                                     username=f'@{message.from_user.username}')

    await manager.switch_to(BotMenu.comment_list)