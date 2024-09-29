from rest_framework import viewsets
from .serializers import CourseSerializer, LessonSerializer
from .models import Course, Lesson
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse


class CoursesFullData(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonsView(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('course', None)
        if slug:
            return Lesson.objects.filter(course__slug=slug)
        return Lesson.objects.all()


def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    return HttpResponse('You did it!!!')