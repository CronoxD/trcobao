from django.db import models
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username