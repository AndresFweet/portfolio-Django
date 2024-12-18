import os
from django.core.wsgi import get_wsgi_application

# Configuración del entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')

# Iniciar la aplicación
application = get_wsgi_application()

# Crear automáticamente un superusuario (sin variables de entorno)
from django.contrib.auth import get_user_model
from django.db import OperationalError, IntegrityError

User = get_user_model()

try:
    # Define los datos del superusuario aquí directamente
    username = "admin"
    email = "andresjh10@hotmail.com"
    password = "admin123"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully!")
    else:
        print(f"Superuser '{username}' already exists.")
except (OperationalError, IntegrityError) as e:
    # Evitar errores si las migraciones no se han ejecutado
    print(f"Could not create superuser: {e}")
