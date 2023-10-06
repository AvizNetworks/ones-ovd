## <b> Multi-Chassis Link Aggregation Group (MC-LAG) </b>

This is a pair of links that terminates on two cooperating switches and appears as an ordinary link aggregation group (LAG). 
### <b> Layer 2 Multi Chassis LAG</b>

![Layer 2](../img/layer2(mc-lag).png)

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
 <th colspan='2'>PortChannel(LACP) and Member</th>
 </tr>
 <tr>
  <tr>
  <td>

<b># Enable LACP</b><br>
set interface aggregate-ethernet &lt;lag-if-name><br>
 aggregated-ether-options lacp enable true<br>
</br>
<b># Add members</b><br>
set interface gigabit-ethernet &lt;port-id> ether-options 802.3ad ae1

  </td>
  <td>

<b>#Add Port Channel</b><br>
config port channel add &lt;PCH ID><br><br>
<b>#Add Members</b><br>
config port channel member add &lt;PCH-ID> &lt;member-port>

  </td>
  </tr>
  <tr>
  <th colspan='2'>MC-LAG</th>
  </tr>
  <tr>
  <td>

<b>#MCLAG Domain</b><br>
set protocols mlag domain<Br>
set protocols mlag domain <domain-id> node <0 | 1><br>
</br>
<b>#MCLAG PEER</b><br>
set protocols mlag domain &lt;domain-id> interface &lt;lag-interface> link &lt;link-id><br>
set protocols mlag domain &lt;domain-id> peer-ip &lt;peer-ipv4-address> peer-link &lt;peer-interface-name><br>
set protocols mlag domain &lt;domain-id> peer-ip &lt;peer-ipv4-address> peer-vlan &lt;vlan-id><br>
</br>
<b>#MCLAG Members</b><br>
set interface gigabit-ethernet <port-id> ether-options 802.3ad <lag-if><br>
</br>
<b>#MCLAG Show</b><br>
run show mlag link {<link-id>| summary}<Br>


  </td>
  <td>

<b>#MCLAG Domain & Peer Configuration</b><br>
config interface ip add &lt;VLAN ID> &lt;SVI-IP><br>
config mclag add &lt;mclag-id> &lt;local-ip> &lt;remote-ip> &lt;peer-pch><br>
config mclag unique-ip add &lt;peer-vlan>,br
</br>
<b>#MCLAG  Members</b><br>
</br>
config mclag member add &lt;mclag-id> &lt;member-pch><br>
</br>
<b>#MCLAG Show</b><br>
show mclag brief<br>
Show mac<br>

  </td>
  </tr>
  <tr>
  <th colspan='2'>VLAN</th>
  </tr>
  <tr>
  <td>

<b>#VLAN Configuration</b><br>
set vlans vlan-id <id><br>
set interface aggregate-ethernet &lt;lag-if> family ethernet-switching port-mode trunk<br>
set interface aggregate-ethernet &lt;lag-if> family ethernet-switching vlan members &lt;vid><br>

  </td>
  <td>

<b>#VLAN Configuration</b><br>
config vlan add &lt;id><br>
config vlan member add &lt;vid> &lt;pch-id><br>

  </td>
  </tr>
</table>

<table>
<tr>
<th colspan='2'>SONiC Port Channel Configuration</th>
</tr>
<tr>
<td colspan='2'>

<b># Creating port channel on the MCLAG pair switches running SONiC</b><br> 
config portchannel add PortChannel01<br>
config portchannel add PortChannel02<br>
config portchannel add PortChannel03<br>
config portchannel member add PortChannel01 Ethernet0<br>
config portchannel member add PortChannel02 Ethernet1<br>
config portchannel member add PortChannel03 Ethernet56<br>
config portchannel member add PortChannel03 Ethernet60<br>
</br>
<b># Creating VLAN interface on MC LAG pair switches running SONiC</b><br>
config vlan add 10<br>
config vlan add 100<br>
config vlan member add 10 PortChannel03<br>
config vlan member add -u 100 PortChannel01<br>
config vlan member add 100 PortChannel02<br>
config vlan member add 100 PortChannel03<br>
</br>
<b>#Configure MCLAG pair switches with domain ID and child member links</b><br>
config mclag add 1 192.168.10.1 192.168.10.2 PortChannel03<br>
config mclag unique-ip add Vlan10<br>
config mclag member add 1 PortChannel01<br>
config mclag member add 1 PortChannel02<br>
</br>
<b>#SONiC configuration for MC LAG peer health check</b> <br>
config interface ip add Vlan10 192.168.10.1/24<Br>
config interface ip add Vlan10 192.168.10.2/24<Br>
</br>
<b>#SONiC Command to Display MC LAG operationalstatus</b><br>
 show mclag brief<br>
</br>
<b># SONiC command to show MAC address learned for host traffic through member link interfaces</b><br> 
show mac
```
No.    Vlan  MacAddress         Port           Type
-----  ------  -----------------  -------------  -------
    1      10  68:21:5F:29:C0:D2  PortChannel03  Static
    2     100  B8:6A:97:19:BA:12  PortChannel01  Dynamic
    3     100  80:A2:35:5A:22:50  PortChannel02  Dynamic
Total number of entries 3
```
</td>
</tr>
</table>