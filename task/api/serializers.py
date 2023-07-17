from rest_framework import serializers
from task.models import Task, Status

class TaskSerializerModel(serializers.ModelSerializer):
    
    class Meta:
        model= Task
        fields = ('__all__')
        
class StatusSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields = ('__all__')
       