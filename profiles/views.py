
#payslips/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import UserProfile

class ProfileListView(ListView):
    model = UserProfile
    context_object_name = 'profile_list'
    template_name = 'profile/profile_list.html'


class ProfileDetailView(DetailView): # new
    model = UserProfile
    context_object_name = 'profile'
    template_name = 'profile/profile_detail.html'

class ProfileCreateView(CreateView):
    model = UserProfile
    template_name = 'profile/profile_create.html'
    fields = '__all__'

class ProfileUpdateView(UpdateView):
    model  = UserProfile
    template_name  = 'profile/profile_edit.html'
    fields = ['jobTitle', 'jobNumber', 'basicPay', 'deductions', 'allowances']
