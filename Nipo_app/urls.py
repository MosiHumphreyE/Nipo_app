from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from Nipo_student.api import views as student_api_views


schema_view = get_swagger_view(title='Nipo student')

#Students routes
student_router = routers.DefaultRouter()
student_router.register(r'student', student_api_views.StudentViewSet)
student_router.register(r'school', student_api_views.SchoolViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('Nipo_student.urls')),
    url(r'^swagger/$', schema_view),
    url(r'^api/', include(student_router.urls))

]
