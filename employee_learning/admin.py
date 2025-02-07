from django.contrib import admin

# Register your models here.

from .models import Division, Employee, PersonalInfo, LearningCourse

admin.site.register(Employee)
admin.site.register(Division)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)