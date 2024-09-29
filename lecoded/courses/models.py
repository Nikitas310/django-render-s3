from django.db import models
from django.utils.text import slugify
from django.db.models import Count


class Course(models.Model):

    name = models.CharField(max_length=255, verbose_name='Course name')
    pic = models.ImageField(null=True, blank=True, verbose_name='Course picture')
    description = models.TextField(null=True, verbose_name='Course Description')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.name}'.capitalize()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):

    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Course')
    title = models.CharField(max_length=255, verbose_name='Lesson title')
    description = models.TextField(default='', verbose_name='Lesson description')
    in_course_id = models.IntegerField(default='0', verbose_name='In course ID')

    def __str__(self):
        return f'{self.title}'.capitalize()

    def save(self, *args, **kwargs):
        self.in_course_id = Lesson.objects.filter(course=self.course).count() + 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ('course', 'in_course_id')
        unique_together = ('course', 'in_course_id')

