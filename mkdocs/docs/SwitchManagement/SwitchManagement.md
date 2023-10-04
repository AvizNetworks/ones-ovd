# Switch Management
Operator has to login to PICOS and SONiC switch as super user using “sudo su”

<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
  }

  th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: left;
    vertical-align: top;
    word-wrap: break-word;
    width: 50%; 
  }
  

  th {
    color: white;
    background-color: ;
  }
</style>



<table>
  <tr>
    <th>PICOS</th>
    <th>SONiC</th>
  </tr>
 <tr>
   <td>
  
  <b># OOB Management IP</b>
  <b># Syntax</b>
   set system management-ethernet &lt;mgmt-if> ip-address IPv4 &lt;ip-address>
   run show system management-ethernet

   <b>#Example</b>
   set system management-ethernet eth0 ip-address IPv4 192.168.10.5/24<br>
   <b>#Inband Management IP</b>
   <b>#Syntax</b>
   set system inband vlan-interface &lt;vlan-interface-name>
   set system inband loopback &lt;ip-address>
   set system inband routed-interface &lt;routed-interface-name><br>

   <b>#Example</b>
   set system inband vlan-interface VLAN400
   set system inband loopback 192.168.10.1
   set system inband routed-interface rif-ge3

</td>

<td>

<b># OOB Management IP</b>
<b>#Syntax</b>
config interface ip add &ltmgmt-if> &ltIpv4_address> / &ltIpv4_subnet> &ltgateway_ipv4_address>

<b>#Example</b>
config interface ip add eth0 192.168.1.1/24 192.168.1.254 

<b># OOB Management IP with VRF</b>
<b>#Syntax</b>
config VRF  add mgmt
config interface ip add mgmt &lt;VRF-NAME> Ipv4_address>/ &lt;Ipv4_subnet> &lt;gateway_IPV4_address> 

<b>#Example</b>
config VRF  add mgmt
config interface ip add mgmt VRF-1 192.168.1.1/24 192.168.1.254

<b># Command to verify management ip address configured</b> 
show management_interface address
Management IP address = 192.168.1.1/24
Management Network Default Gateway = 192.168.1.254

</td>
 </tr>
 <tr>
   <th colspan="2">Switch Reboot</th>
 </tr>
 <tr>
 <td>

<b>#Command in PICOS to reboot system but it will cause traffic disruption</b>
request system reboot

<b># Command sets the system log file to save to disk.</b>
set system syslog local-file disk
tail -f /var/log/messages

</td>
 <td>

<b>#Command  to perform system reboot which cause some disruption of data traffic -</b> 
reboot

<b>#Command defines the cause of reboot of a sonic device</b> 
show reboot-cause
show reboot-cause history

<b>#Command  enables a switch to reboot up quickly  with minimum disruption to the data plane. </b>
fast-reboot

<b>#Warm reboot commands perform  in-service NOS upgrade without impacting the data plane traffic</b> 
warm-reboot -v
config warm_restart enable/disable
config warm_restart enable

<b># Command shows configuration of warm restart setting and show whether that service is enabled or disabled </b>
show warm_restart config
show warm_restart state

<b># Command to view syslogs</b>
tail -f /var/log/syslog 

</td>
 </tr>
 <tr>
   <th colspan="2">Upgrade NOS</th>
 </tr>
 <tr>
 <td>

<b>#Command to check the version in PICOS</b> 
Version

<b>#Command to upgrade  the version in PICOS</b> 
upgrade
upgrade [image_name] [factory-default] [backup-file=(*.lst)]
image_name - Image with bin format file(*.bin)
factory-default - Recovery configuration to factory default
backup-file=(*.lst) - Specify a user defined backup list

upgrade backup-file=/admin/back_files.lst onie-installer-picos-4.0.1-x86.bin Sync

<b># Example</b>
upgrade onie-installer-picos-4.0.1-x86.bin

  </td>
<td>

<b>#Syntax</b> 
<b>#Command to check the version in SONiC</b> 
Show version

<b>#Command to upgrade  the version in SONiC</b> 
sonic-installer
sonic-installer install
sonic-installer install [OPTIONS] &lt;image_file_path>
sonic-installer list

<b># Command to set which image will be used for default boot image after any system reboot</b>
sonic-installer set-default
sonic-installer set-default &lt;image_name>
sonic-installer set-next-boot <image_name>

<b># Operator can use following command to remove a saved sonic image in device flash/disk -</b>
sonic-installer remove
sonic-installer remove [y|-yes] &lt;image_name>

</td>
    </tr>
 <tr>
   <th colspan="2">Configuration Save</th>
 </tr>
 <tr>
 <td>

<b># Command to save the configuration on PICOS</b>
save myconfig.conf

<b># CLI to  delete and re-add  a new save config -</b>
load override myconfig.conf

<b># Merge a new config on top of existing running configuration –</b>
load merge myconfig.conf

</td>
 <td>
 
<b>\# Command to save the configuration on SONiC</b>
config save -y

<b>\# Command  to  delete and re-add  a new save config -</b> 
config reload &lt;config_db.json/SONiCYang>

<b>\# Command to load the configuration from json.db</b>
config load &lt;config json file>

<b>\# Replace  a new configuration on top of existing running configuration -</b>
config replace &lt;config_db.json/SONiCYang>

</td>
 </tr>
 <tr>
   <th colspan="2">Platform Information</th>
 </tr>   
<tr>
 <td>
<b>#Platform show commands</b><br>
<b>#syntax</b><br>
run show system serial-number<br>
run show system rpsu<br>
 run show system serial-number<br>
run show system temperature<br>
run show system uptime<br>
run show system connections<br>
 run show system core-dumps<br>
run show system cpu-usage<Br>
run show system rpsu<br>
run show system date<br>
run show system fan<br>
 run show system memory-usage<br>
run show system name<Br>
run show system temperature<br>
run show system users<br>
</td>
 <td>
<b>#Command to verify platform details in SONiC</b></br>
<b>#Syntax</b><br>
show system Status<br>
show clock<Br>
show boot<br>
show environment<br>
show system status<br>
show reboot-cause<br>
show uptime<br>
show logging<Br>
show users<Br>
show platform fan<br>
show platform firmware status<br>
show platform firmware version<br>
show platform pcieinfo<Br>
show platform psustatus<Br>
show platform ssdhealth<br>
show platform summary<BR>
show platform syseeprom<br>
show platform temperature<br>
show interfaces transceiver<br>
</td>
 </tr>

 
</table>