from django.db import models


class Marque(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Article(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    remise = models.FloatField(default=0, max_length=1000)
    discription = models.CharField(max_length=500)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Article_images(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)

