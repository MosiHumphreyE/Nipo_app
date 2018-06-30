from django.db import models

class School(models.Model):
	id = models.CharField(primary_key=True, max_length=15)
	name = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	DateAdded = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
	reg_no = models.CharField(primary_key=True, max_length=15)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	school_id = models.ForeignKey(School, on_delete=models.CASCADE)
	DateAdded = models.DateTimeField(auto_now_add=True)


