import hashlib

from django.db import models
from django.utils import timezone


# Create your models here.


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, max_length=64, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def generate_unique_id(self):
        if self.created is None:
            self.created = timezone.now()

        hash_data = str(self.created).encode('utf-8')

        return hashlib.sha256(hash_data).hexdigest()



    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        if not self.id:
            self.id = self.generate_unique_id()

        obj = super().save(*args, force_insert, force_update, using, update_fields)

        return obj