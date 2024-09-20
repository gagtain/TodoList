from aiogram_dialog import DialogManager

from api.task_api import task_api


async def get_tags(dialog_manager: DialogManager, **middleware_data):
    task_list = await task_api.get_tags_list(middleware_data['event_from_user'].id)
    data = {
        "tags": [
            (f"{task['name']}", index)
            for index, task in enumerate(task_list)
        ]
    }
    return data