from tortoise import fields
from tortoise.models import Model



class Region(Model):
    hudud_id = fields.IntField(pk=True)
    hudud = fields.CharField(50, unique=True)

    def full_format(self):
        return {"hudud": self.hudud,
                'hudud_id': self.hudud_id,
                "muvaffaqiyat": True}

    def __str__(self):
        return self.hudud


class Date(Model):
    id = fields.IntField(pk=True)
    hudud = fields.CharField(50)
    kun = fields.CharField(50)
    hafta_kun = fields.CharField(50)
    kun_full = fields.CharField(50)
    fajr = fields.CharField(50)
    iftar = fields.CharField(50)

    def full_format(self):
        return {
            "hafta_kuni": self.hafta_kun,
            "kun": self.kun_full,
            "izoh": f'Ramazon {self.kun}',
            "vaqtlar": {
                    "iftorlik": self.iftar,
                    "saharlik": self.iftar
            }
        }

    def response_format(self):
        return {self.hudud: self.full_format()}

    def __str__(self):
        return self.day_full