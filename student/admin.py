from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	list_display = ['studentName' , 'studentGender' , 'studentPicture']

admin.site.register(Student , StudentAdmin)