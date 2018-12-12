
# Django
from django.contrib import admin

# Models
from students.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('user', 'status')