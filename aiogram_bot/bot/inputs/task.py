import datetime

from aiogram import types
from aiogram_dialog import DialogProtocol, DialogManager



async def on_input_name(
        message: types.Message, dialog: DialogProtocol, manager: DialogManager,
):
    manager.dialog_data["telegram_id"] = message.from_user.id
    manager.dialog_data["name"] = message.text
    await manager.next()


async def on_input_desk(
        message: types.Message, dialog: DialogProtocol, manager: DialogManager,
):
    manager.dialog_data["description"] = message.text
    await manager.next()



async def on_input_dead_line_time(
        message: types.Message, dialog: DialogProtocol, manager: DialogManager,
):
    try:
        date_time = datetime.datetime.strptime(message.text, "%Y-%m-%d:%H:%M")
    except Exception as e:
        await manager.show()
        return

    manager.dialog_data["dead_line_time"] = date_time.strftime('%Y-%m-%d:%H:%M')




    await manager.done()