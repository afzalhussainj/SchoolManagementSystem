from django.contrib import admin
from .models import Student, Staff, School

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Staff)