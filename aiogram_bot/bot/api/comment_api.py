from api.base import BaseAPI
from config.settings import Settings


class CommentAPI(BaseAPI):

    base_url = Settings().fast_api_url

    async def create_comment(self, telegram_id: str, task_id: int, text: str, username: str):
        data = {
            'task_id': task_id,
            'text': text,
            'telegram_id': str(telegram_id),
            'username': username
        }
        response = await self.request('/comment', json=data, method='POST')
        return response.status == 200

    async def get_task_comments(self, task_id: int):
        params = {
            'task_id': task_id
        }
        response = await self.request('/comment', params=params, method='GET')
        return await response.json()


    async def get_comment(self, task_id: int):
        response = await self.request(f'/comment/{task_id}', method='GET')
        return await response.json()


comment_api = CommentAPI()
