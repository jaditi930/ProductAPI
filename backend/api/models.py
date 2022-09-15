from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(blank=False,max_length=120)
    price=models.FloatField(null=False)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)
