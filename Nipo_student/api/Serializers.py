from rest_framework import serializers
from Nipo_student import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['reg_no','first_name','middle_name','last_name','school_id','DateAdded']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ['id','name','location','DateAdded']
