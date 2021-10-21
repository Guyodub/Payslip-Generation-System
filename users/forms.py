# users/forms.py
#forms.py
'''
We import CustomUser model via get_user_model
which looks to our AUTH_USER_MODEL config
in settings.py

Then we create new forms CustomUserCreationForm and 
CustomUserChangeForm that extends the base user forms 
imported above ans specify swapping in our CustomUser model
and displaying the fields email and username

The password field is implictly included by default 

'''
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
