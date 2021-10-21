# Create your tests here.
#tests.py
'''
Import TestCase and get_user_model 

Then create tests::

test_create_user to confirm that a user can be created.

First we set our user model to the variable User and
then create one via the manager method create_user which
does the actual work of creating a new user with the proper permissions.

For test_create_superuser test that a superuser can be created.
'''

'''
test sign up functionality!

test_signup_template which tests for the status code, template used and 
both included and excluded text similarly to how we did it in the last chapter of the homepage.
'''

from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'guyo',
            email = 'guyodubjarso@gmail.com',
            password = '123'
        )

        self.assertEqual(user.username, 'guyo')
        self.assertEqual(user.email, 'guyodubjarso@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'guyo',
            email = 'guyodubjarso@gmail.com',
            password = '123'
        )

        self.assertEqual(admin_user.username, 'guyo')
        self.assertEqual(admin_user.email, 'guyodubjarso@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase): # new
    username = 'guyo'
    email = 'guyodubjarso@gmail.com'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
        
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)




