from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'skype']
    fieldsets = [
            ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
            ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
            (None, {'fields': ['courses']})
            ]
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horizontal = ['courses']
admin.site.register(Student, StudentAdmin)
