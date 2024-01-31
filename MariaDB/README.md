## ▪️ MariaDB 🦭

**Local Installation:**
	
	> $ sudo apt update
	> $ sudo apt install mariadb-server
	> $ sudo mysql_secure_installation

Then access the DB:

	> $ sudo mariadb
	
OR

	> $ mariadb -h YOUR_HOST_NAME -u username -ppassword database_name

Where to connect locally you simply put localhost and the credentials you'll setup eventually with the command below.
<br>
If you want to connect to a remote DB, you'll have to enter the IP address of the remote db.
<br>
database_name is optional.

Setup User and Grant Privileges (While inside MariaDB):

	> CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
	> GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
	> FLUSH PRIVILEGES;
 
**⚠️  NOTE:** When granting privileges the current configuration 'user'@'localhost' means that you are giving privileges for user on connections from the current host.
<br>
If you would like to actually connect from another IP with user, you'd need to change 'localhost' with 'ip_address' where ip_address is the address where you would like to connect remotely from.
<br>
Also, you can simply put the wildcard '%' like 'user'@'%' to grant privileges on user connecting from any ip_address.

[More on Users](https://mariadb.com/kb/en/create-user/)
[More on Privileges](https://mariadb.com/kb/en/grant/)

**Docker:**

Create Container:

	> $ sudo docker run -p 3306:3306 --name mdb -e MARIADB_ROOT_PASSWORD=password -d mariadb:latest

Get into MariaDB CLI (and into the Container running it):

	> $ sudo docker exec -i -t mdb mariadb -u root -ppassword

To Connect to a Local Docker Image running MariaDB from outside the Container but on the same Machine:

Get the Docker Container IP Address :

	 > $ sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' MARIA_DB_CUSTOM_CONTAINER_ID_OR_NAME

Where the CUSTOM_CONTAINER_ID_OR_NAME is the one you've assigned with --name flag in docker run

Connect then to MariaDB from outside the container, but locally (Outside the Container, but same machine from MariaDB-Client):

	> $ sudo mariadb -h DOCKER_IP_ADDRESS -u MARIADB_USER -pMARIADB_PASSWORD

**Accept External Connections from different IP/Machines - BOTH Local and Docker:**

Locate the 50-server.cnf file, usually located in 
	
	/etc/mysql/mariadb.conf.d 

Then cd into the folder.

Edit the File with a Text Editor (Nano will do fine):

	> $ apt-get update
	> $ apt install nano
	> $ nano 50-server.cnf

Find and set the bind-address to 0.0.0.0 and comment out (with #) the line skip-networking (if in the file):

	Replace: #bind-address 		= 127.0.0.1 
 	With: bind-address = 0.0.0.0

Then restart the local DB with:

	> $ sudo systemctl restart mariadb

OR with (can also be used inside MariaDB Container /bin/bash Shell):

	> $ sudo service mariadb restart

OR, restart the Container:

 	> $ sudo docker restart MARIA_DB_CUSTOM_CONTAINER_ID_OR_NAME

Locate your IP Address with:

	> $ ip a

Connect to MariaDB and Create a new that can connect from anywhere with all permissions when connecting from anywhere:

	> CREATE USER 'user'@'%' IDENTIFIED BY 'password';

Grant necessary privileges to User:

	> GRANT ALL PRIVILEGES ON *.* TO 'user'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;

Where * . * stands for ALL_DATABASES, You can also use db_name*.* to only let the user use the database db_name.

Apply Changes:

	> FLUSH PRIVILEGES;

**⚠️  NOTE:** On Docker the line bind-address in 50-server.cnf is usually already commented out.

**⚠️  NOTE:** In some cases, for connecting from an external machine, you might also have to configure the Firewall to accept external connection from a list of trusted different IP Addresses and open the Port (in this case 3306) to listen for incoming connections.
 
**Check that everything was successful**

Run an Ubuntu empty container with:

	> $ sudo docker run -i -t ubuntu bash
	
Then:

	> $ apt-get update
	> $ apt-get install mariadb-client

Connect to Remote MariaDB Server:

	> mariadb -u your_username -h host_ip_addr -pyour_password

**To Use MariaDB with Python:**

	> $ sudo apt install libmariadb3 libmariadb-dev
	> $ pip install mariadb

[MariaDB Docs](https://mariadb.com/kb/en/documentation/)
[MariaDB Knowledge Base](https://mariadb.com/kb/en/)
[MariaDB Python Connector](https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/)
