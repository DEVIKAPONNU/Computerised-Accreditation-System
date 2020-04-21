from django.db import models
from django.db.models import Model
from django import forms
from django.contrib.auth.models import User



class Semester1(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester2(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester3(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester4(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester5(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester6(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester7(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class Semester8(models.Model):
    sub_name = models.CharField(max_length=50, unique=True)
    co1 = models.CharField(max_length=200,blank=True)
    co2 = models.CharField(max_length=200,blank=True)
    co3 = models.CharField(max_length=200,blank=True)
    co4 = models.CharField(max_length=200, blank=True)
    co5 = models.CharField(max_length=200, blank=True)
    co6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.sub_name
    def __unicode__(self):
        return self.sub_name
class InternshipTable(models.Model):
    iname = models.CharField(max_length=50,null=False)
    organisation = models.CharField(max_length=200,null=False)
    from_date=models.DateField()
    to_date=models.DateField()
    def __str__(self):
        return self.iname
    def __unicode__(self):
        return self.iname

class OnlinecourseTable(models.Model):
    course_name = models.CharField(max_length=50,null=False)
    website = models.CharField(max_length=200,null=False)
    course_date=models.DateField()
    def __str__(self):
        return self.course_name
    def __unicode__(self):
        return self.course_name

class BTechProgram(models.Model):
    ProgramName = models.CharField(max_length=10)
    Department= models.CharField(max_length=50, unique=True)
    YearOfStart = models.IntegerField()
    InTake = models.IntegerField()
    IncreaseInTakeIfAny = models.CharField(max_length=10)
    YearOfIncrease = models.CharField(max_length=10)
    AICTEApproval = models.BooleanField()
    AccreditationStatus = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.Department
    def __unicode__(self):
        return self.Department

class VisionMission(models.Model):
    Vision = models.CharField(max_length=500)
    Mission= models.CharField(max_length=500)
    Area = models.CharField(max_length=15)
    def __str__(self):
        return self.Area
    def __unicode__(self):
        return self.Area

class ContactInfo(models.Model):
    InstitutionHeadName = models.CharField(max_length=50)
    HeadDesignation= models.CharField(max_length=500)
    NBACoordinatorName = models.CharField(max_length=50)
    CoordinatorDesignation= models.CharField(max_length=500)
    def __str__(self):
        return self.InstitutionHeadName
    def __unicode__(self):
        return self.InstitutionHeadName


class ExpertTalk(models.Model):
    AcademicYear = models.CharField(max_length=7)
    Gap = models.CharField(max_length=30)
    Topic = models.CharField(max_length=100)
    Date=models.DateField()
    ExpertWithDesignation = models.CharField(max_length=100)
    Studentsnumber = models.IntegerField()
    RelavantPO_PSO = models.CharField(max_length=20)
    def __str__(self):
        return self.Topic
    def __unicode__(self):
        return self.Topic

class RegularEmployee(models.Model):
    AcademicYear = models.CharField(max_length=7)
    EngineeringMaleMin = models.IntegerField()
    EngineeringMaleMax = models.IntegerField()
    EngineeringFemaleMin = models.IntegerField()
    EngineeringFemaleMax = models.IntegerField()
    OtherFacultyMaleMin = models.IntegerField()
    OtherFacultyMaleMax = models.IntegerField()
    OtherFacultyFemaleMin = models.IntegerField()
    OtherFacultyFemaleMax = models.IntegerField()
    NonTeachingMaleMin = models.IntegerField()
    NonTeachingMaleMax = models.IntegerField()
    NonTeachingFemaleMin = models.IntegerField()
    NonTeachingFemaleMax = models.IntegerField()
    def __str__(self):
        return self.AcademicYear
    def __unicode__(self):
        return self.AcademicYear

class ContractEmployee(models.Model):
    AcademicYear = models.CharField(max_length=7)
    EngineeringMaleMin = models.IntegerField()
    EngineeringMaleMax = models.IntegerField()
    EngineeringFemaleMin = models.IntegerField()
    EngineeringFemaleMax = models.IntegerField()
    OtherFacultyMaleMin = models.IntegerField()
    OtherFacultyMaleMax = models.IntegerField()
    OtherFacultyFemaleMin = models.IntegerField()
    OtherFacultyFemaleMax = models.IntegerField()
    NonTeachingMaleMin = models.IntegerField()
    NonTeachingMaleMax = models.IntegerField()
    NonTeachingFemaleMin = models.IntegerField()
    NonTeachingFemaleMax = models.IntegerField()
    def __str__(self):
        return self.AcademicYear
    def __unicode__(self):
        return self.AcademicYear

class Maintenance(models.Model):
    Problem = models.CharField(max_length=200)
    ImprovementNeeded = models.CharField(max_length=200)
    def __str__(self):
            return self.Problem
    def __unicode__(self):
            return self.Problem
class Facility(models.Model):
    LabName = models.CharField(max_length=20)
    Systems = models.IntegerField()
    Projectors = models.IntegerField()
    Scanners = models.IntegerField()
    Printers = models.IntegerField()
    def __str__(self):
            return self.LabName
    def __unicode__(self):
            return self.LabName
