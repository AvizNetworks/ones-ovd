## L3-VXLAN Symmetric IRB Configuration

![L3-VXLAN](../img/L3-VXLAN-Sym.png)

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
<th>PICOS </th>
<th>SONiC</th>
</tr>
<tr>
<td>

<b># Configure physical interfaces, VLAN interfaces and assign VLAN IDs and IP addresses.</b><br>
set interface gigabit-ethernet ge-x/y/z  family ethernet-switching native-vlan-id &lt;vlan-id1><br>
set interface gigabit-ethernet ge-x/y/z  family ethernet-switching native-vlan-id &lt;vlan-id2><br>
<br>
set interface gigabit-ethernet ge-x/y/z  family ethernet-switching port-mode "trunk"<br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching vlan members &lt;vlan-id1><br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching vlan members &lt;vlan-id2><br>
<br>
set l3-interface loopback lo address &lt;SYSTEM_LOOPBACK1>  prefix-length 32<br>
set l3-interface loopback lo address &lt;SYSTEM_LOOPBACK2>  prefix-length 32<Br>
set l3-interface loopback lo address &lt;SYSTEM_LOOPBACK_IPV6>  prefix-length 128<br>
<br>
set l3-interface vlan-interface vlan&lt;VLAN_NUMBER>  vrf "VRF_NAME"<br>
set l3-interface vlan-interface vlan&lt;VLAN_NUMBER>  address &lt;IP_ADDRESS>  prefix-length &lt;SUBNET_LENGTH><br>
<br>
set l3-interface vlan-interface vlan&lt;VLAN_NUMBER>  vrf "VRF_NAME"<br>
<br>
<b>#Enable IP routing and configure VRF and hostname</b><br>
set ip routing enable true<br>
set ip vrf &lt;VRF_NAME><br>
set vxlans vrf &lt;VRF_NAME>  l3-vni &lt;VNI_VALUE>  prefix-routes-only<br>
delete vxlans vrf &lt;VRF_NAME>  l3-vni &lt;VNI_VALUE>  prefix-routes-only<br>
set vxlans vrf vrf1 l3-vni &lt;VNI_VALUE>  prefix-routes-only<br>
<br><br>
<b># Enable IP Routing and Configure VRF</b><br>
set ip routing enable true<br>
set ip vrf vrf1<br>
<br>
<b>#Create an L3 VNI in vrf1.</b><br>
set vxlans source-interface lo address &lt;SYSTEM_LOOPBACK><br>
set vxlans vrf &lt;VRF-NAME> l3-vni &lt;VNI_VALUE><br>
<br>
<b>#Advertise all VNI through BGP routing</b><br>
set protocol bgp evpn advertise-all-vni<br>
<br>
<b>#Enable EVPN Between BGP Peers</b><br>
set protocols bgp local-as &lt;LOCAL_AS_NUMBER><br>
set protocols bgp router-id &lt;SYSTEM_LOOPBACK><br>
set protocols bgp neighbor &lt;ebgp_neighbor_ip>  remote-as &lt;REMOTE_AS_NUMBER><br>
set protocols bgp ebgp-requires-policy false<br>
set protocols bgp local-as &lt;LOCAL_ASN_NUMBER><br>
set protocols bgp router-id &lt;SYSTEM_LOOPBACK><br>
set protocols bgp neighbor &lt;ebgp_neighbor_ip> remote-as "external"<br>
set protocols bgp neighbor &lt;ebgp_neighbor_ip>  update-source "&lt;SYSTEM_LOOPBACK>”<br>
set protocols bgp neighbor &lt;ebgp_neighbor_ip>  evpn activate true<br>
set protocols bgp ipv4-unicast network &lt;Prefix_subnet_advertised> <br>
<br>
<b># Configure BGP routing and advertise EVPN routes</b><br> 
set protocols bgp evpn advertise-all-vni<br>
set protocols bgp evpn advertise ipv4-unicast<br>
set protocols bgp vrf &lt;VRF_NAME>  local-as &lt;LOCAL_AS_NUMBER><br>
set protocols bgp vrf &lt;VRF_NAME>  router-id &lt;SYSTEM_LOOPBACK><br>
set protocols bgp vrf &lt;VRF_NAME>  ipv4-unicast network &lt;PREFIX_SUBNET_ADVERTISED><br>
set protocols bgp vrf &lt;VRF_NAME>  evpn advertise ipv4-unicast<br>

</td>
<td>

<b># Configure physical interfaces, VLAN interfaces and assign VLAN IDs and IP addresses</b>
<b>config interface ip add Loopback0 &lt;SYSTEM_LOOPBACK></b><br>
<br>
<b>#Configure VRF Setting</b><br>
config vrf add &lt;VRF-NAME><br>
config interface vrf bind VLAN&lt;VLAN_NUMBER> &lt;VRF-NAME><br>
config interface ip add VLAN&lt;VLAN_NUMBER> &lt;IP_ADDRESS><br>
<br>
<b>#Create VxLAN,map VNI to VLAN</b><br>
config vxlan add vtep &lt;SOURCE_VTEP_IP><br>
config vxlan evpn_nvo add nvo vtep<br>
config vxlan map add vtep &lt;VLAN-ID> &lt;VNI_VALUE><Br>
config save -y <br>
<br>
<b>#Configure layer3 VNI and map it to VRF value</b><br>
config vrf add_vrf_vni_map &lt;VRF-NAME> &lt;VNI_VALUE>  <br>
config save -y <br>
<br>
<b>#Establish a BGP environment for EVPN</b><br>
\# vtysh command<br>
router bgp &lt;LOCAL_AS_NUMBER> <br>
neighbor &lt;ebgp_neighbor_ip> remote-as &lt;REMOTE_AS_NUMBER><br>
address-family ipv4 unicast<br>
network %lt;PREFIX_ADVERTISED><br>
exit<br>
address-family l2vpn evpn<br>
neighbor &lt;ebgp_neighbor_ip> activate<br> =
advertise-all-vni<br>
end<br>
<br>
<b># Configure VRF and VNI values</b> <br>
configure terminal<br>
vrf &lt;VRF-NAME><br>
vni &lt;VNI_VALUE><br>
end<br>
<br>
<b># Configure BGP routing and advertise EVPN routes</b><br> 
router bgp &lt;LOCAL_AS_NUMBER>  vrf &lt;VRF-NAME><br>    
address-family ipv4 unicast<br>                                        
redistribute connected<br>                                   
address-family l2vpn evpn<br>                                          
advertise ipv4 unicast<br>
write<br>
<br>
<b># Commands to verify VXLAN tunnels</b><br> 
show vxlan interface<br>
show vxlan vlanvnimap<br>
show vxlan tunnel<br>
show vxlan remotevtep<Br>
<br>
<b>#Commands to verify EVPN routes and BGP routes</b><br> 
show evpn vni detail<br>
show bgp summary<br>
show ip route vrf all<Br>

</td>
</tr>
</table>
<br>

![L3-VXLAN EVPN](../img/L3-VXLAN-EVPN.png)

<br>
<table>
<tr>
<th>Sample SONiC L3-VXLAN EVPN Symmetric IRB Example</th>
</tr>
<tr>
<td>

</u><b>#Configure IP address and  Loopback IPs of both switches.</b></u><br>
</u></b>AS5835-54X</b></u><br>
admin@SONIC01:~$ config interface ip add Loopback0 1.1.1.1/32<br>
admin@SONIC01:~$ config interface ip add Ethernet48 10.0.0.4/31<br>
<br>
<u><b>A4630-54PE</b></u><br>
admin@SONIC02:~$ config interface ip add Loopback0 2.2.2.2/32<br>
admin@SONIC02:~$ config interface ip add Ethernet52 10.0.0.5/31<br>
<br>
<b># Configure VRF Setting</b><br>
<u><b>AS5835-54X</b></u><br>
admin@SONIC01:~$ config vrf add Vrf01<br>
admin@SONIC01:~$ config interface vrf bind Vlan30 Vrf01<br>
admin@SONIC01:~$ config interface vrf bind Vlan10 Vrf01<br>
admin@SONIC01:~$ config interface ip add Vlan10 192.168.1.254/24 <br>
<br>
<u><b>A4630-54PE</b></u><br>
admin@SONIC02:~$ config vrf add Vrf01<br>
admin@SONIC02:~$ config interface vrf bind Vlan30 Vrf01<br>
admin@SONIC02:~$ config interface vrf bind Vlan20 Vrf01<Br>
admin@SONIC02:~$ config interface ip add Vlan20 192.168.2.254/24<br>
<br>
<b><u>#Establish BGP Session between Ethernet48 and Ethernet52</u></b><br>  
<b><u>AS5835-54X</u></b><br>
admin@SONIC01:~$ vtysh<br>
sonic# configure terminal<br>
sonic(config)# router bgp 65100<br>
sonic(config-router)# neighbor 10.0.0.5 remote-as 65100<br>
sonic(config-router)# address-family ipv4 unicast<br>
sonic(config-router-af)# network 1.1.1.1/32<br>
sonic(config-router-af)# exit<br>
sonic(config-router)# address-family l2vpn evpn<br>
sonic(config-router-af)# neighbor 10.0.0.5 activate<br>
sonic(config-router-af)# advertise-all-vni<br>
sonic(config-router-af)# end<br>
<Br>
sonic# configure terminal<br>
sonic(config)# vrf Vrf01<br>
sonic(config-vrf)# vni 3000<br>
sonic(config-vrf)# end<br>
sonic# configure terminal<br> 
sonic(config)# router bgp 65100 vrf Vrf01<br>
sonic(config-router)# address-family ipv4 unicast<br>
sonic(config-router-af)# redistribute connected<br>
sonic(config-router-af)# exit<br>
sonic(config-router)# address-family l2vpn evpn<br>
sonic(config-router-af)# advertise ipv4 unicast <br>
sonic(config-router-af)# end<br>
sonic# write<br>
<br>
<u><b>A4630-54PE</b></u><br>
admin@SONIC02:~$ vtysh<br>
sonic# configure terminal<br>
sonic(config)# router bgp 65100<br>
sonic(config-router)# neighbor 10.0.0.4 remote-as 65100<br>             
sonic(config-router)# address-family ipv4 unicast<br>
sonic(config-router-af)# network 2.2.2.2/32<br>
sonic(config-router-af)# exit<br>
sonic(config-router)# address-family l2vpn evpn<br>
sonic(config-router-af)# neighbor 10.0.0.4 activate<br>
sonic(config-router-af)# advertise-all-vni<br>
sonic(config-router-af)# end<br>
sonic# configure terminal<br>
sonic(config)# vrf Vrf01<br>
sonic(config-vrf)# vni 3000<br>
sonic(config-vrf)# end<br>
sonic# configure terminal<br> 
sonic(config)# router bgp 65100 vrf Vrf01<br>
sonic(config-router)# address-family ipv4 unicast<br>
sonic(config-router-af)# redistribute connected<br>
sonic(config-router-af)# exit<br>
sonic(config-router)# address-family l2vpn evpn<br>
sonic(config-router-af)# advertise ipv4 unicast<br>
sonic(config-router-af)# end<br>
sonic# write<br>
<br>
<b><u>#Create Vxlan</u></b><br>
<b><u>AS5835-54X</u></b><br>
<b># configuring VTEP_name (vtep) and its IP address</b><br> 
admin@SONIC01:~$ config vxlan add vtep 1.1.1.1<br>
<br>
<b>#create nvo_name (nvo) and bind it to VTEP_name (vtep)</b><br>
admin@SONIC01:~$ config vxlan evpn_nvo add nvo vtep<br>
<br>
<b># Command to map VXLAN VNI to VLAN</b><br>
admin@SONIC01:~$ config vxlan map add vtep 10 1000<br>
admin@SONIC01:~$ config vxlan map add vtep 30 3000<br>
admin@SONIC01:~$ config save -y<br>
<br>
<b><u>#A4630-54PE</u></b><br>
<b># configuring VTEP_name (vtep) and its IP address</b><br> 
admin@SONIC02:~$ config vxlan add vtep 2.2.2.2<br>
<br>
<b>#create nvo_name (nvo) and bind it to VTEP_name (vtep)</b><br>
admin@SONIC02:~$ config vxlan evpn_nvo add nvo vtep<br>
<br>
<b># Command to map VXLAN VNI to VLAN</b><br>
admin@SONIC02:~$ config vxlan map add vtep 20 2000<br>
admin@SONIC02:~$ config vxlan map add vtep 30 3000<br>
admin@SONIC02:~$ config save -y<br>
<br>
<b># Configure the  layer3 VNI on both switches.</b><br>
<b><u>AS5835-54X</u></b><br>
admin@SONIC01:~$ config vrf add_vrf_vni_map Vrf01 3000<br>
<br>
<b><u>A4630-54PE</u></b><br>
admin@SONIC01:~$ config vrf add_vrf_vni_map Vrf01 3000<br>
<br>
<b># Verify  EVPN-VNI Route Status</b>
<b><u>AS5835-54X</u></b><br>
sonic# show evpn vni detail<br>
VNI: 1000<br>
 Type: L2<br>
 Tenant VRF: Vrf01<br>
 VxLAN interface: vtep-10<br>
 VxLAN ifIndex: 67<br>
 SVI interface: Vlan10<br>
 SVI ifIndex: 9<br>
 Local VTEP IP: 1.1.1.1<br>
 Mcast group: 0.0.0.0<br>
 No remote VTEPs known for this VNI<br>
 Number of MACs (local and remote) known for this VNI: 1<br>
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 1<br>
 Advertise-gw-macip: No<br>
 Advertise-svi-macip: No<br>
VNI: 3000<br>
  Type: L3<br>
  Tenant VRF: Vrf01<br>
  Local Vtep Ip: 1.1.1.1<br>
  Vxlan-Intf: vtep-30<br>
  SVI-If: Vlan30<br>
  State: Up<br>
  VNI Filter: none<br>
  System MAC: 00:a0:c9:00:00:00<br>
  Router MAC: 00:a0:c9:00:00:00<br>
  L2 VNIs: 1000<br>
<br>
<b><u>#A4630-54PE</u></b><br>
sonic# show evpn vni detail<br>
VNI: 2000<br>
 Type: L2<br>
 Tenant VRF: Vrf01<br>
 VxLAN interface: vtep-20<br>
 VxLAN ifIndex: 78<br>
 SVI interface: Vlan20<br>
 SVI ifIndex: 76<br>
 Local VTEP IP: 2.2.2.2<br>
 Mcast group: 0.0.0.0<br>
 No remote VTEPs known for this VNI<br>
 Number of MACs (local and remote) known for this VNI: 1<br>
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 1<br>
 Advertise-gw-macip: No<br>
 Advertise-svi-macip: No<br>
VNI: 3000<br>
  Type: L3<br>
  Tenant VRF: Vrf01<br>
  Local Vtep Ip: 2.2.2.2<br>
  Vxlan-Intf: vtep-30<br>
  SVI-If: Vlan30<br>
  State: Up<br>
  VNI Filter: none<br>
  System MAC: 68:21:5f:29:c0:d2<br>
  Router MAC: 68:21:5f:29:c0:d2<br>
  L2 VNIs: 2000<br>
<br>
<br>
<b># Verify BGP Route Summary</b><br>
<br>
<b><u>AS5835-54X</u></b><br>
sonic# show bgp summary<br>
IPv4 Unicast Summary (VRF default):<br>
BGP router identifier 188.188.9.14, local AS number 65100 vrf-id 0<br>
BGP table version 17<br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 723 KiB of memory<br>

<pre>
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.5        4      65100      1436      1449        0    0    0 03:02:18            1        1 N/A
Total number of neighbors 1
</pre>
<br>
L2VPN EVPN Summary (VRF default):<br>
BGP router identifier 188.188.9.14, local AS number 65100 vrf-id 0<br>
BGP table version 0<br>
RIB entries 27, using 4968 bytes of memory<br>
Peers 1, using 723 KiB of memory<br>

<pre>
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.5        4      65100      1436      1449        0    0    0 03:02:18            4        4 N/A
Total number of neighbors 1
</pre>
<br>
<b><u>A4630-54PE</u></b><br>
sonic# show bgp summary<br>
IPv4 Unicast Summary (VRF default):<br>
BGP router identifier 188.188.9.6, local AS number 65100 vrf-id 0<br>
BGP table version 8<br>
RIB entries 3, using 552 bytes of memory<br>
Peers 1, using 723 KiB of memory<br>

<pre>
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.4        4      65100       220       221        0    0    0 03:02:18            1        1 N/A
Total number of neighbors 1
</pre>
<br>
L2VPN EVPN Summary (VRF default):<br>
BGP router identifier 188.188.9.6, local AS number 65100 vrf-id 0<br>
BGP table version 0<br>
RIB entries 11, using 2024 bytes of memory<br>
Peers 1, using 723 KiB of memory<br>

<pre>
Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
10.0.0.4        4      65100       220       221        0    0    0 03:02:18            4        4 N/A
Total number of neighbors 1
</pre>
<br>
<b># Validate EVPN route learning</b><br>
<b><u>AS5835-54X</u></b><br>
<b>sonic# show ip route vrf all</b><br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued, r - rejected, b - backup<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t - trapped, o - offload failure<br>
VRF Vrf01:<br>
C>* 192.168.1.0/24 is directly connected, Vlan10, 03:18:41<br>
K>* 192.168.1.254/32 [0/0] is directly connected, Vlan10, 03:18:41<br>
B>* 192.168.2.0/24 [200/0] via 2.2.2.2, Vlan30 onlink, weight 1, 03:04:24<br>
B>* 192.168.2.2/32 [200/0] via 2.2.2.2, Vlan30 onlink, weight 1, 02:21:18<br>
VRF default:<br>
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 22:59:15<br>
K * 1.1.1.1/32 [0/0] is directly connected, Loopback0, 22:54:06<br>
C>* 1.1.1.1/32 is directly connected, Loopback0, 22:54:06<br>
B>* 2.2.2.2/32 [200/0] via 10.0.0.5, Ethernet48, weight 1, 03:04:24<br>
C>* 10.0.0.4/31 is directly connected, Ethernet48, 03:07:18<br>
K>* 10.0.0.4/32 [0/0] is directly connected, Ethernet48, 22:45:24<br>
C>* 188.188.0.0/16 is directly connected, eth0, 22:59:15<br>
<br>
sonic# show bgp l2vpn evpn<br>
BGP table version is 14, local router ID is 188.188.9.14<br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]<br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
<br>

<pre>
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
</pre>

<b><u>>#A4630-54PE</u></b><btr>
<b>sonic# show ip route vrf all</b><br>
Codes: K - kernel route, C - connected, S - static, R - RIP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T - Table, v - VNC, V - VNC-Direct, A - Babel, F - PBR,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f - OpenFabric,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> - selected route, * - FIB route, q - queued, r - rejected, b - backup<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t - trapped, o - offload failure<br>
VRF Vrf01:<br>
B>* 192.168.1.0/24 [200/0] via 1.1.1.1, Vlan30 onlink, weight 1, 03:04:23<br>
B>* 192.168.1.1/32 [200/0] via 1.1.1.1, Vlan30 onlink, weight 1, 02:20:51<br>
C>* 192.168.2.0/24 is directly connected, Vlan20, 03:07:28<br>
K>* 192.168.2.254/32 [0/0] is directly connected, Vlan20, 03:07:28<br>
VRF default:<br>
K>* 0.0.0.0/0 [0/202] via 188.188.1.1, eth0, 03:17:24<br>
B>* 1.1.1.1/32 [200/0] via 10.0.0.4, Ethernet52, weight 1, 03:04:23<br>
K * 2.2.2.2/32 [0/0] is directly connected, Loopback0, 03:07:29<br>
C>* 2.2.2.2/32 is directly connected, Loopback0, 03:07:29<br>
C>* 10.0.0.4/31 is directly connected, Ethernet52, 03:07:17<br>
K>* 10.0.0.5/32 [0/0] is directly connected, Ethernet52, 03:07:18<br>
C>* 188.188.0.0/16 is directly connected, eth0, 03:17:24<br>
<br>
sonic# show bgp l2vpn evpn<br>
BGP table version is 12, local router ID is 188.188.9.6<br>
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal<br>
Origin codes: i - IGP, e - EGP, ? - incomplete<br>
EVPN type-1 prefix: [1]:[EthTag]:[ESI]:[IPlen]:[VTEP-IP]<br>
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]<br>
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]<br>
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]<br>
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]<br>
<pre>
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
</pre>

</td>
</tr>
</table>