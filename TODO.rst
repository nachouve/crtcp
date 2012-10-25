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
-----------------------------------
* Avanzar más en el modelo: UPAI (Unid. Paisaxe), etc
* Cada par UPAI/bloque es probable que sea una encuesta individual. Esto obliga que hagamos encuestas automáticas.
* Ampliar Survey para que guarde relación con las UPAI y con las categorías/bloque de participación ("Límites Unidades", "Sinais de identidade", "Valores a destacar", "Permanencia-Cambio", "Conflictos-Consensos", ...)
* Al tener tantas encuestas, estamos obligados a ofrecer un resumen de participación en cada encuesta, estadísticas globales, etc.
* Crear widget mapa en django-crowdsourcing
* Poder almacenar contenidos del mapa en BD (capas, grupos, capa de consulta, etc.) y generar GUI en la parte de administración para configurar el mapa del XVM (generar xvm.config.yaml y xvm.layers.yaml). OJO, algunas serán WMS y otras geodjango.
* Introducir datos de pruebas y surveys de pruebas para empezar a maquetar


Tercera fase: ...
-------------------------------------
* Devolver información formateada en el Info del mapa



Configurar cuentas de correo para userena
===========================================

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = ‘smtp.gmail.com’
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘yourgmailaccount@gmail.com’
EMAIL_HOST_PASSWORD = ‘yourgmailpassword’



