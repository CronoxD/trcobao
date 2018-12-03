
# Django
from django.contrib import admin

# Locals
from Teachers.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone_number', 'avatar')