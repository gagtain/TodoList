import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Checkbox
from aiogram_dialog.widgets.text import Format


def paginated_tasks(on_click):
    return ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='s_scroll_tasks',
            item_id_getter=operator.itemgetter(1),
            items='tasks',
            on_click=on_click,

        ),
        height=1,
        id='tasks_ids'
    )


def paginated_comments(on_click):
    return ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='s_scroll_comments',
            item_id_getter=operator.itemgetter(1),
            items='comments',
            on_click=on_click,

        ),
        height=1,
        id='comment_ids'
    )
