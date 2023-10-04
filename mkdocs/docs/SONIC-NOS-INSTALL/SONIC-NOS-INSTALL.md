# SONiC NOS Installation from ONIE  
Before entering into ONIE install mode, operator should ensure to uninstall the PICOS
Note: Switch shall automatically enter the ONIE install mode if there's no NOS installed yet.

Step 1. Enter the ONIE install mode

<div style="border: 1px solid black; padding: 10px;">
Step 1. Enter the ONIE install mode<br>
</ve>
*ONIE: Install OS <br>                                                   
 ONIE: Rescue <br>                                                         	
 ONIE: Uninstall OS<br>                                                     	
 ONIE: Update ONIE <br>                                                     	
 ONIE: Embed ONIE  <br>                                                     	
 DIAG: Accton Diagnostic (accton_as7326_56x) <br>
 </br>                          	
                                                                        	
     Use the ^ and v keys to select which entry is highlighted.
     Press enter to boot the selected OS, `e' to edit the commands
     before booting or `c' for a command-line.
    The highlighted entry will be executed automatically in 2s.

</div>

Since switch will automatically start the ONIE Service Discovery, the ONIE-Stop command ensures the  users enter the keywords  easily. This is not a mandatory  command but it  won't affect installation no matter whether the user executes it or not though   it will enable users  to clear the ONIE running logs screen .  

\# ONIE-stop

<div style="border: 1px solid black; padding: 10px;">
<b>Step 2: Call the command to stop ONIE discovery process because DHCP server is not available</b> 
ONIE:/ # onie-stop<br>
discover: installer mode detected.<br>
Stopping: discover... done.<br>
</br>
<b>Step 3. Setup the ip address binding to switch management port</b>
ONIE:/ # ifconfig eth0 192.168.1.2 netmask 255.255.255.0<br>
Caution: If user does not specific any management IP statically , Default ONIE  will get ip from DHCP server <br>
<b>Step 4. Install the image from the remote URL via TFTP server IP location 
ONIE:/ # onie-nos-install tftp://192.168.1.1/SONiC.<br>Edgecore-SONiC_20230330_091754_ec202111_352.bin</b><br>
If the installation is successful, the device will reboot automatically and boot-up with SONiC.
</div>


# \# Example SONiC Image upgrade from ONIE prompt 

<div style="border: 1px solid black; padding: 10px;">
<b># Login using the console port and reboot the switch</b><br>
Enter ONIE mode

<b># The Switch will reboot and boot into 'ONIE: Install OS' mode, run the below command to stop auto-discovery
 ONIE:/ # onie-stop</b>

<b># Assign 'eth0' with a management-IP to copy image from remote server</b>
ONIE:/ # ifconfig eth0 &lt;mgmt-ip> netmask &lt;netmask> up

<b># If server is present on different network using below command to add a default route</b>
ONIE:/ # route add default gw &lt;gw-ip>

<b>via SCP</b> 
<b>#SCP method to copy the SONiC  image file</b>
ONIE:/ # scp &lt;user>@&lt;server-ip>:/&lt;dir>/sonic_image.bin

<b># Install copied image -</b>
ONIE:/ # onie-nos-install &lt;sonic_image.bin>
ONIE:/ # onie-nos-install http://&lt;IP>:<port>/<sonic_image.bin>

<b>via HTTP</b>
ONIE:/ # onie-nos-install http://&lt;IP>:&lt;port>/&lt;sonic-image-nos.bin>
</div>