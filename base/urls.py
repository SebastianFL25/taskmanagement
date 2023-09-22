from django.urls import path
from base.views import Login,Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
    
my_app= 'base'

urlpatterns = [
    path("login/",Login.as_view(),name="login"),
    path("logout/",Logout.as_view(),name="logout"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path("refresh-token/",UserTokenRefresh.as_view(),name="refreshtoken")
]