# Docker Linux Apache PHP MySQLCli


## Build Docker Container
By using WSL and github, clone the source code locally (like docker pull)
    
    # git clone
    git clone https://github.com/webgriffe/docker-php-apache-base.git

    # docker build with a tag locally by using Dockerfile
    docker build -t logansql/linux-apache-php-ext .

    # docker run detached, mount volume at host 
    # To prepare Windows Docker for remote volume
    # 1) Windows Docker=>Setting...=>Shared Drive=>enable C drive
    # 2) hosts windows directory C:\logan\test\testdata
    docker run -d -p 80:80 --name test-apache-php -v C:\logan\test\testdata:/var/www/html logansql/linux-apache-php-ex


    Directory: C:\logan\test\testdata

```

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/22/2018   2:28 PM            120 hello.php
-a----        3/22/2018   2:35 PM            103 phpinfo.php

```
## Connect to Container
    # verify the volume mounted
    docker exec -it test-apache-php bash
    ls -l /var/www/html
```
-rwxr-xr-x 1 root root 120 Mar 22 18:28 hello.php
-rwxr-xr-x 1 root root 103 Mar 22 18:35 phpinfo.php
```

## Link to MySQL Container
    # Link to container test-mysql as mysql
    # 
    # start mysql container 
    docker start test-mysql
    #
    docker ps
```CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
9a719b54cee9        mysql               "docker-entrypoint.s…"   7 days ago          Up 8 seconds        0.0.0.0:3306->3306/tcp   test-mysql
```
    # remove the all container
    docker rm test-apache-php
    #
    # build a new container with link to mysql container
    docker run -d -p 80:80 --name test-apache-php -v C:\logan\test\testdata:/var/www/html --link test-mysql:mysqldb logansql/linux-apache-php-ext

## Test MySQL inside Container: test-apache-php

    # connect to the container interactively
    docker exec -it test-apache-php bash
    mysql -utestuser -h mysqldb -ptestuser
```mysql>
mysql> use logandb
Database changed
mysql> CREATE TABLE IF NOT EXISTS products (
    ->          productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
    ->          productCode  CHAR(3)       NOT NULL DEFAULT '',
    ->          name         VARCHAR(30)   NOT NULL DEFAULT '',
    ->          quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
    ->          price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
    ->          PRIMARY KEY  (productID)
    ->        );
Query OK, 0 rows affected (0.06 sec)

mysql> INSERT INTO products VALUES (1001, 'PEN', 'Pen Red', 5000, 1.23);
Query OK, 1 row affected (0.04 sec)
mysql> select database() as db, user() as user;
+--------+---------------------+
| db     | user                |
+--------+---------------------+
| testDB | testuser@172.17.0.3 |
+--------+---------------------+
1 row in set (0.00 sec)

```
## References

[MySQLTutorial](https://www.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Beginner.html)

