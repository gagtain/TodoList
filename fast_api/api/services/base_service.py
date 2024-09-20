import json
from typing import List

from loaders import redis
from schemas.base_schema import PyModel
from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository
from schemas.comments_schema import CommentBase


class BaseService:

    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository: SqlAlchemyRepository = repository

    async def create(self, model: PyModel) -> ModelType:


        return await self.repository.create(data=model.model_dump())

    async def update(self, pk: int, model: PyModel) -> ModelType:
        return await self.repository.update(data=model.model_dump(), id=pk)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(id=pk)

    async def get(self, pk: int) -> ModelType:
        return await self.repository.get_single(id=pk)

    async def get_multi(self, limit, offset, **filters) -> List[ModelType]:

        return await self.repository.get_multi(limit=limit, offset=offset, **filters)