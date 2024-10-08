import os
from pathlib import Path
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application

class SDPConfigTest(TestCase):
    def test_secret_key_setting(self):
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertNotEqual(settings.SECRET_KEY, '')

    def test_debug_setting(self):
        self.assertFalse(settings.DEBUG)  # False is safer for production

    def test_allowed_hosts_setting(self):
        self.assertIn('testserver', settings.ALLOWED_HOSTS)

    def test_installed_apps(self):
        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.auth', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.contenttypes', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.sessions', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.messages', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.staticfiles', settings.INSTALLED_APPS)
        self.assertIn('login', settings.INSTALLED_APPS)
        self.assertIn('main', settings.INSTALLED_APPS)

    def test_middleware(self):
        self.assertIn('django.middleware.security.SecurityMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.contrib.sessions.middleware.SessionMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.middleware.common.CommonMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.middleware.csrf.CsrfViewMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.contrib.auth.middleware.AuthenticationMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.contrib.messages.middleware.MessageMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.middleware.clickjacking.XFrameOptionsMiddleware', settings.MIDDLEWARE)

    def test_root_urlconf_setting(self):
        self.assertEqual(settings.ROOT_URLCONF, 'SDP.urls')

    def test_wsgi_application_setting(self):
        self.assertEqual(settings.WSGI_APPLICATION, 'SDP.wsgi.application')

    def test_database_setting(self):
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.sqlite3')
        self.assertIsInstance(settings.DATABASES['default']['NAME'], (str, Path))

    def test_language_code_setting(self):
        self.assertEqual(settings.LANGUAGE_CODE, 'en-us')

    def test_time_zone_setting(self):
        self.assertEqual(settings.TIME_ZONE, 'UTC')

    def test_static_url_setting(self):
        self.assertEqual(settings.STATIC_URL, '/static/')

    def test_default_auto_field_setting(self):
        self.assertEqual(settings.DEFAULT_AUTO_FIELD, 'django.db.models.BigAutoField')

    def test_login_redirect_url_setting(self):
        self.assertEqual(settings.LOGIN_REDIRECT_URL, 'main')

class SDPURLsTest(TestCase):
    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')
        resolver = resolve('/admin/')
        self.assertEqual(resolver.app_name, 'admin')

    def test_login_url(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.__name__, 'login_view')  # Assuming your view function is named 'login_view'

    def test_main_url(self):
        resolver = resolve('/main/')
        self.assertEqual(resolver.func.__name__, 'main')  # Assuming your view function is named 'main'
        
class SDPWSGITest(TestCase):
    def test_wsgi_application(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SDP.settings')
        application = get_wsgi_application()
        self.assertIsNotNone(application)

class SDPASGITest(TestCase):
    def test_asgi_application(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SDP.settings')
        application = get_asgi_application()
        self.assertIsNotNone(application)