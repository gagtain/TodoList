from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Cancel, Back, Button, Next
from aiogram_dialog.widgets.text import Const, Format

from getters.comments import get_comments, get_comment_info
from getters.tags import get_tags
from getters.tasks import get_tasks, get_task_info
from inputs.comment import on_comment_text_create
from inputs.task import on_input_name, on_input_desk, on_input_dead_line_time
from keyboards.inline.tags import paginated_tags
from on_cloused.task import create_task_dialog
from states.bot import BotMenu
from states.task import TaskState

from keyboards.inline.task import paginated_tasks, paginated_comments
from selected.task import on_chosen_tasks, on_chosen_comments, comment_task, comment_task_create, on_select_tag

task_name_window = Window(
    Const("Напишите название задачи"),
    MessageInput(on_input_name),
    Cancel(),
    state=TaskState.name,

)

task_description_window = Window(
    Const("Напишите описание задачи"),
    MessageInput(on_input_desk),
    Back(),
    state=TaskState.descriptions,
)

task_tags_window = Window(
    Const("Выберите теги"),
    paginated_tags(on_select_tag),
    Next(),
    Back(),
    state=TaskState.tags,
    getter=get_tags
)

task_dead_line_window = Window(
    Const("Напишите дедлайн задачи в формате '%Y-%m-%d:%H:%M', пример: 2024-02-01:11:11"),
    Back(),
    MessageInput(on_input_dead_line_time),
    state=TaskState.dead_line_time,
)

dialog_task_main = Dialog(task_name_window, task_description_window, task_tags_window, task_dead_line_window,
                          on_close=create_task_dialog)

dialog_task_list = Dialog(Window(
    Const("Список задач"),
    paginated_tasks(on_chosen_tasks),
    Cancel(Const('Выход')),
    state=BotMenu.select_tasks,
    getter=get_tasks
),
    Window(
        Format('''
Название: {task.name}
Описание: {task.description}
Дата создания {task.created}
Дедлайн: {task.dead_line_time}
Теги: {task.tag_data}
        '''),
        Button(
            Const('Комментарии'),
            id='comments_task',
            on_click=comment_task
        ),
        Back(Const('Вернуться')),
        state=BotMenu.task_info,
        getter=get_task_info
    ),
    Window(
        Const("Список комментариев"),
        paginated_comments(on_chosen_comments),
        Button(Const('Создать'
                     ),
               on_click=comment_task_create,
               id='create_comments'
               ),
        Back(Const('Вернуться')),
        state=BotMenu.comment_list,
        getter=get_comments
    ),
    Window(
        Format('''
Кто: {task.username}
Текст: {task.text}
        '''),
        Back(Const('Вернуться')),
        state=BotMenu.comment_info,
        getter=get_comment_info
    ),
    Window(
        Const('Напишите текст комментария'),
        Back(Const('Вернуться')),
        MessageInput(on_comment_text_create),
        state=BotMenu.comment_create,
    ),

)
