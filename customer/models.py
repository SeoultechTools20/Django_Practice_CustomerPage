from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    master = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    birthday = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)
    gender = models.BooleanField(default=True,null=True)
    degree = models.IntegerField(null=True)

    def __str__(self):
        return self.name + '(' + str(self.id) + ')'
