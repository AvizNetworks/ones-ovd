## <b> SVI & DHCP Relay</b>

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
<th colspan='2'>SVI</th>
</tr>
<tr>
<td>

<b># Create VLAN IDs</b> <br>
<b>#Syntax </b><br>
set vlans vlan-id &lt;vlan1><br>
set vlans vlan-id &lt;vlan2><br>
</br>
<b># Create an interface binded to Layer3 VLAN</b><br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching native-vlan-id &lt;vlan1><br>
set interface gigabit-ethernet ge-x/y/z family ethernet-switching native-vlan-id &lt;vlan2><br>
</br>
<b># Create Layer 3 VLAN IDs</b><br> 
<b>#Syntax </b><br>
set vlans vlan-id&lt;vlan1> l3-interface vlan-&lt;number1><br>
set vlans vlan-id <vlan2> l3-interface vlan-&lt;number2><br>
set vlan-interface interface vlan-&lt;number1> vif vlan-&lt;number1> address &lt;ip_address1> prefix-length &lt;subnet><br>
set vlan-interface interface vlan-&lt;number1>  vif vlan-&lt;number1> address &lt;ip_address2>1 prefix-length &lt;subnet><br>
</br>
<b># Verify Layer3 interface</b><br>
run show vlan-interface<br>
</br>
<b>#Verify Ip routes</b><br>
run show ip routes 

</td>
<td>
<b># Create VLANs</b><br> 
config vlan add &lt;vlan_value1><br>       
config vlan add &lt;vlan_value2><br>
</br>
<b># show vlan configuration</b><br>
show vlan config <br>
</br>
<b>#Add Interface to vlan in Tagged (Trunk) mode:</b>
config vlan member add &lt;vlan_value1> Ethernet&lt;interface1><br>
config vlan member add &lt;vlan_value2> Ethernet&lt;interface2><br>
<br>
<b># Inter-VLAN routing</b><br>
<b># Configure IP addresses on VLAN1 and VLAN2</b>
<b># Syntax</b><br>
config interface ip add Vlan&lt;number1> &lt;IP_ADDRESS1><br>    
config interface ip add Vlan&lt;number2> &lt;IP_ADDRESS2> <br>   
</br>
<b># Example</b><br>
config interface ip add Vlan1 192.168.1.2/24<br>       
config interface ip add Vlan2 192.168.2.1/24<br>
</br>
<b># Validate  Ip Interface</b><br>
show ip interface<br>
</br>
<b># Verify the Subinterface and VLAN status</b><br>
show vlan  brief<br>

</td>
</tr>
<tr>
<th colspan='2'>DHCP Relay</th>
</tr>
<tr>
<td>

<b># DHCP Relay Command</b><br>
<b>#Enable IP routing function when using DHCP relay.</b><br>
<br>set ip routing enable &lt;true | false><br>
</br>
<b># Enable the DHCP relay function on the L3 VLAN interface connected to the client.</b><br>
 set protocols dhcp relay interface &lt;vlan-interface-name> disable &lt;true | false><br>
</br>
<b># Configure the IP address of the DHCP server.</b><br>
  set protocols dhcp relay interface&lt;vlan-interface-name> dhcp-server-address &lt;ipv4-address><br>
</br>
<b># Configure the IP address of the DHCP relay agent.</b><br>
  set protocols dhcp relay interface &lt;vlan-interface-name> relay-agent-address &lt;agent-ipv4-address>
  
</td>
<td>
<b>#  SONiC Command to enable DHCP relay</b><br>
config feature state dhcp_relay enabled<br>
</br>
<b># Enable DHCP relay on Vlan number</b><br> 
config vlan dhcp_relay add &lt;vlan_number> &lt;IP_ADDRESS><br>
</br>
<b>#Enable DHCP relay on Loopback interface</b><br>
config vlan dhcp_relay src_intf add &lt;vlan_number> Loopback0<br>
</br>
<b>#Example</b><br>
config vlan dhcp_relay add 10 192.168.20.100<Br>
config vlan dhcp_relay src_intf add 10 Loopback0<br>


</td>
</tr>
</table>