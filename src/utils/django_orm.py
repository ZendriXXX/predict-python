from django.db import models


def duplicate_orm_row(obj: models.Model):
    obj.pk = None
    return obj
