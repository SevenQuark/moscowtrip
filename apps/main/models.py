from django.db import models
from picklefield.fields import PickledObjectField
from apps.main import placer


class Place(models.Model):
    place_id = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    data = PickledObjectField()
    day1 = PickledObjectField()
    day2 = PickledObjectField()
    day3 = PickledObjectField()
    day4 = PickledObjectField()
    day5 = PickledObjectField()
    day6 = PickledObjectField()
    day7 = PickledObjectField()


class InstagramImage(models.Model):
    create_date = models.DateTimeField()
    place_id = models.ForeignKey(Place)
