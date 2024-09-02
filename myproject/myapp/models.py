from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Class(models.Model):
    class_name = models.CharField(max_length=20)

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)