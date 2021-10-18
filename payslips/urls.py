# payslips/urls.py
from django.urls import path
from .views import PayListView, PayDetailView, ProfileCreateView# new
urlpatterns = [
    path('', PayListView.as_view(), name='pay_list'),
    path('profile/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('<int:pk>', PayDetailView.as_view(), name='pay_detail'), # new
    ]