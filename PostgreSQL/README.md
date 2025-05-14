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

---

# Setting up PostgreSQL and pgAdmin with Docker

## Setting up PostgreSQL

To install PostgreSQL for Docker, you will need to open the terminal, command line, or PowerShell, depending on your operating system. We will then proceed to install the Postgres image. A **Docker image** is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and system tools.

Use the following command to get the Postgres image:

```bash
docker pull postgres
Now you should see the Postgres Image in your Docker desktop application in the Image tab.

After pulling the Docker image, the next step is to start the Docker container to initiate the database and make it operational.

A Docker container is a lightweight and isolated runtime environment that encapsulates an application’s necessary dependencies, configurations, and code, allowing it to run consistently across different systems.

Use the following command to create a Docker container (remember to change the password):

Bash

docker run --name sqltutorial -e POSTGRES_PASSWORD=marviniscool -p 5432:5432 -d postgres
In the Docker Desktop App you should now see the following:

We created a container using the docker run command.

We use --name to choose a name for our container (e.g., sqltutorial).
-e allows us to set environment variables; in this case, we set the database password to marviniscool (remember to change the password). You can also add POSTGRES_USER=mycustomuser to change the username from the default postgres to a name of your choice.
-p 5432:5432 maps port 5432 on your computer to port 5432 inside the container, which is handy for accessing the database later without any port-related confusion.
Lastly, we use -d to let our container run in detached mode (in the background) and specify that we want to use the postgres image.
If you want to learn more about Docker or the docker run command, check out the documentation:
docker run | Docker Documentation

Alternatively, we can use the command line to check if the Docker container is running by executing the following command:

Bash

docker ps
If you see output similar to the following, you can be sure that your container is up and running:

## Installing pgAdmin4

Now, let’s move on to installing pgAdmin 4. PgAdmin 4 is a popular web-based administration and management tool for PostgreSQL. It provides a user-friendly interface that lets you interact with your databases, execute SQL queries, monitor database performance, and much more, without having to navigate complex command lines.

The installation process is analogous to the process of installing PostgreSQL. We are going to pull the pgAdmin 4 image using Docker, which simplifies the setup process.

Input the following command into your terminal to install pgAdmin 4:

Bash

docker pull dpage/pgadmin4
You should be able to see the image in the Image tab of your Docker Desktop App.

Once we’ve downloaded the image, we can create and run our Docker container. The command below sets up a new Docker container named pgadmin-container, maps port 5050 on your machine to port 80 on the container (pgAdmin's default HTTP port), and sets the default email and password to access the pgAdmin 4 interface.

Here is the command to run the pgAdmin 4 Docker container:

Bash

docker run --name pgadmin-container -p 5050:80 \
  -e PGADMIN_DEFAULT_EMAIL=user@domain.com \
  -e PGADMIN_DEFAULT_PASSWORD=catsarecool \
  -d dpage/pgadmin4
Remember to replace user@domain.com and catsarecool with your desired email and a strong password.

Connecting to Database Container using pgAdmin 4
Log in to pgAdmin 4
Once the container is successfully running (if you encounter any issues, it’s a good idea to check the Docker Desktop app to ensure the container is running), you can access pgAdmin by navigating to http://localhost:5050 in a web browser of your choice.

You will then see a login prompt. You will be able to log in with the e-mail address and password that you specified when running the pgAdmin container (in our example, “user@domain.com” and “catsarecool”).

Connect to Database Container / Add Server
In the next step, we are going to connect to the PostgreSQL database container. For this, you need to click on Add New Server:

And enter the relevant information to connect to our database. In the General tab, under the Name field, we can choose an Alias to refer to our database in pgAdmin (e.g., "SQL Tutorial DB"):

Next, click on the Connection tab. Before we proceed, it’s important to obtain the IP address of the “sqltutorial” container. To find the IP address, you can execute the following command in your terminal (Linux/macOS) or PowerShell (Windows):

Bash

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' sqltutorial
In our case, let's assume it returned the IP address 172.17.0.2 (this may or may not be true for you; use the IP address returned by the command). Now we enter all the connection information:

Host name/address: 172.17.0.2 (or the IP address you found)
Port: 5432
Maintenance database: postgres (this is the default)
Username: postgres (or mycustomuser if you set it during docker run)
Password: marviniscool (or whatever password you selected for the PostgreSQL container)
Optional: Check Save password?
Click Save, and you will be able to select your database server from the Object Explorer menu on the left side.

Congratulations, now your environment should be up and running! For questions about pgAdmin 4, refer to the documentation:

pgAdmin 4 Documentation
pgAdmin - PostgreSQL Tools for Windows, Mac, Linux and the Web
Optional: Test Connection
As an optional last step, we are going to create a database and table using pgAdmin 4 and then try to read the table from the terminal. If you have never worked with databases before, some of these concepts might be overwhelming, but these steps will be covered in detail in succeeding tutorials.

Creating a database and table from pgAdmin 4
In pgAdmin's Object Explorer, expand your server (e.g., "SQL Tutorial DB").

Right-click on ‘Databases’ and select ‘Create’ -> ‘Database…’.

Name your database (for instance, ‘my_new_database’) and then click ‘Save’.

Now, navigate to the database you just created (e.g., my_new_database) in the Object Explorer. Expand it, then expand Schemas -> public.
5.  Right-click on “Tables” and select ‘Create’ -> ‘Table…’.

In the General tab, set the Name of the table to “cattable”.

Switch to the Columns tab. We will create two columns:
* Click the + (Add) button to create the first column.
* Name: id
* Data type: bigserial (or serial for older PostgreSQL versions) - this automatically creates an auto-incrementing integer.
* Set Not Null? to Yes.
* Set Primary Key? to Yes.
* Click the + (Add) button again for the second column.
* Name: catname
* Data type: text
* Set Not Null? to Yes.

Click Save.

Now that we have created the table, we want to add one row of data.

In the Object Explorer, find your new table (cattable under public -> Tables).

Right-click on cattable -> View/Edit Data -> All Rows.

A new panel will open showing the table data (it will be empty). Click on the Add row button (often a + icon or a button in the toolbar of the data view panel).

An empty new row will appear. Click in the catname cell and enter a cool cat name, such as “Bam Bam”.
13. Click the Save Data Changes button (often a floppy disk icon) in the toolbar of the data view panel to save the row to the database. (Please note that we do not need to enter a value in the id field; since we set the data type to bigserial/serial, it will automatically select an ID).

### Querying the Table from the Terminal

With our database and table set up in pgAdmin 4, let’s switch over to the terminal to read the data from the table.

First, we need to connect to our database server in our Docker container using psql:

Bash

docker exec -it sqltutorial psql -U postgres
(If you set a custom user, replace postgres with mycustomuser).

You will be prompted for the password if one is set for the user and not embedded in other ways.

Second, once inside the psql prompt (it will look something like postgres=#), we need to connect to the database “my_new_database” (or whatever you named it) that we created earlier in pgAdmin 4:

SQL

\c my_new_database
The prompt should change to my_new_database=#.

Last but not least, we can use a SELECT statement to select all the rows from the table:

SQL

SELECT * FROM cattable;
You should see an output like this:

 id | catname
----+---------
  1 | Bam Bam
(1 row)
And there you have it! You should see the contents of the ‘cattable’ within ‘my_new_database’ that you created in pgAdmin 4. This validates that pgAdmin 4 and the terminal are both successfully interacting with the PostgreSQL database inside your Docker container.
