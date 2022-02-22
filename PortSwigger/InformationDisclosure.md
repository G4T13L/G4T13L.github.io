# Information Disclosure

## How to find and exploit information disclosure vulnerabilities

### Common sources of information disclosure

#### Error messages

##### Lab 1: Information disclosure in error messages

Le agregamos cualquier texto al parametro **productid** y nos arrojara el error con la version del framework que esta usando.
![infodis1.1.png](infodis1.1.png)

#### Debugging data

##### Lab 2: Information disclosure on debug page

En el código fuente encontramos un comentario de un enlace `/cgi-bin/phpinfo.php`, otra manera de encontrar esta ruta es realizando fuzzing a los directorios con wfuzz o otra herrramienta que busque directorios por diccionario.

![infodis2.1.png](infodis2.1.png)

Aqui si buscamos las variables de entorno encontraremos la variable **SECRET_KEY**.

![infodis2.2.png](infodis2.2.png)