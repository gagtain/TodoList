from aiogram import Router

from handlers.common import base

on = Router(name="common")
on.include_routers(
    base.on
)