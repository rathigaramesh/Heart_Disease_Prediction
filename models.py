from django.db import models

# Create your models here.
class hkdModel(models.Model):
    
    age = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.FloatField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
    sex_male = models.BooleanField()
