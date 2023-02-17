from django.contrib.auth.views import LoginView

from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LoginView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
]
