from django.contrib import admin
from .models import  SystemAdmin,Course,Student,CourseRequest
# Register your models here.
admin.site.register(Student)
admin.site.register(SystemAdmin)
admin.site.register(Course)
admin.site.register(CourseRequest)


# change admin site header
admin.site.site_header = "Education Admin"
admin.site.site_title = "Education Admin Portal"