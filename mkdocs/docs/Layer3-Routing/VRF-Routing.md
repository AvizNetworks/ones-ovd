## <b> VRF Routing</b> 

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
<b># Command to configure VRRP</b><br>
set ip routing enable true<Br>
set ip vrf vrf1 description east<br>
set ip vrf vrf2 description east<br>
</br>
<br># Command to  bind the Layer 3 VLAN interface to the VRF.<br>
 set vlan-interface interface vlan&lt;vlan-id> vrf &lt;VRF-ID><br>
</br>
<b># Command to add static route entry into the VRF.</b><br>
 set protocols static vrf &lt;VRF-ID>  route &lt;IPV4_address>  next-hop &lt;IPV4_address><br>
 set protocols static vrf &lt;VRF-ID>  route &lt;IPV6_address>  next-hop &lt;IPV6_address<br>
</br>
<b># Command to validate show VRF instance created</b><br> 
run show vrf<br>

</td>
<td>
<b># SONiC command to create a VRF-</b><br>
<b>#Syntax</b> <br>
config vrf add<br>
config vrf add &lt;vrf-name><br>
config vrf del &lt;vrf-name><Br>
config vrf add_vrf_vni_map &lt;vrf-name> <vni><Br>
</br>
<b>#  Command  to bind Layer 3 VLAN interface to the VRF.</b><br>
config vrf add &lt;VRF-ID><br>
config vxlan add vtep &lt;VTEP_ENDPOINT_IP><br>
config vxlan evpn_nvo add evpnnvo vtep<br>
config vrf add_vrf_vni_map &lt;VRF-ID>  &lt;VNI_VALUE><br>
</br>
<b># Command  to unbind the Layer 3 VLAN interface to the VRF</b><br>
<b># Syntax </b><br>
config vrf del_vrf_vni_map &lt;vrf-name><br>
</br>
<b># Command to configure  a static route entry into the VRF</b><br>
<b># Example</b><Br>
ip route &lt;A.B.C.D/M> &lt;A.B.C.D> nexthop-vrf &lt;vrf-name><br>
</br>
<b># Command to import VRF table into default routing table</b><br>  
import vrf default<br>
</br>
<b>#Command to add bgp routing entry with VRF  and import route leaking policy into VRF routing table</b><br>
router bgp &lt;AS_NUMBER> vrf <VRF-ID><br>
address-family ipv4 unicast<br>
router bgp &lt;AS_NUMBER>  vrf <VRF-ID><br>
address-family ipv4 unicast<br>

</td>
</tr>
</table>

<table>
<tr>
<th colspan='2'>SONiC- VRF Routing</th>
</tr>
<tr>
<td colspan='2'>
<b># Create VRF instance</b><br>
admin@sonic:~$ config vrf add Vrf_01<br>
<b># Binding the Ethernet0 to VRF instance.</b><br>
admin@sonic:~$ config interface vrf bind Ethernet0 Vrf_01<Br>
<b># Checking the VRF</b><br>
admin@sonic:~$ show vrf<br>
VRF 	Interfaces<br>
------  ------------<br>
Vrf_01  Ethernet0<br>

```
admin@sonic:~$ show ip interfaces
Interface	Master	IPv4 address/mask	Admin/Oper	BGP Neighbor	Neighbor IP
-----------  --------  -------------------  ------------  --------------  -------------
Ethernet0	Vrf_01	192.168.1.1/24   	up/up   	N/A         	N/A
Loopback0          	10.1.0.1/32      	up/up     	N/A         	N/A
docker0     	       240.127.1.1/24   	up/down   	N/A         	N/A
eth0               	188.188.97.31/16 	up/up     	N/A         	N/A
lo                 	127.0.0.1/8      	up/up     	N/A         	N/A
```
<b># Checking the routing table.</b><br>
admin@sonic:~\$ show ip route vrf Vrf_01<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<br>
VRF Vrf_01:<br>
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:02:37<Br>
admin@sonic:~\$ show ip route vrf all<Br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<br>
VRF Vrf_01:<br>
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:00:31<Br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:15:16<br>
C>* 10.1.0.1/32 is directly connected, Loopback0, 00:15:16<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:15:16<Br>
</br>
<b># Management VRF</b><br>
<b># Create Management VRF</b><br>
admin@sonic:~\$ config vrf add mgmt<br>
<b># Checking the Management VRF</b><br>
admin@sonic:~\$ show mgmt-vrf<br>
ManagementVRF : Enabled<br>
Management VRF interfaces in Linux:<br>
128: mgmt: &lt;NOARP,MASTER,UP,LOWER_UP> mtu 65536 qdisc noqueue state UP mode DEFAULT group default qlen 1000<br>
	link/ether 52:2f:cc:b8:28:b5 brd ff:ff:ff:ff:ff:ff promiscuity 0 minmtu 68 maxmtu 1500<br>
	vrf table 5000 addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535<br>
2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master mgmt state UP mode DEFAULT group default qlen 1000<br>
	link/ether 80:a2:35:4f:4f:40 brd ff:ff:ff:ff:ff:ff<br>
129: lo-m: &lt;BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master mgmt state UNKNOWN mode DEFAULT group default qlen 1000<br>
	link/ether 0a:25:2e:1f:32:90 brd ff:ff:ff:ff:ff:ff<Br>
admin@sonic:~\$ show ip interfaces<br>
``````
Interface	Master	IPv4 address/mask	Admin/Oper	BGP Neighbor	Neighbor IP
-----------  --------  -------------------  ------------  --------------  -------------
Ethernet0	Vrf_01	192.168.1.1/24   	up/up     	N/A         	N/A
Loopback0          	10.1.0.1/32      	up/up     	N/A         	N/A
docker0            	240.127.1.1/24   	up/down   	N/A         	N/A
eth0     	mgmt  	188.188.97.31/16 	up/up     	N/A         	N/A
lo                 	127.0.0.1/8      	up/up     	N/A         	N/A
lo-m     	mgmt  	127.0.0.1/8      	up/up     	N/A     	    N/A
``````
<b>#Checking the routing table.</b><br>
admin@sonic:~\$ show ip route vrf mgmt<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<BR>
VRF mgmt:<br>
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:12:12<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:12:12<br>
admin@sonic:~\$ show ip route vrf all<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<br>
VRF Vrf_01:<Br>
C>* 192.168.1.0/24 is directly connected, Ethernet0, 00:01:04<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<Br>
C>* 10.1.0.1/32 is directly connected, Loopback0, 00:01:05<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F - PBR, f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued route, r - rejected route<br>
VRF mgmt:<br>
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:01:21<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:01:21<br>

</td>
</tr>
</table>