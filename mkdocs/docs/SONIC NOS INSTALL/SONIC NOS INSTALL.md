# SONiC NOS Installation from ONIE  
Before entering into ONIE install mode, operator should ensure to uninstall the PICOS
Note: Switch shall automatically enter the ONIE install mode if there's no NOS installed yet.

Step 1. Enter the ONIE install mode

GNU GRUB  version 2.02
``` 
+----------------------------------------------------------------------------+
|*ONIE: Install OS                                                       	|
| ONIE: Rescue                                                           	|
| ONIE: Uninstall OS                                                     	|
| ONIE: Update ONIE                                                      	|
| ONIE: Embed ONIE                                                       	|
| DIAG: Accton Diagnostic (accton_as7326_56x)                            	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
+----------------------------------------------------------------------------+
     Use the ^ and v keys to select which entry is highlighted.
     Press enter to boot the selected OS, `e' to edit the commands
     before booting or `c' for a command-line.
    The highlighted entry will be executed automatically in 2s.

 
``` 
Since switch will automatically start the ONIE Service Discovery, the ONIE-Stop command ensures the  users enter the keywords  easily. This is not a mandatory  command but it  won't affect installation no matter whether the user executes it or not though   it will enable users  to clear the ONIE running logs screen .  

\# ONIE-stop

```
Step 2: Call the command to stop ONIE discovery process because DHCP server is not available 
ONIE:/ # onie-stop
discover: installer mode detected.
Stopping: discover... done.

Step 3. Setup the ip address binding to switch management port
ONIE:/ # ifconfig eth0 192.168.1.2 netmask 255.255.255.0
Caution: If user does not specific any management IP statically , Default ONIE  will get ip from DHCP server 
Step 4. Install the image from the remote URL via TFTP server IP location 
ONIE:/ # onie-nos-install tftp://192.168.1.1/SONiC.Edgecore-SONiC_20230330_091754_ec202111_352.bin
If the installation is successful, the device will reboot automatically and boot-up with SONiC.
```

# \# Example SONiC Image upgrade from ONIE prompt 

```
# Login using the console port and reboot the switch
Enter ONIE mode

# The Switch will reboot and boot into 'ONIE: Install OS' mode, run the below command to stop auto-discovery
ONIE:/ # onie-stop

# Assign 'eth0' with a management-IP to copy image from remote server
ONIE:/ # ifconfig eth0 <mgmt-ip> netmask <netmask> up

# If server is present on different network using below command to add a default route
ONIE:/ # route add default gw <gw-ip>

via SCP 
#SCP method to copy the SONiC  image file
ONIE:/ # scp <user>@<server-ip>:/<dir>/sonic_image.bin

# Install copied image -
ONIE:/ # onie-nos-install <sonic_image.bin>
ONIE:/ # onie-nos-install http://<IP>:<port>/<sonic_image.bin>

via HTTP
ONIE:/ # onie-nos-install http://<IP>:<port>/<sonic-image-nos.bin>

```