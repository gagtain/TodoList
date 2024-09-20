from aiogram.fsm.state import StatesGroup, State

class BotMenu(StatesGroup):
    select_tasks = State()
    task_info = State()
    comment_create = State()
    comment_list = State()
    comment_info = State()