from aiogram_dialog import DialogManager

from api.comment_api import comment_api
from api.task_api import task_api
from utils.universal_model import Object


async def get_comments(dialog_manager: DialogManager, **middleware_data):

    task_list = await task_api.get_task_list(middleware_data['event_from_user'].id)

    comment_list = await comment_api.get_task_comments(task_list[int(dialog_manager.dialog_data['task_id'])]['id'])
    data = {
        "comments": [
            (f"{comment['username']}", comment['id'])
            for comment in comment_list
        ]
    }
    return data


async def get_comment_info(dialog_manager: DialogManager, **middleware_data):
    ctx = dialog_manager.current_context()
    comment_id = int(ctx.dialog_data.get('comment_id'))
    task = await comment_api.get_comment(comment_id)


    data = {
        "task": Object(task)
    }
    return data