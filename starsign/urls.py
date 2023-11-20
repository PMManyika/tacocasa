from django.urls import path
from . import views

urlpatterns = [
    path("", views.find_star, name="find_star"),
    path(
        "find_star_sign_success/",
        views.find_starsign_success,
        name="find_starsign_success",
    ),
    path(
        "success/<str:sign>/<str:gift>/",
        views.find_starsign_success,
        name="find_starsign_success",
    ),
    path("clear-session/", views.clear_session_and_redirect, name="clear_session"),
]
