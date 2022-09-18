from tortoise import fields

from app.database.models.abstact_base import AbstractBaseModel
from app.database.models.abstract_datetime import AbstractDateTime


class Advertisement(AbstractBaseModel, AbstractDateTime):
    id_th = fields.BigIntField(null=False)
    from_city = fields.CharField(null=False, max_length=100)
    to_cite = fields.CharField(null=False, max_length=100)
    date = fields.DateField(null=False)
    from_time = fields.TimeField(null=False)
    to_time = fields.TimeField(null=False)
    rating = fields.IntField(default=2)
    count_feedback = fields.IntField(default=0)
    count_place = fields.IntField(default=1)
    count_passenger = fields.IntField(default=1)
    price = fields.IntField(default=0)
