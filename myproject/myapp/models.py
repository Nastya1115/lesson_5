from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=20, unique=True)
    subject_description = models.CharField(max_length=20)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_surname = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Class(models.Model):
    class_name = models.CharField(max_length=20, unique=True)
    class_year = models.IntegerField()

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_surname = models.CharField(max_length=20)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

class Schedule(models.Model):
    day = models.CharField(max_length=10)
    start_time = models.CharField(max_length=5)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    shedule_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Grade(models.Model):
    grade = models.IntegerField()
    date = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)