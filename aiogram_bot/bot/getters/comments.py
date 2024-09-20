from aiogram_dialog import DialogManager

from api.comment_api import comment_api
from utils.universal_model import Object


async def get_comments(dialog_manager: DialogManager, **middleware_data):
    task_list = await comment_api.get_task_comments(dialog_manager.dialog_data['task_id'])
    data = {
        "comments": [
            (f"{task['username']}", task['id'])
            for task in task_list
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