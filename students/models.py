from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """
    Student's Model
    """
    user = models.OneToOneField(User, on_delete='CASCADE')

    ACTI = 'ACTI'
    IRRE = 'IRRE'
    BAJ = 'BAJ'


    STATUS_CHOICES = (
        (ACTI, 'Activo'),
        (IRRE, 'Irregular'),
        (BAJ, 'Baja'),
    )

    status = models.CharField(
        max_length = 5,
        choices=STATUS_CHOICES,
        default=ACTI
    )

    government_id = models.CharField(max_length=10)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username