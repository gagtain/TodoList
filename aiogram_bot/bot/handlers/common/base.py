from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.base.start import get_start_keyboard
from setup.translator import translators
from states.bot import BotMenu
from states.task import TaskState

on = Router(name=__name__)



@on.message(CommandStart())
async def start(
        msg: types.Message | types.CallbackQuery,
        l10n: TranslatorRunner,
        state: FSMContext
):
    await state.clear()
    if isinstance(msg, types.CallbackQuery):
        msg = msg.message
    await msg.answer(
        l10n.get('start'),
        reply_markup=await get_start_keyboard(l10n)
    )


@on.message(F.text.in_([x.get('task_list') for x in translators]))
async def get_task_list(
        msg: types.Message | types.CallbackQuery,
        l10n: TranslatorRunner,
        state: FSMContext,
        dialog_manager: DialogManager
):
    await dialog_manager.start(BotMenu.select_tasks, mode=StartMode.NORMAL)


@on.message(F.text.in_([x.get('create_task') for x in translators]))
async def create_task(
        msg: types.Message | types.CallbackQuery,
        l10n: TranslatorRunner,
        dialog_manager: DialogManager
):
    await dialog_manager.start(TaskState.name, mode=StartMode.NORMAL)

