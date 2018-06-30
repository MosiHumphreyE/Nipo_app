from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class StudentView(View):

	# get method for testing my app and urls nothing of importances here
	def get(self, request, id):
		return HttpResponse('<h1>the requested student is {} </h1>'.format(id))


