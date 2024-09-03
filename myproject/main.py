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
        3. Add Student \n
        4. Add Student \n
        5. Add Schedule \n
        6. Add Grade \n
        7. Exit  
    ''')
    if i == '1':
        Subject.objects.create(subject_name=input("Enter subject's name: \n"), subject_description=input("Enter subject's description: \n"))
    if i == '2':
        Teacher.objects.create(teacher_name=input("Enter teacher's name: \n"), teacher_surname=input("Enter teacher's surname: \n"), subject=Subject.objects.get(subject_name=input("Enter teacher's subject: \n")))
    elif i == '7':
        go = False
    else:
        print('incorrect action!')