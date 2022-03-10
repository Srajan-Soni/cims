from django.db import models

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'status'


class State(models.Model):
    state = models.CharField(max_length=35)

    class Meta:
        db_table = 'states'


class City(models.Model):
    city = models.CharField(max_length=35)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'cities'
