import os
import sys

# Добавляем путь к проекту (на случай, если Vercel его не видит)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Явно указываем, где искать настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application
