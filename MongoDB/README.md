## ▪️ MongoDB 🍃

**Local Installation:**

[MongoDB Installation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)

⚠️  **NOTE:** As of today, a MongoDB 7.0 binary for Debian 12 is not available yet. 
We can use Ubuntu's repo for MongoDB to install the Version 7.0 on Debian 12.
(you might want to use an earlier version for a smoother compatibility though - USE DOCKER WHEN IN DOUBT!!)

Make sure your system is up to date:

	> $ sudo apt update && sudo apt upgrade
	> $ sudo apt install build-essential libjpeg-dev libpng-dev libtiff-dev

Import the MongoDB GPG key to ensure package authenticity:

	> $ curl -fsSL https://pgp.mongodb.com/server-7.0.asc |sudo gpg  --dearmor -o /etc/apt/trusted.gpg.d/mongodb-server-7.0.gpg

Next, you need to create a MongoDB list file in the `/etc/apt/sources.list.d/` directory to add the repo to the source list. 
You can create this file using the following command:

	> $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list

After creating the MongoDB list file, you need to update the package list and install MongoDB:

	> $ sudo apt-get update
	> $ sudo apt-get install -y mongodb-org

Next, Start the Mongod Service (It's not a typo!!) and verify:

	> $ sudo systemctl start mongod
	> $ sudo systemctl status mongod

As a result, The MongoDB service is running as a ‘mongod’ with the default port ‘27017’

Enable Mongod to Start on boot [Optional]:

	> $ sudo systemctl enable mongod

Connect to MongoDB Shell:

	> $ sudo mongosh

Then, create a User Admin with Password:
	
	> use admin
	> db.createUser({user:"admin", pwd:"password", roles:[{role:"root", db:"admin"}]})
	
Now, exit from mongoshell and log back in with:

	> $ sudo mongosh -u admin -p password

You'll be asked to prompt your password.

To test everything works fine, create a new database and insert one document into a collection:

	> $ use newdb
	> $ db.newcollection.insert({"fieldone": 1, "fieldtwo": "hello"})
	> $ db.newcollection.find()

**Docker:**

First, mkdir for a Mongo dir and cd into it:

	> $ mkdir MongoDocker
	> $ cd MongoDocker

Pull the MongoDB Docker Image:
	
	> $ sudo docker pull mongodb/mongodb-community-server

Run the Image as a Container:

	> $ sudo docker run --name mongo -p 27017:27017 -d mongodb/mongodb-community-server:latest

Connect to the Mongo Shell:

	> $ sudo docker exec -i -t mongo mongosh

Create a User Admin with Password:
	
	> use admin
	> db.createUser({user:"admin", pwd:"password", roles:[{role:"root", db:"admin"}]})

To Connect to a Local Docker Container running MongoDB from outside the Container but on the same Machine:

Get the Docker Container IP Address :

	 > $ sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' MONGO_DB_CUSTOM_CONTAINER_ID_OR_NAME

Where the CUSTOM_CONTAINER_ID_OR_NAME is the one you've assigned with --name flag in docker run

Connect then to MongoDB from outside the container, but locally (Outside the Container, but same machine from MongoDB-Client):

	> $ sudo mongosh --host DOCKER_IP_ADDRESS -u MONGODB_USER -p MONGODB_PASSWORD

Connect to the Shell:

	> $ sudo docker exec -i -t mongo /bin/bash

⚠️  **NOTE:**  To connect as the Root, add the Flag -u to the docker exec command followed by the root user (-u root)

**Accept External Connections from different IP/Machines - BOTH Local and Docker:**

Locate the mongod.conf file, usually located in:
	
	/etc/mongod.conf

(Mind that in Docker the File is named 'mongod.conf.orig' at the same location)

To Enable External Connections, edit the File with a Text Editor (Nano will do fine):

	> $ apt-get update
	> $ apt install nano
	> cd etc
	> $ nano mongod.conf (OR mongod.conf.orig)
	
Then locate the bind ip directive and change it to 0.0.0.0, and restart MongoDB:
	
	> $ sudo systemctl restart mongod

OR, restart the Container if MongoDB is running there:
	
	> $ sudo docker restart MONGODB_CONTAINER_ID_OR_NAME

⚠️  **NOTE:** You may want to configure a Firewall an to better setup authentications and permissions on both your MongoDB and Server.

**⚠️  NOTE:** In some cases, for connecting from an external machine, you might also have to configure the Firewall to accept external connection from a list of trusted different IP Addresses and open the Port (in this case 27017) to listen for incoming connections.

In those cases:

	> $ sudo ufw allow from remote_IP_address to any port 27017

OR (unsafe):

	> $ sudo ufw allow 27017

Then:

	> $ sudo ufw reload

If you're handling sensitive data, make sure you know exactly what you're doing.
<br>
Eventually, enroll in some courses regarding Networking and Security.

[Full Enable External Connections Tutorial on MongoDB](https://linuxgenie.net/how-to-enable-remote-access-and-secure-mongodb-database/)
[Yet Another Unofficial Tutorial on Enabling External Connections on MongoDB Docker](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster/)

**You now have a fully functioning Local MongoDB Installation, to use it with Python:**

	> $ sudo pip install pymongo

[MongoDB Docker](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/)
[MongoDB Docs](https://www.mongodb.com/docs/)
[MongoDB Python](https://pymongo.readthedocs.io/en/stable/)
