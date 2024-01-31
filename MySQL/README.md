## ▪️ MySQL 🐬

**Local Installation:**

[MySQL Installation](https://dev.mysql.com/doc/mysql-installer/en/)

⚠️  **NOTE:** As of today, MySQL is not available in the Debian 12 repository and it's been officially replaced by MariaDB (why would you ever want MySQL bro?). 
<br>
However, you can download and add an apt MySQL repository to your Debian system.

There are plenty of reasons why MariaDB is preferable over MySQL, however, you can work around it and get a clean installation with some trick, which I won't show you here, cause I don't want to break your Debian Installation.
(I might be a bit dramatic about breaking Linux Installations, but just trust me)

You know what would be cool to have in these cases?
Exactly, ditch dolphins, embrace whales, Docker comes in help!

**Docker:**

First, mkdir for a MySQL dir and cd into it:

	> $ mkdir SakilaDocker
	> $ cd SakilaDocker

Pull the MySQL Docker Image:
	
	> $ sudo docker pull mysql

Run the Image as a Container:

	> $ sudo docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD="password" -d mysql

Connect to the MySQL Shell:

	> $ sudo docker exec -i -t mysql mysql -u root -ppassword

Use -h (Host Flag) to specify the host to which you want to connect.

Connect to the Shell:

	> $ sudo docker exec -i -t mysql /bin/bash

⚠️  **NOTE:**  To connect as the Root, add the Flag -u to the docker exec command followed by the root user (-u root)

Create a new user and grant it permissions (while inside MySQL Container):

	> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
	> GRANT ALL ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
	> FLUSH PRIVILEGES;

Mind that you can replace 'localhost' with '%' to create an user able to connect from any ip address and that has all the privileges when connecting from any ip address.

[More on Users](https://dev.mysql.com/doc/refman/8.0/en/create-user.html)
[More On Privileges](https://dev.mysql.com/doc/refman/8.0/en/grant.html)

In case you want to connect outside the Container but in the same machine, you can follow the below procedure:

Get the Docker Container IP Address :

	 > $ sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' MYSQL_CUSTOM_CONTAINER_ID_OR_NAME

Then, simply run:

	> $ mysql -h MYSQL_CONTAINER_IP_ADDRESS -u username -ppassword

**Accept External Connections:**

First of all, the easiest way to allow external connections to your Docker based MySQL is to pass an Env variable as follows:

	> $ sudo docker run --name=name -p 3306:3306 -e MYSQL_ROOT_PASSWORD=PASSWORD -e MYSQL_ROOT_HOST:"%" -d mysql

use `MYSQL_ROOT_HOST:"%"` to allow remote connect from any IP. 
<br>
For defined IP's replace % with your external IP address.

A second option is to use the Database mysql while inside your MySQL Container  MySQL cli and set the host to “%” so it can be possible to login from any address::

	mysql> use mysql;
	mysql> update mysql.user set host = '%' where user='user';
	mysql> FLUSH PRIVILEGES;

A third option would be would be the following:

First, locate the conf.d file, usually located in

	> /etc/mysql/conf.d

Now, I might ask again the question: why would you ever want MySQL bro?
But I'll focus on providing a solution.

As MySQL has been acquired by ORACLE, MySQL builds the image with ORACLE Linux, so, to edit our file, we first need to update the packages and install nano, but without the apt package manager, so:
(While Inside the MySQL Containers' - and in the Terminal)

	> $ microdnf update
	> $ microdnf install nano

Then locate mysqld.cnf file (sometimes it's mysql.cnf), usually located in /etc/mysql/mysql.conf.d/

	> $ nano /etc/mysql/mysql.conf.d/mysqld.cnf

Then set the bind-address to 0.0.0.0:

	Replace: #bind-address 		= 127.0.0.1 
	With: bind-address = 0.0.0.0

Then restart the DB:

For local db or in Docker Container cli:

	> service mysql restart

OR restart the container with:

	> $ sudo docker restart MYSQL_CUSTOM_CONTAINER_ID_OR_NAME
	
**⚠️ NOTE:** In some cases, for connecting from an external machine, you might also have to configure the Firewall to accept external connection from a list of trusted different IP Addresses and open the Port (in this case 3306) to listen for incoming connections.	

In those cases:

	> $ sudo ufw allow from remote_IP_address to any port 3306

OR (unsafe):

	> $ sudo ufw allow 3306

Then:

	> $ sudo ufw reload

If you're handling sensitive data, make sure you know exctly what you're doing.
<br>
Eventualy, enroll in some courses regarding Networking and Security.

**To Use MySQL with Python:**

	> $ pip install mysql-connector-python
 
[MySQL Docker](https://dev.mysql.com/doc/mysql-installation-excerpt/8.3/en/docker-mysql-getting-started.html)
[MySQL Docs](https://dev.mysql.com/doc/)
[MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/)
