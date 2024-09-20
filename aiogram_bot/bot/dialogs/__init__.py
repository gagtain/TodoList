from aiogram import Router

from dialogs.task import dialog_task_main, dialog_task_list

on = Router(name="dialogs")
on.include_routers(
    dialog_task_main,
    dialog_task_list,
)