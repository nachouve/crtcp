====
TODO
====

Tareas
======

Primera fase: prueba tecnológica I
----------------------------------
* Hacer unas cuantas páginas estáticas (flatpages app)
* Encuesta con 1 pregunta (django-crowdsourcing)
* Configurar gestión de usuarios (django-userena)
* Ligar la encuesta a un usuario registrado
* Insertar un mapa en medio de la encuesta

Segunda fase: prueba tecnológica II
----------------------------------
* Poder almacenar contenidos del mapa en BD (capas, grupos, capa de consulta, etc.)
* Devolver información formateada en el Info del mapa
* 

Configurar cuentas de correo para userena
===========================================

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = ‘smtp.gmail.com’
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘yourgmailaccount@gmail.com’
EMAIL_HOST_PASSWORD = ‘yourgmailpassword’



