from django.db import models

# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return  self.name

class Branch(models.Model):
    dist=models.ForeignKey(District,on_delete=models.CASCADE, related_name='branch')
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Url(models.Model):
    dist = models.ForeignKey(District, on_delete=models.CASCADE)
    url=models.URLField(max_length=650)


    def __str__(self):
        return self.url
class Places(models.Model):
    name = models.CharField(max_length=250)
    dist=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    url=models.ForeignKey(Url,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return  self.name

class Kyc(models.Model):
    fname=models.CharField(max_length=250)
    dob=models.DateField(auto_now=True)
    mobile=models.CharField(max_length=13)
    mailid=models.CharField(max_length=250)
    address=models.TextField()
    def __str__(self):
        return  self.fname


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name



class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name