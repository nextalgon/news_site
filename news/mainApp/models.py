from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="kategoriya nomi")

    def __str__(self):
        return self.name


class NewTopic(models.Model):
    name = models.CharField(max_length=100, verbose_name="yanglikning nomi")
    time = models.DateTimeField(verbose_name='vaxti')
    image = models.ImageField(null=True, verbose_name='rasm')
    description = models.TextField(max_length=10000, verbose_name='opisanie')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)