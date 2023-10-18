# <b>Configuration convertor from Cumulus to SONiC</b>

This Configuration convertor is  intended for network administrators with CUMULUS background. This guide will help network administrators  to migrate their current CUMULUS deployment for various Fabric networks to SONiC . CUMULUS User guide <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/</a> can be used as a checklist to get started with the  migration plan from CUMULUS to SONiC. Following  document provides example configuration commands for comparison.

## <b>Switch Management</b>

Operator has to login to CUMULUS and SONiC switch as super user using `sudo su`

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
    <th>CUMULUS</th>
    <th>SONiC</th>
  </tr>
  <tr>
  <th colspan='2'>Management IP</th>
  </tr>
 <tr>
   <td>
        
<b># OOB Management IP</b><br />
<b># Syntax</b><br />
nv set interface eth0 ip address <IP_ADDRESS>/<SUBNET><br />
nv set interface eth0 ip gateway <GATEWAY_IP><br /><br />

<b># Configure edit /etc/network/interfaces file</b><br />
<b># Example</b><br />
sudo nano /etc/network/interfaces <br /><br />

<b># Management interface </b><br />
auto eth0<br />
iface eth0 <br />
    address 192.0.2.42/24 <br />
        gateway 192.0.2.1<br /><br />

<b># OOB  Management IP with VRF</b><br />
<b># Syntax</b><br />
<b>#Management VRF is enabled by default in Cumulus Linux so logins to the switch are set into the management VRF context.</b>
To disable management VRF, following are the options-<br />
Run NCLU command - net del vrf mgmt command<br />
Remove  the auto mgmt and auto eth0 stanzas from the /etc/network/interfaces file and reboot the switch<br /><br />

<b>#Example command brings down the management VRF, then brings it back up with the ifup --with-depends mgmt command:</b><br />
sudo ifdown mgmt<br />
sudo ifup --with-depends mgmt<br /><br />
        

   </td>

<td>
<b># OOB Management IP</b><br />
<b># Syntax</b><br />
config interface ip add &lt;mgmt-if&gt; &lt;Ipv4_address&gt; / &lt;Ipv4_subnet&gt; &lt;gateway_ipv4_address&gt;<br /><br />

<b># Example</b><br />
config interface ip add eth0 192.168.1.1/24 192.168.1.254<br /><br />

<b># OOB Management IP with VRF</b><br />
<b># Syntax</b><br />
config VRF add mgmt<br />
config interface ip add mgmt &lt;VRF-NAME&gt; &lt;Ipv4_address&gt;/&lt;Ipv4_subnet&gt; &lt;gateway_IPV4_address&gt;<br /><br />

<b># Example</b><br />
config VRF add mgmt<br />
config interface ip add mgmt VRF-1 192.168.1.1/24 192.168.1.254<br /><br />

<b># Command to verify management IP address configured</b><br />
show management_interface address<br />
Management IP address = 192.168.1.1/24<br />
Management Network Default Gateway = 192.168.1.254<br />
</td>
</tr>


<tr>
<th colspan="2">Switch Reboot</th>
</tr>


<tr>
<td>
<b># Linux Command in CUMULUS to reboot the system but it will cause traffic disruption</b><br />
<code>sudo reboot</code><br /><br />

<b># Linux Cold restart - cold restarts the system and resets all the hardware devices on the switch</b><br />
    <code>sudo csmgrctl -c</code><br /><br />

<b># Linux Fast restart - fast restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware</b><br />
<code>sudo csmgrctl -f</code><br /><br />

<b># Linux Warm restart system with no interruption to traffic for existing route entries</b><br />
<code>sudo csmgrctl -w</code><br />
</td>

<td>
<b># Command to perform a system reboot which may cause some disruption of data traffic</b><br />
<code>reboot</code><br /><br />

<b># Command to define the cause of reboot of a Sonic device</b><br />
<code>show reboot-cause</code><br />
<code>show reboot-cause history</code><br /><br />

<b># Command to enable a switch to reboot quickly with minimum disruption to the data plane</b><br />
<code>fast-reboot</code><br /><br />

<b># Warm reboot commands perform in-service NOS upgrade without impacting the data plane traffic</b><br />
<code>warm-reboot -v</code><br />
<code>config warm_restart enable/disable</code><br />
<code>config warm_restart enable</code><br /><br />

<b># Command to show the configuration of warm restart settings and whether the service is enabled or disabled</b><br />
<code>show warm_restart config</code><br />
<code>show warm_restart state</code><br /><br />

<b># Command to view syslogs</b><br />
<code>tail -f /var/log/syslog</code><br />
</td>
</tr>

<tr>
   <th colspan="2">Upgrade NOS</th>
</tr>

<tr>
<td>
<b># Command to check the version in CUMULUS</b><br />
<code>nv show platform software installed</code><br /><br />

<b># ONIE install Cumulus image via FTP</b><br />
<code>ONIE#onie-nos-install ftp://local-ftp-server/cumulus-install-[PLATFORM].bin</code><br /><br />

<b># ONIE install Cumulus image via TFTP</b><br />
<code>ONIE#onie-nos-install tftp://local-tftp-server/cumulus-install-[PLATFORM].bin</code><br /><br />

<b># Syntax to Upgrade Cumulus Switch</b><br />
<code>sudo onie-install -a -i http://10.x.x.x/cumulus-linux-4.1.0-mlx-amd64.bin</code><br />
<code>sudo reboot</code><br /><br />

<b># Cumulus Install command using the installer</b><br />
<code>sudo -E apt-get update</code><br /><br />

<b># Command to see the additional package dependencies that will be installed or upgraded</b><br />
<code>sudo -E apt-get upgrade --dry-run</code><br /><br />

<b># Upgrade all the packages to the latest distribution</b><br />
<code>sudo -E apt-get upgrade</code><br /><br />

<b># Reboot the switch</b><br />
<code>sudo reboot</code><br />
</td>



<td>
<b># Command to check the version in SONiC</b><br />
<code>Show version</code><br /><br />

<b># Command to upgrade the version in SONiC</b><br />
<code>sonic-installer</code><br />
<code>sonic-installer install</code><br />
<code>sonic-installer install [OPTIONS] &lt;image_file_path&gt;</code><br />
<code>sonic-installer list</code><br /><br />

<b># Command to set which image will be used for default boot image after any system reboot</b><br />
<code>sonic-installer set-default</code><br />
<code>sonic-installer set-default &lt;image_name&gt;</code><br />
<code>sonic-installer set-next-boot &lt;image_name&gt;</code><br /><br />

<b># Operator can use the following command to remove a saved SONiC image in device flash/disk</b><br />
<code>sonic-installer remove</code><br />
<code>sonic-installer remove [y|-yes] &lt;image_name&gt;</code><br />
</td>
</tr>

<tr>
   <th colspan="2">Configuration Save</th>
</tr>


<tr>
<td>
<b># Command to save the configuration on Cumulus</b><br />
<code>sudo config-backup</code><br />
<code>sudo config-backup -d -D &lt;CONFIG_FILE&gt;</code><br />
<code>sudo config-backup -q -X .*~$</code><br />
<code>sudo config-backup -pv</code><br /><br />

<b># Command to restore configuration</b><br />
<code>sudo config-restore -b config_backup-2019-04-23-21.30.47_leaf01</code><br />
<code>sudo config-restore -n 10</code><br />
<code>sudo config-restore -N</code><br />
<code>sudo config-restore -L -N</code><br /><br />

<b># CLI to delete and re-add a new saved config</b><br />
<code>net add &lt;config_file&gt;</code><br />
<code>net del &lt;config_file&gt;</code><br /><br />

<b># Use the net pending command to review staged changes</b><br />
<code>net pending &lt;config_file&gt;</code><br /><br />

<b># Command to commit the changes in config</b><br />
<code>net commit</code><br /><br />

<b># Command to revert the last config change</b><br />
<code>net abort</code><br />
</td>
<td>
<b># Command to save the configuration on SONiC</b><br />
<code>config save -y</code><br /><br />

<b># Command to delete and re-add a new saved config</b><br />
<code>config reload &lt;config_db.json/SONiCYang&gt;</code><br /><br />

<b># Command to load the configuration from a JSON file</b><br />
<code>config load &lt;config_json_file&gt;</code><br /><br />

<b># Replace a new configuration on top of the existing running configuration</b><br />
<code>config replace &lt;config_db.json/SONiCYang&gt;</code><br />
</td>
</tr>

<tr>
   <th colspan="2">Platform Information</th>
</tr> 

<tr>
<td>
<b># Show system platform information</b><br />
<code>sudo decode-syseeprom</code><br /><br />

<b># Command to show the platform type</b><br />
<code>sudo decode-syseeprom</code><br />
</td>

<td>
<b># Command to verify platform details in SONiC</b><br />
<b># Syntax</b><br />
<code>show system status</code><br />
<code>show clock</code><br />
<code>show boot</code><br />
<code>show environment</code><br />
<code>show system status</code><br />
<code>show reboot-cause</code><br />
<code>show uptime</code><br />
<code>show logging</code><br />
<code>show users</code><br />
<code>show platform fan</code><br />
<code>show platform firmware status</code><br />
<code>show platform firmware version</code><br />
<code>show platform pcieinfo</code><br />
<code>show platform psustatus</code><br />
<code>show platform ssdhealth</code><br />
<code>show platform summary</code><br />
<code>show platform syseeprom</code><br />
<code>show platform temperature</code><br />
<code>show interfaces transceiver</code><br />
</td>
</tr>
</table>

## <b>Management Services</b>

<table>
<tr>
    <td><b>CUMULUS</b</td>
    <td><b>SONiC</b></td>
</tr>

<tr>
   <td colspan='2'><b>SYSLOG</b></td>
</tr>

<tr>
<td>
<b># Configure syslog server</b><br />
<b># Syntax</b><br />
<code>net add syslog host ipv4 &lt;IP_ADDRESS&gt; port udp &lt;PORT_NUMBER&gt;</code><br />
<code>net pending</code><br />
<code>net commit</code><br /><br />

<b># Example</b><br />
<code>net add syslog host ipv4 192.168.0.254 port udp 514</code><br />
<code>net pending</code><br />
<code>net commit</code><br /><br />

<b># Command to delete syslog server</b><br />
<code>net del syslog host ipv4 &lt;IP_ADDRESS&gt; port udp &lt;PORT_NUMBER&gt;</code><br />
</td>

<td>
<b># Syslog commands in SONiC</b><br />

<b># Syntax</b><br />
<code>config syslog add</code><br />
<code>config syslog delete</code><br /><br />

<b># Command to add or delete a specific syslog server IP</b><br />
<code>config syslog add &lt;ipv4-address&gt; --source &lt;source_ipv4_address&gt;</code><br />
<code>config syslog del &lt;ipv4-address&gt;</code><br /><br />

<b># View syslog for a particular protocol in SONiC</b><br />
<code>show logging</code><br />
<code>show logging &lt;any_protocol&gt;</code><br /><br />

<b># Command to show syslog server IP and port configuration</b><br />
<code>show syslog</code><br /><br />

<b># Location of syslog configuration file</b><br />
Configuration file for syslog available at: /etc/rsyslog.conf<br /><br />

<b># Example Configuration</b><br />
<code>config syslog add 1.1.1.1 --source 192.168.8.231</code><br />
<code>config syslog del 1.1.1.1</code><br /><br />

<b># Command to view syslog file location</b><br />
Path: /var/log/syslog*<br />
</td>
</tr>

<tr><td colspan='2'><b>ZTP</b></td></tr>


<tr>
<td>
<b># Configuration to enable Zero Touch Provisioning</b><br />
<b># Syntax</b><br />

<b># ZTP Over DHCP command</b><br />
<b># Example</b><br />
<code>Edit /etc/dhcp/dhcpd.conf file for an ISC DHCP server</code><br />
<code>option cumulus-provision-url code 239 = text;</code><br />
<code>subnet 192.0.2.0 netmask 255.255.255.0 {</code><br />
<code>range 192.0.2.100 192.168.0.200;</code><br />
<code>option cumulus-provision-url "http://192.0.2.1/demo.sh";</code><br /><br />

<b># Command to specify the hostname of the switch in ZTP script</b><br />
<b># Example</b><br />
<code>subnet 192.168.0.0 netmask 255.255.255.0 {</code><br />
<code>range 192.168.0.100 192.168.0.200;</code><br />
<code>option cumulus-provision-url "http://192.0.2.1/demo.sh";</code><br />
<code>host dc1-tor-sw1 { hardware ethernet 44:38:39:00:1a:6b; fixed-address 192.168.0.101; option host-name "dc1-tor-sw1"; }</code><br /><br />

<b># Command function to demonstrate the ZTP function through a Linux call</b><br />
<code>function init_ztp(){</code><br />
<code>CUMULUS_TARGET_RELEASE=5.0.0</code><br />
<code>CUMULUS_CURRENT_RELEASE=$(cat /etc/lsb-release | grep RELEASE | cut -d "=" -f2)</code><br />
<code>IMAGE_SERVER_HOSTNAME=webserver.example.com</code><br />
<code>IMAGE_SERVER="http://"$IMAGE_SERVER_HOSTNAME"/"$CUMULUS_TARGET_RELEASE".bin"</code><br />
<code>ZTP_URL="http://"$IMAGE_SERVER_HOSTNAME"/ztp.sh"</code><br />
<code>if [ "$CUMULUS_TARGET_RELEASE" != "$CUMULUS_CURRENT_RELEASE" ]; then</code><br />
<code>ping_until_reachable $IMAGE_SERVER_HOSTNAME</code><br />
<code>/usr/cumulus/bin/onie-install -fa -i $IMAGE_SERVER -z $ZTP_URL && reboot</code><br />
<code>else</code><br />
<code>init_ztp && reboot</code><br />
<code>exit 0</code><br />
<code>}</code><br /><br />

<b># Command to test the ZTP Scripts</b><br />
<b># Validate and debug your ZTP scripts</b><br />
<code>sudo ztp -v -r http://192.x.x.x/script.sh</code><br /><br />

<b># Verify ZTP status</b><br />
<code>sudo systemctl -l status ztp.service</code><br />
</td>

<td>
<b># Configuration</b><br />
<b># Syntax</b><br />

<b># Enable the ZTP services</b><br />
<code>admin@sonic:~$ config ztp enable</code><br /><br />

<b># Running the ZTP Services</b><br />
<code>admin@sonic:~$ config ztp run -y</code><br /><br />

<b># Check the ZTP Status</b><br />
<code>admin@sonic:~$ show ztp status</code><br /><br />

<b># Check the /etc/sonic, user will be able to see config_db.json</b><br />
<code>admin@sonic:~$ ls /etc/sonic/ | grep config_db.json</code><br />
<code>Config_db.json</code><br /><br />

<b># Server where ZTP server is hosted, the operator can edit in a customized way various parameters like URL, source path location, destination path location during ZTP automated discovery process</b><br />
<b># Example</b><br />
<code>Example for ztp.json.</code><br />
<code>{
    "ztp": {
        "01-configdb-json": {
            "url": {
                "source": "tftp://188.188.36.36/7326_56X_config_db.json",
                "destination": "/etc/sonic/config_db.json"
            }
        },
        "02-firmware": {
            "install": {
                "url": "http://188.188.36.36:8000/sonic-broadcom.bin",
                "skip-reboot": true
            }
        }
    }
}</code><br />
</td>
</tr>

<tr><td colspan='2'><b>SNMP</b></td></tr>
<tr>
<td>
<b># Add SNMP Community and Agent Address</b><br />

<b># Command to start SNMP service</b><br />
<code>sudo systemctl start snmpd.service</code><br /><br />

<b># Enable snmpd daemon to start automatically after reboot</b><br />
<code>sudo systemctl enable snmpd.service</code><br /><br />

<b># Command to reload</b><br />
<code>sudo systemctl daemon-reload</code><br /><br />

<b># Configure the snmp daemon to listen on the localhost IPv4 and IPv6 interfaces</b><br />
<code>net add snmp-server listening-address localhost</code><br />
<code>net add snmp-server listening-address localhost-v6</code><br /><br />

<b># Configure SNMP listening address on the loopback interface</b><br />
<code>net add snmp-server listening-address localhost</code><br /><br />

<b># Configure snmpd daemon to listen on all interfaces for either IPv4 or IPv6</b><br />
<code>net add snmp-server listening-address all</code><br />
<code>net add snmp-server listening-address all-v6</code><br /><br />

<b># Configure snmpd to listen to a specific IPv4 or IPv6 address</b><br />
<code>net add snmp-server listening-address &lt;SNMP_LISTENING_ADDRESS&gt;</code><br /><br />

<b># Configure SNMPv3 username</b><br />
<code>net add snmp-server username &lt;SNMP_USERNAME&gt; auth-none</code><br /><br />

<b># Configure SNMP server username with password options</b><br />
<b># Example</b><br />
<code>net add snmp-server username user1 auth-none</code><br />
<code>net add snmp-server username user2 auth-md5 user2password</code><br />
<code>net add snmp-server username user1 auth-none oid 1.3.6.1.2.1</code><br />
<code>net add snmp-server username user1 auth-none oid system</code><br />
<code>net add snmp-server username user3 auth-sha testshax encrypt-aes testaesx oid 1.3.6.1.2.1</code><br />
</td>

<td>
<b># SONiC - Add SNMP Community and Agent Address</b><br />

<b># Syntax to add SNMP community</b><br />
<code>config snmp community add &lt;snmp_community_name&gt; &lt;Mode_Readonly or read Write&gt</code><br /><br />

<b># Example to add SNMP community</b><br />
<code>config snmp community add testcomm ro</code><br /><br />

<b># Command to add SNMP Agent IP address</b><br />
<code>config snmpagent add &lt;Agent_IPV4_Address> -v &lt;VRF-NAME></code><br /><br />

<b># Command to add SNMP user</b><br />
<b># Syntax</b><br />
<code>config snmp user add &lt;user> (noAuthNoPriv | AuthNoPriv | Priv) (RO | RW) [[(MD5 | SHA | MMAC-SHA-2) &lt;auth_password>] [(DES | AES) &lt;encrypt_password>]</code><br /><br />

<b># Example to add SNMP user</b><br />
<code>config snmp user add testuser3 priv rw md5 testuser3_auth_pass aes testuser3_encrypt_pass</code><br /><br />

<b># Add SNMP traps and SNMP server target address</b><br />
<code>config snmptrap modify 2 &lt;Server_IP_Address></code><br />
<code>show snmptrap</code><br />
<code>show snmp agentaddress</code><br />
<code>show running configuration snmp</code><br />
</td>
</tr>

<tr>
<td colspan='2'><b>AAA/Radius</b> </td>
</tr>

<tr>
<td>
<b># Configure Radius Server IP and Port</b><br />

<b># Local Fallback Authentication</b><br />
<code>sudo useradd -u 1002 -g 1001 -o -s /sbin/radius_shell johnadmin</code><br /><br />

<b># Enable the local privileged user to run sudo and NCLU commands</b><br />
<code>sudo adduser &lt;USERNAME> netedit</code><br />
<code>sudo adduser &lt;USERNAME> sudo</code><br />
<code>sudo systemctl restart netd</code><br /><br />

<b># Modify /etc/passwd file to move the local user line before the radius_priv_user</b><br />
<code>sudo vi /etc/passwd</code><br />
<code>johnadmin:x:1002:1001::/home/johnadmin:/sbin/radius_shell</code><br />
<code>radius_priv_user:x:1002:1001::/home/radius_priv_user:/sbin/radius_shell</code><br /><br />

<b># Set the local password for the local user</b><br />
<code>sudo passwd johnadmin</code><br /><br />

<b># Verify radius client configuration</b><br />
<code>net add interface &lt;INTERFACE_NAME></code><br />
<code>source /etc/network/interfaces.d/*.intf</code><br />
</td>
<td>
<b># SONiC - Configure Radius Server IP and Port</b><br />

<b># Syntax to configure AAA authentication login</b><br />
<code>config aaa authentication login {radius | tacacs+ | local} [radius | tacacs+ | local]</code><br />
<code>config radius add &lt;Radius_server_ip></code><br /><br />

<b># Show Radius commands</b><br />
<code>show aaa</code><br />
<code>show radius</code><br /><br />

<b># AAA authentication options</b><br />
<b># Syntax</b><br />
<code>aaa authentication login tacacs+</code><br /><br />

<b># If one AAA server fails, go to the backup AAA server for authentication</b><br />
<code>aaa authentication failthrough &lt;enable/disable/default></code><br />
<code>aaa authentication fallback &lt;enable/disable/default></code><br /><br />

<b># AAA accounting enable commands in SONiC</b><br />
<b># Syntax</b><br />
<code>config aaa accounting local</code><br />
<code>config aaa accounting tacacs+</code><br /><br />

<b># Command to add AAA accounting server IP and bind it to a data interface</b><br />
<code>config radius add &lt;accounting_server_ip></code><br />
<code>config radius add &lt;accounting_server_ip> --s &lt;source_interface></code><br />
</td>
</tr>

<tr><td colspan='2'><b>sFlow</b></td></tr>
<tr>
<td>
<b># sFlow Commands</b><br />

<b># Start sFlow process</b><br />
<code>sudo systemctl start hsflowd.service</code><br /><br />

<b># Validate which sFlow agent IP was selected</b><br />
<code>grep agentIP /etc/hsflowd.auto</code><br /><br />

<b># Command to send sFlow to an in-band collector on the default VRF:</b><br />
<code>sudo systemctl enable hsflowd.service</code><br />
<code>sudo systemctl start hsflowd.service</code><br />
</td>

<td>
<b># Command to add sFlow collector</b><br />
<code>config sflow collector add &lt;collector_name1> &lt;sflow_collector_ipv4> &lt;port_number></code><br />
<code>config sflow collector add &lt;collector_name2> &lt;sflow_collector_ipv6> &lt;port_number></code><br /><br />

<b># Command to delete sFlow collector</b><br />
<code>config sflow collector del &lt;collector-name1></code><br />
<code>config sflow collector del &lt;collector-name2></code><br /><br />

<b># Command to add and delete sFlow agent</b><br />
<code>config sflow agent-id add</code><br />
<code>config sflow agent-id del</code><br /><br />

<b># Command to bind sFlow agent to an interface</b><br />
<code>config sflow agent-id add &lt;Ethernet_interface_number></code><br />
<code>config sflow agent-id add &lt;loop_interface_number></code><br /><br />

<b># Command to enable/disable sFlow</b><br />
<code>config sflow enable</code><br />
<code>config sflow disable</code><br />
<code>config sflow interface</code><br />
<code>config sflow interface &lt;enable/disable></code><br />
<code>config sflow interface enable &lt;Ethernet_interface></code><br /><br />

<b># Configure sFlow sample rate and interval</b><br />
<code>config sflow interface sample-rate &lt;interface_name> &lt;sample_rate></code><br />
<code>config sflow polling-interval &lt;time_interval_seconds></code><br /><br />

<b># Command to show sFlow configuration</b><br />
<code>show sflow</code><br />
<code>show sflow interface</code><br />
</td>
</tr>



<tr><td colspan='2'><b>NTP</b></td></tr>

<tr><td>
<b># Configuring the NTP Server IP Address</b><br />
<code>net add time ntp server .cumulusnetworks.pool.ntp.org iburst</code><br /><br />

<b># Commands to add the NTP server to the list of servers in /etc/ntp.conf</b><br />
<code>ps -ef | grep ntp</code><br /><br />

<b># Verify that ntpd is running on the system</b><br />
<code>net show time ntp servers</code><br /><br />

<b># Verify the NTP peer status</b><br />
<code>net del time ntp server 0.cumulusnetworks.pool.ntp.org</code><br />
<code>net del time ntp server 1.cumulusnetworks.pool.ntp.org</code><br /><br />

<b># Command to change the NTP source interface</b><br />
<code>net add time ntp source &lt;interface_name></code><br /><br />

<b># Validate NTP configuration</b><br />
<code>sudo systemctl restart ntp</code><br />
<code>sudo systemctl status -n0 ntp.service</code><br /><br />

<b># Edit the /etc/ntp.conf file to specify the server you want to use</b><br />
<code>sudo nano /etc/ntp.conf</code><br />
<code>server ntp.your-provider.example</code><br />
</td>

<td>
<b># Command to configure NTP Server IP</b><br />
<code>config ntp add &lt;NTP_SERVER_IP></code><br /><br />

<b># Example</b><br />
<code>config ntp add 10.101.118.10</code><br /><br />

<b># Command to delete a configured NTP Server IP</b><br />
<code>config ntp del &lt;ip_address></code><br /><br />

<b># Restart NTP-config daemon after applying NTP server config through config_db.json</b><br />
<code>systemctl restart ntp-config</code><br /><br />

<b># Command to list system timezone</b><br />
<code>timedatectl list-timezones</code><br /><br />

<b># Command to modify the time zone</b><br />
<code>timedatectl set-timezone &lt;TIME_ZONE></code><br /><br />

<b># Command to show the NTP server information</b><br />
<code>show ntp</code><br />
</td>
</tr>
</table>



## <b>Port Mirroring</b>
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
<th>CUMULUS</th>
<th>SONiC</th>
</tr>

<tr>
<td>
<b># Configuring Port Mirroring</b><br />

<b># Syntax to configure SPAN with NCLU</b><br />
<code>net add port-mirror session &lt;session-id> (ingress|egress) span src-port &lt;interface> dst-port &lt;interface></code><br />

<b># Syntax to configure ERSPAN with NCLU</b><br />
<code>net add port-mirror session &lt;session-id> (ingress|egress) erspan src-port &lt;interface> src-ip &lt;interface> dst-ip &lt;ip-address></code><br /><br />

<b># Command to mirror all packets received on swp1, and copy and transmit the packets to swp2 for monitoring</b><br />
<code>net add port-mirror session 1 ingress span src-port &lt;Source_interface> dst-port &lt;dest_interface></code><br />

<b># Command to mirror all packets that are sent out of swp1, and copy and transmit the packets to swp2 for monitoring</b><br />
<code>net add port-mirror session 1 egress span src-port &lt;Source_interface> dst-port &lt;dest_interface></code><br /><br />

<b># Show Session Configuration</b><br />
<code>net show port-mirror session 1</code><br />

<b># Show SPAN and ERSPAN configuration for all sessions</b><br />
<code>net show port-mirror session all</code><br /><br />

<b># Delete a SPAN or ERSPAN session</b><br />
<code>net del port-mirror session 1</code><br />

<b># Delete all SPAN or ERSPAN sessions</b><br />
<code>net del port-mirror session all</code><br /><br />

<b># ERSPAN Command Example</b><br />
<code>net add port-mirror session 1 ingress erspan src-port swp1 src-ip 10.10.10.1 dst-ip 10.10.10.234</code><br />
</td>
<td>
<b># Create a Mirror Session</b><br />
<code>config mirror_session add ts1_everflow &lt;Source_Ip_address> &lt;destination_Ip_Address> &lt;dscp_number> &lt;queue_number></code><br /><br />

<b># Command to create ACL table</b><br />
<code>config acl add table ACL_Mirror MIRROR --description 'mirror' --stage ingress --ports Ethernet0</code><br /><br />

<b># Command to create an ACL JSON file and load it to the configuration database for everflow</b><br />
<code>cat acl.json</code><br />
<code>{
    "ACL_RULE": {
        "ACL_Mirror|ACE_Mirror": {
            "PRIORITY": "55",
            "IP_TYPE": "ipv4any",
            "MIRROR_ACTION": "ts1_everflow"
        }
    }
}</code><br /><br />

<b># Command to load the acl.json with new config related to ACL applied</b><br />
<code>config load acl.json -y</code><br /><br />

<b># Command to verify the mirror status</b><br />
<code>show mirror_session</code><br /><br />

<b># Command to create a mirror session for SPAN</b><br />
<code>config mirror_session span add &lt;session_name> &lt;Destination_interface_Analyzer> &lt;Source_intertface_switch></code><br /><br />

<b># Command to create a mirror session for Remote SPAN</b><br />
<code>config mirror_session erspan add &lt;session_name> &lt;src_ip> &lt;dst_ip> &lt;dscp> &lt;ttl> [gre_type] [queue] [src_port] [direction]</code><br /><br />

<b># Command to create a mirror session and ACL table</b><br />
<code>config mirror_session span add &lt;session_name> &lt;Destination_port> &lt;Source_port> &lt;Direction></code><br /><br />

<b># Example</b><br />
<code>config acl add  table Test MIRROR -p Ethernet8 -s ingress</code><br /><br />

<b># Command to verify the mirror table</b><br />
<code>show mirror_session</code><br /><br />

<b># Create ACL JSON file and load it to the configuration database for Mirror</b><br />
<code>cat acl.json</code><br />
<code>{
    "ACL_RULE": {
        "Test|Forward": {
            "PRIORITY": "2",
            "MIRROR_ACTION": "test",
            "VLAN_ID": "20"
        }
    }
}</code><br /><br />

<b># Command to load the JSON file with ACL config applied</b><br />
<code>config load acl.json -y</code><br />
<code>config save -y</code><br /><br />

<b># Command to check the status of ACL table and mirror session</b><br />
<code>show mirror_session</code><br />
<code>show acl table</code><br /><br />
</td>
</tr>
</table>

<!-- ################################################# -->

## <b>Layer 2 Switching</b>
### <b>Interface and Port VLAN</b>

![Layer2 Switching](../img/image1CumulusMigration.png)

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
    <th>CUMULUS</th>
    <th>SONiC</th>
</tr>
<tr><th>Port VLAN</th></tr>

<tr>
<td>
    <b># Create VLANs</b><br />
    <code>net add bridge bridge ports swp1-2</code><br />
    <code>net add bridge bridge vids 100,200</code><br /><br />

    <b># Configure an Ethernet port to override the bridge VIDs</b><br />
    <code>net add bridge bridge ports swp1-3</code><br />
    <code>net add bridge bridge vids 100,200</code><br />
    <code>net add bridge bridge pvid 1</code><br />
    <code>net add interface swp3 bridge vids 200</code><br /><br />

    <b># Command to add a primary VLAN nativeVLAN</b><br />
    <code>net add bridge bridge PVID 1</code><br /><br />

    <b># Configure the new VLAN reserved range</b><br />
    <code>sudo cat /etc/cumulus/switchd.conf</code><br />
    <code>Resv_vlan_range 1 to 100</code><br /><br />

    <b># Command to restart switch services</b><br />
    <code>sudo systemctl restart switchd.service</code><br />
</td>
<td>
    <b># Configure Interface Speed</b><br />
    <code>config interface speed Ethernet&lt;interface> &lt;speed></code><br />
    <code>config interface advertised-speeds Ethernet&lt;interface> &lt;speed></code><br /><br />

    <b># Set Auto Negotiation for an Ethernet Interface</b><br />
    <code>config interface autoneg Ethernet&lt;interface> enable</code><br /><br />

    <b># Show Auto Negotiation Status for an Ethernet Interface</b><br />
    <code>show interface autoneg status Ethernet0</code><br /><br />

    <b># Show Operational Status of Interfaces</b><br />
    <code>show interface status</code><br /><br />

    <b># Configure 4x10GE Breakout for a 40GE Port</b><br />
    <code>config interface breakout Ethernet1 '4x10G'</code><br /><br />

    <b># Show Interface Breakout Options</b><br />
    <code>show interface breakout</code><br /><br />

    <b># Configure FEC Mode of an Ethernet Interface</b><br />
    <code>config interface fec Ethernet&lt;interface> &lt;FEC_MODE></code><br /><br />

    <b># Create VLANs</b><br />
    <code>config vlan add &lt;vlan_value1></code><br />
    <code>config vlan add &lt;vlan_value2></code><br /><br />

    <b># Show VLAN Configuration</b><br />
    <code>show vlan config</code><br /><br />

    <b># Add Interface to VLAN in Tagged (Trunk) Mode</b><br />
    <code>config vlan member add &lt;vlan_value1> Ethernet&lt;interface1></code><br />
    <code>config vlan member add &lt;vlan_value2> Ethernet&lt;interface2></code><br /><br />

    <b># Add Interface to VLAN in Untagged (Access) Mode</b><br />
    <code>config vlan member add -u &lt;vlan_value1> Ethernet&lt;interface1></code><br />
    <code>config vlan member add -u &lt;vlan_value2> Ethernet&lt;interface2></code><br /><br />

    <b># Show VLAN Information</b><br />
    <code>show vlan brief</code><br />
</td>
</tr>

<tr><td colspan='2'><b>LAG-</b> IEEE 802.3ad link aggregation mode that allows one or more links to be aggregated together to form a link aggregation group (LAG) so that a media access control (MAC) client can treat the group as if it were a single link. IEEE 802.3ad link aggregation is the default mode.
</td></tr>


<tr>
<td>
    <b># Create Dynamic LACP in an Aggregated Interface</b><br />
    <b># Syntax</b><br />
    The bond is configured by default in IEEE 802.3ad link aggregation mode - LACP<br />
    <code>net add bond [bond-name] bond slaves [slaves]</code><br />
    <code>net pending</code><br /><br />

    <b># Example</b><br />
    <b># Command to create a bond called bond0 with 4 member link ports swp1, swp2, swp3, and swp4</b><br />
    <code>net add bond bond0 bond slaves swp1-4</code><br />
    <code>net pending</code><br />
    <code>net commit</code><br /><br />

    <b># Change LACP Mode to balance-xor</b><br />
    <code>net add bond bond1 bond mode balance-xor</code><br /><br />

    <b># Change LACP Mode to 802.3ad</b><br />
    <code>net add bond bond1 bond mode 802.3ad</code><br /><br />

    <b># Command to Verify LACP LAG Information</b><br />
    <code>net show interface bond1</code><br />
</td>

<td>
<b># Create Port Channel</b><br />
<b># Syntax</b><br />
<code>config portchannel add PortChannel&lt;Channel1&gt;</code><br /><br />

<b># Add Members to Port Channel</b><br />
<code>config portchannel add PortChannel&lt;Channel1&gt; Ethernet&lt;interface&gt;</code><br /><br />

<b># Command to Verify Port Channel Interface</b><br />
<code>show interface portchannel</code><br /><br />

<b># Command to Show VLAN Status</b><br />
<code>show vlan brief</code><br /><br />

<b># Command to Show IP Interface Status</b><br />
<code>show ip interfaces</code><br />
<code>show interfaces status</code><br /><br />

<b># Command to Create a PortChannel Interface and Set the Specific LACP Key</b><br />
<code>config portchannel add PortChannel&lt;Channel1&gt; --lacp-key &lt;Key-number&gt;</code><br />
<code>config portchannel member add PortChannel&lt;Channel1&gt; Ethernet&lt;interface&gt;</code><br /><br />

<b># Command to Create a PortChannel Interface in Fast Rate Mode</b><br />
<code>config portchannel add PortChannel&lt;number&gt; --fast-rate true</code><br /><br />

<b># Command to Create a PortChannel Interface in Static Mode</b><br />
<code>config portchannel add PortChannel&lt;interface&gt; --static true</code><br /><br />

<b># Command to Add Member Ports to PortChannel Interface</b><br />
<code>config portchannel member add PortChannel&lt;number&gt; Ethernet&lt;interface1&gt;</code><br />
<code>config portchannel member add PortChannel&lt;number&gt; Ethernet&lt;interface2&gt;</code><br /><br />

<b># Save the Setting to config_db.json</b><br />
<code>config save -y</code><br /><br />

<b># Add Member Ports to PortChannel Interface</b><br />
<code>config portchannel member add PortChannel&lt;interface&gt; Ethernet&lt;interface1&gt;</code><br />
<code>config portchannel member add PortChannel&lt;interface&gt; Ethernet&lt;interface2&gt;</code><br /><br />

<b># Command to Show Interface PortChannel</b><br />
<code>show interfaces portchannel</code><br />
</td>
</tr>
</table>


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

  th, [

  ]
</style>

<table>
<tr><th>CUMULUS</th><th>SONiC</th></tr>

<tr><th>FDB/MAC</th></tr>

<tr>
<td>
    <b># MAC Learning Configurations</b><br /><br />

    <b># Command to Show MAC Addresses of Bridge</b><br />
    <code>net show bridge macs</code><br /><br />

    <b># Command to Set MAC Aging Address</b><br />
    <code>net add bridge bridge ageing 600</code><br /><br />

    <b># Command to Show MAC Entries Learned and Filtered Based on Hostname, MAC Address, etc.</b><br />
    <!-- Add the relevant command here -->
</td>
<td>
    <b># Display the MAC (FDB) Entries</b><br />
    <code>show mac</code><br /><br />

    <b># Display the MACs Learned on a Particular VLAN ID</b><br />
    <code>show mac -v &lt;vlan_value&gt;</code><br /><br />

    <b># Display the MACs Learned on a Particular Port</b><br />
    <code>show mac -p Ethernet&lt;interface&gt;</code><br /><br />

    <b># Clear the MAC (FBD) Table</b><br />
    <code>sonic-clear FDB all</code>
</td>
</tr>

</table>

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
<tr><th>CUMULUS</th><th>SONiC</th></tr>

<tr>
<td>
    <b># Syntax for Displaying MAC Entries</b><br />
    <code>netq show macs &lt;mac&gt; [vlan &lt;1-4096&gt;] [origin] [around &lt;text-time&gt;] [json]</code><br /><br />

    <b># Syntax for Displaying MAC Entries on a Specific Host</b><br />
    <code>netq &lt;hostname&gt; show macs &lt;mac&gt; [vlan &lt;1-4096&gt;] [origin | count] [around &lt;text-time&gt;] [json]</code><br /><br />

    <b># Syntax for Displaying MAC Entries on a Specific Egress Port</b><br />
    <code>netq &lt;hostname&gt; show macs egress-port &lt;egress-port&gt; &lt;mac&gt; [vlan &lt;1-4096&gt;] [origin] [around &lt;text-time&gt;] [json]</code><br /><br />

    <b># Syntax for Displaying MAC History</b><br />
    <code>netq [&lt;hostname&gt;] show mac-history &lt;mac&gt; [vlan &lt;1-4096&gt;] [diff] [between &lt;text-time&gt; and &lt;text-endtime&gt;] [listby &lt;text-list-by&gt;] [json]</code><br /><br />

    <b># Syntax for Displaying MAC Commentary</b><br />
    <code>netq [&lt;hostname&gt;] show mac-commentary &lt;mac&gt; vlan &lt;1-4096&gt; [between &lt;text-time&gt; and &lt;text-endtime&gt;] [json]</code>
</td>
<td>
    <b># Check MAC Aging Time</b><br />
    <code>show mac aging-time</code>
</td>
</tr>
</table>


### <b>Multi-Chassis Link Aggregation Group (MC-LAG)</b>

This is a pair of links that terminates on two cooperating switches and appears as an ordinary link aggregation group (LAG). 


#### <b>Layer 2 Multi Chassis LAG</b>

![Layer2 MultiChasis LAG](../img/Image2CumulusMigration.png)

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
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td colspan='2'><b>PortChannel (LACP) and Member </b></td>
</tr>

<tr>
<td>
    <b># Enable LACP</b><br />
    <code>net add bond bond1 bond mode 802.3ad</code><br />
    <code>net add bond bond2 bond mode 802.3ad</code><br /><br />

    <b># Add Members</b><br />
    <code>net add bond bond1 bond slaves swp1-4</code><br />
    <code>net add bond bond2 bond slaves swp5-8</code>
</td>

<td>
    <b># Add Port Channel</b><br />
    <code>config port channel add &lt;PCH ID&gt;</code><br /><br />

    <b># Add Members</b><br />
    <code>config port channel member add &lt;PCH-ID&gt; &lt;member-port&gt;</code>
</td>
</tr>

<tr><td colspan='2'><b>MC-LAG</b></td></tr>

<tr>
<td>
    <b># Command to add unique MLAG ID (clag-id) to each bond.</b><br />
    <code>net add bond bond1 clag id 1</code><br />
    <code>net add bond bond2 clag id 2</code><br /><br />

    <b># Command to add the bonds to a bridge</b><br />
    <code>net add bridge bridge ports bond1,bond2</code><br /><br />

    <b># Command to set peer link IP address</b><br />
    <code>net add clag peer sys-mac &lt;MAC_ADDRESS_SYSTEM&gt; interface &lt;interface_name&gt;1-4 primary backup-ip &lt;IP_ADDRESS&gt;</code><br /><br />

    <b># Validate status of MC LAG config</b><br />
    <code>net show clag</code><br /><br />

    <b># Verify all MCLAG settings</b><br />
    <code>clagctl params</code><br /><br />

    <b># Monitor MCLAG services</b><br />
    <code>systemctl status clagd.service</code>
</td>
<td>
    <b># MCLAG Domain & Peer Configuration</b><br />
    <code>config interface ip add &lt;VLAN ID&gt; &lt;SVI-IP&gt;</code><br />
    <code>config mclag add &lt;mclag-id&gt; &lt;local-ip&gt; &lt;remote-ip&gt; &lt;peer-pch&gt;</code><br />
    <code>config mclag unique-ip add &lt;peer-vlan&gt;</code><br /><br />

    <b># MCLAG Members</b><br />
    <code>config mclag member add &lt;mclag-id&gt; &lt;member-pch&gt;</code><br /><br />

    <b># MCLAG Show</b><br />
    <code>show mclag brief</code><br />
    <code>Show mac</code>
</td>

</tr>

<tr><td colspan='2'><b>VLAN</b></td></tr>

<tr>
<td>
    <b># Add VLAN members to bridge</b><br />
    <code>net add bridge bridge ports &lt;INTERFACE_NAME&gt;1-2</code><br />
    <code>net add bridge bridge vids &lt;vlan-id1&gt;,&lt;vlan-id2&gt;</code><br />
</td>

<td>
    <b># VLAN Configuration</b><br />
    <code>config vlan add &lt;id&gt;</code><br />
    <code>config vlan member add &lt;vid&gt; &lt;pch-id&gt;</code>
</td>

</tr>
</table>


<b>SONiC Port Channel Configuration </b>
```yaml
# Creating port channel on the MCLAG pair switches running SONiC 
config portchannel add PortChannel01
config portchannel add PortChannel02
config portchannel add PortChannel03
config portchannel member add PortChannel01 Ethernet0
config portchannel member add PortChannel02 Ethernet1
config portchannel member add PortChannel03 Ethernet56
config portchannel member add PortChannel03 Ethernet60

# Creating VLAN interface on MC LAG pair switches running SONiC
config vlan add 10
config vlan add 100
config vlan member add 10 PortChannel03
config vlan member add -u 100 PortChannel01
config vlan member add 100 PortChannel02
config vlan member add 100 PortChannel03

#Configure MCLAG pair switches with domain ID and child member links
config mclag add 1 192.168.10.1 192.168.10.2 PortChannel03
config mclag unique-ip add Vlan10
config mclag member add 1 PortChannel01
config mclag member add 1 PortChannel02

#SONiC configuration for MC LAG peer health check 
config interface ip add Vlan10 192.168.10.1/24
config interface ip add Vlan10 192.168.10.2/24

#SONiC Command to Display MC LAG operationalstatus
 show mclag brief

# SONiC command to show MAC address learned for host traffic through member link interfaces 
show mac
No.    Vlan  MacAddress         Port           Type
-----  ------  -----------------  -------------  -------
    1      10  68:21:5F:29:C0:D2  PortChannel03  Static
    2     100  B8:6A:97:19:BA:12  PortChannel01  Dynamic
    3     100  80:A2:35:5A:22:50  PortChannel02  Dynamic
Total number of entries 3

```


#### Layer 3 Multi Chassis LAG 

![Layer3 MultiChasis LAG](../img/Layer3ImageCUMULUS.png)

```yaml
# Command to create PortChannel on MC LAG Pair switches 
config portchannel add PortChannel01
config portchannel add PortChannel02
config portchannel add PortChannel03
config portchannel member add PortChannel01 Ethernet0
config portchannel member add PortChannel02 Ethernet1
config portchannel member add PortChannel03 Ethernet56
config portchannel member add PortChannel03 Ethernet60

```

```yaml
# Commands to Create Port Channel IPs on MC LAG pair switches 
config interface ip add PortChannel01 192.168.11.1/24
config interface ip add PortChannel02 192.168.12.1/24
config interface ip add PortChannel03 192.168.10.1/24

config interface ip add PortChannel01 192.168.11.1/24
config interface ip add PortChannel02 192.168.12.1/24
config interface ip add PortChannel03 192.168.10.2/24

```

```yaml
# command to configure MCLAG on MC LAG pair switches  (Domain ID, VLANs and MLAG members)
config mclag add 1 192.168.10.2 192.168.10.1
config mclag member add 1 PortChannel01
config mclag member add 1 PortChannel02

config mclag add 1 192.168.10.1 192.168.10.2
config mclag member add 1 PortChannel01
config mclag member add 1 PortChannel02

```

```yaml
# SONiC command to Configure IP for MCLAG Peer health check on MC LAG peers
config interface ip add Vlan10 192.168.10.1/24
config interface ip add Vlan10 192.168.10.2/24
```


```yaml
# Command to show MCLAG Status
#MC1 switch configuration - 
show interfaces portchannel
Flags: A - active, I - inactive, Up - up, Dw - Down, N/A - not available,
       S - selected, D - deselected, * - not synced
  No.  Team Dev       Protocol     Ports                          Oper Key  Admin Key    Fast Rate
-----  -------------  -----------  ---------------------------  ----------  -----------  -----------
  01  PortChannel01  LACP(A)(Up)  Ethernet0(S)                       101  auto         false
  02  PortChannel02  LACP(A)(Up)  Ethernet1(S)                       102  auto         false
  03  PortChannel03  LACP(A)(Up)  Ethernet60(S) Ethernet56(S)        103  auto         false

show mclag brief  
       Domain ID                    : 1
        Role                         : Active
        Session Status               : Up
       Peer Link Status             :
        Source Address               : 192.168.10.1
        Peer Address                 : 192.168.10.2
        Peer Link                    :
       Keepalive Interval           : 1 secs
        Session Timeout              : 15 secs
        System MAC                   : 00:a0:c9:00:00:00
       Number of MCLAG Interfaces   : 2
        MCLAG Interface              Local/Remote Status
        PortChannel01                Up/Up
        PortChannel02                Up/Up


MC2 switch configuration - 

admin@sonic:~$ show interfaces portchannel
Flags: A - active, I - inactive, Up - up, Dw - Down, N/A - not available,
       S - selected, D - deselected, * - not synced
  No.  Team Dev       Protocol     Ports                          Oper Key  Admin Key    Fast Rate
-----  -------------  -----------  ---------------------------  ----------  -----------  -----------
  01  PortChannel01  LACP(A)(Up)  Ethernet0(S)                       101  auto         false
  02  PortChannel02  LACP(A)(Up)  Ethernet1(S)                       102  auto         false
  03  PortChannel03  LACP(A)(Up)  Ethernet60(S) Ethernet56(S)        103  auto         false
admin@sonic:~$ show mclag brief  
       Domain ID                    : 1
        Role                         : Standby
        Session Status               : Up
        Peer Link Status             :
        Source Address               : 192.168.10.2
        Peer Address                 : 192.168.10.1
        Peer Link                    :
        Keepalive Interval           : 1 secs
        Session Timeout              : 15 secs
        System MAC                   : 00:a0:c9:00:00:00
        Number of MCLAG Interfaces   : 2
        MCLAG Interface              Local/Remote Status
        PortChannel01                Up/Up
        PortChannel02                Up/Up

```


```yaml
SONiC Command to verify ARP synchronization
mclagdctl dump arp -i 1
No.   IP                  MAC                 DEV                 Flag
1     192.168.12.2        80:a2:35:5a:22:50   PortChannel02       R
2     192.168.11.2        b8:6a:97:19:ba:12   PortChannel01       L
```




<!-- #################################################### -->

### <b>Link Layer Discovery protocol</b>
LLDP is a standard link-layer discovery protocol which can broadcast its capability, IP address, ID, and interface name as TLVs (Type/Length/Value) in LLDP PDUs (Link Layer Discovery Protocol Data Units). 

![LLDP](../img/LLDP.png)

<table>
<tr>
<th>CUMULUS</th>
<th>SONiC</th>
</tr>

<tr>
<td>
<b># Command to Configure LLDP</b>
<br />
<code>sudo cat /etc/lldpd.conf</code>
<br />
<code>configure lldp tx-interval 40</code>
<br />
<code>configure lldp tx-hold 3</code>
<br />
<code>configure system interface pattern *,!eth0,swp*</code> <br />

<b># Command to Show All Neighbors on All Ports and Interfaces</b>
<br />
<code>sudo lldpcli show neighbors</code><br />

<b># Command to Show LLDP Statistics for All Ports</b>
<br />
<code>sudo lldpcli show statistics</code> <br />

<b># Command to Show LLDP Running Configuration</b>
<br />
<code>sudo lldpcli show running-configuration</code><br />
</td>

<td>
<b># Command to Enable / Disable LLDP globally</b>
<br />
<code>config feature state lldp enabled</code>
<br />
<code>config feature state lldp disabled</code> <br />

<b># Command to Configure LLDP information</b>
<br />
<code>config lldp global hello_timer &lt;timer_value&gt;</code>
<br />
<code>config lldp global management_ip &lt;switch_mgmt_ip&gt;</code>
<br />
<code>config lldp global system_description AS5835-Leaf1</code>
<br />
<code>config lldp global system_name &lt;LEAF1&gt;</code><br />

<b># Command to validate LLDP status</b>
<br />
<code>show feature status lldp</code>
<br />
<code>show lldp table</code>
<br />
<code>show lldp neighbors</code>
<br />
<code>show lldp global</code><br />

<b># Command to enable/disable LLDP over local interfaces</b>
<br />
<code>docker exec -i lldp lldpcli</code>
<br />
<code>configure ports Ethernet&lt;interface&gt; lldp status disable</code>
<br />
<code>configure ports Ethernet&lt;interface&gt; lldp status enable</code>< br />
</td>
</tr>
</table>

## <b>Layer 3 Routing</b>

### <b>Routed Interface</b>
<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
<b># Command to configure IP addresses for interface swp1</b>
<br />
<code>net add interface swp1 ip address &lt;IP_ADDRESS&gt;/&lt;SUBNET&gt;</code><br />

<b># Command to bring up an interface or apply changes to an existing interface</b>
<br />
<code>sudo ifup &lt;ifname&gt;</code><br />

<b># Command to bring down a single interface</b>
<br />
<code>sudo ifdown &lt;ifname&gt;</code><br />

<b># Checking the Configuration</b>
<br />
<code>net show interface &lt;INTERFACE_NAME&gt;</code>
<br />
<code>net show interface alias</code><br />

<b># Command to add a static route</b>
<br />
<code>net add routing route &lt;NETWORK_ROUTE&gt; &lt;NEXT_HOP&gt;</code><br />

<b># Command to delete a static route</b>
<br />
<code>net delete routing route &lt;NETWORK_ROUTE&gt;</code><br />

<b># Command to verify static routes</b>
<br />
<code>net show route static</code><br />
</td>

<td>
<b># Command to add a Layer 3 Interface address on a physical interface</b>
<br />
<code>config interface ip add Ethernet&lt;Number1&gt; &lt;IP_ADDRESS></code>
<br />
<code>config interface ip add &lt;vlan_number> &lt;IP_ADDRESS></code><br />

<b># Example</b>
<br />
<code>config interface ip add Loopback&lt;Number&gt; 10.0.2.1/32</code>
<br />
<code>config interface ip add Ethernet0 172.16.10.1/31</code>
<br />
<code>config interface ip add Vlan100 18.0.0.1/24</code><br />

<b># Command to create a sub-interface</b>
<br />
<code>config interface ip add Ethernet&lt;interface_number&gt;.&lt;vlan-id> &lt;IP_ADDRESS></code><br />

<b># Example</b>
<br />
<code>config interface ip add Ethernet0.10 192.168.10.2/24</code><br />

<b># Validate sub-interface operational status</b>
<br />
<code>show subinterfaces status</code><br />

<b># Command to add static routes</b>
<br />
<code>ip route &lt;Network_IP_ADDRESS> &lt;SUBNET_MASK> &lt;NEXTHOP></code><br />

<b># Command to delete a static route</b>
<br />
<code>no ip route &lt;Network_IP_ADDRESS> &lt;SUBNET_MASK></code><br />

<b># Command to verify static routes</b>
<br />
<code>show ip route</code><br />
</td>
</table>

### <b>SVI & DHCP Relay</b>

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>


<tr>
<td colspan='2'>SVI</td>
</tr>

<tr>
<td>
    <b># Create VLAN ID</b>
    <br />
    <code>net add bridge bridge ports &lt;interface_name&gt;1-2</code>
    <br />
    <code>net add bridge bridge vids &lt;vlan-id1&gt;,&lt;vlan-id2&gt;</code>
    <br /><br />

    <b># Create an interface binded to Layer3 VLAN</b>
    <br />
    <code>net add vlan &lt;VLAN-ID> vrf &lt;VRF_NAME></code>
    <br /><br />

    <b># Commands configure an SVI using swp1, swp2 ports and VLAN ID</b>
    <br />
    <code>net add bridge bridge ports&lt;interface_name&gt;1-2</code>
    <br />
    <code>net add vlan &lt;VLAN-ID> ip address &lt;IP_ADDRESS>/&lt;SUBNET></code>
    <br /><br />

    <b># Command to Bring up and Bring down Layer 3 interface</b>
    <br />
    <code>net add interface swp1 link down</code>
    <br />
    <code>net del interface swp1 link down</code>
    <br /><br />

    <b># Verify Layer3 interface</b>
    <br />
    <code>net show interface swp1</code>
    <br /><br />

    <b># Verify IP routes</b>
    <br />
    <code>ip route show</code>
</td>
<td>
    <b># Create VLANs</b>
    <br />
    <code>config vlan add &lt;vlan_value1></code>
    <br />
    <code>config vlan add &lt;vlan_value2></code>
    <br /><br />

    <b># Show VLAN configuration</b>
    <br />
    <code>show vlan config</code>
    <br /><br />

    <b># Add Interface to VLAN in Tagged (Trunk) mode:</b>
    <br />
    <code>config vlan member add &lt;vlan_value1> Ethernet&lt;interface1></code>
    <br />
    <code>config vlan member add &lt;vlan_value2> Ethernet&lt;interface2></code>
    <br /><br />

    <b># Inter-VLAN routing</b>
    <br />
    <b># Configure IP addresses on VLAN1 and VLAN2</b>
    <br />
    <code>config interface ip add Vlan<number1> &lt;IP_ADDRESS1></code>
    <br />
    <code>config interface ip add Vlan<number2> &lt;IP_ADDRESS2></code>
    <br /><br />

    <b># Example</b>
    <br />
    <code>config interface ip add Vlan1 192.168.1.2/24</code>
    <br />
    <code>config interface ip add Vlan2 192.168.2.1/24</code>
    <br /><br />

    <b># Validate IP Interface</b>
    <br />
    <code>show ip interface</code>
    <br /><br />

    <b># Verify the Subinterface and VLAN status</b>
    <br />
    <code>show vlan brief</code>
</td>
</tr>

<tr>
<td colspan='2'><b>DHCP Relay</b></td>
</tr>

<tr>
<td>
    <b># DHCP Relay Command</b>
    <br /><br />
    <b># Command to set DHCP server IP address, layer 3 VLAN, and relay interfaces</b>
    <br />
    <code>net add dhcp relay interface &lt;relay_interface1></code>
    <br />
    <code>net add dhcp relay interface &lt;relay_interface2></code>
    <br />
    <code>net add dhcp relay interface vlan&lt;VLAN-ID></code>
    <br />
    <code>net add dhcp relay server &lt;SERVER_IP></code>
    <br />
    <code>net pending</code>
    <br />
    <code>net commit</code>
    <br /><br />

    <b># Configure the IP address of the DHCP relay agent</b>
    <br />
    <code>net add dhcp relay giaddr-interface &lt;AGENT_INTERFACE></code>
    <br /><br />

    <b># Command to allocate IP to relay Agent</b>
    <br />
    <code>net add dhcp relay giaddr-interface &lt;interface_name> &lt;IP_ADDRESS></code>
</td>
<td>
    <b># SONiC Command to enable DHCP relay</b>
    <br />
    <code>config feature state dhcp_relay enabled</code>
    <br /><br />

    <b># Enable DHCP relay on VLAN number</b>
    <br />
    <code>config vlan dhcp_relay add &lt;vlan_number> &lt;IP_ADDRESS></code>
    <br /><br />

    <b># Enable DHCP relay on Loopback interface</b>
    <br />
    <code>config vlan dhcp_relay src_intf add &lt;vlan_number> Loopback0</code>
    <br /><br />

    <b># Example</b>
    <br />
    <code>config vlan dhcp_relay add 10 192.168.20.100</code>
    <br />
    <code>config vlan dhcp_relay src_intf add 10 Loopback0</code>
</td>

</tr>
</table>


### <b>BGP Routing</b>

![BGP Routing](../img/BGP_ROUTING.png)

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Command to configure BGP routing</b>
    <br /><br />
    <b># Command to set BGP node by assigning an ASN</b>
    <br />
    <code>net add bgp autonomous-system &lt;ASN_NUMBER></code>
    <br /><br />

    <b># Command to set auto BGP to assign an ASN automatically</b>
    <br />
    <code>net add bgp auto leaf</code>
    <br /><br />

    <b># Command to assign Router-ID</b>
    <br />
    <code>net add bgp router-id &lt;SYSTEM_LOOPBACK_IP></code>
    <br /><br />

    <b># Command to specify BGP neighbor</b>
    <br />
    <code>net add bgp neighbor &lt;NEIGHBOR_IP_ADDRESS> remote-as external</code>
    <br /><br />

    <b># Command to advertise specifics using network</b>
    <br />
    <code>net add bgp ipv4 unicast network &lt;LOOPBACK_IP></code>
    <br />
    <code>net add bgp ipv4 unicast network &lt;NETWORK_IP_ADDRESS></code>
    <br /><br />

    <b># Example</b>
    <br />
    <code>net add bgp autonomous-system 65101</code>
    <br />
    <code>net add bgp router-id 10.10.10.1</code>
    <br />
    <code>net add bgp neighbor 10.0.1.0 remote-as external</code>
    <br />
    <code>net add bgp ipv4 unicast network 10.10.10.1/32</code>
    <br />
    <code>net add bgp ipv4 unicast network 10.1.10.0/24</code>
    <br /><br />

    <b># Command to show BGP routes summary</b>
    <br /><br />
    <b># Syntax</b>
    <br />
    <code>net show bgp summary</code>
    <br />
    <code>net show bgp ipv4 unicast summary</code>
    <br />
    <code>net show bgp ipv4 unicast</code>
    <br />
    <code>net show bgp ipv4 unicast &lt;network_address></code>
    <br />
    <code>net show bgp neighbor &lt;interface_name></code>
</td>
<td>
    <b># vtysh Sonic command to configure BGP routing</b>
    <br />
    <code>router bgp &lt;ASN_NUMBER></code>
    <br />
    <code>bgp router-id &lt;System_loopback_IP></code>
    <br />
    <code>no bgp ebgp-requires-policy</code>
    <br />
    <code>bgp bestpath as-path multipath-relax</code>
    <br />
    <code>neighbor FABRIC peer-group</code>
    <br />
    <code>neighbor FABRIC capability extended-nexthop</code>
    <br />
    <code>neighbor &lt;Neighbor_IP> remote-as &lt;REMOTE_ASN_NUMBER></code>
    <br />
    <code>neighbor &lt;Neighbor_IP> peer-group FABRIC</code>
    <br /><br />

    <b># Example BGP routing configuration</b>
    <br />
    <code>router bgp 65001</code>
    <br />
    <code>bgp router-id 10.0.2.1</code>
    <br />
    <code>no bgp ebgp-requires-policy</code>
    <br />
    <code>bgp bestpath as-path multipath-relax</code>
    <br />
    <code>neighbor FABRIC peer-group</code>
    <br />
    <code>neighbor FABRIC capability extended-nexthop</code>
    <br />
    <code>neighbor 172.16.10.0 remote-as 2001</code>
    <br />
    <code>neighbor 172.16.10.0 peer-group FABRIC</code>
    <br />
    <code>neighbor 172.16.10.8 remote-as 2002</code>
    <br />
    <code>neighbor 172.16.10.8 peer-group FABRIC</code>
    <br />
    <code>neighbor 192.168.3.1 remote-as 2003</code>
    <br />
    <code>neighbor 192.168.3.1 peer-group FABRIC</code>
    <br /><br />

    <b># Command to show BGP routes summary</b>
    <br />
    <code>show ip bgp summary</code>
    <br />
    <code>show ip bgp neighbors</code>
    <br />
    <code>show ip bgp network</code>
    <br />
    <code>show ipv6 bgp summary</code>
    <br />
    <code>show ipv6 bgp neighbors</code>
    <br />
    <code>show ipv6 bgp network</code>
</td>

</tr>

</table>


### <b>OSPF Routing</b>

![OSPF Routing](../img/OSPF_ROUTING.png)

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td><b>OSPF Routing</b></td>
</tr>

<tr>
<td>
    <b># Configure OSPF routing</b>
    <br /><br />
    <b># Configure the unnumbered interface</b>
    <br />
    <code>net add loopback lo ip address &lt;system_loopback_ip></code>
    <br />
    <code>net add interface &lt;interface_number> ip address &lt;ip_address></code>
    <br />
    <code>net add ospf router-id &lt;system_loopback_ip></code>
    <br />
    <code>net add ospf network &lt;network_address> area &lt;AREA_NUMBER></code>
    <br />
    <code>net add ospf passive-interface &lt;interface_name1></code>
    <br />
    <code>net add ospf passive-interface &lt;interface_name2></code>
    <br /><br />

    <b># Command to configure OSPF passive interface</b>
    <br />
    <code>net add ospf passive-interface default</code>
    <br />
    <code>net del ospf passive-interface &lt;interface_name></code>
    <br /><br />

    <b># Configure to set network type to point-to-point</b>
    <br />
    <code>net add interface &lt;interface_name> ospf network point-to-point</code>
    <br />
    <code>net add interface &lt;interface_name> ospf hello-interval &lt;hello-interval-time-secs></code>
    <br />
    <code>net add interface &lt;interface_name> ospf dead-interval &lt;dead-interval-time-secs></code>
    <br /><br />

    <b># Configure OSPF interface with priority</b>
    <br />
    <code>net add interface &lt;interface_name> ospf priority &lt;priority_number></code>
    <br />
    <code>net add interface &lt;interface_name> ospf message-digest-key 1 md5 &lt;KEY_VALUE></code>
    <br />
    <code>net add interface &lt;interface_name> ospf authentication message-digest</code>
    <br /><br />

    <b># Command to create a summary route for all the routes in a network address range in a specific area &lt;Area_number></b>
    <br />
    <code>sudo vtysh</code>
    <br />
    <code>router ospf</code>
    <br />
    <code>area &lt;area_number> range &lt;network_address></code>
    <br /><br />

    <b># Command to verify OSPF neighbor</b>
    <br />
    <code>net show ospf neighbor</code>
    <br />
    <code>net show route ospf</code>
    <br /><br />

    <b># Example Configuration - OSPF Routing</b>
    <br />
    <code>net add loopback lo ip address 10.10.10.1/32</code>
    <br />
    <code>net add interface &lt;interface_name> ip address &lt;address_ip></code>
    <br />
    <code>net add ospf router-id 10.10.10.1</code>
    <br />
    <code>net add ospf network 10.10.10.1/32 area 0</code>
    <br />
    <code>net add ospf network 10.0.1.0/31 area 0</code>
    <br />
    <code>net add ospf passive-interface swp1</code>
    <br />
    <code>net add ospf passive-interface swp2</code>
    <br /><br />

    <b># Configure the unnumbered interface</b>
    <br />
    <code>net add loopback lo ip address 10.10.10.1/32</code>
    <br />
    <code>net add interface swp51 ip address 10.10.10.1/32</code>
</td>

<td>
    <b># Configure OSPF routing</b>
    <br /><br />
    <b># Syntax</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>ospf router-id &lt;router-id></code>
    <br />
    <code>network &lt;Network_address> area &lt;Area_number></code>
    <br />
    <code>network &lt;Network_address1> area &lt;Area_number1></code>
    <br />
    <code>network &lt;Network_address2> area &lt;Area_number2></code>
    <br /><br />

    <b># Command to set OSPF time intervals</b>
    <br />
    <code>interface Ethernet&lt;interface></code>
    <br />
    <code>ip ospf hello-interval &lt;hello-interval-time-secs></code>
    <br />
    <code>ip ospf dead-interval &lt;dead-interval-time-secs></code>
    <br />
    <code>router ospf</code>
    <br />
    <code>area &lt;aread_number> authentication</code>
    <br /><br />

    <b># Command to set OSPF authentication key</b>
    <br />
    <code>interface Ethernet&lt;interface></code>
    <br />
    <code>ip ospf authentication</code>
    <br />
    <code>ip ospf authentication-key &lt;key></code>
    <br /><br />

    <b># Command to set OSPF MD5 Authentication</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>area 0 authentication message-digest</code>
    <br />
    <code>interface Ethernet&lt;interface></code>
    <br />
    <code>ip ospf message-digest-key &lt;key> md5 &lt;key></code>
    <br /><br />

    <b># Command to configure OSPF Virtual links</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>area &lt;area_number> virtual-link &lt;System_loopback></code>
    <br /><br />

    <b># Command to verify OSPF IP routes learned</b>
    <br />
    <code>show ip route</code>
    <br /><br />

    <b># Configuration OSPF Routing - Example</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>ospf router-id 1.1.1.1</code>
    <br />
    <code>network 10.0.0.0/31 area 0</code>
    <br />
    <code>network 192.168.10.0/24 area 0</code>
    <br />
    <code>network 192.168.20.0/24 area 0</code>
    <br />
    <code>network 192.168.30.0/24 area 0</code>
    <br /><br />

    <b># Enable OSPF hello timers under the interface - Example</b>
    <br />
    <code>interface Ethernet56</code>
    <br />
    <code>ip ospf hello-interval 20</code>
    <br />
    <code>ip ospf dead-interval 20</code>
    <br /><br />

    <b># Enable OSPF Authentication globally - Example</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>area 0 authentication</code>
    <br /><br />

    <b># Enable OSPF Authentication over the interface - Example</b>
    <br />
    <code>interface Ethernet56</code>
    <br />
    <code>ip ospf authentication</code>
    <br />
    <code>ip ospf authentication-key 123</code>
    <br /><br />

    <b># Enable OSPF MD5 Key - Example</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>area 0 authentication message-digest</code>
    <br />
    <code>interface Ethernet56</code>
    <br />
    <code>ip ospf message-digest-key 1 md5 123</code>
    <br /><br />

    <b># Verify IP routing Table - Example</b>
    <br />
    <code>show ip route</code>
    <br /><br />

    <b># Configure OSPF virtual links - Example</b>
    <br />
    <code>router ospf</code>
    <br />
    <code>area 1 virtual-link 3.3.3.3</code>
    <br />
    <code>router ospf</code>
    <br />
    <code>area 1 virtual-link 2.2.2.2</code>
</td>

</tr>
</table>

![OSPF Routing Image 2](../img/OSPF_IMAGE2.png)

```yaml
#AS7326-56X-OS1 Configuration

# VLAN and IP Configuration
config interface ip add Loopback0 1.1.1.1/32
config vlan member add 10 Ethernet0
config vlan member add 20 Ethernet0
config vlan member add 30 Ethernet0
config interface ip add Ethernet0.10 192.168.10.1/24
config interface ip add Ethernet0.20 192.168.20.1/24
config interface ip add Ethernet0.30 192.168.30.1/24
config interface ip add Ethernet56 10.0.0.0/31

#OSPF Configuration
admin@sonic:~$ vtysh
sonic(config)# router ospf
sonic(config-router)# network 10.0.0.0/31 area 0
sonic(config-router)# network 192.168.10.0/24 area 0
sonic(config-router)# network 192.168.20.0/24 area 0
sonic(config-router)# network 192.168.30.0/24 area 0

#OSPF Routing Verification Command
sonic# show ip ospf neighbor
Neighbor ID     Pri State           Dead Time Address         Interface            RXmtL RqstL DBsmL
192.168.25.1      1 Full/DR           31.440s 10.0.0.1        Ethernet56:10.0.0.0      0     0     0

sonic# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:07:45
C>* 1.1.1.1/32 is directly connected, Loopback0, 00:07:25
O   10.0.0.0/31 [110/10] is directly connected, Ethernet56, 00:06:42
C>* 10.0.0.0/31 is directly connected, Ethernet56, 00:07:25
C>* 188.188.0.0/16 is directly connected, eth0, 00:07:46
O>* 192.168.5.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32
O   192.168.10.0/24 [110/10] is directly connected, Vlan10, 00:04:54
C>* 192.168.10.0/24 is directly connected, Vlan10, 00:07:24
O>* 192.168.15.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32
O   192.168.20.0/24 [110/10] is directly connected, Vlan20, 00:04:50
C>* 192.168.20.0/24 is directly connected, Vlan20, 00:07:24
O>* 192.168.25.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32
O   192.168.30.0/24 [110/10] is directly connected, Vlan30, 00:04:47
C>* 192.168.30.0/24 is directly connected, Vlan30, 00:07:24

#AS7326-56X-OS2 Configuration
# VLAN and IP Configuration
config interface ip add Loopback0 2.2.2.2/32
config vlan member add 5 Ethernet0
config vlan member add 15 Ethernet0
config vlan member add 25 Ethernet0
config interface ip add Ethernet0.5 192.168.51/24
config interface ip add Ethernet0.15 192.168.15.1/24
config interface ip add Ethernet0.25 192.168.25.1/24
config interface ip add Ethernet56 10.0.0.1/31

#OSPF Configuration
admin@sonic:~$ vtysh
sonic(config)# router ospf
sonic(config-router)# network 10.0.0.0/31 area 0
sonic(config-router)# network 192.168.5.0/24 area 0
sonic(config-router)# network 192.168.15.0/24 area 0
sonic(config-router)# network 192.168.25.0/24 area 0

#OSPF Routing Verification Command
OS2:
sonic# show ip ospf neighbor
Neighbor ID     Pri State           Dead Time Address         Interface            RXmtL RqstL DBsmL
188.188.98.39     1 Full/Backup       33.721s 10.0.0.0        Ethernet56:10.0.0.1      0     0     0

sonic# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 02:15:38
C>* 2.2.2.2/32 is directly connected, Loopback0, 02:15:18
O   10.0.0.0/31 [110/10] is directly connected, Ethernet56, 00:08:47
C>* 10.0.0.0/31 is directly connected, Ethernet56, 00:08:47
C>* 188.188.0.0/16 is directly connected, eth0, 02:15:39
O   192.168.5.0/24 [110/10] is directly connected, Vlan5, 00:35:34
C>* 192.168.5.0/24 is directly connected, Vlan5, 00:35:34
O>* 192.168.10.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:14
O   192.168.15.0/24 [110/10] is directly connected, Vlan15, 00:35:34
C>* 192.168.15.0/24 is directly connected, Vlan15, 00:35:34
O>* 192.168.20.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:10
O   192.168.25.0/24 [110/10] is directly connected, Vlan25, 00:35:34
C>* 192.168.25.0/24 is directly connected, Vlan25, 00:35:34
O>* 192.168.30.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:07

```


### <b>VRF Routing</b>

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Command to configure VRRP</b>
    <br />
    <code>set ip routing enable true</code>
    <br />
    <code>set ip vrf &lt;VRF-ID&gt; description “Description_value”</code>
    <br /><br />
    
    <b># Command to bind the Layer 3 VLAN interface to the VRF.</b>
    <br />
    <code>set vlan-interface interface vlan&lt;vlan-id&gt; vrf &lt;VRF-ID&gt;</code>
    <br /><br />
    
    <b># Command to add a static route entry into the VRF.</b>
    <br />
    <code>set protocols static vrf &lt;VRF-ID&gt;  route &lt;IPV4_address&gt;  next-hop &lt;IPV4_address&gt;</code>
    <br />
    <code>set protocols static vrf &lt;VRF-ID&gt;  route &lt;IPV6_address&gt;  next-hop &lt;IPV6_address&gt;</code>
    <br /><br />
    
    <b># Command to validate and show VRF instances created</b>
    <br />
    <code>run show vrf</code>

</td>
<td>
    <b># SONiC command to create a VRF</b>
    <br />
    <code>config vrf add</code>
    <br />
    <code>config vrf add &lt;vrf-name&gt;</code>
    <br />
    <code>config vrf del &lt;vrf-name&gt;</code>
    <br />
    <code>config vrf add_vrf_vni_map &lt;vrf-name&gt; &lt;vni&gt;</code>
    <br /><br />
    
    <b># Command to bind Layer 3 VLAN interface to the VRF</b>
    <br />
    <code>config vrf add &lt;VRF-ID&gt;</code>
    <br />
    <code>config vxlan add vtep &lt;VTEP_ENDPOINT_IP&gt;</code>
    <br />
    <code>config vxlan evpn_nvo add evpnnvo vtep</code>
    <br />
    <code>config vrf add_vrf_vni_map &lt;VRF-ID&gt; &lt;VNI_VALUE&gt;</code>
    <br /><br />
    
    <b># Command to unbind the Layer 3 VLAN interface from the VRF</b>
    <br />
    <code>config vrf del_vrf_vni_map &lt;vrf-name&gt;</code>
    <br /><br />
    
    <b># Command to configure a static route entry into the VRF</b>
    <br />
    <code>ip route &lt;A.B.C.D/M&gt; &lt;A.B.C.D&gt; nexthop-vrf &lt;vrf-name&gt;</code>
    <br /><br />
    
    <b># Command to import VRF table into the default routing table</b>
    <br />
    <code>import vrf default</code>
    <br /><br />
    
    <b># Command to add BGP routing entry with VRF and import route leaking policy into VRF routing table</b>
    <br />
    <code>router bgp &lt;AS_NUMBER&gt; vrf &lt;VRF-ID></code>
    <br />
    <code>address-family ipv4 unicast</code>
    <br />
    <code>router bgp &lt;AS_NUMBER> vrf &lt;VRF-ID></code>
    <br />
    <code>address-family ipv4 unicast</code>
</td>
</tr>
</table>

<!-- ###################################################### -->

<b>SONIC - VRF Routing</b>

```yaml
# Create VRF instance
admin@sonic:~$ config vrf add Vrf_01
# Binding the Ethernet0 to VRF instance.
admin@sonic:~$ config interface vrf bind Ethernet0 Vrf_01
# Checking the VRF
admin@sonic:~$ show vrf
VRF 	Interfaces
------  ------------
Vrf_01  Ethernet0
admin@sonic:~$ show ip interfaces
Interface	Master	IPv4 address/mask	Admin/Oper	BGP Neighbor	Neighbor IP
-----------  --------  -------------------  ------------  --------------  -------------
Ethernet0	Vrf_01	192.168.1.1/24   	up/up   	N/A         	N/A
Loopback0          	10.1.0.1/32      	up/up     	N/A         	N/A
docker0     	       240.127.1.1/24   	up/down   	N/A         	N/A
eth0               	188.188.97.31/16 	up/up     	N/A         	N/A
lo                 	127.0.0.1/8      	up/up     	N/A         	N/A
# Checking the routing table.
admin@sonic:~$ show ip route vrf Vrf_01
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
VRF Vrf_01:
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:02:37
admin@sonic:~$ show ip route vrf all
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
VRF Vrf_01:
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:00:31
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:15:16
C>* 10.1.0.1/32 is directly connected, Loopback0, 00:15:16
C>* 188.188.0.0/16 is directly connected, eth0, 00:15:16

# Management VRF
# Create Management VRF
admin@sonic:~$ config vrf add mgmt
# Checking the Management VRF
admin@sonic:~$ show mgmt-vrf
ManagementVRF : Enabled
Management VRF interfaces in Linux:
128: mgmt: <NOARP,MASTER,UP,LOWER_UP> mtu 65536 qdisc noqueue state UP mode DEFAULT group default qlen 1000
	link/ether 52:2f:cc:b8:28:b5 brd ff:ff:ff:ff:ff:ff promiscuity 0 minmtu 68 maxmtu 1500
	vrf table 5000 addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master mgmt state UP mode DEFAULT group default qlen 1000
	link/ether 80:a2:35:4f:4f:40 brd ff:ff:ff:ff:ff:ff
129: lo-m: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master mgmt state UNKNOWN mode DEFAULT group default qlen 1000
	link/ether 0a:25:2e:1f:32:90 brd ff:ff:ff:ff:ff:ff
admin@sonic:~$ show ip interfaces
Interface	Master	IPv4 address/mask	Admin/Oper	BGP Neighbor	Neighbor IP
-----------  --------  -------------------  ------------  --------------  -------------
Ethernet0	Vrf_01	192.168.1.1/24   	up/up     	N/A         	N/A
Loopback0          	10.1.0.1/32      	up/up     	N/A         	N/A
docker0            	240.127.1.1/24   	up/down   	N/A         	N/A
eth0     	mgmt  	188.188.97.31/16 	up/up     	N/A         	N/A
lo                 	127.0.0.1/8      	up/up     	N/A         	N/A
lo-m     	mgmt  	127.0.0.1/8      	up/up     	N/A     	    N/A
#Checking the routing table.
admin@sonic:~$ show ip route vrf mgmt
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
VRF mgmt:
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:12:12
C>* 188.188.0.0/16 is directly connected, eth0, 00:12:12
admin@sonic:~$ show ip route vrf all
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
VRF Vrf_01:
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:01:04
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
C>* 10.1.0.1/32 is directly connected, Loopback0, 00:01:05
Codes: K - kernel route, C - connected, S - static, R - RIP,
   	O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
   	T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
   	F - PBR, f - OpenFabric,
   	> - selected route, * - FIB route, q - queued route, r - rejected route
VRF mgmt:
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:01:21
C>* 188.188.0.0/16 is directly connected, eth0, 00:01:21
```

### <b>L2-VXLAN Asymmetric IRB Configuration</b>

![L2-VXLAN Asymmetric IRB Configuration](../img/L2VXLAN.png)

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Configure VLAN ID, L3 VLAN interfaces, loopback interfaces, and IP addressing.</b><br /><br />

    <b># Syntax</b><br />
    <code>net add vlan &lt;VLAN-ID&gt; vrf &lt;VRF_NAME&gt;</code><br /><br />

    <b># Command to create two unique VXLAN devices-</b><br />
    <code>net add interface &lt;interface_name1&gt; bridge access &lt;vlan1&gt;</code><br />
    <code>net add interface &lt;interface_name2&gt; bridge access &lt;vlan2&gt;</code><br />
    <code>net add vxlan vni&lt;number1&gt; vxlan id &lt;vlan1&gt;</code><br />
    <code>net add vxlan vni&lt;number2&gt; vxlan id &lt;vlan2&gt;</code><br /><br />

    <b># Configure VXLAN VNI and map VNI IDs to VLAN IDs.</b><br />
    <code>net add bridge bridge ports  vni&lt;number1&gt;,vni&lt;number2&gt;</code><br />
    <code>net add bridge bridge vids &lt;vlan1&gt;,&lt;vlan2&gt;</code><br />
    <code>net add vxlan vni&lt;number1&gt; bridge access &lt;vlan1&gt;</code><br />
    <code>net add vxlan vni&lt;number2&gt; bridge access &lt;vlan2&gt;</code><br /><br />

    <b># Command to configure VXLAN tunnels with local and remote VTEP tunnel IP</b><br />
    <code>net add loopback lo vxlan local-tunnelip &lt;local_ip&gt;</code><br />
    <code>net add vxlan vni-&lt;vni_value&gt;  vxlan remoteip &lt;remote_ip&gt;</code><br /><br />

    <b># Configure and advertise BGP L2 EVPN Routes</b><br />
    <code>net add bgp autonomous-system &lt;ASN_NUMBER&gt;</code><br />
    <code>net add bgp l2vpn evpn neighbor &lt;NEIGHBOR_IP&gt; remote-as internal</code><br />
    <code>net add bgp l2vpn evpn neighbor &lt;NEIGHBOR_IP&gt;  activate</code><br />
    <code>net add bgp l2vpn evpn advertise-all-vni</code><br /><br />

    <b># Command to show VXLAN traffic stats</b><br />
    <code>net show bgp l2vpn evpn summary</code><br />
    <code>net show bgp l2vpn evpn vni</code><br />
    <code>net show evpn vni</code><br />
    <code>net show evpn mac vni &lt;VNI_VALUE&gt;</code><br />
    <code>net show evpn mac vni all</code><br />
    <code>net show evpn next-hops vni all</code><br />
    <code>nv show nve vxlan</code><br />
</td>
<td>
    <b># Configure LoopBack, VLAN IDs, and IP addressing</b><br /><br />

    <b># Syntax</b><br />
    <code>config vlan add &lt;VLAN-ID&gt;</code><br />
    <code>config vlan member add &lt;VLAN-ID&gt; Ethernet&lt;interface1&gt;</code><br />
    <code>config interface ip add Loopback0 &lt;SYSTEM_LOOPBACK&gt;</code><br /><br />

    <b># Configure BGP routing</b><br />
    <code>router bgp &lt;LOCAL_AS_NUMBER&gt;</code><br />
    <code>bgp router-id &lt;SYSTEM_LOOPBACK&gt;</code><br />
    <code>neighbor &lt;ebgp_neighbor_ip> remote-as &lt;REMOTE_AS_NUMBER&gt;</code><br />
    <code>address-family ipv4</code><br />
    <code>network &lt;Network_prefix_advertised&gt;</code><br /><br />

    <b># Configure VXLAN VNI and map VNI IDs to VLAN IDs</b><br />
    <code>config vxlan add vtep &lt;SOURCE_VTEP_IP&gt;</code><br />
    <code>config vxlan evpn_nvo add nvo vtep</code><br />
    <code>config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE&gt;</code><br />
    <code>config vxlan add vtep &lt;DEST_VTEP_IP&gt;</code><br />
    <code>config vxlan evpn_nvo add nvo vtep</code><br />
    <code>config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE&gt;</code><br /><br />

    <b># Configure and advertise BGP L2 EVPN Routes</b><br />
    <code>router bgp &lt;LOCAL_AS_NUMBER&gt;</code><br />
    <code>address-family l2vpn evpn</code><br />
    <code>neighbor &lt;ebgp_neighbor_ip> activate</code><br />
    <code>Advertise-all-vni</code><br /><br />

    <b># Show VXLAN tunnels, interfaces, and EVPN route details</b><br />
    <code>show ip route</code><br />
    <code>show vxlan interface</code><br />
    <code>show vxlan vlanvnimap</code><br />
    <code>show vxlan tunnel</code><br />
    <code>show vxlan remotevtep</code><br />
    <code>show evpn vni detail</code><br />
</td>
</tr>
</table>

![L2-VXLAN EVPN topology between edge core SONiC switches](../img/L2VXLANIMG2.png)

<b>Sample SONiC- L2VXLAN EVPN Asymmetric IRB </b>

```yaml
Step 1: Configure IP address to Loopback0 of both switches.
AS7326-56X
admin@AS7326-56X:~$ config interface ip remove Loopback0 10.1.0.1/32   
admin@AS7326-56X:~$ config interface ip add Loopback0 1.1.1.1/32

AS5835-54X:
admin@AS5835-54X:~$ config interface ip remove Loopback0 10.1.0.1/32   
admin@AS5835-54X:~$ config interface ip add Loopback0 2.2.2.2/32

Step 2: Establish BGP Session between Ethernet52 and announce the network.
AS7326-56X:
admin@AS7326-56X:~$ vtysh
Hello, this is FRRouting (version 7.2.1-sonic).
Copyright 1996-2005 Kunihiro Ishiguro, et al.
AS7326-56X# configure terminal
AS7326-56X(config)# router bgp 65100
AS7326-56X(config-router)# bgp router-id 1.1.1.1
AS7326-56X(config-router)# neighbor 10.0.0.1 remote-as 65100
AS7326-56X(config-router)# address-family ipv4
AS7326-56X(config-router-af)# network 1.1.1.1/32
AS7326-56X(config-router-af)# end
AS7326-56X# exit
AS5835-54X:
admin@AS5835-54X:~$ vtysh
Hello, this is FRRouting (version 7.2.1-sonic).
Copyright 1996-2005 Kunihiro Ishiguro, et al.
AS5835-54X# configure terminal
AS5835-54X(config)# router bgp 65100
AS5835-54X(config-router)# bgp router-id 2.2.2.2
AS5835-54X(config-router)# neighbor 10.0.0.0 remote-as 65100
AS5835-54X(config-router)# address-family ipv4
AS5835-54X(config-router-af)# network 2.2.2.2/32
AS5835-54X(config-router-af)# end
AS5835-54X# exit

Step 3. Create Vxlan
AS7326-56X:
admin@AS7326-56X:~$ config vxlan add vtep 1.1.1.1
admin@AS7326-56X:~$ config vxlan evpn_nvo add nvo vtep
admin@AS7326-56X:~$ config vxlan map add vtep 30 3000
AS5835-54X:
admin@AS5835-54X:~$ config vxlan add vtep 2.2.2.2
admin@AS5835-54X:~$ config vxlan evpn_nvo add nvo vtep
admin@AS5835-54X:~$ config vxlan map add vtep 30 3000
Note :
VNI (VxLAN Network Identifier) : virtual extension of VLAN over IP network.
VTEP (VXLAN Tunnel End Point) : an entity that originates and/or terminates VXLAN tunnels which is specified by a source IP address.
Only one VTEP is allowed on one device. Please use loopback IP address for VTEP's IP address.
NVO (Network Virtualization Overlay)
Only one NVO is allowed on one device.
VNI (VxLAN Network Identifier) : virtual extension of VLAN over IP network.

Step 4: Advertise  L2VPN EVPN routes. 
AS7326-56X:
admin@AS7326-56X:~$ vtysh
Hello, this is FRRouting (version 7.2.1-sonic).
Copyright 1996-2005 Kunihiro Ishiguro, et al.
AS7326-56X#
AS7326-56X# configure terminal
AS7326-56X(config)# router bgp 65100
AS7326-56X(config-router)# address-family l2vpn evpn
AS7326-56X(config-router-af)# neighbor 10.0.0.1 activate
AS7326-56X(config-router-af)# advertise-all-vni
AS5835-54X:
admin@AS5835-54X:~$ vtysh
Hello, this is FRRouting (version 7.2.1-sonic).
AS5835-54X# 
AS5835-54X# configure terminal
AS5835-54X(config)# router bgp 65100
AS5835-54X(config-router)# address-family l2vpn evpn
AS5835-54X(config-router-af)# neighbor 10.0.0.0 activate
AS5835-54X(config-router-af)# advertise-all-vni

Check VxLAN  interface configuration.AS7326-56X:
admin@AS7326-56X:~$ show vxlan interface 
VTEP Information:
VTEP Name : vtep, SIP : 1.1.1.1
Source interface : Loopback0
AS5835-54X:
admin@AS5835-54X:~$ show vxlan interface 
VTEP Information:
VTEP Name : vtep, SIP : 2.2.2.2
Source interface : Loopback0

Check vxlan and VLAN mapping.AS7326-56X:
admin@AS7326-56X:~$ show vxlan vlanvnimap
+--------+-------+
| VLAN   |   VNI |
+========+=======+
| Vlan30 |  3000 |
+--------+-------+
Total count : 1
AS5835-54X:
admin@AS5835-54X:~$ show vxlan vlanvnimap
+--------+-------+
| VLAN   |   VNI |
+========+=======+
| Vlan30 |  3000 |
+--------+-------+
Total count : 1

Check the status for Vxlan tunneling. 
AS7326-56X:(202111.3)
admin@AS7326-56X:~$ show vxlan tunnel
vxlan tunnel name    source ip    destination ip    tunnel map name    tunnel map mapping(vni -> vlan)
-------------------  -----------  ----------------  -----------------  ---------------------------------
vtep                 1.1.1.1                       map_3000_Vlan30    3000 -> Vlan30
Total count : 1

AS7326-56X:(202111.3)
admin@AS7326-56X:~$ show vxlan remotevtep
+---------+---------+-------------------+--------------+
| SIP 	| DIP 	| Creation Source   | OperStatus   |
+=========+=========+===================+==============+
| 1.1.1.1 | 2.2.2.2 | EVPN          	| oper_up  	|
+---------+---------+-------------------+--------------+
Total count : 1

AS5835-54X:(202111.3)
admin@AS5835-54X:~$ show vxlan tunnel
vxlan tunnel name    source ip    destination ip    tunnel map name    tunnel map mapping(vni -> vlan)
-------------------  -----------  ----------------  -----------------  ---------------------------------
vtep                 2.2.2.2                      map_3000_Vlan30    3000 -> Vlan30
Total count : 1

AS5835-54X:(202111.3)
admin@AS5835-54X:~$ show vxlan remotevtep
| SIP 	| DIP 	| Creation Source   | OperStatus   |
+=========+=========+===================+==============+
| 2.2.2.2 | 1.1.1.1 | EVPN          	| oper_up  	|
+---------+---------+-------------------+--------------+
Total count : 1
 
Check the Mac learning.
AS7326-56X:(202111.3)


admin@AS7326-56X:~$ show mac
  No.	Vlan  MacAddress     	Port            	Type
-----  ------  -----------------  ------------------  -------
	1  	30  8C:EA:1B:30:DA:50  VxLAN DIP: 2.2.2.2  Static
	2  	30  8C:EA:1B:30:DA:4F  Ethernet0       	Dynamic
Total number of entries 2

AS7326-56X(202111.3)
admin@AS7326-56X:~$ show mac
  No.	Vlan  MacAddress     	Port   	Type
-----  ------  -----------------  ---------  -------
	1  	30  8C:EA:1B:30:DA:4F  Ethernet0  Dynamic
Total number of entries 1
admin@AS7326-56X:~$ show vxlan remotemac all
+--------+-------------------+--------------+-------+-------+---------+
| VLAN   | MAC           	| RemoteVTEP   | ESI   |   VNI | Type	|
+========+===================+==============+=======+=======+=========+
| Vlan30 | 8c:ea:1b:30:da:50 | 2.2.2.2  	|   	|  3000 | dynamic |
+--------+-------------------+--------------+-------+-------+---------+
Total count : 1
Note.
"8C:EA:1B:30:DA:50" is synced from remote vtep(2.2.2.2).
"8C:EA:1B:30:DA:4F" is learned locally.

AS5835-54X:(202111.3)
admin@AS5835-54X:~$ show mac
  No.	Vlan  MacAddress     	Port            	Type
-----  ------  -----------------  ------------------  -------
	1  	30  8C:EA:1B:30:DA:50  Ethernet0       	Dynamic
	2  	30  8C:EA:1B:30:DA:4F  VxLAN DIP: 1.1.1.1  Static
Total number of entries 2

AS5835-54X:(202111.3)
admin@AS5835-54X:~$ show mac
  No.	Vlan  MacAddress     	Port   	Type
-----  ------  -----------------  ---------  -------
	1  	30  8C:EA:1B:30:DA:50  Ethernet0  Dynamic
Total number of entries 1
admin@AS5835-54X:~$ show vxlan remotemac all
+--------+-------------------+--------------+-------+-------+---------+
| VLAN   | MAC           	| RemoteVTEP   | ESI   |   VNI | Type	|
+========+===================+==============+=======+=======+=========+
| Vlan30 | 8c:ea:1b:30:da:4f | 1.1.1.1  	|   	|  3000 | dynamic |
+--------+-------------------+--------------+-------+-------+---------+
Total count : 1
 
Check IPv4 BGP session
AS7326-56X:


AS7326-56X# show bgp ipv4 summary
IPv4 Unicast Summary:
BGP router identifier 1.1.1.1, local AS number 65100 vrf-id 0
BGP table version 6
RIB entries 3, using 552 bytes of memory
Peers 1, using 20 KiB of memory
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.1    	4  	65100  	80  	85    	0	0	0 01:01:28        	1
Total number of neighbors 1

AS5835-54X:
AS5835-54X# show bgp ipv4 summary
IPv4 Unicast Summary:
BGP router identifier 2.2.2.2, local AS number 65100 vrf-id 0
BGP table version 6
RIB entries 3, using 552 bytes of memory
Peers 1, using 20 KiB of memory
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.0    	4  	65100  	79  	79    	0	0	0 01:01:28        	1
Total number of neighbors 1

Check L2EVPN BGP session

AS7326-56X:
AS7326-56X# show bgp l2vpn evpn summary
BGP router identifier 1.1.1.1, local AS number 65100 vrf-id 0
BGP table version 0
RIB entries 3, using 552 bytes of memory
Peers 1, using 20 KiB of memory
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.1    	4  	65100  	82  	87    	0	0	0 01:03:43        	3
Total number of neighbors 1
AS5835-54X:
AS5835-54X# show bgp l2vpn evpn summary
BGP router identifier 2.2.2.2, local AS number 65100 vrf-id 0
BGP table version 0
RIB entries 3, using 552 bytes of memory
Peers 1, using 20 KiB of memory
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.0    	4  	65100  	81  	81    	0	0	0 01:03:43        	3
Total number of neighbors 1

Check underlay routing
AS7326-56X:


AS7326-56X# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
F - PBR, f - OpenFabric,
> - selected route, * - FIB route, q - queued route, r - rejected route
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:49:45
C>* 1.1.1.1/32 is directly connected, Loopback0, 00:49:14
B>* 2.2.2.2/32 [200/0] via 10.0.0.1, Ethernet52, 00:42:04
C>* 10.0.0.0/31 is directly connected, Ethernet52, 00:49:13
C>* 188.188.0.0/16 is directly connected, eth0, 00:49:45

AS5835-54X:


AS5835-54X# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
F - PBR, f - OpenFabric,
> - selected route, * - FIB route, q - queued route, r - rejected route
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:49:57
B>* 1.1.1.1/32 [200/0] via 10.0.0.0, Ethernet52, 00:42:25
C>* 2.2.2.2/32 is directly connected, Loopback0, 00:46:34
C>* 10.0.0.0/31 is directly connected, Ethernet52, 00:46:33
C>* 188.188.0.0/16 is directly connected, eth0, 00:49:57

Check Vxlan VNI status
AS7326-56X:
AS7326-56X# show evpn vni detail 
VNI: 3000
Type: L2
Tenant VRF: default
VxLAN interface: vtep-30
VxLAN ifIndex: 68
Local VTEP IP: 1.1.1.1
Mcast group: 0.0.0.0
Remote VTEPs for this VNI:
2.2.2.2 flood: HER
Number of MACs (local and remote) known for this VNI: 3
Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 3
Advertise-gw-macip: No

AS5835-54X:
AS5835-54X# show evpn vni detail 
VNI: 3000
Type: L2
Tenant VRF: default
VxLAN interface: vtep-30
VxLAN ifIndex: 66
Local VTEP IP: 2.2.2.2
Mcast group: 0.0.0.0
Remote VTEPs for this VNI:
1.1.1.1 flood: HER
Number of MACs (local and remote) known for this VNI: 3
Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 3
Advertise-gw-macip: No

Check the evpn mac learning
AS7326-56X:
AS7326-56X# show evpn mac vni all
VNI 3000 #MACs (local and remote) 3
MAC           	Type   Intf/Remote VTEP  	VLAN  Seq #'s
8c:ea:1b:30:da:50 remote 2.2.2.2                 	1/0
8c:ea:1b:30:da:4f local  Ethernet0         	30	0/0

AS5835-54X:
AS5835-54X# show evpn mac vni all
VNI 3000 #MACs (local and remote) 3MAC           	Type   Intf/Remote VTEP  	VLAN  Seq #'s
8c:ea:1b:30:da:50 local  Ethernet0         	30	0/0
8c:ea:1b:30:da:4f remote 1.1.1.1                 	1/0

Check the type 2 EVPN route
AS7326-56X:
AS7326-56X# show bgp l2vpn evpn route type macip 
BGP table version is 2, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
                   Network          Next Hop            Metric LocPrf Weight Path
            Extended Community
Route Distinguisher: 1.1.1.1:2
*> [2]:[0]:[48]:[8c:ea:1b:cc:10:a4]
                    1.1.1.1                            32768 i
                    ET:8 RT:65100:3000
Route Distinguisher: 2.2.2.2:2
*>i[2]:[0]:[48]:[80:a2:35:5a:22:50]
                    2.2.2.2                       100      0 i
                    RT:65100:3000 ET:8
Displayed 2 prefixes (2 paths) (of requested type)

AS5835-54X:
AS5835-54X# show bgp l2vpn evpn route type macip 
BGP table version is 2, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 1.1.1.1:2
*>i[2]:[0]:[48]:[8c:ea:1b:cc:10:a4]
                    1.1.1.1                       100      0 i
                    RT:65100:3000 ET:8
Route Distinguisher: 2.2.2.2:2
*> [2]:[0]:[48]:[80:a2:35:5a:22:50]
                    2.2.2.2                            32768 i
                    ET:8 RT:65100:3000
Displayed 2 prefixes (2 paths) (of requested type)

Check the type 3 EVPN route
 AS7326-56X:


AS7326-56X# show bgp l2vpn evpn route type multicast 
BGP table version is 3, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
Network Next Hop Metric LocPrf Weight Path
Extended Community
Route Distinguisher: 1.1.1.1:2
*> [3]:[0]:[32]:[1.1.1.1]
1.1.1.1 32768 i
ET:8 RT:65100:3000
Route Distinguisher: 2.2.2.2:2
*>i[3]:[0]:[32]:[2.2.2.2]
2.2.2.2 100 0 i
RT:65100:3000 ET:8
Displayed 2 prefixes (2 paths) (of requested type)

AS5835-54X:
AS5835-54X# show bgp l2vpn evpn route type multicast 
BGP table version is 3, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
Network Next Hop Metric LocPrf Weight Path
Extended Community
Route Distinguisher: 1.1.1.1:2
*>i[3]:[0]:[32]:[1.1.1.1]
1.1.1.1 100 0 i
RT:65100:3000 ET:8
Route Distinguisher: 2.2.2.2:2
*> [3]:[0]:[32]:[2.2.2.2]
2.2.2.2 32768 i
ET:8 RT:65100:3000
```


### <b>L3-VXLAN Symmetric IRB Configuration</b>

![L3-VXLAN Symmetric IRB Configuration](../img/L3IMG1.png)

<table>
<tr>
<td><b>CUMULUS</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Configure physical interfaces, VLAN interfaces, and assign VLAN IDs and IP addresses</b><br /><br />

    <code>net add vlan &lt;VLAN-ID&gt; vrf &lt;VRF_NAME&gt;</code><br /><br />

    <b># Create an L3 VNI in vrf1.</b><br />
    <b># Configure a Per-tenant VXLAN Interface</b><br />
    <code>net add vxlan vni-&lt;VNI_NUMBER&gt; vxlan id &lt;VLAN-ID&gt;</code><br />
    <code>net add vxlan vni-&lt;VNI_NUMBER&gt; bridge access &lt;VLAN-ID&gt;</code><br />
    <code>net add vxlan vni-&lt;VNI_NUMBER&gt; vxlan local-tunnelip &lt;LOCAL_IP&gt;</code><br />
    <code>net add vxlan vni-&lt;VNI_NUMBER&gt; vxlan remoteip &lt;REMOTE_IP&gt;</code><br />
    <code>net add bridge bridge ports vni&lt;VNI_NUMBER&gt;</code><br /><br />

    <b># Configure an SVI for the Layer 3 VNI</b><br />
    <code>net add vlan &lt;VLAN-ID> vrf &lt;VRF_NAME></code><br /><br />

    <b># Configure the VRF to Layer 3 VNI Mapping</b><br />
    <code>net add vrf &lt;VRF_NAME> vni&lt;VNI_NUMBER></code><br /><br />

    <b># Configure and BGP EVPN routes</b><br />
    <code>net add bgp vrf &lt;VRF_NAME> l2vpn evpn advertise ipv4 unicast</code><br /><br />

    <b># Configure and advertise BGP L2 EVPN Routes</b><br />
    <code>net add bgp autonomous-system &lt;ASN_NUMBER></code><br />
    <code>net add bgp l2vpn evpn neighbor &lt;NEIGHBOR_IP> remote-as internal</code><br />
    <code>net add bgp l2vpn evpn neighbor  &lt;NEIGHBOR_IP>  activate</code><br />
    <code>net add bgp l2vpn evpn advertise-all-vni</code><br /><br />

    <b># VTYSH command for BGP L2VPN EVPN command</b><br />
    <code>router bgp &lt;ASN_NUMBER> vrf &lt;VRF_NAME></code><br />
    <code>address-family l2vpn evpn</code><br />
    <code>advertise ipv4 unicast</code><br /><br />

    <b># Command to show BGP L2VPN EVPN VNI routes</b><br />
    <b># NCLU Command</b><br />
    <code>net show bgp l2vpn evpn vni &lt;VNI_NUMBER></code><br /><br />

    <b># VTYSH shell command</b><br />
    <code>sudo vtysh</code><br />
    <code>show bgp l2vpn evpn route</code><br />
    <code>net show bgp vrf &lt;VRF_NAME> ipv4 unicast</code><br /><br />

    <b># Command to show VXLAN traffic stats</b><br />
    <code>net show bgp l2vpn evpn summary</code><br />
    <code>net show bgp l2vpn evpn vni</code><br />
    <code>net show evpn vni</code><br />
    <code>net show evpn mac vni &lt;VNI_VALUE></code><br />
    <code>net show evpn mac vni all</code><br />
    <code>net show evpn next-hops vni all</code><br />
    <code>nv show nve vxlan</code><br />
</td>

<td>
    <b># Configure physical interfaces, VLAN interfaces, and assign VLAN IDs and IP addresses</b><br /><br />

    <code>config interface ip add Loopback0 &lt;SYSTEM_LOOPBACK&gt;</code><br /><br />

    <b># Configure VRF Setting</b><br />
    <code>config vrf add &lt;VRF-NAME&gt;</code><br />
    <code>config interface vrf bind VLAN&lt;VLAN_NUMBER&gt; &lt;VRF-NAME&gt;</code><br />
    <code>config interface ip add VLAN&lt;VLAN_NUMBER> &lt;IP_ADDRESS&gt;</code><br /><br />

    <b># Create VxLAN and map VNI to VLAN</b><br />
    <code>config vxlan add vtep &lt;SOURCE_VTEP_IP&gt;</code><br />
    <code>config vxlan evpn_nvo add nvo vtep</code><br />
    <code>config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE&gt;</code><br />
    <code>config save -y</code><br /><br />

    <b># Configure layer3 VNI and map it to VRF value</b><br />
    <code>config vrf add_vrf_vni_map &lt;VRF-NAME> &lt;VNI_VALUE></code><br />
    <code>config save -y</code><br /><br />

    <b># Establish a BGP environment for EVPN</b><br />
    <b># vtysh command</b><br />
    <code>router bgp &lt;LOCAL_AS_NUMBER></code><br />
    <code>neighbor &lt;ebgp_neighbor_ip> remote-as &lt;REMOTE_AS_NUMBER></code><br />
    <code>address-family ipv4 unicast</code><br />
    <code>network &lt;PREFIX_ADVERTISED></code><br />
    <code>exit</code><br />
    <code>address-family l2vpn evpn</code><br />
    <code>neighbor &lt;ebgp_neighbor_ip> activate</code><br />
    <code>advertise-all-vni</code><br />
    <code>end</code><br /><br />

    <b># Configure VRF and VNI values</b><br />
    <code>configure terminal</code><br />
    <code>vrf &lt;VRF-NAME></code><br />
    <code>vni &lt;VNI_VALUE></code><br /><br />

    <b># Configure BGP routing and advertise EVPN routes</b><br />
    <code>router bgp &lt;LOCAL_AS_NUMBER>  vrf &lt;VRF-NAME></code><br />
    <code>address-family ipv4 unicast</code><br />
    <code>redistribute connected</code><br />
    <code>address-family l2vpn evpn</code><br />
    <code>advertise ipv4 unicast</code><br />
    <code>write</code><br /><br />

    <b># Commands to verify VXLAN tunnels</b><br />
    <code>show vxlan interface</code><br />
    <code>show vxlan vlanvnimap</code><br />
    <code>show vxlan tunnel</code><br />
    <code>show vxlan remotevtep</code><br /><br />

    <b># Commands to verify EVPN routes and BGP routes</b><br />
    <code>show evpn vni detail</code><br />
    <code>show bgp summary</code><br />
    <code>show ip route vrf all</code><br />
</td> 
</tr>
</table>

![L3-VXLAN EVPN Symmetric IRB](../img/L3IMG2.png)

<b>Sample SONiC L3-VXLAN EVPN Symmetric IRB Example</b>

```yaml
# Configure IP address and  Loopback IPs of both switches.
AS5835-54X
admin@SONIC01:~$ config interface ip add Loopback0 1.1.1.1/32
admin@SONIC01:~$ config interface ip add Ethernet48 10.0.0.4/31

A4630-54PE
admin@SONIC02:~$ config interface ip add Loopback0 2.2.2.2/32
admin@SONIC02:~$ config interface ip add Ethernet52 10.0.0.5/31

# Configure VRF Setting
AS5835-54X
admin@SONIC01:~$ config vrf add Vrf01                                                           
admin@SONIC01:~$ config interface vrf bind Vlan30 Vrf01                                          
admin@SONIC01:~$ config interface vrf bind Vlan10 Vrf01                                          
admin@SONIC01:~$ config interface ip add Vlan10 192.168.1.254/24                            

A4630-54PE
admin@SONIC02:~$ config vrf add Vrf01                                                             
admin@SONIC02:~$ config interface vrf bind Vlan30 Vrf01                                         
admin@SONIC02:~$ config interface vrf bind Vlan20 Vrf01                                           
admin@SONIC02:~$ config interface ip add Vlan20 192.168.2.254/24                                  

#Establish BGP Session between Ethernet48 and Ethernet52  
AS5835-54X
admin@SONIC01:~$ vtysh                                                                                 
sonic# configure terminal
sonic(config)# router bgp 65100                                                                        
sonic(config-router)# neighbor 10.0.0.5 remote-as 65100                                      
sonic(config-router)# address-family ipv4 unicast                                       
sonic(config-router-af)# network 1.1.1.1/32                                                 
sonic(config-router-af)# exit
sonic(config-router)# address-family l2vpn evpn                                          
sonic(config-router-af)# neighbor 10.0.0.5 activate                                      
sonic(config-router-af)# advertise-all-vni                                                      
sonic(config-router-af)# end

sonic# configure terminal                                                                              
sonic(config)# vrf Vrf01                                                                                 
sonic(config-vrf)# vni 3000                                                                            
sonic(config-vrf)# end
sonic# configure terminal 
sonic(config)# router bgp 65100 vrf Vrf01                                                      
sonic(config-router)# address-family ipv4 unicast                                        
sonic(config-router-af)# redistribute connected                                           
sonic(config-router-af)# exit
sonic(config-router)# address-family l2vpn evpn                                          
sonic(config-router-af)# advertise ipv4 unicast                                              
sonic(config-router-af)# end
sonic# write

A4630-54PE
admin@SONIC02:~$ vtysh                                                                                 
sonic# configure terminal
sonic(config)# router bgp 65100                                                                   
sonic(config-router)# neighbor 10.0.0.4 remote-as 65100             
sonic(config-router)# address-family ipv4 unicast                                       
sonic(config-router-af)# network 2.2.2.2/32                                                 
sonic(config-router-af)# exit
sonic(config-router)# address-family l2vpn evpn                                          
sonic(config-router-af)# neighbor 10.0.0.4 activate                                      
sonic(config-router-af)# advertise-all-vni                                                      
sonic(config-router-af)# end
sonic# configure terminal                                                                              
sonic(config)# vrf Vrf01                                                                                 
sonic(config-vrf)# vni 3000                                                                            
sonic(config-vrf)# end
sonic# configure terminal 
sonic(config)# router bgp 65100 vrf Vrf01                                                     
sonic(config-router)# address-family ipv4 unicast                                        
sonic(config-router-af)# redistribute connected                                           
sonic(config-router-af)# exit
sonic(config-router)# address-family l2vpn evpn                                          
sonic(config-router-af)# advertise ipv4 unicast                                              
sonic(config-router-af)# end
sonic# write


#Create Vxlan
AS5835-54X
# configuring VTEP_name (vtep) and its IP address 
admin@SONIC01:~$ config vxlan add vtep 1.1.1.1  

#create nvo_name (nvo) and bind it to VTEP_name (vtep)
admin@SONIC01:~$ config vxlan evpn_nvo add nvo vtep      

# Command to map VXLAN VNI to VLAN                                        
admin@SONIC01:~$ config vxlan map add vtep 10 1000                                                
admin@SONIC01:~$ config vxlan map add vtep 30 3000                                               
admin@SONIC01:~$ config save -y

#A4630-54PE
# configuring VTEP_name (vtep) and its IP address 
admin@SONIC02:~$ config vxlan add vtep 2.2.2.2     

#create nvo_name (nvo) and bind it to VTEP_name (vtep)
admin@SONIC02:~$ config vxlan evpn_nvo add nvo vtep     

# Command to map VXLAN VNI to VLAN                                           
admin@SONIC02:~$ config vxlan map add vtep 20 2000                                                
admin@SONIC02:~$ config vxlan map add vtep 30 3000                                               
admin@SONIC02:~$ config save -y     

# Configure the  layer3 VNI on both switches.
AS5835-54X
admin@SONIC01:~$ config vrf add_vrf_vni_map Vrf01 3000            

A4630-54PE
admin@SONIC01:~$ config vrf add_vrf_vni_map Vrf01 3000            

# Verify  EVPN-VNI Route Status 
AS5835-54X
sonic# show evpn vni detail
VNI: 1000
 Type: L2
 Tenant VRF: Vrf01
 VxLAN interface: vtep-10
 VxLAN ifIndex: 67
 SVI interface: Vlan10
 SVI ifIndex: 9
 Local VTEP IP: 1.1.1.1
 Mcast group: 0.0.0.0
 No remote VTEPs known for this VNI
 Number of MACs (local and remote) known for this VNI: 1
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 1
 Advertise-gw-macip: No
 Advertise-svi-macip: No
VNI: 3000
  Type: L3
  Tenant VRF: Vrf01
  Local Vtep Ip: 1.1.1.1
  Vxlan-Intf: vtep-30
  SVI-If: Vlan30
  State: Up
  VNI Filter: none
  System MAC: 00:a0:c9:00:00:00
  Router MAC: 00:a0:c9:00:00:00
  L2 VNIs: 1000

#A4630-54PE
sonic# show evpn vni detail
VNI: 2000
 Type: L2
 Tenant VRF: Vrf01
 VxLAN interface: vtep-20
 VxLAN ifIndex: 78
 SVI interface: Vlan20
 SVI ifIndex: 76
 Local VTEP IP: 2.2.2.2
 Mcast group: 0.0.0.0
 No remote VTEPs known for this VNI
 Number of MACs (local and remote) known for this VNI: 1
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 1
 Advertise-gw-macip: No
 Advertise-svi-macip: No
VNI: 3000
  Type: L3
  Tenant VRF: Vrf01
  Local Vtep Ip: 2.2.2.2
  Vxlan-Intf: vtep-30
  SVI-If: Vlan30
  State: Up
  VNI Filter: none
  System MAC: 68:21:5f:29:c0:d2
  Router MAC: 68:21:5f:29:c0:d2
  L2 VNIs: 2000


# Verify BGP Route Summary

AS5835-54X
sonic# show bgp summary
IPv4 Unicast Summary (VRF default):
BGP router identifier 188.188.9.14, local AS number 65100 vrf-id 0
BGP table version 17
RIB entries 3, using 552 bytes of memory
Peers 1, using 723 KiB of memory
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.5        4      65100      1436      1449        0    0    0 03:02:18            1        1 N/A
Total number of neighbors 1
L2VPN EVPN Summary (VRF default):
BGP router identifier 188.188.9.14, local AS number 65100 vrf-id 0
BGP table version 0
RIB entries 27, using 4968 bytes of memory
Peers 1, using 723 KiB of memory
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.5        4      65100      1436      1449        0    0    0 03:02:18            4        4 N/A
Total number of neighbors 1

A4630-54PE
sonic# show bgp summary
IPv4 Unicast Summary (VRF default):
BGP router identifier 188.188.9.6, local AS number 65100 vrf-id 0
BGP table version 8
RIB entries 3, using 552 bytes of memory
Peers 1, using 723 KiB of memory
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.4        4      65100       220       221        0    0    0 03:02:18            1        1 N/A
Total number of neighbors 1
L2VPN EVPN Summary (VRF default):
BGP router identifier 188.188.9.6, local AS number 65100 vrf-id 0
BGP table version 0
RIB entries 11, using 2024 bytes of memory
Peers 1, using 723 KiB of memory
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.4        4      65100       220       221        0    0    0 03:02:18            4        4 N/A
Total number of neighbors 1


# Validate EVPN route learning
AS5835-54X
sonic# show ip route vrf all
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
       f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
VRF Vrf01:
C>* 192.168.1.0/24 is directly connected, Vlan10, 03:18:41
K>* 192.168.1.254/32 [0/0] is directly connected, Vlan10, 03:18:41
B>* 192.168.2.0/24 [200/0] via 2.2.2.2, Vlan30 onlink, weight 1, 03:04:24
B>* 192.168.2.2/32 [200/0] via 2.2.2.2, Vlan30 onlink, weight 1, 02:21:18
VRF default:
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 22:59:15
K * 1.1.1.1/32 [0/0] is directly connected, Loopback0, 22:54:06
C>* 1.1.1.1/32 is directly connected, Loopback0, 22:54:06
B>* 2.2.2.2/32 [200/0] via 10.0.0.5, Ethernet48, weight 1, 03:04:24
C>* 10.0.0.4/31 is directly connected, Ethernet48, 03:07:18
K>* 10.0.0.4/32 [0/0] is directly connected, Ethernet48, 22:45:24
C>* 188.188.0.0/16 is directly connected, eth0, 22:59:15

sonic# show bgp l2vpn evpn
BGP table version is 14, local router ID is 188.188.9.14
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 188.188.9.6:2
*>i[2]:[0]:[48]:[80:a2:35:5a:22:50]
                    2.2.2.2                       100      0 i
                    RT:65100:2000 ET:8
*>i[2]:[0]:[48]:[80:a2:35:5a:22:50]:[32]:[192.168.2.2]
                    2.2.2.2                       100      0 i
                    RT:65100:2000 RT:65100:3000 ET:8 Rmac:68:21:5f:29:c0:d2
*>i[3]:[0]:[32]:[2.2.2.2]
                    2.2.2.2                       100      0 i
                    RT:65100:2000 ET:8
Route Distinguisher: 188.188.9.14:2
*> [2]:[0]:[48]:[b8:6a:97:19:ba:12]
                    1.1.1.1                            32768 i
                    ET:8 RT:65100:1000
*> [2]:[0]:[48]:[b8:6a:97:19:ba:12]:[32]:[192.168.1.1]
                    1.1.1.1                            32768 i
                    ET:8 RT:65100:1000 RT:65100:3000 Rmac:00:a0:c9:00:00:00
*> [3]:[0]:[32]:[1.1.1.1]
                    1.1.1.1                            32768 i
                    ET:8 RT:65100:1000
Route Distinguisher: 192.168.1.254:3
*> [5]:[0]:[24]:[192.168.1.0]
                    1.1.1.1                  0         32768 ?
                    ET:8 RT:65100:3000 Rmac:00:a0:c9:00:00:00
Route Distinguisher: 192.168.2.254:3
*>i[5]:[0]:[24]:[192.168.2.0]
                    2.2.2.2                  0    100      0 ?
                    RT:65100:3000 ET:8 Rmac:68:21:5f:29:c0:d2
Displayed 8 out of 8 total prefixes

#A4630-54PE
sonic# show ip route vrf all
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,
       f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
VRF Vrf01:
B>* 192.168.1.0/24 [200/0] via 1.1.1.1, Vlan30 onlink, weight 1, 03:04:23
B>* 192.168.1.1/32 [200/0] via 1.1.1.1, Vlan30 onlink, weight 1, 02:20:51
C>* 192.168.2.0/24 is directly connected, Vlan20, 03:07:28
K>* 192.168.2.254/32 [0/0] is directly connected, Vlan20, 03:07:28
VRF default:
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 03:17:24
B>* 1.1.1.1/32 [200/0] via 10.0.0.4, Ethernet52, weight 1, 03:04:23
K * 2.2.2.2/32 [0/0] is directly connected, Loopback0, 03:07:29
C>* 2.2.2.2/32 is directly connected, Loopback0, 03:07:29
C>* 10.0.0.4/31 is directly connected, Ethernet52, 03:07:17
K>* 10.0.0.5/32 [0/0] is directly connected, Ethernet52, 03:07:18
C>* 188.188.0.0/16 is directly connected, eth0, 03:17:24

sonic# show bgp l2vpn evpn
BGP table version is 12, local router ID is 188.188.9.6
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 188.188.9.6:2
*> [2]:[0]:[48]:[80:a2:35:5a:22:50]
                    2.2.2.2                            32768 i
                    ET:8 RT:65100:2000
*> [2]:[0]:[48]:[80:a2:35:5a:22:50]:[32]:[192.168.2.2]
                    2.2.2.2                            32768 i
                    ET:8 RT:65100:2000 RT:65100:3000 Rmac:68:21:5f:29:c0:d2
*> [3]:[0]:[32]:[2.2.2.2]
                    2.2.2.2                            32768 i
                    ET:8 RT:65100:2000
Route Distinguisher: 188.188.9.14:2
*>i[2]:[0]:[48]:[b8:6a:97:19:ba:12]
                    1.1.1.1                       100      0 i
                    RT:65100:1000 ET:8
*>i[2]:[0]:[48]:[b8:6a:97:19:ba:12]:[32]:[192.168.1.1]
                    1.1.1.1                       100      0 i
                    RT:65100:1000 RT:65100:3000 ET:8 Rmac:00:a0:c9:00:00:00
*>i[3]:[0]:[32]:[1.1.1.1]
                    1.1.1.1                       100      0 i
                    RT:65100:1000 ET:8
Route Distinguisher: 192.168.1.254:3
*>i[5]:[0]:[24]:[192.168.1.0]
                    1.1.1.1                  0    100      0 ?
                    RT:65100:3000 ET:8 Rmac:00:a0:c9:00:00:00
Route Distinguisher: 192.168.2.254:3
*> [5]:[0]:[24]:[192.168.2.0]
                    2.2.2.2                  0         32768 ?
                    ET:8 RT:65100:3000 Rmac:68:21:5f:29:c0:d2
Displayed 8 out of 8 total prefixes
```

## <b>QoS Configuration</b>
<table>
<tr>
<td><b>CUMULUS(SN2700)</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Commands to create QoS classifiers</b><br /><br />

    <b># To change the default profile to map PCP 0 to switch priority 4</b><br />
    <code>nv set qos mapping default-global trust l2</code><br />
    <code>nv set qos mapping default-global pcp 0 switch-priority 4</code><br /><br />

    <b># Configuration to change the default profile to map ingress DSCP 22 to switch priority 4</b><br />
    <code>nv set qos mapping default-global trust l3</code><br />
    <code>nv set qos mapping default-global dscp 22 switch-priority 4</code><br />
    <code>nv show qos mapping default-global dscp 22</code><br /><br />

    <b># Command to assign all traffic to switch priority 3</b><br />
    <code>nv set qos mapping default-global trust port</code><br />
    <code>nv set qos mapping default-global port-default-sp 3</code><br />
    <code>nv show qos mapping default-global</code><br /><br />

    <b># Configuration to remark switch priority 0 to egress DSCP 22</b><br />
    <code>nv set qos remark default-global rewrite l3</code><br />
    <code>nv set qos remark default-global switch-priority 0 dscp 22</code><br /><br />

    <b># Configure PFC</b><br />
    <code>nv set qos pfc default-global switch-priority 0</code><br />
    <code>nv set qos pfc default-global tx enable</code><br />
    <code>nv set qos pfc default-global rx disable</code><br />
    <code>nv set qos pfc default-global cable-length 50</code><br /><br />

    <b># Assign switch priority 2 to egress queue 7</b><br />
    <code>nv set qos egress-queue-mapping default-global switch-priority 2 traffic-class 7</code><br /><br />

    <b># Show the egress queue mapping configuration for the default profile</b><br />
    <code>nv show qos egress-queue-mapping default-global</code><br /><br />

    <b># Applies the traffic shaping configuration to swp1, swp2, swp3, and swp5.</b><br />
    <code>nv set qos egress-shaper shaper1 traffic-class 2 min-rate 100</code><br />
    <code>nv set qos egress-shaper shaper1 traffic-class 2 max-rate 500</code><br />
    <code>nv set qos egress-shaper shaper1 port-max-rate 200000</code><br />
    <code>nv set interface swp1-swp3,swp5 qos egress-shaper profile shaper1</code><br /><br />

    <b># Remarking configuration</b><br />
    <code>nv set qos remark remark_port_group1 rewrite l3</code><br />
    <code>nv set interface swp1 qos remark profile remark_port_group1</code><br />
    <code>nv set qos remark remark_port_group2 switch-priority 0 dscp 37</code><br />
    <code>nv set qos remark remark_port_group2 switch-priority 1 dscp 37</code><br />
    <code>nv set interface swp2 qos remark profile remark_port_group2</code><br /><br />

    <b># Egress scheduling</b><br />
    <code>nv set qos egress-scheduler list2 traffic-class 2,5,6 mode dwrr</code><br />
    <code>nv set qos egress-scheduler list2 traffic-class 2,5 bw-percent 50</code><br />
    <code>nv set qos egress-scheduler list2 traffic-class 6 mode strict</code><br />
    <code>nv set interface swp1,swp3,swp18 qos egress-scheduler profile list2</code><br />
    <code>nv set interface swp2 qos egress-scheduler profile list1</code><br />
</td>
<td>
    <b># Commands to create QoS classifiers (EdgeCore SONiC Platform - AS9716-32D)</b><br /><br />

    <b># Create a profile for DOT1P/DSCP mapped to TC (Traffic Class).</b><br />
    <b># Example for DSCP:</b><br />
    <code>config qos dscp-tc add DSCP_TC --dscp 7 --tc 1</code><br />
    <b># Modify the existing Dot1p/DSCP to TC profile.</b><br />
    <b># Example for DOT1P:</b><br />
    <code>config qos dot1p-tc update 1p_tc --dot1p 1 --tc 2</code><br />

    <b># Validate the profile for DOT1P/DSCP to Traffic class.</b><br />
    <b># DOT1P to TC:</b><br />
    <code>show qos dot1p-tc</code><br />

    <b># Validate Queue mapping from DSCP queue to Traffic class.</b><br />
    <code>show qos dscp-tc</code><br />

    <b># Create a profile for traffic class and map it to Queue.</b><br />
    <code>config qos tc-queue add TC_Q --tc 1 --queue 2</code><br />

    <b># Validate the profile of Traffic class to Queue.</b><br />
    <code>show qos tc-queue</code><br />

    <b># Binding the mapping table to the specified interface.</b><br />
    <code>config interface qos dscp-tc bind Ethernet0 DSCP_TC</code><br />

    <b># Validate the binding table.</b><br />
    <code>show interfaces qos</code><br />

    <b># Clear the queue counter</b><br />
    <code>sonic-clear queue counters</code><br />

    <b># Check Specific Ethernet port (egress port) queue counters.</b><br />
    <code>show queue counters Ethernet8</code><br />

    <b># Marking configuration</b><br />
    <b># Create a profile for DOT1P remarking.</b><br />
    <b># Example for DOT1P:</b><br />
    <code>config qos remark dot1p add remark_dot1p --tc 0 --dot1p 1</code><br />

    <b># Validate the remark profile.</b><br />
    <code>show qos remark dot1p</code><br />

    <b># Bind the remark table to the egress interface.</b><br />
    <code>config interface qos remark dot1p bind Ethernet8 remark_dot1p</code><br />

    <b># Validate the binding table.</b><br />
    <code>show interfaces qos</code><br />

    <b># Scheduler Configuration (EdgeCore SONiC platform - AS7326-56X)</b><br />
    <b># Set the scheduler mode.</b><br />
    <code>config scheduler add strict_mode --sched_type STRICT</code><br />

    <b># Validate scheduler status.</b><br />
    <code>show scheduler</code><br />

    <b># Bind the scheduler to Ethernet sub-interface.</b><br />
    <b># Example:</b><br />
    <code>config interface scheduler bind queue Ethernet 5.3 strict_mode</code><br />

    <b># Command to unbind the scheduler from the Ethernet interface.</b><br />
    <code>config interface scheduler unbind queue Ethernet 5.3</code><br />

    <b># Validate scheduler status.</b><br />
    <code>show interfaces scheduler</code><br />

    <b># Set the scheduler mode</b><br />
    <b># Example:</b><br />
    <code>config scheduler add wrr_7 --sched_type WRR --weight 7</code><br />
    <code>config scheduler add wrr_3 --sched_type WRR --weight 3</code><br />

    <b># Validate scheduler status.</b><br />
    <code>show scheduler</code><br />

    <b># Bind the scheduler to Ethernet interface.</b><br />
    <b># Example:</b><br />
    <code>config interface scheduler bind queue Ethernet5 3 wrr_7</code><br />
    <code>config interface scheduler bind queue Ethernet5 4 wrr_3</code><br />

    <b># Validate scheduler status.</b><br />
    <code>show interfaces scheduler</code><br />
</td>
</tr>

</table>

## <b>ACL Configuration</b>

<table>
<tr>
<td><b>CUMULUS(SN2700)</b></td>
<td><b>SONiC</b></td>
</tr>

<tr>
<td>
    <b># Command to create ACL rules</b><br /><br />

    <b># Install and Manage ACL Rules with NCLU command</b><br />
    <code>-A FORWARD -i &lt;interface_name> -s &lt;source_ip> -d &lt;destination_ip> -p tcp -j ACCEPT</code><br /><br />

    <b># Create ACL rule with NCLU command</b><br />
    <code>net add acl ipv4 &lt;ACL_NAME> accept tcp source-ip &lt;source_ip> source-port any dest-ip &lt;destination_ip> dest-port any</code><br /><br />

    <b># Apply ACL rule to inbound or outbound interface</b><br />
    <code>net add int &lt;interface_name> acl ipv4 &lt;ACL_NAME> inbound</code><br /><br />

    <b># Verify the ACL rule</b><br />
    <code>net show configuration acl</code><br /><br />

    <b># Command to apply ACL rule to a control plane interface</b><br />
    <code>net add control-plane acl ipv4 &lt;ACL_NAME> inbound</code><br /><br />

    <b># To remove an ACL rule</b><br />
    <code>net del acl ipv4 &lt;ACL_NAME></code><br /><br />

    <b># Command to examine the current state of ACLs and list all installed ACL rules</b><br />
    <code>sudo cl-acltool -L all</code><br /><br />
</td>
<td>
    <b># Command to create ACL Tables</b><br /><br />

    <b># Syntax</b><br />
    <code>config acl add table &lt;ACL_table_name> L3 --description 'ACL_Test1' --stage 'ingress' --ports 'Ethernet&lt;number>'</code><br /><br />

    <b># Example</b><br />
    <code>config acl add table ACL_Test1 L3V6 --description 'ACL_Test1' --stage 'egress' --ports 'Ethernet16'</code><br /><br />

    <b># Command to delete ACL tables</b><br />
    <code>config acl remove table &lt;ACL_Table_Name></code><br /><br />

    <b># Command to create ACL Rule with source_ip_address</b><br />
    <b># Example</b><br />
    <code>config acl add rule --src-ip4 100.0.0.1 --priority 3 ACL_Test1 deny</code><br /><br />

    <b># Commands to verify ACL table and rule created</b><br />
    <code>show acl table</code><br />
    <code>show acl rule</code><br /><br />
</td>
</tr>
</table>

## <b>References</b>

### <b>Cumulus References</b>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Quick-Start-Guide/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-41/Layer-3/Management-VRF/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Monitoring-and-Troubleshooting/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Installation-Management/Back-up-and-Restore/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-50/System-Configuration/Smart-System-Manager/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/knowledge-base/Setup-and-Getting-Started/Cumulus-Linux-Command-Reference-Guide/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-43/Installation-Management/Upgrading-Cumulus-Linux/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-41/Layer-3/Management-VRF/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Layer-2/Link-Layer-Discovery-Protocol/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-44/System-Configuration/Netfilter-ACLs/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-54/Layer-1-and-Switch-Ports/Quality-of-Service/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-41/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/</a>
- <a>https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-42/Network-Virtualization/Static-VXLAN-Tunnels/</a>


### <b>Edgecore SONIC References</b>

- <a>https://support.edge-core.com/hc/en-us/articles/900004369066--Enterprise-SONiC-OSPF-Open-Shortest-Path-First-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000789566--Enterprise-SONiC-BGP-Step-1-Establish-BGP-Session</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000809363--Enterprise-SONiC-BGP-Step-2-1-Redistribute-routes-to-BGP-process-Optional-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900002377366--Enterprise-SONiC-BGP-Unnumbered</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900004277226--Enterprise-SONiC-VRF-Virtual-routing-and-forwarding-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900002380706--Enterprise-SONiC-MC-LAG</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900002741223--Enterprise-SONiC-Symmetric-EVPN-IRB</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900002720523--Enterprise-SONiC-EVPN-L2-VxLAN</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000214926--Enterprise-SONiC-ACL-Access-Control-List-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/9391323739417--Enterprise-SONiC-ZTP-Zero-Touch-Provisioning-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000240066--Enterprise-SONiC-QoS-Quality-of-Service-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000198943--Enterprise-SONiC-DHCP-Relay</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000307246--Enterprise-SONiC-SONiC-overview</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900004277226--Enterprise-SONiC-VRF-Virtual-routing-and-forwarding-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900000214266--Enterprise-SONiC-LLDP-Link-Layer-Discovery-Protocol-</a>
- <a>https://support.edge-core.com/hc/en-us/articles/900007074363--Enterprise-SONiC-Sub-Interface</a>































