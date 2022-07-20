from django.contrib import admin

from main_app.models import Course, CourseCategory, News

admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(News)
