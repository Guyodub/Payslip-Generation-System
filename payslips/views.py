
#payslips/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import UserProfile

class PayListView(ListView):
    model = UserProfile
    context_object_name = 'pay_list'
    template_name = 'payslips/pay_list.html'

class PayDetailView(DetailView): # new
    model = UserProfile
    context_object_name = 'pay'
    template_name = 'payslips/pay_detail.html'

class ProfileCreateView(CreateView):
    model = UserProfile
    template_name = 'payslips/profile_create.html'
    fields = '__all__'

class ProfileUpdateView(UpdateView): # new
    model = UserProfile
    template_name = 'payslips/profile_edit.html'
    fields = '__all__'

