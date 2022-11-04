from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField("Slug", max_length=255)
    # products

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}/"


class Product(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField("Slug", max_length=255)
    description = models.TextField("Description", null=True, blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name="products",
    )
    price = models.IntegerField("Price")
    image = models.ImageField("Image", upload_to="products/", null=True, blank=True)

    def __str__(self):
        return self.name
