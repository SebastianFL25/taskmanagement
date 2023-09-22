from django.urls import path
from .views import CreateGenericView,LisGenericAPIView,UpdateGenericAPIView,RetrieveDestroyGenericAPIView,Password

urlpatterns = [
    path("register/",CreateGenericView.as_view(),name="register"),
    path("list/",LisGenericAPIView.as_view(),name="list-user"),
    path("update/<int:pk>",UpdateGenericAPIView.as_view(),name="update-user"),
    path("retrieveanddestroy/<int:pk>",RetrieveDestroyGenericAPIView.as_view(),name="destroy-retrieve-user"),
    path("password/<int:pk>/",Password.as_view(),name="password-user"),

    
]