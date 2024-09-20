from pydantic import BaseModel


class CommentBase(BaseModel):
    task_id: str
    telegram_id: str
    username: str

    text: str

    class Config:
        from_attributes = True

class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    text: str


class CommentResponse(CommentBase):
    id: int


class CommentListResponse(BaseModel):
    id: int | None = None
    task_id: str | None = None
    telegram_id: str | None = None
    text: str | None = None
