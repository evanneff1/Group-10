from django.db import models

class MissingPersons(models.Model):
    date_missing = models.DateField()
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=30)

    def __str__(self):
        return (self.first_name, self.last_name)
