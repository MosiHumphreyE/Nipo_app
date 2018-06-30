from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from Nipo_student.api import views as student_api_views


schema_view = get_swagger_view(title='Nipo student')

# Students routes which includes two models
student_router = routers.DefaultRouter()
student_router.register(r'student', student_api_views.StudentViewSet)
student_router.register(r'school', student_api_views.SchoolViewSet)

urlpatterns = [
	# Nothing of importance still here 
    path('admin/', admin.site.urls),
    # Urls to the student app nothing of importance just on test method
    path('student/', include('Nipo_student.urls')),
    # Swagger view for viewind the api eg: localhost:8000/swagger gives you all the api
    url(r'^swagger/$', schema_view), 
    # api urls for the student and school data
    url(r'^api/', include(student_router.urls))

]
