from aiogram_dialog import DialogManager
from api.task_api import task_api
from utils.universal_model import Object


async def get_tasks(dialog_manager: DialogManager, **middleware_data):
    task_list = await task_api.get_task_list(middleware_data['event_from_user'].id)
    data = {
        "tasks": [
            (f"{task['name']}", index)
            for index, task in enumerate(task_list)
        ]
    }
    return data


async def get_task_info(dialog_manager: DialogManager, **middleware_data):
    ctx = dialog_manager.current_context()
    task_id = int(ctx.dialog_data.get('task_id'))
    task_list = await task_api.get_task_list(middleware_data['event_from_user'].id)
    task = task_list[task_id]
    task['tag_data'] = ", ".join([x['name'] for x in task['tag_list']])

    data = {
        "task": Object(task)
    }
    return data

