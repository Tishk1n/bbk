from tortoise import fields

from app.database.models.abstact_base import AbstractBaseModel
from app.database.models.abstract_datetime import AbstractDateTime


class User(AbstractBaseModel, AbstractDateTime):
    id_tg = fields.BigIntField(null=False, unique=True)
    active = fields.BooleanField(default=False)
    balance = fields.IntField(default=0)
    advertisements = fields.ManyToManyField('models.Advertisement')
    success = fields.ManyToManyField('models.Success')
    referrals = fields.ManyToManyField('models.User')
    referrer = fields.BigIntField(default=0)
    last_profit = fields.IntField(default=0)

    class Meta:
        table = "users"
