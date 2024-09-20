from aiogram_dialog.manager.manager import ManagerImpl

from api.task_api import task_api
from keyboards.base.start import get_start_keyboard
from main import bot


async def create_task_dialog(dialog, manager: ManagerImpl):
    data = manager.current_context().dialog_data

    if len(data.keys()) < 4:
        return

    if data.get('tag_list'):
        tags = await task_api.get_tags_list(manager.dialog_data["telegram_id"])

        data['tag_list'] = [tags[int(x)]['id'] for x in data['tag_list']]
    else:
        data['tag_list'] = []
    await task_api.create_task(**data)
    await bot.send_message(data['telegram_id'], "Создано!",
        reply_markup=await get_start_keyboard(manager.middleware_data['l10n']))