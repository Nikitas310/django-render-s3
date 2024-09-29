from django.contrib import admin
from .models import Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'in_course_id',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)