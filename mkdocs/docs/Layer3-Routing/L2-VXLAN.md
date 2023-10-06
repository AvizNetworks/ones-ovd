## <b> L2-VXLAN Asymmetric IRB Configuration</b>

![L2-VXLAN](../img/L2-VXLAN-asym.png)

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

<br><br>

<table>
<tr>
<th>PICOS</th>
<th>SONiC</th>
</tr>
<tr>
<td>
<b># Configure VLAN ID, L3 VLAN interfaces loopback interfaces and IP addressing.</b><br>
<b>#Syntax</b><br>
set vlans  vlan-id &lt;VLAN-ID><br>
set ip routing enable true<br>
set ip vrf &lt;VRF_NAME><br>
<br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching native-vlan-id &lt;vlan-id1><br>
set interface gigabit-ethernet ge-a/b/c family ethernet-switching native-vlan-id &lt;vlan-id2><br>
<br>
set l3-interface loopback lo address &lt;System_loopback_1>  prefix-length 32<br>
<br>
set l3-interface loopback &lt;VRF_NAME> address &lt;System_loopback_2> prefix-length 32<br>
<br>
set l3-interface vlan-interface vlan&lt;vlan_number>  address &lt;IP_address> prefix-length &lt;subnet_length><br>
<br>
<b># Configure VXLAN VNI and map VNI IDs to VLAN IDs.</b><br>
set vlans vlan-id &lt;VLAN-ID>  l3-interface "vlan&lt;VLAN_NUMBER>"<Br>
set vxlans source-interface lo address &lt;SYSTEM_LOOPBACK><br>
set vxlans vni &lt;VNI_VALUE>  vlan &lt;VLAN-ID><Br>
<br>
<b># Configure BGP related configuration</b><br>
set protocols bgp local-as &lt;LOCAL_AS_NUMBER><br>
set protocols bgp router-id &lt;SYSTEM_LOOPBACK><br>
set protocols bgp neighbor &lt;BGP_NEIGHBOR_IP> remote-as "internal"<br>
set protocols bgp neighbor &lt;BGP_NEIGHBOR_IP> update-source "&lt;SYSTEM_LOOPBACK>"<br>
set protocols bgp neighbor &lt;BGP_NEIGHBOR_IP>  evpn activate true<br>
set protocols bgp evpn advertise-all-vni<br>
set protocols bgp evpn advertise ipv4-unicast<br>
set protocols bgp local-as &lt;LOCAL_AS_NUMBER><br>
set protocols bgp router-id &lt;SYSTEM_LOOPBACK><br>
set protocols bgp evpn advertise ipv4-unicast<br>
<br>
<b>#Verify Configuration- routes and VXLAN tunnels</b><br>
run show route <br>
run show bgp route<br> 
run show vxlan evpn route <Br>
run show vxlan tunnel<br>
<br>
<b>#Advertise BGP EVPN Routes</b><br> 
set protocols bgp evpn advertise-all-vni<br>
set vxlans source-interface loopback address &lt;SYSTEM_LOOPBACK><br>
set vxlans vni &lt;VNI_VALUE>  encapsulation vlan &lt;VLAN-ID><br>
<br>
<b>#Command to show VXLAN traffic stats</b><br> 
run show vxlan statistics<br>

</td>
<td>

<b># Configure LoopBack, VLAN IDs , Ip addressing </b><br>
<b># Syntax</b><Br>
config vlan add &lt;VLAN-ID><br>
config vlan member add &lt;VLAN-ID> Ethernet&lt;interface1><br>
config interface ip add Loopback0 &lt;SYSTEM_LOOPBACK><br>
<br>
<br><br>
<b># Configure BGP routing</b><br> 
router bgp &lt;LOCAL_AS_NUMBER><Br>
bgp router-id &lt;SYSTEM_LOOPBACK><BR>
neighbor &lt;ebgp_neighbor_ip>  remote-as &lt;REMOTE_AS_NUMBER><br>
address-family ipv4<br>
network &lt;Network_prefix_advertised><br>
<br>
<b>#Configure VXLAN VNI and map VNI IDs to VLAN IDs</b><br>
config vxlan add vtep &lt;SOURCE_VTEP_IP><br>
config vxlan evpn_nvo add nvo vtep<br>
config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE><br>
<br>
config vxlan add vtep &lt;DEST_VTEP_IP><br>
config vxlan evpn_nvo add nvo vtep<br>
config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE><br>
<br>
<br><br>
<b>#Advertise L2 EVPN Routes</b><br> 
router bgp &lt;LOCAL_AS_NUMBER><br>
address-family l2vpn evpn<br>
neighbor &lt;ebgp_neighbor_ip> activate<br>
Advertise-all-vni<br>
<br>
<br><br>
<b>#Show VXLAN tunnels , interfaces</b><br>  
show ip route<br>
show vxlan interface<br>
show vxlan vlanvnimap<br>
show vxlan tunnel<Br>
show vxlan remotevtep<Br>
show evpn vni detail<Br>

</td>
<tr>
</table>

![L2-VXLAN-EVPN-topology](../img/L2-VXLAN-EVPN-topology.png)

<table>
<tr>
<th colspan='2'>Sample SONiC- L2VXLAN EVPN Asymmetric IRB </th>
</tr>
<tr>
<td colspan='2'>
<b><u>Step 1: Configure IP address to Loopback0 of both switches.</u></b><br>
<b>AS7326-56X</b><br>
admin@AS7326-56X:~$ config interface ip remove Loopback0 10.1.0.1/32<br>   
admin@AS7326-56X:~$ config interface ip add Loopback0 1.1.1.1/32<Br>
<br>
<b>AS5835-54X:</b><br>
admin@AS5835-54X:~$ config interface ip remove Loopback0 10.1.0.1/32<br>   
admin@AS5835-54X:~$ config interface ip add Loopback0 2.2.2.2/32<br>
<br>
<b><u>Step 2: Establish BGP Session between Ethernet52 and announce the network.</u></b><br>
<b>AS7326-56X:</b><br>
admin@AS7326-56X:~$ vtysh<br>
Hello, this is FRRouting (version 7.2.1-sonic).<Br>
Copyright 1996-2005 Kunihiro Ishiguro, et al.<br>
AS7326-56X# configure terminal<br>
AS7326-56X(config)# router bgp 65100<br>
AS7326-56X(config-router)# bgp router-id 1.1.1.1<br>
AS7326-56X(config-router)# neighbor 10.0.0.1 remote-as 65100<br>
AS7326-56X(config-router)# address-family ipv4<br>
AS7326-56X(config-router-af)# network 1.1.1.1/32<br>
AS7326-56X(config-router-af)# end<br>
AS7326-56X# exit<br>
<b>AS5835-54X:</b><br>
admin@AS5835-54X:~$ vtysh<br>
Hello, this is FRRouting (version 7.2.1-sonic).<br>
Copyright 1996-2005 Kunihiro Ishiguro, et al.<br>
AS5835-54X# configure terminal<Br>
AS5835-54X(config)# router bgp 65100<Br>
AS5835-54X(config-router)# bgp router-id 2.2.2.2<br>
AS5835-54X(config-router)# neighbor 10.0.0.0 remote-as 65100<Br>
AS5835-54X(config-router)# address-family ipv4<br>
AS5835-54X(config-router-af)# network 2.2.2.2/32<Br>
AS5835-54X(config-router-af)# end<br>
AS5835-54X# exit<br>
<br>
<u><b>Step 3. Create Vxlan</b><br></u>
<b>AS7326-56X:</b>
admin@AS7326-56X:~$ config vxlan add vtep 1.1.1.1<br>
admin@AS7326-56X:~$ config vxlan evpn_nvo add nvo vtep<Br>
admin@AS7326-56X:~$ config vxlan map add vtep 30 3000<br>
<b>AS5835-54X:</b><br>
admin@AS5835-54X:~$ config vxlan add vtep 2.2.2.2<br>
admin@AS5835-54X:~$ config vxlan evpn_nvo add nvo vtep<br>
admin@AS5835-54X:~$ config vxlan map add vtep 30 3000<br>
<b>Note :</b><br>
VNI (VxLAN Network Identifier) : virtual extension of VLAN over IP network.<br>
VTEP (VXLAN Tunnel End Point) : an entity that originates and/or terminates VXLAN tunnels which is specified by a source IP address.<Br>
Only one VTEP is allowed on one device. Please use loopback IP address for VTEP's IP address.<br>
NVO (Network Virtualization Overlay)<br>
Only one NVO is allowed on one device.<br>
VNI (VxLAN Network Identifier) : virtual extension of VLAN over IP network.<br>
<br>
<b><u>Step 4: Advertise  L2VPN EVPN routes.</u></b><br> 
<b>AS7326-56X:</b><br>
admin@AS7326-56X:~$ vtysh<br>
Hello, this is FRRouting (version 7.2.1-sonic).<Br>
Copyright 1996-2005 Kunihiro Ishiguro, et al.<br>
AS7326-56X#<br>
AS7326-56X# configure terminal<Br>
AS7326-56X(config)# router bgp 65100<br>
AS7326-56X(config-router)# address-family l2vpn evpn<br>
AS7326-56X(config-router-af)# neighbor 10.0.0.1 activate<br>
AS7326-56X(config-router-af)# advertise-all-vni<br>
AS5835-54X:<br>
admin@AS5835-54X:~$ vtysh<Br>
Hello, this is FRRouting (version 7.2.1-sonic).<br>
AS5835-54X# <br>
AS5835-54X# configure terminal<br>
AS5835-54X(config)# router bgp 65100<br>
AS5835-54X(config-router)# address-family l2vpn evpn<br>
AS5835-54X(config-router-af)# neighbor 10.0.0.0 activate<br>
AS5835-54X(config-router-af)# advertise-all-vni<br>
<br>
<u><b>Check VxLAN  interface configuration.AS7326-56X:</b></u><br>
admin@AS7326-56X:~$ show vxlan interface<br> 
VTEP Information:<br>
VTEP Name : vtep, SIP : 1.1.1.1<br>
Source interface : Loopback0<Br>
AS5835-54X:<br>
admin@AS5835-54X:~$ show vxlan interface<BR> 
VTEP Information:<Br>
VTEP Name : vtep, SIP : 2.2.2.2<br>
Source interface : Loopback0<br>
<br>
<b>Check vxlan and VLAN mapping.AS7326-56X:</b><br>
admin@AS7326-56X:~$ show vxlan vlanvnimap<br>

<pre>
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
</pre>
<br><br>
<b><u>Check the status for Vxlan tunneling.</b></u><br>
<u><b>AS7326-56X:(202111.3)</b></u><br>
admin@AS7326-56X:~$ show vxlan tunnel<br>

<pre>
vxlan tunnel name    source ip    destination ip    tunnel map name    tunnel map mapping(vni -> vlan)
-------------------  -----------  ----------------  -----------------  ---------------------------------
vtep                 1.1.1.1                       map_3000_Vlan30    3000 -> Vlan30
Total count : 1
</pre>
<br><br>
<b><u>AS7326-56X:(202111.3)</u></b><br>
admin@AS7326-56X:~$ show vxlan remotevtep<br>

<pre>
+---------+---------+-------------------+--------------+
| SIP 	| DIP 	| Creation Source   | OperStatus   |
+=========+=========+===================+==============+

| 1.1.1.1 | 2.2.2.2 | EVPN          	| oper_up  	|
+---------+---------+-------------------+--------------+
Total count : 1
</pre>
<br><br>
<u><b>AS5835-54X:(202111.3)</b></u><br>
admin@AS5835-54X:~$ show vxlan tunnel<br>
<pre>
vxlan tunnel name    source ip    destination ip    tunnel map name    tunnel map mapping(vni -> vlan)
-------------------  -----------  ----------------  -----------------  ---------------------------------
vtep                 2.2.2.2                      map_3000_Vlan30    3000 -> Vlan30
Total count : 1
</pre>
<br><br>
<u><b>AS5835-54X:(202111.3)</b></u><br>
admin@AS5835-54X:~$ show vxlan remotevtep<br>

<pre>
| SIP 	| DIP 	| Creation Source   | OperStatus   |
+=========+=========+===================+==============+
| 2.2.2.2 | 1.1.1.1 | EVPN          	| oper_up  	|
+---------+---------+-------------------+--------------+
Total count : 1
 </pre>
<br><br>
<b><u>Check the Mac learning.</u></b><br>
<b>AS7326-56X:(202111.3)</b><br>
<br>
admin@AS7326-56X:~$ show mac<br>

<pre>
  No.	Vlan  MacAddress     	Port            	Type
-----  ------  -----------------  ------------------  -------
	1  	30  8C:EA:1B:30:DA:50  VxLAN DIP: 2.2.2.2  Static
	2  	30  8C:EA:1B:30:DA:4F  Ethernet0       	Dynamic
Total number of entries 2
</pre>
<br><br>
<u><b>AS7326-56X(202111.3)</b></u><br>
admin@AS7326-56X:~$ show mac<br>

<pre>
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
</pre>
<br><br>
<u><b>AS5835-54X:(202111.3)</b></u><br>
admin@AS5835-54X:~$ show mac<br>

<pre>
  No.	Vlan  MacAddress     	Port            	Type
-----  ------  -----------------  ------------------  -------
	1  	30  8C:EA:1B:30:DA:50  Ethernet0       	Dynamic
	2  	30  8C:EA:1B:30:DA:4F  VxLAN DIP: 1.1.1.1  Static
Total number of entries 2
</pre>
<br><br>
<u><b>AS5835-54X:(202111.3)</b></u><br>
admin@AS5835-54X:~$ show mac<br>

<pre>
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
 </pre>
 <br><br>
<b>Check IPv4 BGP session</b><br>
<b><u>AS7326-56X:</u></b><br>
<br>
AS7326-56X# show bgp ipv4 summary<br>
IPv4 Unicast Summary:<br>
BGP router identifier 1.1.1.1, local AS number 65100 vrf-id 0<br>
BGP table version 6<br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 20 KiB of memory<br>

<pre>
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.1    	4  	65100  	80  	85    	0	0	0 01:01:28        	1
Total number of neighbors 1
</pre>
<br><br>
<u><b>AS5835-54X:</b></u><br>
AS5835-54X# show bgp ipv4 summary<br>
IPv4 Unicast Summary:<br>
BGP router identifier 2.2.2.2, local AS number 65100 vrf-id 0<br>
BGP table version 6<Br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 20 KiB of memory<br>

<pre>
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.0    	4  	65100  	79  	79    	0	0	0 01:01:28        	1
Total number of neighbors 1
</pre>
<br><br>
<u><b>Check L2EVPN BGP session</u></b><br>
<br>
<b><u>AS7326-56X:</b></u><br>
AS7326-56X# show bgp l2vpn evpn summary<br>
BGP router identifier 1.1.1.1, local AS number 65100 vrf-id 0<br>
BGP table version 0<br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 20 KiB of memory<br>

<pre>
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.1    	4  	65100  	82  	87    	0	0	0 01:03:43        	3
Total number of neighbors 1
</pre>
<br><br>
AS5835-54X:<br>
AS5835-54X# show bgp l2vpn evpn summary<Br>
BGP router identifier 2.2.2.2, local AS number 65100 vrf-id 0<br>
BGP table version 0<br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 20 KiB of memory<br>

<pre>
Neighbor    	V     	AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
10.0.0.0    	4  	65100  	81  	81    	0	0	0 01:03:43        	3
Total number of neighbors 1
</pre>
<br><br>
<u><b>Check underlay routing</b></u><br>
<u><b>AS7326-56X:</b></u><br>
<br><br>
AS7326-56X# show ip route<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<br>
F - PBR, f - OpenFabric,<br>
\> - selected route, * - FIB route, q - queued route, r - rejected route<br>
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 00:49:45<br>
C>* 1.1.1.1/32 is directly connected, Loopback0, 00:49:14<br>
B>* 2.2.2.2/32 [200/0] via 10.0.0.1, Ethernet52, 00:42:04<br>
C>* 10.0.0.0/31 is directly connected, Ethernet52, 00:49:13<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:49:45<br>
<br>
<b><u>AS5835-54X:</u></b><br>
<br>
AS5835-54X# show ip route<br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<Br>
T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,<Br>
F - PBR, f - OpenFabric,<br>
\> - selected route, * - FIB route, q - queued route, r - rejected route<Br>
K>* 0.0.0.0/0 [0/0] via 188.188.1.1, eth0, 00:49:57<br>
B>* 1.1.1.1/32 [200/0] via 10.0.0.0, Ethernet52, 00:42:25<br>
C>* 2.2.2.2/32 is directly connected, Loopback0, 00:46:34<br>
C>* 10.0.0.0/31 is directly connected, Ethernet52, 00:46:33<br>
C>* 188.188.0.0/16 is directly connected, eth0, 00:49:57<br>
<br>
<u><b>Check Vxlan VNI status</b></u><br>
<u><b>AS7326-56X:</b></u><br>
AS7326-56X# show evpn vni detail<br> 
VNI: 3000<br>
Type: L2<br>
Tenant VRF: default<br>
VxLAN interface: vtep-30<br>
VxLAN ifIndex: 68<br>
Local VTEP IP: 1.1.1.1<br>
Mcast group: 0.0.0.0<br>
Remote VTEPs for this VNI:<Br>
2.2.2.2 flood: HER<br>
Number of MACs (local and remote) known for this VNI: 3<br>
Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 3<br>
Advertise-gw-macip: No<br>
<br><br>
<b><u>AS5835-54X:</u></b><br>
AS5835-54X# show evpn vni detail<br> 
VNI: 3000<br>
Type: L2<br>
Tenant VRF: default<br>
VxLAN interface: vtep-30<br>
VxLAN ifIndex: 66<br>
Local VTEP IP: 2.2.2.2<br>
Mcast group: 0.0.0.0<Br>
Remote VTEPs for this VNI:<br>
1.1.1.1 flood: HER<br>
Number of MACs (local and remote) known for this VNI: 3<br>
Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 3<br>
Advertise-gw-macip: No<br>
<br><br>
<b><u>Check the evpn mac learning</u></b><br>
<b><u>AS7326-56X:</u></b><br>
AS7326-56X# show evpn mac vni all<br>
VNI 3000 #MACs (local and remote) 3<br>
<pre>
MAC           	Type   Intf/Remote VTEP  	VLAN  Seq #'s
8c:ea:1b:30:da:50 remote 2.2.2.2                 	1/0
8c:ea:1b:30:da:4f local  Ethernet0         	30	0/0
</pre>
<br><br>
<u><b>AS5835-54X:</b></u><br>
AS5835-54X# show evpn mac vni all<br>
</pre>
VNI 3000 #MACs (local and remote) 3MAC           	Type   Intf/Remote VTEP  	VLAN  Seq #'s
8c:ea:1b:30:da:50 local  Ethernet0         	30	0/0
8c:ea:1b:30:da:4f remote 1.1.1.1                 	1/0
</pre>
<br><br>
<u><b>Check the type 2 EVPN route</b></u><br>
<b><u>AS7326-56X:</u></b><br>
AS7326-56X# show bgp l2vpn evpn route type macip<br> 
BGP table version is 2, local router ID is 1.1.1.1<br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]<Br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<Br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
<pre>
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
</pre>
<br><br>
<b><u>AS5835-54X:</u></b><br>
AS5835-54X# show bgp l2vpn evpn route type macip<br> 
BGP table version is 2, local router ID is 2.2.2.2<Br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]<br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<Br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
<pre>
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
</pre>
<br><br>
<b><u>Check the type 3 EVPN route</u></b><br>
 <b><u>AS7326-56X:</b></u><br>
<br><br>
AS7326-56X# show bgp l2vpn evpn route type multicast<br> 
BGP table version is 3, local router ID is 1.1.1.1<br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
Network Next Hop Metric LocPrf Weight Path<br>
Extended Community<br>
Route Distinguisher: 1.1.1.1:2<br>
*> [3]:[0]:[32]:[1.1.1.1]<br>
1.1.1.1 32768 i<br>
ET:8 RT:65100:3000<Br>
Route Distinguisher: 2.2.2.2:2<br>
*>i[3]:[0]:[32]:[2.2.2.2]<br>
2.2.2.2 100 0 i<br>
RT:65100:3000 ET:8<Br>
Displayed 2 prefixes (2 paths) (of requested type)<br>
<br><br>
<b><u>AS5835-54X:</u></b><br>
AS5835-54X# show bgp l2vpn evpn route type multicast<br> 
BGP table version is 3, local router ID is 2.2.2.2<br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
Network Next Hop Metric LocPrf Weight Path<br>
Extended Community<br>
Route Distinguisher: 1.1.1.1:2<br>
*>i[3]:[0]:[32]:[1.1.1.1]<br>
1.1.1.1 100 0 i<br>
RT:65100:3000 ET:8<br>
Route Distinguisher: 2.2.2.2:2<br>
*> [3]:[0]:[32]:[2.2.2.2]<br>
2.2.2.2 32768 i<br>
ET:8 RT:65100:3000<br>

</td>
</tr>
</table>