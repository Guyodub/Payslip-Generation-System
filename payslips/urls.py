# payslips/urls.py
from django.urls import path
from .views import PayListView, PayDetailView, ProfileCreateView, ProfileUpdateView # new
urlpatterns = [
    path('profile/<int:pk>/edit/', ProfileUpdateView .as_view(), name='profile_edit'), # new
    path('', PayListView.as_view(), name='pay_list'),
    path('profile/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('<int:pk>', PayDetailView.as_view(), name='pay_detail'), # new
    ]