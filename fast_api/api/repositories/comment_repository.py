from config.database.db_helper import db_helper
from models.comment import CommentModel
from repositories.sqlalchemy_repository import SqlAlchemyRepository, ModelType
from schemas.comments_schema import CommentCreate, CommentUpdate


class CommentRepository(SqlAlchemyRepository[ModelType, CommentCreate, CommentUpdate]):
    pass


comment_repository = CommentRepository(model=CommentModel, db_session=db_helper.get_db_session)
