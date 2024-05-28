from django.urls import path
from .views import AccountRegisterView, LoginView

urlpatterns = [
    path("register/", AccountRegisterView.as_view()),
    path("login/", LoginView.as_view()),
]
