from django.db import models

# Create your models here.
class Recommendation(models.Model):
    email = models.EmailField()
    temp = models.FloatField()
    humidity = models.IntegerField()
    windspeed = models.FloatField()
    date = models.DateField(auto_now_add=True)
    rec = models.JSONField()

    def __str__(self):
        return '{} {}: {}'.format(self.email, self.date, self.rec)