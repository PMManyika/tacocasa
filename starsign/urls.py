from django.urls import path
from . import views

urlpatterns = [
    # Home page or the initial page where users start finding their star sign
    path("", views.find_star, name="find_star"),
    # URL pattern for handling the AJAX request to find the star sign
    # Assuming 'find_star' view handles both the initial rendering and the AJAX request
    path("find-star-sign/", views.find_star, name="ajax_find_star"),
    # URL pattern for handling the success page after mobile number submission
    # Assuming 'find_starsign_success' view takes 'sign' and 'gift' as arguments
    path(
        "success/<str:sign>/<str:gift>/",
        views.find_starsign_success,
        name="find_starsign_success",
    ),
    # URL pattern for clearing session and restarting the process
    path("clear-session/", views.clear_session_and_redirect, name="clear_session"),
]
