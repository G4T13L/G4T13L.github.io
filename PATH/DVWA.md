# DVWA

DVWA es una aplicación web en PHP/MySQL el cual es vulnerable con objetivo de probar algunas de las mas comunes vulnerabilidades web.

## Instalación

Se puede instalar fácilmente usando docker con la guía de [aquí](https://hub.docker.com/r/vulnerables/web-dvwa)

Resumido es :

Para obtener la imagen

```bash
docker pull vulnerables/web-dvwa
```

Para correr la aplicación

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

dejar la terminal corriendo, para cerrarlo darle ctrl+c

## Ejercicios de la iso

* Brute Force
* Command Injection
* CSRF
* File Inclusion
* File Upload
* Insecure CAPTCHA
* SQL Injection
* SQL Injection (Blind)
* Weak Session IDs
* XSS (DOM)
* XSS (Reflected)
* XSS (Stored)
* CSP Bypass
* JavaScript

## Procedimiento para el trabajo

* Instalar
* Investigar sobre la vulnerabilidad(Tema que veo, tema que leo)
* Probar lo aprendido con lo leído anteriormente y verificar que es vulnerable
* Ver el codigo que te proporciona cada sección
* Podés aumentar la dificultad modificando la cookie o en la sección de **"DVWA Security"**

## Recomendaciones

Cuando entras por primera vez ingresa cualquier usuario y contraseña luego te volverá a pedir una cuenta y le das en crear o editar la base de datos.

No te atasques con un mismo ejercicio, si llevas mucho tiempo entonces busca la solución en internet y busca como llego a esa respuesta.