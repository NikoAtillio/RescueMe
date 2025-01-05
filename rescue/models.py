from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.species}"

class RescueCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    rescue_center = models.ForeignKey(RescueCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name