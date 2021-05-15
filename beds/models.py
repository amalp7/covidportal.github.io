from django.db import models

from django.contrib.auth.models import User

# Create your models here.
dt = (
    ('AL','Alapuzha'),
    ('ER','Ernakulam'),
    ('ID','Iduki'),
    ('KN','Kannur'),
    ('KL','Kollam'),
    ('KS','Kasargod'),
    ('KT','Kottayam'),
    ('KZ','Kozhikode'),
    ('MA','Malapuram'),
    ('PL','Palakkad'),
    ('PT','Pathanamthitta'),
    ('TV','Thiruvanathapuram'),
    ('TS','Thrissur'),
    ('WA','Wayanad')
)

class Hospital(models.Model):
    sc = (
        ('gov','government'),
        ('prv','private')
    )

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=2,choices=dt)
    phone = models.CharField(max_length=15)
    sector = models.CharField(max_length=3,choices=sc)
    covid_beds = models.IntegerField()
    normal_beds = models.IntegerField()
    icu_beds = models.IntegerField()
    ventilator = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.name+" "+self.location

class Patient(models.Model):
    ct =(
        ('cv','Covid'),
        ('NC','Non-covid')
    )
    st = (
        ('W','Waiting'),
        ('A','Admitted'),
        ('D', 'Discharged')
    )        
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    adharno = models.IntegerField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    district = models.CharField(max_length=2,choices=dt)
    category = models.CharField(max_length=2,choices=ct)
    # status = models.CharField(max_length=2,choices=st)
    status = models.CharField(max_length=2,choices=st,blank=True,default='W') #to make this field not required and default value W

    def __str__(self):
        return self.name


class BedAllocation(models.Model):
    ct = (
        ('C','Covid'),
        ('N','Normal'),
        ('I','Icu'),
        ('V','Ventilator')
    )        
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    category =models.CharField(max_length=2,choices=ct)

    def __str__(self):  
        return str(self.patient) #return self.patient will return a non-string so add str(self.patient) to make it string