# <b> Layer 2 Switching</b>
## <b> Interface and port VLAN</b>

![interface and port vlan](../img/interface_and_port.png)

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
     <th colspan='2'>Port, VLAN</th>
    </tr>
   <tr>
  <td>

<b>#Configure Access and Trunk Mode over interfaces</b><br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching port-mode access<br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching port-mode trunk<br>
</br>
<b># Create VLANs </b><br>
set vlans vlan-id &lt;vlan_value><Br>
run show vlans<br>
</br>
<b># Add VLAN members to ethernet ports for tagged packet</b><br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching vlan members &lt;vlan_member1><br>
</br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching vlan members &lt;vlan_member2><br>
</br>
<b># Add VLAN members to ethernet ports for untagged packet</b><br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching vlan members &lt;member1> untagged<Br>
</br>
set interface gigabit-ethernet &lt;ethernet_interface> family ethernet-switching vlan members &lt;member2> untagged

  </td>
  <td>

<b>#Configure Access and Trunk Mode over interfaces</b><br>
config interface speed Ethernet&lt;interface> &lt;speed><br>
config interface advertised-speeds Ethernet&lt;interface> &lt;speed><br>
</br>
<b>#Command to set Auto Negotiation for an ethernet interface</b><Br>  
config interface autoneg Ethernet&lt;interface> enable<Br>
</br>
<b>#Command to show status of Auto Negotiation for an ethernet interface</b><Br>
show interface autoneg status Ethernet0<br>
</Br>
<b>#Command to show operational status of interface</b><br> 
show interface status<Br>
</br>
<b>#Example command to configure 4x10GE breakout  for a 40GE port</b><br>
config interface breakout Ethernet1 '4x10G'<br>
</br>
<b>#Command to show interface breakout options</b><br>
show interface breakout<br>
</br>
<b>#Command to configure FEC mode of an ethernet interface</b><br> 
config interface fec Etherne&lt;interface> &lt;FEC_MODE><br>
</br>
<b># Create VLANs</b><br> 
config vlan add &lt;vlan_value1> <br>      
config vlan add &lt;vlan_value2><br>
</br>
<b># show vlan configuration </b><br>
show vlan config <Br>
</br>
<b>#Add Interface to vlan in Tagged (Trunk) mode:</b><br>
config vlan member add &lt;vlan_value1> Ethernet&lt;interface1><br>
config vlan member add &lt;vlan_value2> Ethernet&lt;interface2><br>
</br>
<b>#Add Interface to vlan in untagged (access) mode:</b><br>
config vlan member add -u &lt;vlan_value1> Ethernet&lt;interface1><br>
config vlan member add -u &lt;vlan_value2> Ethernet&lt;interface2><br>
</br>
<b>#Command to show vlan information </b><br>
show vlan brief   <br>

  </td>
  </tr>
   </table>

  <table>
   <tr>
   <th colspan='2'>LAG</th>
 </tr>
 <tr>
  <tr>
  <td>

<b>#Command to create static LAG in an aggregated interface ae1</b><br>
<b>#Syntax</b><br>
ovs-vsctl  add-port br0 ae1 vlan_mode=trunk tag=1 -- set Interface ae1 type=pica8_lag<br>
ovs-vsctl -- set Interface ae1 options:lag_type=static<br>
ovs-vsctl -- set Interface ae1 options:members=ge-x/x/x , ge-x/x/x<Br>
</br>
<b>#Command to create dynamic LACP in an aggregated interface ae1</b><br>
set interface aggregate-ethernet ae1 aggregated-ether-options lacp enable true<br>
set interface aggregate-ethernet ae1 aggregated-ether-options min-selected-port &lt;number_of_ports><br>
set interface gigabit-ethernet ge-x/x/x ether-options 802.3ad ae1<Br>
set interface gigabit-ethernet ge-x/x/x ether-options 802.3ad ae1<br>
set interface gigabit-ethernet gge-x/x/x ether-options 802.3ad ae1<br>
set interface gigabit-ethernet ge-x/x/x ether-options 802.3ad ae1<br>
Commit<BR>
</br>
<b>#Command to display LACP LAG information</b> <BR>
run show interface aggregate-ethernet ae1<br>
</br>
<b>#Configure one LAG ae1 with three memberports.</b><br>
set interface gigabit-ethernet ge-x/y/z ether-options 802.3ad ae1<br>
set interface gigabit-ethernet ge-x/y/z ether-options 802.3ad ae1<br>
set interface gigabit-ethernet ge-x/y/z ether-options 802.3ad ae1<br>

  </td>
  <td>

<b>#Create port channel</b><br>
<b>#syntax </b><br>
config portchannel add PortChannel&lt;Channel1><br>
</br>
<b>#Add members to port channel</b><br>
config portchannel add PortChannel&lt;Channel1>  Ethernet&lt;interface><br>
</br>
<b># Command to verify port channel interface</b><br>
show interface portchannel<Br>
</br>
<b># Command to show vlan status</b><br> 
show vlan brief <br>
</br>
<b># Command to show ip interface status</b><br> 
show ip interfaces<br>
show interfaces status<br>
<b>#Command to create a PortChannel interface and set the specific LACP key.</b><br>
config portchannel add PortChannel&lt;Channel1>  --lacp-key &lt;Key-number><br>
config portchannel member add PortChannel&lt;Channel1><br>
 Ethernet&lt;interface><br>
</br>
<b>#Command to create a PortChannel interface in fast rate mode</b><br>
config portchannel add PortChannel&lt;number> --fast-rate true<br>
</br>
<b>#Command to create a PortChannel interface in static mode</b><br>
config portchannel add PortChannel&lt;interface>  --static true<br>
</br>
<b>#Command to add member ports to PortChannel interface</b><br>
config portchannel member add PortChannel&lt;number> Ethernet&lt;interface1><Br> 
config portchannel member add PortChannel&lt;number> Ethernet&lt;interface2> <br>
</br>
<b># Save the setting to config_db.json</b><br>
config save -y<br>
</br>
<b>#Add member ports to PortChannel interface</b><br>
config portchannel member add PortChannel&lt;interface> Ethernet&lt;interface1><Br> 
config portchannel member add PortChannel&lt;interface> Etherne&lt;interface2><Br> 
</br>
<b># Command to show interface portchannel</b><br>
 show interfaces portchannel <br>

  </td>
  </tr>
  </table>

 <table>
 <tr>
   <th>PICOS</th>
   <th>SONiC</th>
 </tr>
 <tr>
 <th colspan='2'>FDB/MAC</th>
 </tr>
 <tr>
  <tr>
  <td>

<b># Command for MAC  Learning Configurations-</b><Br> 
set interface ethernet-switching-options mac-table-aging-time &lt;timer><br>
</br>
<b>#Command to show MAC entries learned</b><br> 
run show ethernet-switching table

  </td>
  <td>

<b>#Display  the MAC (FDB) entries</b><Br>
show mac<Br>
</br>
<b>#Display the MACs learned on the particular VLAN ID</b><Br>
show mac -v &lt;vlan_value><br>
</br>
<b>#Display  the MACs learned on the particular port</b><br>
show mac -p Ethernet&lt;interface><Br>
</br>
<b>#Clear the MAC (FBD) table</b><br>
sonic-clear FDB  all<br>
</br>
<b>#Check MAC aging time</b><br>
 show mac aging-time<br>

  </td>
  </tr>
  </table>
