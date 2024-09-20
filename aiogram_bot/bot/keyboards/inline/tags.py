import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Checkbox, Multiselect
from aiogram_dialog.widgets.text import Format


def paginated_tags(on_click):
    return ScrollingGroup(
        Multiselect(
            Format(' + {item[0]}'),
            Format(' - {item[0]}'),
            id='s_scroll_tags',
            item_id_getter=operator.itemgetter(1),
            on_click=on_click,
            items='tags'
        ),
        height=1,
        id='tag_ids'
    )
