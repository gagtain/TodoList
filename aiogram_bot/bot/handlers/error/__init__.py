from aiogram import Router

from handlers.error import errors

on = Router(name="error")
on.include_routers(
    errors.on,
)