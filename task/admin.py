from django.contrib import admin
from .models import Task,Status





    
class TaskAdmin(admin.ModelAdmin):

    
    list_display = ('title','Description','due_date','user_id','status')
    
class StatusAdmin(admin.ModelAdmin):
    list_display=("id","name")

admin.site.register(Task,TaskAdmin)
admin.site.register(Status)
