import datetime

from api.base import BaseAPI
from config.settings import Settings


class TaskAPI(BaseAPI):

    base_url = Settings().api_url


    async def create_task(self, telegram_id: str, name: str, description: str, dead_line_time: datetime.datetime,
                          tag_list):
        data = {
            'name': name,
            'description': description,
            'telegram_id': telegram_id,
            'dead_line_time': dead_line_time,
            'tag_list': tag_list
        }
        response = await self.request('/api/todo_list/tasks', json=data, method='POST')
        return response.status == 200

    async def get_task_list(self, telegram_id: str):
        params = {
            'tg_id': telegram_id
        }
        response = await self.request('/api/todo_list/tasks', params=params, method='GET')

        return await response.json()


    async def get_task(self, telegram_id: str, task_id: int):
        params = {
            'tg_id': telegram_id,

        }
        response = await self.request(f'/api/todo_list/tasks/{task_id}', params=params, method='GET')
        return await response.json()

    async def get_tags_list(self, telegram_id: str):
        params = {
            'tg_id': telegram_id,

        }
        response = await self.request(f'/api/todo_list/tags', params=params, method='GET')
        return await response.json()

task_api = TaskAPI()
