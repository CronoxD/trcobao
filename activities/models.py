from django.db import models
from teachers.models import Teacher


class Activity(models.Model):
    """ Activities model"""

    teacher = models.ForeignKey(Teacher, on_delete='CASCADE')

    name = models.CharField(max_length=30)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name