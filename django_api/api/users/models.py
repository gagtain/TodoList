from django.contrib.auth.models import AbstractUser
from django.db import models

from based.models import BaseModel


# Create your models here.

class TodoUser(AbstractUser, BaseModel):

    pass