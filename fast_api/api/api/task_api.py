from email.policy import HTTP

import aiohttp

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from config.project_config import settings, Settings
from loaders import redis


class TaskAPI:

    base_url = settings.TASK_API_URL

    async def exist_task(self, task_id):
        for key in await redis.keys():
            if key.endswith(task_id) and key.startswith(':'):
                await redis.set(task_id, "false", 60 * 10)
                raise HTTPException(HTTP_404_NOT_FOUND)
        else:
            res = await redis.get(task_id)
            if res == "true":
                return True
            elif res == 'false':
                raise HTTPException(HTTP_404_NOT_FOUND)

        async with aiohttp.ClientSession() as session:
            async with session.request(method="GET", headers={
                'Authorization': f'EnvToken {Settings().api_token}'
            }, url=self.base_url + f'/api/todo_list/tasks/{task_id}') as response:
                if response.status == 404:
                    await redis.set(task_id, "false")
                    raise HTTPException(HTTP_404_NOT_FOUND)
                if response.status > 404 or response.status < 200:
                    raise HTTPException(response.status, response.content)

        await redis.set(task_id, "true")


        return True

task_api = TaskAPI()