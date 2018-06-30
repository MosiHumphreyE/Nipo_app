from rest_framework import viewsets, filters

from Nipo_student import models
from Nipo_student.api import Serializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = Serializers.StudentSerializer
    http_method_names = ['get', 'post', 'put', 'head', 'patch']

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = models.School.objects.all()
    serializer_class = Serializers.StudentSerializer
    http_method_names = ['get', 'post', 'put', 'head', 'patch']