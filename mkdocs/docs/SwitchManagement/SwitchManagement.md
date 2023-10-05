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
  
  <b># OOB Management IP</b><br>
  <b># Syntax</b><br>
   set system management-ethernet &lt;mgmt-if> ip-address IPv4 &lt;ip-address>
   run show system management-ethernet<br>
</br>
   <b>#Example</b><br>
   set system management-ethernet eth0 ip-address IPv4 192.168.10.5/24<br><br>
   <b>#Inband Management IP</b><br>
   <b>#Syntax</b><br>
   set system inband vlan-interface &lt;vlan-interface-name><br>
   set system inband loopback &lt;ip-address><br>
   set system inband routed-interface &lt;routed-interface-name><br>
</br>
   <b>#Example</b><br>
   set system inband vlan-interface VLAN400<br>
   set system inband loopback 192.168.10.1<br>
   set system inband routed-interface rif-ge3<br>

</td>

<td>

<b># OOB Management IP</b><br>
<b>#Syntax</b><Br>
config interface ip add &ltmgmt-if> &ltIpv4_address> / &ltIpv4_subnet> &ltgateway_ipv4_address><br>
</br>
<b>#Example</b><br>
config interface ip add eth0 192.168.1.1/24 192.168.1.254<br> 
</br>
<b># OOB Management IP with VRF</b><br>
<b>#Syntax</b><Br>
config VRF  add mgmt<br>
config interface ip add mgmt &lt;VRF-NAME> Ipv4_address>/ &lt;Ipv4_subnet> &lt;gateway_IPV4_address> <br>
</br>
<b>#Example</b></br>
config VRF  add mgmt<Br>
config interface ip add mgmt VRF-1 192.168.1.1/24 192.168.1.254<br>
</br>
<b># Command to verify management ip address configured</b><br> 
show management_interface address<br>
Management IP address = 192.168.1.1/24<br>
Management Network Default Gateway = 192.168.1.254<br>

</td>
 </tr>
 <tr>
   <th colspan="2">Switch Reboot</th>
 </tr>
 <tr>
 <td>

<b>#Command in PICOS to reboot system but it will cause traffic disruption</b><br>
request system reboot<br>
<br>
<b># Command sets the system log file to save to disk.</b><br>
set system syslog local-file disk<br>
tail -f /var/log/messages<br>

</td>
 <td>

<b>#Command  to perform system reboot which cause some disruption of data traffic -</b><br> 
reboot<br>
</br>
<b>#Command defines the cause of reboot of a sonic device</b><Br> 
show reboot-cause<Br>
show reboot-cause history<br>
</br>
<b>#Command  enables a switch to reboot up quickly  with minimum disruption to the data plane. </b><br>
fast-reboot<br>
</br>
<b>#Warm reboot commands perform  in-service NOS upgrade without impacting the data plane traffic</b><br> 
warm-reboot -v<br>
config warm_restart enable/disable<Br>
config warm_restart enable<br>
</br>
<b># Command shows configuration of warm restart setting and show whether that service is enabled or disabled </b><br>
show warm_restart config<br>
show warm_restart state<br>
</br>
<b># Command to view syslogs</b><br>
tail -f /var/log/syslog <br>

</td>
 </tr>
 <tr>
   <th colspan="2">Upgrade NOS</th>
 </tr>
 <tr>
 <td>

<b>#Command to check the version in PICOS</b><br> 
Version<br>
</br>
<b>#Command to upgrade  the version in PICOS</b><br> 
upgrade<br>
upgrade [image_name] [factory-default] [backup-file=(*.lst)]<br>
image_name - Image with bin format file(*.bin)<br>
factory-default - Recovery configuration to factory default<br>
backup-file=(*.lst) - Specify a user defined backup list<br>
</br>
upgrade backup-file=/admin/back_files.lst onie-installer-picos-4.0.1-x86.bin Sync<br>
</br>
<b># Example</b><br>
upgrade onie-installer-picos-4.0.1-x86.bin

  </td>
<td>

<b>#Syntax</b> <Br>
<b>#Command to check the version in SONiC</b><br> 
Show version<Br>
</br>
<b>#Command to upgrade  the version in SONiC</b><br> 
sonic-installer<br>
sonic-installer install<br>
sonic-installer install [OPTIONS] &lt;image_file_path><br>
sonic-installer list<br>
</br>
<b># Command to set which image will be used for default boot image after any system reboot</b><br>
sonic-installer set-default<br>
sonic-installer set-default &lt;image_name><br>
sonic-installer set-next-boot <image_name><br>
</br>
<b># Operator can use following command to remove a saved sonic image in device flash/disk -</b><br>
sonic-installer remove<br>
sonic-installer remove [y|-yes] &lt;image_name>

</td>
    </tr>
 <tr>
   <th colspan="2">Configuration Save</th>
 </tr>
 <tr>
 <td>

<b># Command to save the configuration on PICOS</b><br>
save myconfig.conf<br>
</br>
<b># CLI to  delete and re-add  a new save config -</b><Br>
load override myconfig.conf<br>
</br>
<b># Merge a new config on top of existing running configuration –</b><br>
load merge myconfig.conf<br>

</td>
 <td>
 
<b>\# Command to save the configuration on SONiC</b><br>
config save -y<br>
</br>
<b>\# Command  to  delete and re-add  a new save config -</b><br> 
config reload &lt;config_db.json/SONiCYang><br>
</br>
<b>\# Command to load the configuration from json.db</b><br>
config load &lt;config json file><br>
</br>
<b>\# Replace  a new configuration on top of existing running configuration -</b><br>
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