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

First, mkdir for a MariaDB dir and cd into it:

	> $ mkdir MariaDocker
	> $ cd MariaDocker

Pull the MariaDB Docker Image:

	> $ sudo docker pull mariadb

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

In those cases:

	> $ sudo ufw allow from remote_IP_address to any port 3306

OR (unsafe):

	> $ sudo ufw allow 3306

Then:

	> $ sudo ufw reload

If you're handling sensitive data, make sure you know exctly what you're doing.
<br>
Eventualy, enroll in some courses regarding Networking and Security.
 
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

TO CONNECT MARIA DB to a MySQL Workbench:

Launch a MariaDB container
Pull the latest MariaDB image

bash
Copy
Edit
docker pull mariadb:latest
Run the container, mapping container’s MySQL port (3306) to the host, and setting up credentials:

bash
Copy
Edit
docker run -d \
  --name mariadb \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=SuperSecretRootPass \
  -e MYSQL_USER=appuser \
  -e MYSQL_PASSWORD=AppUserPass \
  -e MYSQL_DATABASE=myappdb \
  mariadb:latest
-d
Run detached in the background

--name mariadb
Gives the container a friendly name

-p 3306:3306
Exposes container’s 3306 on host’s 3306

MYSQL_ROOT_PASSWORD / MYSQL_USER / MYSQL_PASSWORD / MYSQL_DATABASE
Bootstrap your initial database and users

Verify it’s running

bash
Copy
Edit
docker ps
You should see a line like:

nginx
Copy
Edit
CONTAINER ID  IMAGE         COMMAND    ...  PORTS                   NAMES
abc123def456  mariadb:latest "docker-entrypoint.s…"   0.0.0.0:3306->3306/tcp  mariadb
2. Test connectivity via CLI
Before firing up MySQL Workbench, ensure the server is reachable:

bash
Copy
Edit
mysql -h 127.0.0.1 -P 3306 -u root -p
Host: 127.0.0.1 (avoids socket vs TCP confusion)

Port: 3306

User: root (or your chosen $MYSQL_USER)

Enter the $MYSQL_ROOT_PASSWORD when prompted

If you see the MariaDB [(none)]> prompt, you’re good to go.

3. Configure MySQL Workbench
Open MySQL Workbench

Create a new connection

Click the “+” next to MySQL Connections

Connection settings

Field	Value
Connection Name	mariadb-docker (any)
Connection Method	Standard (TCP/IP)
Hostname	127.0.0.1
Port	3306
Username	root (or your user)
Password	Store in Vault… → enter SuperSecretRootPass

Test Connection

Click Test Connection

You should see Successfully made the MySQL connection

Save and Open connection

4. (Optional) Fine-tuning & Troubleshooting
Bind-address in MariaDB
If you customized MariaDB’s my.cnf, ensure bind-address = 0.0.0.0 so it listens on all interfaces.

Docker network
If you have multiple containers and want them to talk internally, create a user-defined bridge:

bash
Copy
Edit
docker network create mynet
docker run -d --network mynet --name mariadb … mariadb:latest
Then other containers on mynet can reach mariadb:3306 by hostname.

Firewall
If you run ufw or firewalld, make sure port 3306 on localhost is allowed.

Using localhost vs 127.0.0.1
MySQL Workbench’s “Standard TCP/IP over SSH” can misinterpret localhost as a socket. Stick with 127.0.0.1.

Logs & Errors

bash
Copy
Edit
docker logs mariadb
Check for any startup or authentication errors.

5. Connecting from Other Hosts
If you later need to connect from a different machine on your LAN:

Change the -p flag to bind on a specific interface, e.g.:

bash
Copy
Edit
-p 192.168.1.42:3306:3306
In MySQL Workbench, set Hostname to your host’s LAN IP (e.g. 192.168.1.42).

Make sure your MariaDB user is allowed to connect remotely:

sql
Copy
Edit
GRANT ALL PRIVILEGES ON myappdb.* TO 'appuser'@'%' IDENTIFIED BY 'AppUserPass';
FLUSH PRIVILEGES;

