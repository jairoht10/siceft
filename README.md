# siceft

Sistemas de certificados para eventos, foros y talleres

# Pasos para crear el entorno de desarrollo

Cuando somos un usuario normal del sistema, en el terminal se mostrará el siguiente símbolo: ~$

Cuando accedemos al usuario root del sistema, en el terminal se mostrará el siguiente símbolo: ~#

Probado en Debian y Ubuntu. Instalar los siguientes programas

    ~# apt install curl git graphviz graphviz-dev postgresql phppgadmin python3-dev python3-setuptools virtualenv

Para instalar npm hacer lo siguiente

    ~# curl -sL https://deb.nodesource.com/setup_10.x | bash -

    ~# apt install -y nodejs

Crear las siguientes carpetas

    ~$ mkdir Programación

Desde el terminal, moverse a la carpeta Programación y ejecutar

    ~$ cd Programación/

    ~$ mkdir Python

Entrar a la carpeta Python y hacer lo siguiente

    ~$ cd Python/

    ~$ mkdir EntornosVirtuales ProyectosDjango

Entrar a EntornosVirtuales

    ~$ cd EntornosVirtuales/

    ~$ mkdir Django

Desde el terminal, moverse a la carpeta Django y ejecutar

    ~$ cd Django/

    ~$ virtualenv -p python3 siceft

Para activar el entorno

    ~$ source siceft/bin/activate

Nos movemos a la carpeta ProyectosDjango, descargamos el sistema y entramos a la carpeta con los siguientes comandos

    (siceft) ~$ cd ../../ProyectosDjango/

    (siceft) ~$ git clone https://github.com/jairoht10/siceft.git

    (siceft) ~$ cd siceft/

    (siceft) ~$ cp siceft/settings.py_example siceft/settings.py

Tendremos las carpetas estructuradas de la siguiente manera

    // Entorno virtual
    Programación/Python/EntornosVirtuales/Django/siceft

    // Servidor de desarrollo
    Programación/Python/ProyectosDjango/siceft

Instalar las dependencias de css y js: moverse a la carpeta static y ejecutar

    (siceft) ~$ cd static/

    // Usa el archivo package.json para instalar lo que ya se configuro allí
    (siceft) ~$ npm install

    // Terminado el proceso volver a la carpeta raíz del proyecto
    (siceft) ~$ cd ../

Crear la base de datos para __siceft__ usando PostgresSQL

    // Acceso al usuario postgres
    ~# su postgres

    // Acceso a la interfaz de comandos de PostgreSQL
    postgres@xxx:$ psql

    // Creación del usuario de a base de datos
    postgres=# CREATE USER admin WITH LOGIN ENCRYPTED PASSWORD '123' CREATEDB;
    postgres=# \q

    // Desautenticar el usuario PostgreSQL y regresar al usuario root
    postgres@xxx:$ exit

    // Salir del usuario root
    ~# exit

Puedes crear la base de datos usando la interfaz gráfica phppgadmin

    // Desde algún navegador ir al siguiente sitio y entrar con el usuario que se acaba de crear
    localhost/phppgadmin

    // Nombre de la base de datos: siceft

Instalamos los requemientos que el sistema necesita en el entorno virtual

    (siceft) ~$ pip install -r requirements/dev.txt

Hacer las migraciones y cargar los datos iniciales

    (siceft) ~$ python manage.py makemigrations base usuario evento

    (siceft) ~$ python manage.py migrate

Crear usuario administrador

    (siceft) ~$ python manage.py createsuperuser

Correr el servidor de django

    (siceft) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate
