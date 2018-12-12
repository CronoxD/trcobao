
# Django
from django.contrib import admin

# Locals
from teachers.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ('user', 'first_name', 'last_name', 'is_staff', 'is_verified')

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name'
    )

    list_filter = (
        'created_at',
        'updated_at',
        'user__is_active',
        'user__is_staff'
    )