from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Place1(models.Model):
    person = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    detail = models.TextField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.name = None

    def __str__(self):
        return self.person
