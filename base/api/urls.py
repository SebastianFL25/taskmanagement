from django.urls import path
from .views import CreateGenericView
from base.views import Login,Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/",CreateGenericView.as_view(),name="register"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",Logout.as_view(),name="logout"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]