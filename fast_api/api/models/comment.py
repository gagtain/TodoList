from sqlalchemy.orm import mapped_column, Mapped

from models.base_model import Base


class CommentModel(Base):
    __tablename__ = "comments"

    task_id: Mapped[str] = mapped_column()
    telegram_id: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column()
