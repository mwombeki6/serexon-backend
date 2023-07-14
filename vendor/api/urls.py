from django.urls import path
from .views import (
    registerView,
    get_csrf,
    loginView,
    WhoAmIView,
    VendorOnlyView,
    check_auth,
    logoutView,
    checkEmail,
    email_available
)

urlpatterns = [
    path("csrf_cookie", get_csrf),
    path("check_auth", check_auth),
    path("register", registerView),
    path("login", loginView),
    path("dashboard", WhoAmIView.as_view()),
    path("dashboard2", VendorOnlyView.as_view()),
    path("logout", logoutView),
    path("check_email", checkEmail),
    path("email_available", email_available),
]
