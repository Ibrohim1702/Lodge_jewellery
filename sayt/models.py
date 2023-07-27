from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.email
