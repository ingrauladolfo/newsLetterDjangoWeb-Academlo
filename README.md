# Newsletter API DRF

## Requisitos

Python 3.8 &
PIP

## Instalación

Descarge o clone el repositorio, si decidió el método por descarga también deberá
descomprimir el proyecto.

Abre un consola que apunte al proyecto y realiza lo siguiente.

- Crear entorno virtual **_`python3 -m venv env`_**

- Activar entorno virtual

  - Unix y Mac **_`env\Scripts\activate.bat`_**
  - Windows **_`env/bin/activate`_**

- Instalar dependencias
  - **_`python -m pip install -r requirements.txt_**
- variables de entorno
  - crea un archivo `.env` para las varibles de entorno en la carpeta Newsletter con los siguiente campos
    1. `SECRET_KEY= tu_clave_secreta`
    2. `ALLOWED_HOSTS= Hots_que permites ej. 127.0.0.1`
    3. `DEBUG= Ture/False`
- Aplicar migraciones

  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

> Puedes detener el servidor con ctr + c

- crea un superusuario para las ultimas configuraciones
  En la consola con el servidor parado introduce el siguiente comando

  >     python manage.py createsuperuser

      e introduce tu username, email y password

- Pon en marcha el servidor y crea 2 grupos en el admin de Django:

        	python manage.py runserver
        	accede a admin ej. http://127.0.0.1:8000/admin/
        	Da click en add Group, como nombre al primer grupo es 'administrador'
        	guardalo y agrega otro que tenga como nombre 'usuario' y guardalo
