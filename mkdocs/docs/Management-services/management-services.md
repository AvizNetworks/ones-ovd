# <b> Management Services </b>

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
</style>


<table>
  <tr>
    <th>PICOS</th>
    <th>SONiC</th>
  </tr>
 <tr>
   <th>SYSLOG<th>
 </tr>
 <tr>
  <tr>
    <td>

<b>#Syslog commands in PICOS</b><br>
<b>#Syntax</b><br> 
set system log-level info<br>
syslog monitor on<Br>
set protocols OSPF  traceoptions packet all detail<br>
set system log-level trace<br>
commit<br>
syslog monitor on<br>

</td>
<td>

<b>#Syslog commands in SONiC</b><br>
<b>#Syntax</b><br> 
config syslog add<br> 
config syslog delete<br> 
</br>
<b>#Command to add or delete a specific syslog server IP</b><br>
config syslog add &lt;ipv4-address> --source &lt;source_ipv4_address>&lt;/config><br>
config syslog del &lt;ipv4-address></config><br>
</br>
<b>#View syslog for a particular protocol in SONIC -</b><br>
show logging<br> 
show logging &lt;any_protocol><br> 
</br>
<b># Command to show syslog server IP and port configuration</b><br> 
show syslog<br>
</br>
<b>#Location of syslog configuration file -</b><br>
Configuration file for syslog available at: /etc/rsyslog.conf<br>
</br>
<b>#Example Configuration</b><br>
config syslog add 1.1.1.1 --source 192.168.8.231<br>
config syslog del 1.1.1.1<br>
</br>
<b># Command to view syslog file location</b><br>
Path: /var/log/syslog*

</td>
  </tr>
  <tr>
   <th>ZTP<th>
 </tr>
 <tr>
  <tr>
  <td>
<b># Configuration to enable and disable Zero Touch Provisioning</b><br>
<b># Syntax</b><br>
</br>

ztp-config<br>
Please configure the default PicOS ZTP options:<br>
 (Press other key if no change)<br>
    [1]  PicOS ZTP enabled   * default<br>
    [2]  PicOS ZTP disabled<br>
Enter your choice (1,2):2<br>
PicOS ZTP is disabled.<Br>
 admin@LEAF-A$<Br>
</br>
<b># Alternative Method is to  edit the PICOS  configuration file picos_start.conf and change the value of the ztp_disable variable.</b><br> 
</br>
admin@LEAF-A\$more /etc/picos/picos_start.conf | grep ztp
ztp_disable=true<br>

\# To enable ZTP, the user needs to set ztp_disable to false.

</td>
 <td>

<b>#Configuration</b></br>
<b>#Syntax</b><br>
</br>
<b>#Enable the ZTP services</b><br>
admin@sonic:~$ config ztp enable
<br></br>
<b># Running the ZTP Services</b><br>
admin@sonic:~$ config ztp run -y
<br></br>
<b>#Check the ZTP Status</b>
admin@sonic:~$ show ztp status<br>
</br>
<b>#Check the  /etc/sonic , user will be able to see config_db.json</b><br>
admin@sonic:~$ ls /etc/sonic/ | grep config_db.json<br>
Config_db.json<br>
</br>
<b># Server where ZTP server is hosted , operator can edit in a customized way various parameters like URL , source path  location , destination path location during ZTP automated discovery  process.</b><br>
<b>#Using ZTP to download the config_db.json and the new SONiC version.</b><br>
<b>#Example</b><br>
<b>Example for ztp.json.</b><br>
</br>
```
{
"ztp": {
 "01-configdb-json": {
    "url": {
      "source": "tftp://188.188.36.36/7326_56X_config_db.json",
        "destination": "/etc/sonic/config_db.json"
     }
    },
   "02-firmware": {
      "install": {
        "url": "http://188.188.36.36：8000/sonic-broadcom.bin",
         "skip-reboot": true
         }
      } 
   }
}
```

  </td>
  </tr>
  <tr>
  <th>SNMP</th>
  <th></th>
  </tr>
  <tr>
  <td>

<b># Add SNMP Community and Agent Address</b><br> 
ovs-vsctl set-snmp-enable true<br>
ovs-vsctl show-snmp<br>
snmp is enabled<br>
ovs-vsctl set-snmp-community-name  pica8<br>
ovs-vsctl set-snmp-community-name<br>
</br>
<b>#Syntax</b><br> 
<b># Add SNMP traps and SNMP server target address -</b><br> 
<br>
ovs-vsctl  show-snmp-trap-targets<br>
ovs-vsctl set-snmp-trap-targets &lt;Server_IP_Address><br>
ovs-vsctl set-snmp-trap-targets

  </td>
  <td>

<b># SONiC - Add SNMP Community and Agent Address</b><br> 
<b>#syntax</b><br>
 config snmp community add &ltsnmp_community_name>  &ltMode_Readonly or read Write><br> 
</br>
<b>#Example</b><br>
config snmp community add testcomm ro<br>
</br>
<b># Command to add SNMP Agent IP address</b><br> 
config snmpagent add &lt;Agent_IPV4_Address> -v &lt;VRF-NAME><br> 
</br>
<b># Command to add SNMP user</b><br>
<b>#Syntax </b><br>
config snmp user add &lt;user> (noAuthNoPriv | AuthNoPriv | Priv) (RO | RW) [[(MD5 | SHA | MMAC-SHA-2) &ltauth_password>] [(DES |AES) &lt;encrypt_password>]]<br>
</br>
<b>#Example</b><br>
config snmp user add testuser3 priv rw md5 testuser3_auth_pass aes testuser3_encrypt_pass<br>
</br>
<b># Add SNMP traps and SNMP server target address -</b><br> 
config snmptrap modify 2 &lt;Server_IP_Address><br>
show snmptrap<br>
show snmp agentaddress<br>
show running configuration snmp<br>

  </td>
  </tr>
  <tr>
   <th>AAA/Radius<th>
 </tr>
 <tr>
  <tr>
  <td>

<b># Configure Radius Server IP and Port</b><br>  
set system aaa radius authorization disable &lt;true | false><br>
set system aaa radius authorization server-ip &lt;ipv4_address><br>
set system aaa radius authorization server-ip &lt:ipv4_address> port &lt;integer><br>
set system aaa radius source-interface &lt;interface-name><Br> 
</br>
<b># Show-</b><br>
show system aaa radius<br>
</br>
<b>Enable RADIUS accounting -</b><br>
set system aaa radius accounting disable &lt;true | false><br>
set system aaa radius accounting server-ip <ipv4_address><br>
  </td>
  <td>
<b># SONiC - Configure Radius Server IP and Port</b><br> 
<b>#Syntax </b><br>
config aaa authentication login {radius | tacacs+ | local}  [radius | tacacs+ | local].<br>
config radius add &lt;Radius_server_ip><br>
</br>
<b>#Show Radius commands-</b><br>
show aaa <br>
show radius <br>
</br>
<b>#Command for aaa authentication options</b><br> 
<b>#Syntax</b><br>
aaa  authentication login tacacs+<br>
</br>
<b># If one AAA server fails , go to backup AAA server for authentication</b><br> 
aaa authentication failthrough &lt;enable/disable/default><br> 
aaa authentication fallback &lt;enable/disable/default> <br>
</br>
<b># AAA accounting enable commands in SONiC</b><br>
<b>#Syntax </b><br>
config aaa accounting local<br>
config aaa accounting tacacs+<br>
</br>
<b># Command to add aaa accounting server IP and bind it to a data interface  </b><br>
config radius add &lt;accounting_server_ip><br>
config radius add &lt;accounting_server_ip> --s &lt;source_interface><br>

  </td>
  </tr>
  <tr>
   <th>sFlOW<th>
 </tr>
 <tr>
  <tr>
  <td>

<b>#sflow commands</b><br>
ovs-vsctl  --id=@s create sFlow agent=eth0 target=\"10.10.50.207:9901\" header=128 sampling=5000 polling=30 -- set Bridge br0 sflow=@s<br>
ovs-vsctl list sflow<br>
ovs-vsctl -- clear Bridge br0 sflow

  </td>
  <td>

<b># Command to add  sflow  collector</b><br> 
config sflow collector add &lt;collector_name1>  &lt;sflow_collector_ipv4> &lt;port_number><br>
config sflow collector add &lt;collector_name2>  &lt;sflow_collector_ipv6> &lt;port_number><br>
</br>
<b># Command to delete   sflow  collector </b><br>
config sflow collector del &lt;collector-name1><br>
config sflow collector del &lt;collector-name2><br>
</br>
<b># Command to add  and delete  sflow agent</b><br> 
config sflow  agent-id add<br>
config sflow  agent-id del<br>
</br>
<b># Command to bind  sflow agent  to an interface</b><br> 
config sflow  agent-id add &lt;Ethernet_interface_number><br>
config sflow  agent-id add &lt;loop_interface_number><br>
</br>
<b># Command  Enable / Disable sflow -</b><br>
config sflow  enable<br>
config sflow  disable<br>
config sflow interface<br>
config sflow interface &lt;enable/disable><br>
config sflow  interface enable &lt;Ethernet_interface><br>
<br>
<b># Configure sflow sample rate , interval</b><br> 
config sflow interface sample-rate &lt;interface_name> &lt;sample_rate><br>
config sflow  polling-interval <time_interval_seconds><br>
 </br>
<b># Command to show  sflow  configuration -</b><br>
show sflow<br> 
show sflow  interface
  
  </td>
  </tr>
  <tr>
   <th>NTP<th>
 </tr>
 <tr>
  <tr>
  
  <td>
<b># Configuring the NTP Server IP Address</b><br>
 set system ntp server-ip &lt;NTP_SERVER_IP><br>
</br>
<b># Configuring NTP Source Interface</b>
set system ntp source-interface &lt;VLAN-INTERFACE-NUMBER><br>
</br>
<b>#Configuring Time Zone</b><br>
set system timezone &lt;TIME_ZONE><br>
</br>
<b>#Configuring System Clock</b><br>
set date YYYY:MM:DD -TT

  </td>
  <td>

<b># Command to configure  NTP Server IP</b><br> 
<b>#Syntax </b><br>
config ntp add &lt;NTP_SERVER_IP><br>
</br>
<b># Example</b><br>
config ntp add 10.101.118.10<br>
<br>
<b># Command to delete a configure NTP Server IP</b><br>
config ntp del &lt;ip_address><br>
</br>
<b>#restart NTP-config daemon after applying NTP server config through config_db.json</b><br>
systemctl restart ntp-config<br> 
</br>
<b># Command to list  system timezone.</b><br>
timedatectl list-timezones<br>
</br>
<b>#Command  to modify the time zone</b><br>
timedatectl set-timezone &lt;TIME_ZONE><br>
</br>
<b>#Command  to show the NTP server information</b><br> 
show ntp

  </td>
  </tr>
</table>