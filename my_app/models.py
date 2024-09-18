from django.db import models
from datetime import datetime

# Create your models here.
class Verification(models.Model):
    id = models.AutoField(primary_key=True)
    certificateCourse = models.CharField(max_length=100)
    certificateNo = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    courseName = models.CharField(max_length=100)
    certificateStripes = models.CharField(max_length=100)
    participantName = models.CharField(max_length=100)
    passportNo = models.CharField(max_length=100)
    
    courseDate1 = models.DateField()
    courseDate2 = models.DateField()
    issueDate = models.DateField()
    certificateNumber = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
       
        self.certificateStripes = f"{self.certificateStripes+'/'}"
        self.certificateCourse = f"{self.certificateCourse+'/'}"
     
        # Combine certificateNo, certificateStripes, and certificateCourse to create certificateNumber
        self.certificateNumber = f"{self.certificateStripes}{self.certificateCourse}{self.certificateNo}"
        
        super().save(*args, **kwargs)
    def __str__(self):
        return self.certificateNo
    
class Verification1(models.Model):
    certificateCourse = models.CharField(max_length=100)
    certificateNo = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    courseName = models.CharField(max_length=100)
    certificateStripes = models.CharField(max_length=100)
    participantName = models.CharField(max_length=100)
    passportNo = models.CharField(max_length=100)
    courseDate1 = models.DateField()
    courseDate2 = models.DateField()
    issueDate = models.DateField()

    def __str__(self):
        return self.certificateNo
    
    