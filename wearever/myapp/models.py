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

    #def get_last_rec(self): returns last set of recommended clothing with date in dictionary as {'toprec': X, 'bottomrec': X, 'footwearrec': X, 'layersrec': X, 'date': X}

    #def save_feedback(self, top, bottom, footwear, layers, date): saves feedback into database for date, overrides if feedback already exists for that date (maybe return weather too?)

    #def get_rec(self, temp, humi, wind, user='default'): returns dictionary with recommendations as previously described (no date), if user not specified give default(for non-logged in home page)