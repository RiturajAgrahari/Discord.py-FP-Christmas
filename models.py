from tortoise.models import Model
from tortoise import fields


class Profile(Model):
    id = fields.IntField(primary_key=True)
    discord_id = fields.CharField(max_length=200)
    discord_name = fields.CharField(max_length=224)
    bot_used = fields.IntField(default=0)
    created_on = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.discord_name


class ChristmasResponseEvent(Model):
    id = fields.IntField(primary_key=True)
    user_id = fields.ForeignKeyField("models.Profile", on_delete=fields.CASCADE)
    hero_name = fields.CharField(max_length=100)
    used_on = fields.DatetimeField(auto_now_add=True)



