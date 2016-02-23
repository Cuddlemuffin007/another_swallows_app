from django.db import models


class Stat(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    at_bats = models.IntegerField()
    hits = models.IntegerField()
    runs_batted = models.IntegerField()
    homeruns = models.IntegerField()
    runs = models.IntegerField()
    batting_average = models.FloatField()

    def __str__(self):
        name = "{} {}".format(self.first_name, self.last_name)
        return name
