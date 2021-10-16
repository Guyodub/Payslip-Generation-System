#pay/tests.py
'''
At the top we import SimpleTestCase as well as reverse which is 
useful for testing our URLs.

Then we create a class called HomepageTests that extends SimpleTestCase and within it we 
add a method for each unit test.

We are adding self as the first argument of each unit test
'''


# Create your tests here.
from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, resolve 

from .views import AboutPageView, HomePageView

class HomePageTests(SimpleTestCase):

    '''
    Run the followings tests: 
    1. test_homepage_status_code - to check that the http status code for the homepage equals 200 which
    means that it exists.
    2. test_homepageview_status_code - we are creating a variable called response that acceses the homepage(/)
    and then uses python's assertEqual to check that the status code matches 200.
    3. test_homepage_url_name 
    '''


    '''
    Testing Templates:

    We have testes that the homepage exists but we shou;d also confirm 
    that it uses the correct template.

    The SimpleTestCode comes with a method assertTemplateUsed amd we use it.
    '''

    '''
    Resolve:

    A final views check we do is that our HomePageView resolves a given URL path.

    Django contains the utility function resolve for this purpose.

    We import resolve as well as the HomePageView at the top of this file

    Our actual test, test_homepage_url_resolves_homepageview, checks that the
    name of the view used to resolve /  matches HomePageView
    '''
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    
    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Payslip')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'guyo'
        )
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')

        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'Payslip')


    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'I am a data scientist'
        )
    
    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )