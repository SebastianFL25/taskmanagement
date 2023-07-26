from django.urls import path
from .views import StatusLisCreateApiView,TaskAssingToNewUser,TaskStatus
    
    
urlpatterns = [
    path("status",StatusLisCreateApiView.as_view(),name="list_create_status"),
    path('task/<int:id>/assign/', TaskAssingToNewUser.as_view(), name='assign_task'),
    path('task/<int:id>/complete/', TaskAssingToNewUser.as_view(), name='assign_task'),

   
]