from fastapi import APIRouter
from controllers import comment_controller

def get_apps_router():
    router = APIRouter()
    router.include_router(comment_controller.router)
    return router