from django.urls import path
from .views import SignupView, HomepageView,LoginView,LogoutView

urlpatterns = [
    path("create/", SignupView.as_view(), name="signupurl"),
    path("home/", HomepageView.as_view(), name="homeurl"),
    path("",LoginView.as_view(),name="loginurl"),
    path("logout/",LogoutView.as_view(),name="logouturl"),
]

