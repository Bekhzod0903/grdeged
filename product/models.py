from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import CustomUser
# Create your models here.

class CategoryFood(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_food'

    def __str__(self):
        return self.name

class Foods(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(CategoryFood, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='foods_image/', blank=True, null=True, default='default_img/food_img.png')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        db_table = 'foods'

    def __str__(self):
        return self.name


