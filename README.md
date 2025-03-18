<!-- 
# Titulos
## Subtitulos
### Segundo subtitulo
#### Tercer subtitulo
texto nomal
_efecto cursiva_
`efecto resaltador`
**efecto negrita**
* puntos para resaltar
[Enlaces](https://github.com/ErnestoFlo/CB-SistemaDisk_VB.Net/archive/refs/heads/master.zip)

imagenes ↓
<p align="center" width="100%"><img src="https://raw.githubusercontent.com/ErnestoFlo/CB-SistemaDisk_VB.Net/refs/heads/master/Documentacion/Menu%20pricipal.png" /></p>

resaltar codigo ↓
```vb
    Protected Function conectado()
        Try
            cnn = New SqlConnection("data source=AquiPonesTuInstanciaEnElServidor; initial catalog=sistema_discos ;integrated security= true")
            cnn.Open()
            Return True
        Catch ex As Exception
            MsgBox(ex.Message)
            Return False
        End Try
    End Function
```
cuadros aclarativos ↓
> [!NOTE]
> Cabe recalcar que incluye un contructor vacío o sin parámetros por que es un ejemplo de `sobrecarga de constructores` el cual tiene propósitos muy útiles como los siguientes:_

variaciones ↓
> [!IMPORTANT]
> [!NOTE]  
> [!TIP]
> [!WARNING]  
> [!CAUTION] -->

# Código base para Django - Python

Este repositorio tiene como objetivo el de brindar una base para el desarrollo de aplicaciones en el entorno `Django` utilizando el lenguaje de programación `Python`.

# Inicialización

## Materiales necesarios

Para iniciar a programar en Django, necesitamos tener instalados en nuestro ordenador los siguietes programas:

* [Python]([Enlaces](https://github.com/ErnestoFlo/CB-SistemaDisk_VB.Net/archive/refs/heads/master.zip))
* [Visual Studio Code]([Enlaces](https://code.visualstudio.com/Download))
* [Django]([Enlaces](https://www.djangoproject.com/download/))
* [Xampp]([Enlaces](https://www.apachefriends.org/download.html))

> [!IMPORTANT]
> Cabe aclarar que, con excepción de `Django`, todos estos programas se instalan de manera normal en cualquier ordenador. En el caso de `Django`, se instala mediante la Terminal con ayuda de la extensión de `Python`. En cuando al editor de código `IDE`, puede obtar por su favorito.


## Extensiones para VSC

Estas son algunas extensiones que recomiendo instalar como ayuda para el desarrollo en `Django` en el IDE de `Visual Studio Code`, sin embargo, no son indispensables para el desarrollo.

* Boostrap 5 (Facilita el desarrollo en frontend si utilizas `Boostrap 5`)
* GitHUb Compilot o KIte AutoComplete (Apoyo de IA en codificación)
* Palenight Theme (Paleta de color agradable para programar con `Python`)
* Python (Extensión en VSC)
* Pylance (Preformatos IntelliSense o autocompletado)
* Python debugger (Extensión para Terminal)

# Instalaciones en Terminal

Verificamos que tengamos instalado python:
``` cmd
    python --version
```

$ INSTALAR DJANGO $
- py -m pip install Django==5.1.1
- django-admin startproject [nombreDePY]
COMPROBAR LA INSTALACION
- python
- import django
- django.VERSION
- exit()

$ INSTALAR APLICACIONES $
- entramos a la carpeta del proyecto
- cd [CarpetaDeAplicacion]
- django-admin startapp [nombreDeApp]

$ INICIAR SERVIDOR $
- entramos a la carpeta del sistema
- python manage.py runserver

$ CREAR APLICACIONES $
dentro de la carpeta del proyecto:
- python manage.py startapp crud

$CONFIGURACIÓN DE settings.py$

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crud' ### ingresamos aqui nuestra aplicación ###
]

$ ORDEN DE TRABAJO $
- Generar vista
- Creamos archivo "urls.py" y trabajamos en el
- Creamos y trabajamos en "Templates"

OJO, Para ver lista de paquetes ---> pip list 

$ IMPORTANTE PARA INSTALAR $
- pip install PyMySQL (Para manejar SQL)
- pip install Pillow (Para cargar imagenes)

$ IMPORTAR DATOS A BD $
- py manage.py makemigrations (Generamos la estructura de los datos en el sistema)
- py manage.py migrate (Enviamos la información a la base de datos)

$ CREAR SUPER USUARIO $
- python manage.py createsuperuser

$ CONFIGURAR SERVIDOR DE IMAGENES EN settings.py $
- import os
## Agregamos esta linea de código para habilitar el servidor ##
- MEDIA_ROOT = os.path.join(BASE_DIR, '')
- MEDIA_URL = '/imagenes/'

## Agreagamos esta configuracion en views.py de la aplicación ##
from django.urls import path
from . import views

## Direccionamiento para servidor de imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

$ ESTRUCTURA PARA GENERAR FORMULARIO DE CRUDS $
# creamos archivo forms.py en raiz de la aplicacion #

- from django import forms
- from .models import crud

- class crudForm(form.ModelForm):
    - class meta:
        - model = crud
        - fields = '__all__'