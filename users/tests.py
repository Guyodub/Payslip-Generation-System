# Create your tests here.

'''
Import TestCase and get_user_model 

Then create tests::

test_create_user to confirm that a user can be created.

First we set our user model to the variable User and
then create one via the manager method create_user which
does the actual work of creating a new user with the proper permissions.

For test_create_superuser test that a superuser can be created.
'''

from django.test import TestCase

from django.contrib.auth import get_user_model


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

    




