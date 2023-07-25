from django.urls import path
from .views import StatusLisCreateApiView
    
    
urlpatterns = [
    path("status",StatusLisCreateApiView.as_view(),name="list-create-status"),


]