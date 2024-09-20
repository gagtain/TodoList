from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Multiselect

from states.bot import BotMenu


async def on_chosen_tasks(c: types.CallbackQuery, widget: Select, manager: DialogManager, item_id: str, **kwargs):
    ctx = manager.current_context()

    ctx.dialog_data['task_id'] = item_id
    await manager.switch_to(BotMenu.task_info)


async def comment_task_create(c: types.CallbackQuery, widget: Select, manager: DialogManager, **kwargs):
    await manager.switch_to(BotMenu.comment_create)


async def comment_task(c: types.CallbackQuery, widget: Select, manager: DialogManager, **kwargs):
    await manager.switch_to(BotMenu.comment_list)


async def on_chosen_comments(c: types.CallbackQuery, widget: Select, manager: DialogManager, item_id, **kwargs):
    ctx = manager.current_context()
    ctx.dialog_data['comment_id'] = item_id
    await manager.switch_to(BotMenu.comment_info)


async def on_select_tag(c: types.CallbackQuery, widget: Multiselect, manager: DialogManager, item_id, **kwargs):
    is_checked = widget.is_checked(item_id=item_id)

    if not manager.dialog_data.get('tag_list'):
        manager.dialog_data['tag_list'] = []

    if not is_checked:
        manager.dialog_data['tag_list'].append(item_id)
    else:
        manager.dialog_data['tag_list'].remove(item_id)
