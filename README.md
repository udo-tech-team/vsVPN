#vsVPN

This a Very Simple VPN program based on SSH and PPPD


## Server side

### Requirements 
 - SSH server
 - sudo
 - pppd
 
### How-to
 - Create a VSVPN user with the right shell
	adduser vsvpn --shell /path/to/vsvpn/server.py

 - To allow vsvpn to run pppd, add the following line to /etc/sudoers
	vsvpn		ALL=NOPASSWD:/usr/sbin/pppd
 
 - Add ssh public keys of the clients you want to allow to connect in /home/vsvpn/.ssh/authorized_keys
 - Optional: copy server.conf.example into /etc/vsvpn/server.conf
 
## Client side

### Requirements
 - SSH client
 - pppd

### How-to

 - Generate a SSH keypair: /etc/vsvpn/client_key and /etc/vsvpn/client_key.pub
	ssh-keygen -f /etc/vsvpn/client_key
	chmod 700 /etc/vsvpn/client_key
 
 - Copy client.conf.example into /etc/vsvpn/client.conf
 - Start the client as root
	sudo ./client.py
 
##Todo 

 - routes management on the client side
 - Add a way to automatically attribute IP adress
 - Improve reconnexion