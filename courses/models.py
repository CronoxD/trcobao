
# Django
from django.db import models

# Models
from teachers.models import Teacher
from activities.models import Activity

class Course(models.Model):
    """ Course's Model"""

    teacher = models.ForeignKey(Teacher, on_delete='CASCADE')
    activities = models.ManyToManyField(Activity)

    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name