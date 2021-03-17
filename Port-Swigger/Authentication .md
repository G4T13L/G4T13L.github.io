# Authentication

## Vulnerabilities in password-based login

### Lab 1: User name enumeration via different responses

Para estos laboratorios se estará utilizando burp suite. El ataque se efectuara en la pagina de logeo del laboratorio.

Primero en el burp suite debemos interceptar los paquetes en la pestaña de proxy, luego debemos ingresar algun dato para interceptar la consulta. Entonces tendremos algo como esto:

![auth1.png](auth1.png)

En este caso coloque de usuario `juan` y contraseña `gabriel`.

Click derecho en la consulta y le ponemos `send to intruder, de ahí nos movemos a la pestaña de intruder.

En positions le damos a clear y seleccionamos solo el usuario

![auth1.1.png](auth1.1.png)

type attack: sniper

Nos vamos a payloads y agregamos en payload options en load para cargar la lista de usuarios que nos da la pagina de port swigger.

Luego en options nos vamos a `Grep - Extract` y agregamos con Add, nos da una ventanita en donde le damos a `Fetch response`  y buscamos `Invalid username`

![auth1.1.png](auth1.2.png)

le damos ok y luego en start attack

con eso veremos que los resultados positivos son los que no tengan Invalid username, sino diran Invalid password.

![auth1.3.png](auth1.3.png)

Con eso ya encontramos un usuario, ahora hacemos lo mismo pero cambiando la contraseña con el diccionario que te dan port swigger.

![auth1.4.png](auth1.4.png)

La respuesta que no tiene ningun mensaje de error sería la contraseña correcta.

### Lab 2: Username enumeration via subtly different responses

Para este laboratorio tenemos que realizar el mismo proceso que el anteriro laboratorio pero las respuestas son el mismo en ambos casos aparentemente, en este caso te dan `Invalid username or password.` pero cuando la respuesta es correcta no tiene el punto final

![auth2.1.png](auth2.1.png)

Para la contraseña de la misma manera realizamos un ataque de fuerza bruta y buscamos el que nos de una redireccion o que no nos bote algun mensaje de error.

![auth2.2.png](auth2.2.png)

### Lab 3: Username enumeration via response timing

Para este laboratorio se inicia de la misma manera que laboratorios anterirores enviar la consulta al intruder, en este caso debemos agregar la cabecera `X-Forwarded-For` con una dirección IP pues la pagína revisa la cantidad de intentos registrados por IP. Luego debemos modificar la consulta donde la password debe ser muy larga para que se demore en procesar cuando el usuario sea el correcto.

![auth3.1.png](auth3.1.png)

Seleccionamos el tipo de ataque **Pichfork** para que itere con dos listas, donde una será los dos ultimos digitos de alguna IP y la otra iteraría los nombres de usuarios.

![auth3.2.png](auth3.2.png)

Para la primera lista usaremos un payload de tipo Numbers y se colocara segun la imagen para generar numeros del 1 al 254. En el caso de la segunda lista serán los usuarios como en los anteriores laboratorios.

Ahora deberemos ver como demora cada consulta. También en **columns** seleccionamos la opcion de **response received** para ver el tiempo de respuesta y el que tenga un valor mayor será el resultado correcto.

![auth3.3.png](auth3.3.png)

Finalmente, solo nos faltará buscar la contraseña usando el usuario que encontramos y esperar una redireccion (codigo 302).

## Flawed brute-force protection

### Lab 4: Broken brute-force protection, IP block

Para este laboratorio usamos lo que vimos anteriormente, en este caso queremos buscar la contraseña del usuario **carlos** pero nos bloquean la ip cada 1 min por lo que usaremos credenciales validas luego de cada vez que intentemos otras credenciales para que se reinicie la cantidad de intentos por IP.

Entonces en el intruder useremos el tipo de ataque **Pitchfork** con las listas de esta manera:

![auth4.1.png](auth4.1.png)

tenemos las credenciales validas de usuario **wiener** y contraseña **peter**, intercalamos en usuario wiener con carlos y en contraseña colocamos cada vez que se vaya a usar weiener colocamos peter y en donde se pruebe con carlos le colocamos el elemento de la lista que nos da Port swigger

![auth4.2.png](auth4.2.png)

buscamos por codigo de estado 302 en donde este el usuario carlos para encontrar la consulta correcta.