from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def function_view_test(request):
    return HttpResponse('Holaaaaaaaaaaa')

class ClassViewTest(TemplateView):
    template_name = "test.html"
