import traceback
from typing import List

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from schemas.comments_schema import CommentCreate, CommentResponse, CommentUpdate
from services.comment_service import comment_service

router = APIRouter(prefix='/comment', tags=["comment"])


@router.post("/", response_model=CommentResponse)
async def create_comment(data: CommentCreate) -> CommentResponse:
    try:
        return await comment_service.create(data)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

@router.get('/', response_model=List[CommentResponse])
async def get_comments(task_id: str, limit=100, offset=0) -> List[CommentResponse]:
    try:
        return await comment_service.get_multi(limit=limit, offset=offset, task_id=task_id)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

@router.get('/{id}', response_model=CommentResponse)
async def get_comment(id: int) -> CommentResponse:
    try:
        data = await comment_service.get(id)
        if data is None:
            raise HTTPException(HTTP_404_NOT_FOUND)
        return data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

@router.patch('/{id}', response_model=CommentResponse)
async def update_comments(id: int, data: CommentUpdate) -> CommentResponse:
    try:
        return await comment_service.update(id, data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))

@router.delete('/{id}', response_model=None)
async def delete_comments(id: int) -> CommentResponse:
    try:
        return await comment_service.delete(id)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))