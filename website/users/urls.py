from django.urls import path
from .views import UserLoginView, SignUpView, UserPostDetail
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', UserLoginView.as_view(), name="register"),
    path('sign-up/', SignUpView.as_view(), name = "signup"),
    path('userpost', UserPostDetail.as_view(), name = "userpostdetail"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    ]
    
