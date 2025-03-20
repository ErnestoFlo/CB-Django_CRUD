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

* Lenguaje de programación: [Python](https://github.com/ErnestoFlo/CB-SistemaDisk_VB.Net/archive/refs/heads/master.zip)
* IDE: [Visual Studio Code](https://code.visualstudio.com/Download)
* Framework: [Django](https://www.djangoproject.com/download/)
* Gestor de base de datos SQL: [Xampp](https://www.apachefriends.org/download.html)

> [!IMPORTANT]
> Cabe aclarar que, con excepción de `Django`, todos estos programas se instalan de manera normal en cualquier ordenador. En el caso de `Django`, se instala mediante la Terminal con ayuda de la extensión de `Python`. En cuando al editor de código `IDE`, puede obtar por su favorito.


## Extensiones para VSC

Estas son algunas extensiones que recomiendo instalar como ayuda para el desarrollo en `Django` en el IDE de `Visual Studio Code`, sin embargo, no son indispensables para el desarrollo.

* Boostrap 5 (Facilita el desarrollo en frontend si utilizas `Boostrap 5`)
* GitHub Compilot o KIte AutoComplete (Apoyo de IA en codificación)
* Palenight Theme (Paleta de color agradable para programar con `Python`)
* Python (Extensión en VSC)
* Pylance (Preformatos IntelliSense o autocompletado)
* Python debugger (Extensión para Terminal)

## Instalaciones en Terminal

Verificamos que tengamos instalado `Python`:
``` cmd
    python --version
```

Instalación de `Django`:
```cmd
    py -m pip install Django==5.1.1
```

Comprobamos que se instalo `Django`:
```cmd
    python
    import django
    django.VERSION
    exit()
```

Creación de proyecto y aplicaciones de `Django`:
```cmd
    django-admin startproject [Nombre del proyecto]
    cd [Carpeta de proyecto]
    django-admin startapp [Nombre de aplicacion]
```

Iniciamos proyecto con `Python`
```cmd
    python manage.py startapp [Nombre de aplicacion]
    python manage.py runserver
```

## Configuraciones en documento `settings.py`
Aqui debemos configurar nuestra aplicacion que instalamos, para que el proyecto la tome en cuenta. Esto lo hacemos colocando en nombre de la aplicacion en la configuracion `INSTALLED_APPS`.

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '[Nombre de aplicacion]' ### ingresamos aqui nuestra aplicación ###
]
```

# Comenzamos a trabajar

Antes de iniciar con el desarrollo, debemos asegurarnos en contar con unos ciertos archivos en la carpeta de nuestra aplicacion los cuales son:
* `views.py` (Son las vistas de nuestra aplicación)
* `urls.py` (Son las urls de nuestras vistas)
* `templates` (carpeta donde estaran nuestros htmls)

_en caso de no existir, debemos crearlos_.

> [!NOTE]
> Para que las urls de nuestra aplicacion funcionen correctamente, debemos incluirlas en las urls de nuestro proyecto de la siguiente forma:

```py
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('[nombre de aplicación].urls')), ### EN ESTA LINEA AGREGAMOS LAS URLS DE NUESTRA APP
]
```
## Instalación de MySQL
En este caso, este proyecto esta pensado para ser desarrollado con una base de datos `MySQL` por lo que debemos instalar los paquetes PyMySQl y Pillow los cuales nos permiten utilizar las configuraciones para servidores MySQL y un gestor de servidor de imagenes respectivamente:

```cmd
    pip install PyMySQL
    pip install Pillow
```

> [!NOTE]
> Para comprobar que estos paquetes estes correctamente instalados, podemos usar el comando `pip list` y nos arrojara el listado de nuestros paquetes instalados en la terminal:

```cmd
    Package              Version
    -------------------- -------
    asgiref              3.8.1
    Django               5.1.7
    django-widget-tweaks 1.5.0
    pillow               11.1.0 ←
    pip                  24.3.1
    PyMySQL              1.1.1 ←
    sqlparse             0.5.3
    tzdata               2025.1
```
Por último, es importante configurar en `settings.py` nuestra base de datos, lo cual se hace integrando el formato de MySQL en la sección del documento llamada `DATABASES`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', ### Configuracion MySQL
        'NAME': 'basededatos', ### Nombre de nuestra base de datos
        'USER': 'admin', ### Usuario de acceso a BD
        'PASSWORD': '12345', ### Contraseña de usuario
        'HOST':'localhost', ### IP de acceso a servidor
        'PORT': '3306' ### Puerto donde esta funcionando el servidor
    }
}
```
 ## Instalación de servidor de imagenes

 Gracias al paquete `Pillow`, podemos administrar un servidor de imagenes en nuestra aplicacion, y para poder configurarla, debemos agregar una serie de lineas de código a en `settings.py`:
 ```py
    import os

    MEDIA_ROOT = os.path.join(BASE_DIR, '')
    MEDIA_URL = '/imagenes/'
 ```

Después de esta configuración, debemos habilitar el acceso en las vistas al servidor de imagenes, añadiendo este código en `urls.py`
```py
    from django.urls import path
    from . import views

    ## Direccionamiento para servidor de imagenes
    from django.conf import settings
    from django.contrib.staticfiles.urls import static

    urlpatterns = [
        path('', views.inicio, name='inicio'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ## Esta línea es para tomar de static la url de las imágenes
```

## Configuración de archivos estáticos

Los archivos estáticos nos ayudan a utilizar archivos externos al entorno de `Django`, como lo pueden ser `CSS`, `JavaScript`, `Ajax`, `Vendor`, `SCSS`, etc. Además de poder utilizar archivos multimedia como imágenes y videos. Para configurarlo, debemos crear una carpeta llamada `static` en la raíz de nuestro proyecto y en el archivo `settings.py` debemos agregar el siguiente código:

```py
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
```

## Comandos importantes

Cabe aclarar que necesitamos conocer una serie de comandos que nos ayudaran a gestionar nuestros modelos, arrancar el servidor y darnos accesos al apartado de admistrador. Estos son los comandos que más utilizo:

* py manage.py runserver - Sirve para iniciar el servidor
* py manage.py makemigrations - Genera la estructura de datos en base a los modelos
* py manage.py migrate - Enviamos la estructura de datos nuestra BD
* python manage.py createsuperuser - Creamos un usuario de acceso para nuestro adminsitrador

En escencia es esto. Con esto podemos comenzar a desarrollar en Django:
<p align="center" width="100%"><img src="https://pbs.twimg.com/media/FMqt1JwUcAMwJod?format=jpg&name=900x900" /></p>