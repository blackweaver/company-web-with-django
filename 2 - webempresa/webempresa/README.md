#Para instalar el backend de Django:
conda create -n django2 python=3.6
source activate django2
pip install django==2.0.2
python -m django --version

#Procedo a crear un proyecto django
django-admin startproject 'webempresa'

#Para correr manage.py en el entorno virtual:
Botón derecho: 'Run Python File in Terminal', y luego
python manage.py runserver

#Para ver el entorno virtual en el Visual Studio Code:
python -m pip install -U pylint

#Para instalar la sintaxis del editor:
conda install pylint

# Documentación para los marcadores de Django
https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#built-in-template-tags-and-filters

# Instalación de paquete para manipular imágenes
pip install Pillow

# Creo la primera APP de base para el proyecto
python manage.py startapp core

# Creación de una aplicación para una sección dinámica
python manage.py startapp services

# Crear migración de la base de datos de la sección
python manage.py makemigrations
python manage.py migrate

# Creo el modelo para la tabla Project
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    subtitle = models.CharField(max_length=200, verbose_name = 'Subtítulo')
    content = models.TextField(verbose_name = 'Contenido')
    image = models.ImageField(verbose_name = 'Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ["created"]

    def __str__(self):
        return self.title

# Tipos de campo para el modelo de una base
https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

# Una vez accedo al admin http://127.0.0.1:8000/admin/ creo un superusuario
python manage.py createsuperuser

user: elgorrion
pass: Turco-4972-0

# Hacer que los textos de un nombre sean sustituídos
# En webpersonal/apps.py:

class PortfolioConfig(AppConfig):
    name = 'services'
    verbose_name = 'Servicios'

# En portfolio/models.py:
INSTALLED_APPS = [
   ...
    'services.apps.ServicesConfig',
]

# Importar en el archivo admin.py la app de Service

from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)




