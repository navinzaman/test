from django.db import models


# Create your models here.


class StudentInfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    studentmajor = models.CharField(max_length=100)
    studentyear = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)
    

class CourseData(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=100)
    coursename = models.CharField(max_length=100)
    coursesectioncode = models.IntegerField(max_length=100)
    coursedepartment = models.CharField(max_length=100)
    instructorname = models.CharField(max_length=100)
    
    
class FacultyComment(models.Model):
        facultyemail = models.CharField(max_length=500)
        facultycomment = models.TextField()
        
    
class Enrollment(models.Model):
    student = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

