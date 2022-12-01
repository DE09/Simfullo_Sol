from django.db import models

# Create your models here.
class lcl(models.Model):
    origin = models.CharField(max_length=15)
    dest = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    cur = models.CharField(max_length=15)
    rate = models.CharField(max_length=15)
    unit = models.CharField(max_length=15)
    chargeAt = models.CharField(max_length=15)
    group = models.CharField(max_length=15)
    
class fcl(models.Model):
    origin = models.CharField(max_length=15)
    dest = models.CharField(max_length=15)
    line = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    cur = models.CharField(max_length=15)
    rate = models.CharField(max_length=15)
    unit = models.CharField(max_length=15)
    chargeAt = models.CharField(max_length=15)
    group = models.CharField(max_length=15)
    

class air(models.Model):
    origin = models.CharField(max_length=15)
    dest = models.CharField(max_length=15)
    consol = models.CharField(max_length=15)
    line = models.CharField(max_length=15)
    cur = models.CharField(max_length=15)
    minimum = models.CharField(max_length=15)
    normal = models.CharField(max_length=15)
    over45 = models.CharField(max_length=15)
    over100 = models.CharField(max_length=15)
    over300 = models.CharField(max_length=15)
    over500 = models.CharField(max_length=15)
    over1000 = models.CharField(max_length=15)
    fsc = models.CharField(max_length=15)
    skdl = models.CharField(max_length=15)
    via = models.CharField(max_length=15)
    
class airother(models.Model):
    airother_origin = models.CharField(max_length=15)
    airother_dest = models.CharField(max_length=15)
    airother_consol = models.CharField(max_length=15)
    airother_line = models.CharField(max_length=15)
    airother_name = models.CharField(max_length=15)
    airother_cur = models.CharField(max_length=15)
    airother_rate = models.CharField(max_length=15)
    airother_unit = models.CharField(max_length=15)
    airother_chargeAt = models.CharField(max_length=15)
    


    
    
