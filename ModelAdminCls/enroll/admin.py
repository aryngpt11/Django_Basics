from django.contrib import admin
from enroll.models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass')

admin.site.register(Students,StudentAdmin)
