import os
import django
from django.core.exceptions import ImproperlyConfigured

# Replace YOUR_PROJECT with the actual Django project package if different from "myproject"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

try:
    django.setup()
except ImproperlyConfigured as exc:
    raise SystemExit(f"Failed to configure Django settings: {exc}")

from django.contrib.auth import get_user_model  # noqa: E402

User = get_user_model()
username = "admin"
email = "admin@example.com"
password = "password123"

if User.objects.filter(username=username).exists():
    print("Superuser already exists.")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully.")
