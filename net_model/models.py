from django.db import models

# Create your models here.

class CSV(models.Model):
    DicomID = models.CharField(max_length=60, primary_key=True)
    PatientID = models.CharField(max_length=60)

class DoctorUser(models.Model):
    UserID = models.CharField(max_length=60)
    SearchHistory = models.CharField(max_length=60)
    UserName = models.CharField(max_length=20)


class PatientInfo(models.Model):
    PatientID = models.CharField(max_length=60, primary_key=True)
    PatientName = models.CharField(max_length=20)
    PatientSex = models.CharField(max_length=5)
    PatientBirthday = models.DateField()



class PatientRecord(models.Model):
    RecordID = models.CharField(max_length= 60, primary_key=True)
    PatientID = models.CharField(max_length=60)
    Description = models.TextField()
    PartInfo = models.CharField(max_length=50)
    CTID = models.CharField(max_length=60)
    MedicalTime = models.DateField()
    PointAmount = models.IntegerField()

class CT(models.Model):
    CTID = models.CharField(max_length=60, primary_key=True)
    CTDate = models.DateField()
    PatientID = models.CharField(max_length=60)


class Node(models.Model):
    NodeID = models.CharField(max_length=60)
    Node_x = models.FloatField()
    Node_y = models.FloatField()
    Node_z = models.FloatField()
    Node_Inch = models.FloatField()
    illjudge = models.CharField(max_length=30)
    CTID = models.CharField(max_length=60)