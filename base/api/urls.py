from django.urls import path
from .views import CreateGenericView

urlpatterns = [
    path("register/",CreateGenericView.as_view(),name="register"),
]