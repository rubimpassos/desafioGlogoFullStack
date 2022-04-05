from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _

from .food import get_foods_from_file


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


class ImportedFile(models.Model):
    file = models.FileField(_("arquivo"), upload_to="foods")

    class Meta:
        db_table = "imported_file"

    def __str__(self):
        return self.file.name


@receiver(post_save, sender=ImportedFile)
def import_file(sender, instance, created, **kwargs):
    if not created:
        return

    food_df = get_foods_from_file(instance.file.path)
    db_foods = Food.objects.in_bulk(field_name="name")
    food_to_create = {}
    food_to_update = {}

    for index, row in food_df.iterrows():
        food = Food(
            name=row["name"],
            quantity=row["quantity"],
            proteins=row["proteins"],
            carbohydrates=row["carbohydrates"],
            fats=row["fats"],
        )

        if db_food := db_foods.get(row["name"]):
            food.id = db_food.id
            food_to_update.setdefault(db_food.id, food)
        else:
            food_to_create.setdefault(row["name"], food)

    Food.objects.bulk_create(food_to_create.values(), batch_size=1000)
    Food.objects.bulk_update(
        food_to_update.values(),
        fields=["quantity", "proteins", "carbohydrates", "fats"],
        batch_size=1000,
    )
