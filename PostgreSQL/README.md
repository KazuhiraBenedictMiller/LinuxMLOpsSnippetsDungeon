## Postgre SQL 🐘

**Local Installation:**

[PostgreSQL Installation Guide](https://www.postgresql.org/download/linux/debian/)

There are 2 methods to install locally PostgreSQL on a Debian Machine.

**Method1:**
<br>
Debian comes with Postgres included, so simply update the system and install it with: 

	> $ sudo apt-get update && sudo apt-get upgrade
	> $ sudo apt-get install postgresql

In case you want a specific version of postgres, simply add a dash '-' and the version number, like so: "sudo apt-get install postgresql-12"
<br>
Verify installation and tart postgresql service:

	> $ sudo systemctl status postgresql

Alternatively, start and/or enable the service by replacing "status" with "start" or "enable".

To uninstall:

	> $ sudo apt purge postgresql

**Method2:**
<br>

Create the file repository configuration:

	> $ sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

Then, Import the repository signing key and update package list:

	> $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

OR [RECOMMENDED]:

	> $ curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
	
Finally:
	
	> $ sudo apt-get update

Then, Install Postgresql with:

	> $ sudo apt-get install postgresql
	
In case you want a specific version of postgres, simply add a dash '-' and the version number, like so: "sudo apt-get install postgresql-12"
<br>
Verify installation and tart postgresql service:

	> $ sudo systemctl status postgresql

Alternatively, start and/or enable the service by replacing "status" with "start" or "enable".

To uninstall:

	> $ sudo apt purge postgresql

**Follow-Up for both Methods:**

Now that we have installed PostgreSQL, Set Up the Password on PostgreSQL Database:

	> $ sudo passwd postgres

Then, to Log in the PostgreSQL Server:

	> $ su -- postgres

OR

	> $ sudo su postgres

After you've logged in the PostgreSQL Server, access the PostgreSQL CLI with:

	> $ psql

You can now create a User with:

	> $ CREATE USER username WITH PASSWORD 'password';

And then Grant Privileges with:

	> $ GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO username;

[More on Users](https://www.postgresql.org/docs/16/user-manag.html)
[More on Privileges](https://www.postgresql.org/docs/current/sql-grant.html)

**Docker:**

To use PostgreSQL in a Docker Container, first create a new dir and cd into it:

	> $ mkdir postgredocker
	> $ cd postgredocker

Then, pull the latest (or desired version) of the Postgre image:

	> $ sudo docker pull postgres:latest

Finally, you can run the image with:

	> $ sudo docker run -i -t -d -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -p 5432:5432 --name postgredocker postgres

To then connect to the psql CLI:

	> $ sudo docker exec -i -t postgredocker psql -U username

If you would like to connect from localhost to a Postgres Docker Container running on the same machine:

	> $ sudo psql -h POSTGRES_CONTAINER_IP_ADDRESS -p 5432 -U username

Mind, that as usual, the POSTGRES_CONTAINER_IP_ADDRESS is often 172.17.0.2

**⚠️ NOTE:** Usually, by default postgres docker accept external connections, in case you would like to check simply type from the psql cli 'SHOW listen_addresses;'

**Accept External Connections from different IP/Machines - BOTH Local and Docker:**

Locate the postgresql.conf file, usually located in:
	
	/etc/postgresql/xx/main/

Where xx is the PostgreSQL version that you installed.

Under "Connection Settings", change the following line:

	#listen_addresses = 'localhost'		# what IP address(es) to listen on;

to:

	listen_addresses = '*'		# what IP address(es) to listen on;

Then, configure PostgreSQL to use md5 password authentication in the pg_hba.conf file. This is necessary if you want to connect remotely:

	> $ sudo sed -i '/^host/s/ident/md5/' /etc/postgresql/xx/main/pg_hba.conf
	> $ sudo sed -i '/^local/s/peer/trust/' /etc/postgresql/xx/main/pg_hba.conf
	> $ echo "host all all 0.0.0.0/0 md5" | sudo tee -a /etc/postgresql/xx/main/pg_hba.conf

Where xx is the PostgreSQL version that you installed, so remember to change that.

Then, restart the postgresql.service, like so:

	> $ sudo systemctl restart postgresql

Also remember to allow the PostgreSQL Port, in case your Firewall is activated:

	> $ sudo ufw allow 5432
	> $ sudo ufw reload

On the Remote host, make sure you have the psql cli installed, then open up a terminal and type:

	> $ psql -h REMOTE_IP_ADDRESS -p REMOTE_PORT_NUMBER -U DB_USER DB_NAME

DB_NAME is optional.

And you're good to go!!

**To use PostgreSQL with Python:**

	> $ pip install psycopg2

[PostgreSQL Docs](https://www.postgresql.org/docs/)

**[OPTIONAL]**
**Install pgadmin:**

**Local Installation:**

First import the public key for the repo:

	> $ curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

Then, create the repo config file:

	> $ sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

Install pgadmin:

	> $ sudo apt install pgadmin4

Run a config Script to configure pgadmin:

	> $ sudo /usr/pgadmin4/bin/setup-web.sh

Then, open a browser and type:

	http://localhost/pgadmin4

OR

	http://REMOTE_IP_ADDRESS/pgadmin4

**Docker:**
To install pgadmin, the most convenient way is to do so in a Docker Container, so:

cd into the postgredocker directory and then pull the image:

	> $ cd postgredocker
	> $ sudo docker pull dpage/pgadmin4:latest

The Spin up the Container with:

	> $ sudo docker run --name pgadmin -p 5051:80 -e PGADMIN_DEFAULT_EMAIL=user@mail.com -e PGADMIN_DEFAULT_PASSWORD=password -d dpage/pgadmin

Now, open a browser in local host and type:

	localhost:5051

Log in with the default email and password, and then righ-click on servers -> register and prompt in the server credentials.

If you would like to connect to a pgadmin already running on another machine, then type:

	REMOTE_IP_ADDRESS:5051

**⚠️ NOTE:** To connect to a PostgreSQL DB the IP Address should be 127.0.0.1, if you want to connect to a Docker Container on the same machine it should be the DOCKER_CONTAINER_IP_ADDRESS and if you want to connect to a remote db then it should be the REMOTE_IP_ADDRESS.
