from django.db import models

# Create your models here.
class School(models.Model):
    branch_name = models.CharField(max_length=200)
    branch_address = models.CharField(max_length=1000)
    
    def total_students(self):
        return self.student_set.count()
    
    def total_staff(self):
        return self.staff_set.count()

class Student(models.Model):
    name = models.CharField(max_length=50)
    grades = ['play group', 'nursery'] + [str(i) for i in range(1,11)]
    grade_choices = [(i,i) for i in grades]
    grade = models.CharField(choices=grade_choices, max_length=50)
    fee = models.IntegerField()
    contact = models.CharField(max_length=11)
    branch = models.ForeignKey(School, on_delete=models.PROTECT)

class Staff(models.Model):
    name = models.CharField(max_length=50)
    designation_choices = [
        ("principal" , "principal"),
        ("vice principal" , "vice principal"),
        ("teacher" , "teacher"),
        ("incharge" , "incharge"),
        ("peon" , "peon"),
        ("guard" , "guard")
    ]
    designation = models.CharField(choices=
                                   designation_choices, max_length=50)
    number = models.CharField(max_length=11)
    email = models.EmailField(max_length=250, null=True)
    salary = models.IntegerField()
    branch = models.ForeignKey(School, on_delete=models.PROTECT)
    