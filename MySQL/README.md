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

**Accept External Connections from different IP/Machines - BOTH Local and Docker:**

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

Containerized MySQL Workbench

Pull the Image:
Open your terminal or command prompt and pull the latest linuxserver/mysql-workbench image:

Bash

docker pull lscr.io/linuxserver/mysql-workbench:latest
Create a Persistent Configuration Volume (Recommended):
It's highly recommended to store your MySQL Workbench configuration data outside the container. This way, your settings, connections, and preferences will persist even if you remove and recreate the container.

Create a directory on your host machine where you want to store this data. For example:

Bash

mkdir -p ~/docker_configs/mysql-workbench
Replace ~/docker_configs/mysql-workbench with your preferred path.

Run the Docker Container:
Now, run the container using the docker run command. Here's a typical command:

Bash

docker run -d \
  --name=mysql-workbench \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3000:3000 \
  -p 3001:3001 \
  -v ~/docker_configs/mysql-workbench:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/mysql-workbench:latest
Let's break down the parameters:

-d: Runs the container in detached mode (in the background).
--name=mysql-workbench: Assigns a name to your container for easier management.
-e PUID=1000: Sets the User ID for the container. You should match this to your host user's ID to avoid permission issues with the configuration volume. To find your PUID, you can use the command id -u in your Linux/macOS terminal.
-e PGID=1000: Sets the Group ID for the container. Match this to your host user's GID. To find your PGID, use id -g.
-e TZ=Etc/UTC: Sets the timezone for the container. You can change Etc/UTC to your specific timezone (e.g., Europe/Rome). A list of valid timezones can usually be found online (search for "tz database time zones").
-p 3000:3000: Maps port 3000 on your host to port 3000 in the container. This is for HTTP access to the KasmVNC interface.
-p 3001:3001: Maps port 3001 on your host to port 3001 in the container. This is for HTTPS access to the KasmVNC interface.
-v ~/docker_configs/mysql-workbench:/config: This is crucial for persistence. It mounts the directory you created (~/docker_configs/mysql-workbench on your host) to the /config directory inside the container, where MySQL Workbench stores its configuration. Make sure to replace ~/docker_configs/mysql-workbench with the actual path you created in step 2.
--restart unless-stopped: Configures the container to restart automatically unless you explicitly stop it. This is useful if your server reboots.
lscr.io/linuxserver/mysql-workbench:latest: Specifies the image to use.
Access MySQL Workbench:

Open your web browser.
Navigate to http://<your-host-ip>:3000 or https://<your-host-ip>:3001. If you are running Docker on your local machine, you can use http://localhost:3000 or https://localhost:3001.
You should see the KasmVNC interface, which will load the MySQL Workbench GUI.
Using MySQL Workbench:
Once the GUI loads, you can use MySQL Workbench as you normally would to connect to your MySQL databases, design schemas, run queries, etc.

Important Considerations:

PUID and PGID: Using the correct PUID and PGID is important for file permissions on the mounted /config volume. If you experience permission issues, double-check these values.
Firewall: If you have a firewall enabled on your host machine, ensure that ports 3000 and 3001 (or whichever ports you've mapped) are open.
Security: The KasmVNC interface provided by the linuxserver/mysql-workbench image might have default credentials or no authentication initially. Refer to the LinuxServer.io documentation for this image for details on securing access (e.g., setting USERNAME and PASSWORD environment variables if supported by the KasmVNC base image, or using a reverse proxy).
Connecting to MySQL Databases:
MySQL in another Docker container: If your MySQL server is also running in a Docker container, ensure they are on the same Docker network. You can then connect to the MySQL container using its container name as the hostname in MySQL Workbench (e.g., mysql-server if that's the name of your MySQL container).
MySQL on the Docker host or LAN: You can use the host's IP address or the LAN IP address of the MySQL server. Remember that from within the Workbench container, localhost refers to the container itself, not your host machine.
MySQL on a remote server: Use the public IP address or hostname of the remote MySQL server.
Managing the Container:

View logs: docker logs mysql-workbench
Stop the container: docker stop mysql-workbench
Start the container: docker start mysql-workbench
Remove the container: docker rm mysql-workbench (Note: If you've mapped the /config volume correctly, your data will remain safe on your host).
Alternative: Using Docker Compose

For a more manageable and reproducible setup, especially if you're also running your MySQL database in Docker, you can use Docker Compose. Create a docker-compose.yml file like this:

YAML

version: "3.8"
services:
  mysql-workbench:
    image: lscr.io/linuxserver/mysql-workbench:latest
    container_name: mysql-workbench
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ~/docker_configs/mysql-workbench:/config
    ports:
      - "3000:3000"
      - "3001:3001"
    restart: unless-stopped
    # If you have a MySQL container defined in the same docker-compose file,
    # you might want to add it to a network and use depends_on:
    # networks:
    #   - my_network
    # depends_on:
    #   - mysql_server # if your mysql service is named mysql_server

#  mysql_server: # Example MySQL service
#    image: mysql:latest
#    container_name: mysql-server
#    environment:
#      - MYSQL_ROOT_PASSWORD=yourpassword
#    volumes:
#      - ~/docker_configs/mysql_data:/var/lib/mysql
#    ports:
#      - "3306:3306" # Expose MySQL port if needed from host
#    restart: unless-stopped
#    networks:
#      - my_network

# networks:
#   my_network:
#     driver: bridge
Save this as docker-compose.yml in a new directory. Remember to:

Adjust PUID, PGID, TZ, and the volume path (~/docker_configs/mysql-workbench).
Uncomment and configure the mysql_server service and networks section if you want to run MySQL alongside it.
Then, navigate to that directory in your terminal and run:

Bash

docker-compose up -d
To stop and remove the services:

Bash

docker-compose down
This guide should get you up and running with a dockerized MySQL Workbench using the LinuxServer.io image. Always refer to their official documentation on Docker Hub or their website for the most up-to-date information and advanced configurations.
