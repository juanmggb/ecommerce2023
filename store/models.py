from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default="un-branded")

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "products"


    def __str__(self):

        return str(self.title)
