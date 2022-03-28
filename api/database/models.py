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
    day_full = fields.CharField(max_length=50)
    day_of_ramadan = fields.IntField()

    fajr = fields.DatetimeField()
    iftar = fields.DatetimeField()

    def __str__(self):
        return str(self.day)


__all__ = ["Region", "Date", ]
