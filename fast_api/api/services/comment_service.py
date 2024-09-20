from api.task_api import task_api
from loaders import redis
from repositories.sqlalchemy_repository import ModelType
from schemas.base_schema import PyModel
from schemas.comments_schema import CommentBase, CommentCreate
from services.base_service import BaseService
from repositories.comment_repository import comment_repository


class CommentService(BaseService):

    async def create(self, model: CommentCreate) -> ModelType:
        await task_api.exist_task(model.task_id)
        return await super().create(model)


comment_service = CommentService(repository=comment_repository)
