## <b> OSPF Routing </b>

![OSPF Routing ](../img/OSPF-Routing.png)


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
<th colspan='2'>OSPF Routing </th>
</tr>
<tr>
<td>
<b>#Configure OSPF routing</b><br> 
set protocols ospf router-id &lt;Router_ID><br>
set protocols ospf area &lt;area-id> area-type <type><br>
set protocols ospf area &lt;Aread_ID><br>
set protocols ospf area &lt;Aread_ID>  area-type stub<br>
set protocols ospf area &lt;Aread_ID> area-type nssa<Br>
set protocol ospf interface &lt;vlan-interface> area {&lt;ipv4>|&lt;0-4294967295>}<br>
set vlans vlan-id &lt;vlan-id>  l3-interface "vlan-number"<Br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching native-vlan-id &lt;vlan-id><Br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching native-vlan-id &lt;vlan-id><br>
</br>
set l3-interface vlan-interface vlan&lt;number> address &lt;IPV4_Address>  prefix-length &lt;Subnet><br>
set l3-interface vlan-interface vlan&lt;number> address &lt;IPV4_Address>  prefix-length &lt;Subnet><Br>
set protocols ospf interface vlan-&lt;number> area &lt;aread_id><br>
</br>
<br></br>
<b># Example Configuration - OSPF Routing</b><br> 
set protocols ospf router-id 1.1.1.1<br>
set protocols ospf area &lt;area-id> area-type <type><Br>
set protocols ospf area 0.0.0.0<br>
set protocols ospf area 1.1.1.1 area-type stub<Br>
set protocols ospf area 2.2.2.2 area-type nssa<br>
set protocol ospf interface &lt;vlan-interface> area {&lt;ipv4>|&lt;0-4294967295>}<br>
</br>
set vlans vlan-id 20 l3-interface "vlan-20"<br>
set vlans vlan-id 30 l3-interface "vlan-30"<br>
set interface gigabit-ethernet ge-1/1/1 family ethernet-switching native-vlan-id 20<br>
</br>
set interface gigabit-ethernet ge-1/1/2 family ethernet-switching native-vlan-id 30<br>
</br>
set l3-interface vlan-interface vlan20 address 10.10.70.10 prefix-length 24<br>
set l3-interface vlan-interface vlan30 address 10.10.71.10 prefix-length 24<br>
</br>
set protocols ospf interface vlan-20 area 0.0.0.0<br>
set protocols ospf interface vlan-30 area 0.0.0.0<Br>

</td>
<td>
<b>#Configure OSPF routing</b><br> 
<b>#Syntax</b> <br>
router ospf<br>
ospf router-id &lt;router-id><br>
network &lt;Network_address>  area &lt;Area_number><br>
network &lt;Network_address1>  area &lt;Area_number1><br>
network &lt;Network_address2>  area &lt;Area_number2><br>
</br>
<b>#Command to set OSPF time intervals</b><br>
interface Ethernet&lt;interface><br>
ip ospf hello-interval &lt;hello-interval-time-secs><br>
ip ospf dead-interval &lt;dead-interval-time-secs><br>
router ospf<BR>
area &lt;aread_number> authentication<br>
</b>
<b># Command to set OSPF authentication key</b><br>
interface Ethernet&lt;interface><br>
ip ospf authentication<br>
ip ospf authentication-key &lt;key><br>
</br>
<b># Command to set OSPF  MD5 Authentication</b><br> 
router ospf<br>
area 0 authentication message-digest<br>
interface Ethernet&lt;interface><Br>
ip ospf message-digest-key &lt;key> md5 &lt;key><br>
</br>
<b># Command to configure OSPF Virtual links</b><br> 
router ospf<br>
area &lt;area_number>  virtual-link &lt;System_loopback><br>
</br>
<b># Command to verify OSPF ip routes learned</b><br> 
show ip route<br>
</br>
<b># Configuration OSPF Routing </b><br>
<b># Example</b><br>
router ospf<br>
ospf router-id 1.1.1.1<br>
network 10.0.0.0/31 area 0<br>
network 192.168.10.0/24 area 0<br>
network 192.168.20.0/24 area 0<br>
network 192.168.30.0/24 area 0<br>
</br>
<b>#Enable OSPF hello timers under interface</b><br> 
<b>#Example</b> <Br>
interface Ethernet56<br>
ip ospf hello-interval 20<Br>
ip ospf dead-interval 20<br>
</br>
<b># Enable OSPF Authentication globally</b><br> 
<b>#Example</b> <br>
router ospf<br>
area 0 authentication<br>
</br>
<b># Enable OSPF Authentication over interface</b><br>
<b>#Example</b> <br>
interface Ethernet56<br>
ip ospf authentication<br>
ip ospf authentication-key 123<br>
</br>
<b>#Enable OSPF MD5 Key </b><br>
<b>#Example </b><br>
router ospf<Br>
area 0 authentication message-digest<Br>
interface Ethernet56<br>
ip ospf message-digest-key 1 md5 123<br>
</br>
<b>#Verify Ip routing Table</b><br>
<b>#Example </b><br>
show ip route<Br>
</br>
<b>#Configure OSPF virtual links</b><br>
<b>#Example </b><br>
</br>
router ospf<br>
area 1 virtual-link 3.3.3.3<br>
router ospf<Br>
area 1 virtual-link 2.2.2.2

</td>
</tr>
</table>

![OSPF](../img/OSPF-2.png)

<br></br>

<table>
<tr>
<th colspan='2'>PICOS</th>
</tr>
<tr>
<td colspan='2'>

<u><b>#AS7326-56X-OS1 Configuration</b><br></u>
</br>
<b># VLAN and IP Configuration</b><br>
config interface ip add Loopback0 1.1.1.1/32<Br>
config vlan member add 10 Ethernet0<br>
config vlan member add 20 Ethernet0<br>
config vlan member add 30 Ethernet0<br>
config interface ip add Ethernet0.10 192.168.10.1/24<br>
config interface ip add Ethernet0.20 192.168.20.1/24<Br>
config interface ip add Ethernet0.30 192.168.30.1/24<Br>
config interface ip add Ethernet56 10.0.0.0/31<br>
</br>
<b>#OSPF Configuration</b><br>
admin@sonic:~\$ vtysh
sonic(config)# router ospf<Br>
sonic(config-router)# network 10.0.0.0/31 area 0<br>
sonic(config-router)# network 192.168.10.0/24 area 0<Br>
sonic(config-router)# network 192.168.20.0/24 area 0<br>
sonic(config-router)# network 192.168.30.0/24 area 0<br>
</br>
<b>#OSPF Routing Verification Command</b><br>
sonic# show ip ospf neighbor<br>
Neighbor ID&nbsp;&nbsp;&nbsp;&nbsp;Pri&nbsp;State&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dead Time&nbsp;Address&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interface&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RXmtL&nbsp;RqstL&nbsp;DBsmL<br>
192.168.25.1&nbsp;&nbsp;&nbsp;1&nbsp;Full/DR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;31.440s&nbsp;10.0.0.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ethernet56:10.0.0.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0     0     0<br>
</br>
sonic# show ip route<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
       F - PBR, f - OpenFabric,<br>
       > - selected route, * - FIB route, q - queued route, r - rejected route<br>
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:07:45<br>
C>* 1.1.1.1/32 is directly connected, Loopback0, 00:07:25<br>
O   10.0.0.0/31 [110/10] is directly connected, Ethernet56, 00:06:42<BR>
C>* 10.0.0.0/31 is directly connected, Ethernet56, 00:07:25<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:07:46<br>
O>* 192.168.5.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32<br>
O   192.168.10.0/24 [110/10] is directly connected, Vlan10, 00:04:54<br>
C>* 192.168.10.0/24 is directly connected, Vlan10, 00:07:24<br>
O>* 192.168.15.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32<br>
O   192.168.20.0/24 [110/10] is directly connected, Vlan20, 00:04:50<br>
C>* 192.168.20.0/24 is directly connected, Vlan20, 00:07:24<br>
O>* 192.168.25.0/24 [110/20] via 10.0.0.1, Ethernet56, 00:06:32<br>
O   192.168.30.0/24 [110/10] is directly connected, Vlan30, 00:04:47<br>
C>* 192.168.30.0/24 is directly connected, Vlan30, 00:07:24<br>
</br>
<b><u>#AS7326-56X-OS2 Configuration</u></b><br>
<b># VLAN and IP Configuration</b><br>
config interface ip add Loopback0 2.2.2.2/32<br>
config vlan member add 5 Ethernet0<br>
config vlan member add 15 Ethernet0<br>
config vlan member add 25 Ethernet0<br>
config interface ip add Ethernet0.5 192.168.51/24<Br>
config interface ip add Ethernet0.15 192.168.15.1/24<br>
config interface ip add Ethernet0.25 192.168.25.1/24<br>
config interface ip add Ethernet56 10.0.0.1/31<br>
</br>
<b>#OSPF Configuration</b><br>
admin@sonic:~$ vtysh<br>
sonic(config)# router ospf<br>
sonic(config-router)# network 10.0.0.0/31 area 0<br>
sonic(config-router)# network 192.168.5.0/24 area 0<br>
sonic(config-router)# network 192.168.15.0/24 area 0<br>
sonic(config-router)# network 192.168.25.0/24 area 0<Br>
</br>
<b>#OSPF Routing Verification Command</b><br>
OS2:<br>
sonic# show ip ospf neighbor<br>
Neighbor&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&Pri State&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dead Time Address&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interface&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RXmtL RqstL DBsmL<br>
188.188.98.39&nbsp;&nbsp;&nbsp;1 Full/Backup&nbsp;&nbsp;&nbsp;&nbsp;33.721s 10.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ethernet56:10.0.0.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0     0     0<br>
</br>
<b>sonic# show ip route</b><br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<br>
       F - PBR, f - OpenFabric,<br>
       > - selected route, * - FIB route, q - queued route, r - rejected route<br>
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 02:15:38<br>
C>* 2.2.2.2/32 is directly connected, Loopback0, 02:15:18<br>
O   10.0.0.0/31 [110/10] is directly connected, Ethernet56, 00:08:47<br>
C>* 10.0.0.0/31 is directly connected, Ethernet56, 00:08:47<br>
C>* 188.188.0.0/16 is directly connected, eth0, 02:15:39<Br>
O   192.168.5.0/24 [110/10] is directly connected, Vlan5, 00:35:34<br>
C>* 192.168.5.0/24 is directly connected, Vlan5, 00:35:34<br>
O>* 192.168.10.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:14<br>
O   192.168.15.0/24 [110/10] is directly connected, Vlan15, 00:35:34<br>
C>* 192.168.15.0/24 is directly connected, Vlan15, 00:35:34<br>
O>* 192.168.20.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:10<br>
O   192.168.25.0/24 [110/10] is directly connected, Vlan25, 00:35:34<br>
C>* 192.168.25.0/24 is directly connected, Vlan25, 00:35:34<br>
O>* 192.168.30.0/24 [110/20] via 10.0.0.0, Ethernet56, 00:06:07<br>

</td>
</tr>
</table>