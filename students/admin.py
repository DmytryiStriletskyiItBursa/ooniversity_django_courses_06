from django.contrib import admin
from students.models import Student

# Register your models here.

def upper_case_name(obj):
   return ("%s %s" % (obj.name, obj.surname))
upper_case_name.short_description = 'Full name'

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = [upper_case_name, 'email', 'skype']
    list_filter = ['courses']

    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'surname', 'date_of_birth')
        }),

        ('Contact Info', {
            'fields': ('email', 'phone', 'address', 'skype')
        }),

        (None, {'fields': ['courses']})
    )

    filter_horizontal = ['courses',]

admin.site.register(Student, StudentAdmin)
