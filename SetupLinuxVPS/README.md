## ▪️ Linux Cloud Instance (VPS) 🐧

Most of the times, when renting a server you'll get access to a very minimal installation.
Do not fear!
I'll guide you through the setup of your vps instance, in case it comes with minimal setup.

**Connecting Via Windows:**
 
 Download [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) and run it.
 <br>
 Once in, type the IP address of the remote machine and connect over the port 22.
 <br>
 A new Terminal with the connection established should open asking you to prompt your username (usually "root") and your password (set up at the time of purchase on vendor website).

**Connecting Via Linux:**

Simply type the following command into a Terminal to open a connection with the remote server through the Terminal.

	> $ ssh remote_username@remote_host

Where remote_username is usually "root" (check on vendor website management panel)  and the remote host is the IP Address.
You should be asked then to prompt in your password (set up at the time of purchase on vendor website).

**Set Up - All OS:**

Now that we are connected via SSH, we need to install the very basic packages we'll need on our machine.
<br>
Update Packages and install sudo:

	> $ apt-get update && apt-get upgrade
	> $ apt-get install sudo

Install your favorite Desktop Environment:

	> $ apt-get install xfce4 xfce4-goodies

Install remote Desktop and Firewall:

	> $ apt-get install xrdp
	> $ apt-get install ufw

**⚠️ NOTE:** Be very careful with the firewall setting as you'd need consistent access to the port 22 and the port 3389

Start the Remote Desktop Service:

	> $ sudo systemctl enable xrdp

**OPTIONAL:**

Setup Firewall:
	
	> $ sudo ufw allow 22
	> $ sudo ufw allow 3389
	> $ sudo ufw enable
	> $ sudo ufw reload

Check Ports:

	> $ sudo ufw status

If you want to check if the remote connection to the VPS is up and running, simply type in a terminal (on localhost):

	> $ ping VPS_IP_ADDRESS

Or, if you want to check if a given port is accessible:
	
	> $ telnet VPS_IP_ADDRESS PORT_NUMBER
	
**OPTIONAL:**

Follow this guide to install Firefox on your Linux Machine [Firefox Installation Guide](https://support.mozilla.org/en-US/kb/install-firefox-linux)

You're now set to go and you can connect with a remote desktop connection to a fully functioning Linux Machine on a VPS!!
