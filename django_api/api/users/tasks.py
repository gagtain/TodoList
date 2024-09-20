import asyncio
from asyncio import TaskGroup
from typing import Coroutine, Sequence

from aiogram import Bot
from celery import shared_task
from django.utils import timezone

from django.conf import settings
from todolist.models import Task


@shared_task()
def send_notify_users():
    task_async_list = []

    for task_db_list in divide_chunks(Task.objects.filter(dead_line_time__lte=timezone.now()), 100):
        for task_db in task_db_list:
            task_async_list.append(
                send_notify(task_db)
            )
        asyncio.run(generate_tasks(task_async_list))
        task_async_list = []


async def generate_tasks(func: list[Coroutine]):
    async with TaskGroup() as th:
        for i in func:
            th.create_task(
                i
            )


async def send_notify(task: Task):
    bot = Bot(token=settings.BOT_TG_TOKEN)
    try:
        await bot.send_message(task.telegram_id, "Дедлайн задачи {} наступил".format(task.name))
    except:
        pass

def divide_chunks(items: Sequence, n: int):

    for i in range(0, len(items), n):
        yield items[i:i + n]