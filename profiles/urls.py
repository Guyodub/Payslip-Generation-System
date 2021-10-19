# payslips/urls.py
from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView # new
urlpatterns = [
    path('profile/<int:pk>/edit/',ProfileUpdateView.as_view(), name='profile_edit'), # new
    path('', ProfileListView.as_view(), name='profile_list'),
    path('profile/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('<int:pk>', ProfileDetailView.as_view(), name='profile_detail'), # new
    ]