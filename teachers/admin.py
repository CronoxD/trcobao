
# Django
from django.contrib import admin

# Locals
from teachers.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone_number', 'avatar')