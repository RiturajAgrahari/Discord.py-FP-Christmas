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


# EVENTS

class Event(Model):
    # Primary Key
    id = fields.IntField(primary_key=True)
    # Information
    name = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    start_time = fields.DatetimeField(null=True)
    end_time = fields.DatetimeField(null=True)
    archived = fields.BooleanField(default=False)


# DRAW CARD EVENT MODELS

class Card(Model):
    # Primary key
    id = fields.IntField(primary_key=True)
    # Card details
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    image = fields.CharField(max_length=225)
    # User who got the card
    user = fields.ManyToManyField("models.Profile", related_name="cards", on_delete=fields.CASCADE)


# CHRISTMAS EVENT MODEL
class ChristmasResponseEvent(Model):
    id = fields.IntField(primary_key=True)
    user_id = fields.ForeignKeyField("models.Profile", on_delete=fields.CASCADE)
    hero_name = fields.CharField(max_length=100)
    used_on = fields.DatetimeField(auto_now_add=True)



