from django.urls import path
from Nipo_student.views import StudentView

urlpatterns=[
	path('<int:id>', StudentView.as_view()),
]