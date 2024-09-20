from aiogram.fsm.state import StatesGroup, State

class TaskState(StatesGroup):
    name = State()
    descriptions = State()
    dead_line_time = State()
    tags = State()


