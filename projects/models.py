from django.contrib.postgres.fields import ArrayField
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    job_details = models.CharField(max_length=50, blank=True)
    job_details1 = models.CharField(max_length=50, blank=True)
    job_details2 = models.CharField(max_length=50, blank=True)
    job_details3 = models.CharField(max_length=50, blank=True)
    job_details4 = models.CharField(max_length=50, blank=True)
    job_details5 = models.CharField(max_length=50, blank=True)
    job_details6 = models.CharField(max_length=50, blank=True)
    job_details7 = models.CharField(max_length=50, blank=True)
    job_details8 = models.CharField(max_length=50, blank=True)
    job_details9 = models.CharField(max_length=50, blank=True)
    job_details10 = models.CharField(max_length=50, blank=True)
    job_details11 = models.CharField(max_length=50, blank=True)
    job_details12 = models.CharField(max_length=50, blank=True)
    job_details13 = models.CharField(max_length=50, blank=True)
    job_details14 = models.CharField(max_length=50, blank=True)
    job_details15 = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    image6 = models.ImageField(null=True, blank=True)
    image7 = models.ImageField(null=True, blank=True)
    image8 = models.ImageField(null=True, blank=True)
    image9 = models.ImageField(null=True, blank=True)
    image10 = models.ImageField(null=True, blank=True)
    image11 = models.ImageField(null=True, blank=True)
    image12 = models.ImageField(null=True, blank=True)
    image13 = models.ImageField(null=True, blank=True)
    image14 = models.ImageField(null=True, blank=True)
    image15 = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
