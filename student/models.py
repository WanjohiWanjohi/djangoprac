from django.db import models

# Create your models here.
SEX = [
('M', 'Male'),
('F' , 'Female'),
('N' , 'Non-Binary')
]
class Student(models.Model):
	studentName = models.CharField(max_length=120 , blank=False)
	studentAge = models.IntegerField()
	studentGender = models.CharField(max_length=60 , choices=SEX)
	studentPicture = models.ImageField(upload_to='media/')
	studentFee = models.IntegerField()

	def __str__(self):
		return self.studentName