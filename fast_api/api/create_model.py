import asyncio

from dotenv import load_dotenv
from sqlalchemy import engine_from_config

from config.database.db_helper import db_helper
from models.base_model import Base
from models.comment import CommentModel

load_dotenv()



async def init_models():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(CommentModel.metadata.drop_all)
        await conn.run_sync(CommentModel.metadata.create_all)

asyncio.run(init_models())