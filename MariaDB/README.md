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

Setup User (While inside MariaDB):

	> GRANT ALL ON *.* TO 'user'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;

[More on Users](https://mariadb.com/kb/en/create-user/)
[More on Privileges](https://mariadb.com/kb/en/grant/)

**Docker:**

Create Container:

	> $ sudo docker run -p 127.0.0.1:3306:3306  --name mdb -e MARIADB_ROOT_PASSWORD=Password123! -d mariadb:latest

Get into MariaDB CLI (and into the Container running it):

	> $ sudo docker exec -i -t mdb mariadb --user root -pPassword123!

To Connect to a Local Docker Image running MariaDB from outside the Container but on the same Machine:

Get the Docker image IP Address :

	 > $ sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' MARIA_DB_CUSTOM_CONTAINER_NAME

Where the CUSTOM_CONTAINER_NAME is the one you've assigned with --name flag in docker run

Connect then to MariaDB from outside the container locally:

	> $ sudo mariadb -h DOCKER_IP_ADDRESS -u MARIADB_USER -pMARIADB_PASSWORD

**Accept External Connections - BOTH Local and Docker:**

Locate the 50-server.cnf file, usually located in 
	
	/etc/mysql/mariadb.conf.d 

Then cd into the golder.

Edit the File with a Text Editor (Nano will do fine):

	> $ apt-get update
	> $ apt install nano
	> $ nano 50-server.cnf

Comment the following lines (with #):

	#bind-address 		= 127.0.0.1 

Then restart the DB with:

	> $ sudo systemctl restart mariadb

Locate your IP Address with:

	> $ ip a

Connect to MariaDB and Create a new User:

	> CREATE USER 'your_username'@'host_ip_addr' IDENTIFIED BY 'your_password';

Grant necessary privileges to User:

	> GRANT ALL PRIVILEGES ON *.* TO 'your_username'@'%';

Where * . * stands for ALL_DATABASES, You can also use db_name*.* to only let the user use the database db_name.

Apply Changes:

	> FLUSH PRIVILEGES;

**⚠️  NOTE:** On Docker the line bind-address in 50-server.cnf is usually already commented out.
	
**Check that everything was successful**

Run an Ubuntu empty container with:

	> $ docker run -i -t ubuntu bash
	
Then:

	> $ apt-get update
	> $ apt-get install mariadb-client

Connect to Remote MariaDB Server:

	> mariadb -u your_username -h host_ip_addr -pyour_password

**To Use MariaDB with Python:**

	> $ sudo apt install libmariadb3 libmariadb-dev
	> $ pip install mariadb

[Docker Docs](https://docs.docker.com/)
[MariaDB Docs](https://mariadb.com/kb/en/documentation/)
[MariaDB Knowledge Base](https://mariadb.com/kb/en/)
