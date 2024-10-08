from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Login

# Login App Tests
class LoginModelTests(TestCase):
    def setUp(self):
        Login.objects.create(username="testuser", password="testpass")

    def test_login_creation(self):
        login = Login.objects.get(username="testuser")
        self.assertEqual(login.password, "testpass")

    def test_login_str_method(self):
        login = Login.objects.get(username="testuser")
        self.assertEqual(str(login), "testuser")

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Login.objects.create(username="testuser", password="testpass")

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertRedirects(response, reverse('main'))

    def test_login_view_post_wrong_password(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpass'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Incorrect password.")

    def test_login_view_post_nonexistent_user(self):
        response = self.client.post(reverse('login'), {'username': 'nonexistent', 'password': 'testpass'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Username does not exist.")

class LoginUrlTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)  # Redirects to login page if not authenticated