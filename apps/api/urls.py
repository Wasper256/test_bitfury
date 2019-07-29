from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from apps.accounts import views as auth_views

app_name = 'api'

urlpatterns = [
    path('registration/', auth_views.CreateUserView.as_view()),
    path('login/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('', include('rest_auth.urls')),
    path('', include('apps.posts.urls')),
]
