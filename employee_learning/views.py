from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import LearningCourse, Employee
from django.urls import reverse_lazy
import datetime

class Index (TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

class CourseList (LoginRequiredMixin, ListView):
    # model = LearningCourse
    queryset = LearningCourse.objects.all()
    # queryset = LearningCourse.objects.order_by('title')
    # queryset = LearningCourse.objects.filter(title__startswith='L')
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

class CourseDetail (LoginRequiredMixin, DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'

class CourseCreate (LoginRequiredMixin, CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

class CourseUpdate (LoginRequiredMixin, UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

class CourseDelete (LoginRequiredMixin, DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')

class EmployeeDetail (DetailView):
    model = Employee
    template_name = 'employee_learning/employee_detail.html'
    context_object_name = 'employee_object'