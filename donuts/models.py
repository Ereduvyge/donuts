from django.db import models

# Create your models here

class Donut(models.Model):
    nameID=models.CharField(max_length=30, primary_key=True)
    price=models.FloatField()
    name=models.CharField(max_length=30)
    onSale=models.BooleanField()
    isSpecial=models.BooleanField()
    description=models.TextField()
    image=models.ImageField(upload_to='theme', default='theme/homer.jpg')

    def __unicode__(self):
        return self.name
        return self.description
