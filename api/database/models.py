from tortoise import fields
from tortoise.models import Model


class Region(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(60, unique=True)

    dates: fields.ManyToManyRelation["Date"] = \
        fields.ManyToManyField(
            "models.Date", related_name="regions",
    )

    def __str__(self):
        return self.name


class Date(Model):
    id = fields.IntField(pk=True)

    day = fields.DateField()

    fajr = fields.DatetimeField(auto_now=True)
    iftar = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return str(self.day)
