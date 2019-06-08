from django.db import models


class Marker(models.Model):
    marker_coord = models.IntegerField()
