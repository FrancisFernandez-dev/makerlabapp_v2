📚 MakerLab – Biblioteca Educativa de Modelos 3D
📌 Descripción del Proyecto

MakerLab es una aplicación web desarrollada con Django orientada a la educación. Su objetivo es servir como una biblioteca digital de modelos 3D que apoyen el aprendizaje en colegios, talleres educativos y el hogar, fomentando la creatividad, el pensamiento lógico y el aprendizaje basado en proyectos.

La plataforma permite organizar y administrar recursos educativos en formato 3D, facilitando su uso como material de apoyo para docentes, estudiantes y familias interesadas en el enfoque maker y STEAM.

Este proyecto forma parte de un trabajo académico y demuestra la aplicación práctica de los conocimientos adquiridos en desarrollo web con Django.

🛠️ Tecnologías Utilizadas

Python 3

Django 5

SQLite (base de datos)

HTML5

CSS3

Bootstrap 5

Git & GitHub

🎓 Enfoque Educativo

MakerLab está pensado como un recurso educativo complementario, útil para:

Reforzar contenidos escolares mediante modelos 3D.

Apoyar clases de tecnología, ciencias y educación STEAM.

Facilitar actividades prácticas en colegios.

Promover el aprendizaje activo y creativo en el hogar.

Introducir a niños y jóvenes en el uso de tecnología y fabricación digital.

⚙️ Funcionalidades Principales

Página de inicio con presentación del proyecto educativo.

Biblioteca de modelos 3D organizada por categorías y etiquetas.

Registro, edición y eliminación de modelos (CRUD).

Formularios con validación usando Django Forms.

Asociación de modelos con categorías educativas.

Sistema de autenticación de usuarios.

Panel de administración de Django para gestión de contenidos.

Uso de archivos estáticos (imágenes, estilos y scripts).

🗄️ Base de Datos

La aplicación utiliza SQLite como motor de base de datos, gestionado mediante el ORM de Django, lo que permite:

Definir modelos de datos en Python.

Crear y mantener tablas mediante migraciones.

Relacionar entidades de forma clara.

Realizar consultas eficientes sin escribir SQL directamente.

🧩 Estructura del Proyecto
makerlab/
│
├── manage.py
├── db.sqlite3
│
├── makerlab/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── biblioteca/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── templates/
│   │   └── biblioteca/
│   └── static/
│       └── biblioteca/
│
└── README.md

▶️ Instalación y Ejecución

Clonar el repositorio:

git clone <url-del-repositorio>


Crear y activar entorno virtual:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Instalar dependencias:

pip install django


Ejecutar migraciones:

python manage.py migrate


Crear superusuario:

python manage.py createsuperuser


Ejecutar el servidor de desarrollo:

python manage.py runserver


Acceder a la aplicación:

http://127.0.0.1:8000/

🔐 Autenticación y Seguridad

MakerLab utiliza el sistema de autenticación integrado de Django para:

Gestión de usuarios.

Inicio y cierre de sesión.

Control de acceso a funcionalidades administrativas.

Administración de usuarios desde el panel administrativo.

🎯 Objetivo Académico

Este proyecto demuestra:

Integración de Django con bases de datos.

Uso del ORM para la gestión de información.

Implementación de modelos con y sin relaciones.

Desarrollo de una aplicación web educativa.

Aplicación del patrón MVC/MTV de Django.

👤 Autor

Francis Fernández
Desarrollador Full Stack Python & Maker
Proyecto académico – 2025

✅ Estado del Proyecto

✔ Funcional
✔ Orientado a educación
✔ Listo para evaluación y portafolio
