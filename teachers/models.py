
# Django
from django.db import models

# Models
from django.contrib.auth.models import User

# Teacher model
class Teacher(models.Model):
    """
    Teacher model that extends from Django's User model
    with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, blank=True)

    avatar = models.ImageField(upload_to='teachers/avatars', blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    # GetFunctions

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def is_staff(self):
        return self.user.is_staff

    #def course(self):
    #    courses = Course.object.filter(teacher_id = self.user.id)
    #    return courses