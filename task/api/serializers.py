from rest_framework import serializers
from task.models import Task, Status

class TaskSerializerModel(serializers.ModelSerializer):
    
    class Meta:
        model= Task
        fields =('__all__')
    
    def to_representation(self,instance):
        return {
            'id':instance.id,
            'Title':instance.title,
            'Description':instance.Description,
            'Fecha':instance.due_date,
            'User':instance.user.email,
            'status':instance.status.name
            }

class StatusSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields= ('name',)
        #exclude= ('id',)
    
        def to_representation(self,instance):
            return {
                'status':instance.name
            } 
            
    
class TaskUpdateSerializerModel(serializers.ModelSerializer):

    due_date =serializers.DateTimeField(required=False)
    class Meta:
        model=Task
        fields = ('title','Description','due_date','status',)
        #exclude=('id','user',)
        def to_representation(self,instance):
            return {
            'Title':instance.title,
            'Description':instance.Description,
            'Due_Date':instance.due_date,
            'User':instance.user.email,
            'status':instance.status.name
            } 
            
class TaskAssingToNewUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Task
        fields=('user',)
        
        def to_representation(self,instance):
            return {
            'Title':instance.title,
            'Description':instance.Description,
            'User':instance.user
            
            } 
            
class TaskStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Task
        fields=('status',)
        
        def to_representation(self,instance):
            return {
            'Title':instance.title,
            'Description':instance.Description,
            'status':instance.status
            
            } 
            

       