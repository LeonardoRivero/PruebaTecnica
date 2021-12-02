# PruebaTecnica

## Instalar pipenv para manejar el ambiente virtual del proyecto
Para instalar pip, simplemente ejecute:

    $ pip install --user pipx
    Una vez que esté pipxlisto en su sistema, continúe instalando Pipenv:

    $ pipx instalar pipenv

## Despues de instalar pipenv, dirijase al directorio donde se encuentra el archivo pipfile y ejecute:
    $ pipenv install



## Para correr el proyecto, dirijase al directorio donde se encuentra el archivo manage.py y ejecute:
    $python manage.py runserver

## Los endpoints del proyecto son:
    '/api/empresa/all/', --> lista todas los registros existentes
    '/api/empresa/<int:pk>/',--> muestra los detalles del registro seleccionado por el pk
    '/api/archivos/all/',
    '/api/archivos/<int:pk>/',
