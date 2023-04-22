# Proyecto final Django

- Este proyecto simula un foro de entusiastas por el gaming donde pueden compartir sus experiencias, ideasm, rating, recomendaciones y interactuar entre ellos para jugar en multijugadores juntos si así lo desean en un futuro. La idea central del mismo es acercar a la gente que tiene mismos gustos y pasiones.
- Dentro de los módulos presentes se encuentran: ABM completo tanto de publicaciones como de usuario, sistema de mensajería, listado de mensajes y de publicaciones y agregado de imágenes a las publicaciones y a los usuarios (foto de perfil).

→ Enlace al video subido a YouTube: https://youtu.be/wpz1heJhhJk 

Para poder correr este proyecto es necesario tener instalado python 3.9 o superior. 

## Paquetes necesarios para la instalación
Desde la terminal correr el siguiente comando
```bash
pip3 install django
```

## Cargar datos de pruebas

Para terminal bash en windows/linux/macos:
```bash
python3 manage.py shell < seed_data.py
```

Para terminal cmd/powershell en windows:
Primero entrar al shell de django con
```bash
python3 manage.py shell
```
Una vez en el shell hacer import seed_data
```bash
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import seed_data
```

## Para poder correr el servidor 

Desde la terminal correr el siguiente comando

```bash
python3 manage.py runserver
```