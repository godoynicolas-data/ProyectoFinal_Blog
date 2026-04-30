from django.urls import path
from .views import (
    signup_view,
    CustomLoginView,
    CustomLogoutView,
    profile_view,
    edit_profile_view,
    CustomPasswordChangeView
)

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='change_password'),
]