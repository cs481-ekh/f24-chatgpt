from django.contrib.auth.models import User

User.objects.create_superuser(‘admin’, ‘no@gmail.com’, ‘1234’)