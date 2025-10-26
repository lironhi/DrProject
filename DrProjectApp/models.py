from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class doctor_identification(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    login = models.TextField(db_column='login', max_length=8)
    password = models.TextField(db_column='password',max_length=10)
    idnumber = models.CharField(db_column='idnumber', max_length=9)
    type = models.TextField(db_column='type')

    class Meta:
        managed = False
        db_table = 'drproject_auth'

class new_Patient(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    firstname = models.TextField(db_column='firstname')
    lastname = models.TextField(db_column='lastname')
    age = models.IntegerField(db_column='age')
    gender = models.TextField(db_column='gender')
    idnum = models.CharField(db_column='idnum', max_length=9)
    wbc = models.FloatField(db_column='wbc')
    neut = models.FloatField(db_column='neut')
    lymph = models.FloatField(db_column='lymph')
    rbc = models.FloatField(db_column='rbc')
    hct = models.FloatField(db_column='hct')
    urea = models.FloatField(db_column='urea')
    hb = models.FloatField(db_column='hb')
    creatin = models.FloatField(db_column='creatin')
    iron = models.FloatField(db_column='iron')
    hdl = models.FloatField(db_column='hdl')
    alkaph = models.FloatField(db_column='alkaph')
    smocker = models.TextField(db_column='smocker')
    fever = models.TextField(db_column='fever')
    vomiting = models.TextField(db_column='vomiting')
    diarrhea = models.TextField(db_column='diarrhea')
    medic = models.TextField(db_column='medic')
    diet = models.TextField(db_column='diet')
    sport = models.TextField(db_column='sport')
    pregnant = models.TextField(db_column='pregnant')

    class Meta:
        managed = True
        db_table = 'drproject_patient'