# Business Logic Vulnerabilities

## Excessive trust in client-side controls

### Lab 1: Excessive trust in client-side controls

Interceptamos la consulta al dar click en el boton `add to chart`.

![business1.1png](business1.1.png)

El paquete que se envía lo modificamos para que el precio tenga un valor mas bajo, puede ser 1 o 100 pq los 2 últimos digitos los pone como centavos.

![business1.2.png](business1.2.png)

```
...
productId=1&redir=PRODUCT&quantity=1&price=100
```

Luego entramos al carrito para ver que el precio que tiene la chaqueta es 1$.

![business1.3.png](business1.3.png)

### Lab 2: 2FA broken logic

[business logic 2FA](https://g4t13l.github.io/PortSwigger/Authentication.html#lab-8-2fa-broken-logic)

## Failing to handle unconventional input
### Lab 3: High-level logic vulnerability

Ingresamos las credenciales que nos dieron. Lo que nos piden comprar es la chaqueta de cuero, así lo añadimos al carrito y otro producto cualquiera. Entonces al entrar al carrito, deberiamos ver algo así:

![business3.1.png](business3.1.png)

Interceptamos los paquetes y le damos en aumentar el producto 2, luego le cambiamos la cantidad con -10 para disminuir el precio.

![business3.2.png](business3.2.png)

Vamos probando valores hasta que salga un precio menor a 100$ que es lo que tenemos en la cuenta.

![business3.3.png](business3.3.png)

En este caso llego a costar todo $2.48