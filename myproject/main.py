import sys
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import *

#math = Subject.objects.get(id=1)
#teacher1 = Teacher(teacher_name='Николай', subject=math).save()
go = True
while go == True:
    i = input('''
        1. Add Subject \n
        2. Add Teacher \n
        3. Add Class \n
        4. Add Student \n
        5. Add Schedule \n
        6. Add Grade \n
        7. Exit  
    ''')

    if i == '1':
        try:
            Subject.objects.create(subject_name=input("Enter subject's name: \n"), subject_description=input("Enter subject's description: \n"))
        except:
            print("name must be unique!")

    elif i == '2':
        name = input("Enter teacher's subject: \n")
        if Subject.objects.filter(subject_name=name).exists():
            Teacher.objects.create(teacher_name=input("Enter teacher's name: \n"), teacher_surname=input("Enter teacher's surname: \n"), subject=Subject.objects.get(subject_name=name))
        else:
            print("subject does not exist!")

    elif i == '3':
        try:
            Class.objects.create(class_name=input("Enter class's name: \n"), class_year=input("Enter class's year: \n"))
        except:
            print("name must be unique!")

    elif i == '4':
        class_ = input("Enter student's class: \n")
        if Class.objects.filter(class_name=class_).exists():
            Student.objects.create(student_name=input("Enter student's name: \n"), student_surname=input("Enter student's surname: \n"), student_class=Class.objects.get(class_name=class_))
        else:
            print("class does not exist!")   

    elif i == '5':
        teacher_ = input("Enter shedule's teacher: \n")
        class_ = input("Enter shedule's class: \n")

        if Teacher.objects.filter(teacher_name=teacher_).exists():         
            if Class.objects.filter(class_name=class_).exists():

                Schedule.objects.create(day=input("Enter day: \n"), start_time=input("Enter start time: \n"), teacher=Teacher.objects.get(teacher_name=teacher_), shedule_class=Class.objects.get(class_name=class_), subject=(Teacher.objects.get(teacher_name=teacher_)).subject)

            else:
                print("class does not exist!") 
        else:
            print("teacher does not exist!")  

    elif i == '6':
        student_ = input("Enter student: \n")
        subject_ = input("Enter subject: \n")

        if Student.objects.filter(student_name=student_).exists():         
            if Subject.objects.filter(subject_name=subject_).exists():

                Grade.objects.create(grade=input("Enter grade: \n"), date=input("Enter date: \n"), subject=Subject.objects.get(subject_name=subject_), student=Student.objects.get(student_name=student_))

            else:
                print("subject does not exist!") 
        else:
            print("student does not exist!") 

    elif i == '7':
        go = False
    
    else:
        print('incorrect action!')