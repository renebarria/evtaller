from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Reseña de {self.product.name}"
