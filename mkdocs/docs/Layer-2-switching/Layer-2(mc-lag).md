## Multi-Chassis Link Aggregation Group (MC-LAG) 

This is a pair of links that terminates on two cooperating switches and appears as an ordinary link aggregation group (LAG). 
### Layer 2 Multi Chassis LAG

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

<b>#Add Port Channel</b>
config port channel add &lt;PCH ID><br>
<b>#Add Members</b>
config port channel member add &lt;PCH-ID> &lt;member-port>

  </td>
  </tr>
  <tr>
  <th colspan='2'>MC-LAG</th>
  </tr>
  <tr>
  <td>

<b>#MCLAG Domain</b>
set protocols mlag domain
set protocols mlag domain <domain-id> node <0 | 1>

<b>#MCLAG PEER</b>
set protocols mlag domain &lt;domain-id> interface &lt;lag-interface> link &lt;link-id>
set protocols mlag domain &lt;domain-id> peer-ip &lt;peer-ipv4-address> peer-link &lt;peer-interface-name>
set protocols mlag domain &lt;domain-id> peer-ip &lt;peer-ipv4-address> peer-vlan &lt;vlan-id>

<b>#MCLAG Members</b>
set interface gigabit-ethernet <port-id> ether-options 802.3ad <lag-if>

#MCLAG Show
run show mlag link {<link-id>| summary}


  </td>
  <td>

<b>#MCLAG Domain & Peer Configuration</b>
config interface ip add &lt;VLAN ID> &lt;SVI-IP>
config mclag add &lt;mclag-id> &lt;local-ip> &lt;remote-ip> &lt;peer-pch>
config mclag unique-ip add &lt;peer-vlan>

<b>#MCLAG  Members</b>

config mclag member add <mclag-id> <member-pch>

<b>#MCLAG Show</b>
show mclag brief
Show mac

  </td>
  </tr>
  <tr>
  <th colspan='2'>VLAN</th>
  </tr>
  <tr>
  <td>

<b>#VLAN Configuration</b>
set vlans vlan-id <id>
set interface aggregate-ethernet &lt;lag-if> family ethernet-switching port-mode trunk
set interface aggregate-ethernet &lt;lag-if> family ethernet-switching vlan members &lt;vid>

  </td>
  <td>

<b>#VLAN Configuration</b>
config vlan add &lt;id>
config vlan member add &lt;vid> &lt;pch-id>

  </td>
  </tr>
</table>

<table>
<tr>
<th colspan='2'>SONiC Port Channel Configuration</th>
</tr>
<tr>
<td>

<b># Creating port channel on the MCLAG pair switches running SONiC</b> 
config portchannel add PortChannel01
config portchannel add PortChannel02
config portchannel add PortChannel03
config portchannel member add PortChannel01 Ethernet0
config portchannel member add PortChannel02 Ethernet1
config portchannel member add PortChannel03 Ethernet56
config portchannel member add PortChannel03 Ethernet60

<b># Creating VLAN interface on MC LAG pair switches running SONiC</b>
config vlan add 10
config vlan add 100
config vlan member add 10 PortChannel03
config vlan member add -u 100 PortChannel01
config vlan member add 100 PortChannel02
config vlan member add 100 PortChannel03

<b>#Configure MCLAG pair switches with domain ID and child member links</b>
config mclag add 1 192.168.10.1 192.168.10.2 PortChannel03
config mclag unique-ip add Vlan10
config mclag member add 1 PortChannel01
config mclag member add 1 PortChannel02

<b>#SONiC configuration for MC LAG peer health check</b> 
config interface ip add Vlan10 192.168.10.1/24
config interface ip add Vlan10 192.168.10.2/24

<b>#SONiC Command to Display MC LAG operationalstatus</b>
 show mclag brief

<b># SONiC command to show MAC address learned for host traffic through member link interfaces</b> 
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