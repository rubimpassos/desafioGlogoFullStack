from django.db import models
from django.utils.translation import gettext as _


class Food(models.Model):
    name = models.CharField(_("nome"), max_length=255, unique=True)
    quantity = models.FloatField(_("quantidade"))
    proteins = models.FloatField(_("proteínas"))
    carbohydrates = models.FloatField(_("carboidratos"))
    fats = models.FloatField(_("gorduras"))

    class Meta:
        db_table = "food"

    def __str__(self):
        return self.name
