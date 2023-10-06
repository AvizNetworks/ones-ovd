# <b> Layer 3 Routing</b>
## <b> Routed Interface</b>

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
<td>
<b># Configuring Routed Interface</b><br>
<b># Enable Ethernet port as a layer 3 routed interface.</b><br>
 set interface gigabit-ethernet &lt;interface-name> routed-interface enable &lt;true | false><br>
set interface gigabit-ethernet &lt;interface-name> routed-interface name &lt;string><br>
</br>
<b># Command to bring up the parent routed interface.</b><br> 
 set l3-interface routed-interface &lt;interface-name><br>
</br>
<b>#  Enable IP routing to perform layer 3 forwarding.</b><br>
 set ip routing enable true<br>
</br>
<b># Configuring Sub-interface</b><br>
set vlans vlan-id &lt;vlan-id><br>
set interface gigabit-ethernet &lt;interface-name> routed-interface sub-interface &lt;sub-interface-name> vlan-id &lt;vlan-id><br>
set l3-interface routed-interface &lt;interface-name> address &lt;ip-address> prefix-length &lt;prefix-number><br>
</br>
<b># Checking the Configuration</b><br>
run show interface routed-interface brief<br> 
run show l3-interface routed-interface &lt;interface-name> 

</td>
<td>
<b>#Command to add a Layer3 Interface address on physical interface -</b><br>
<b># Configure physical interface IP</b> <br>
config interface ip add Ethernet&lt;Number1> &lt;IP_ADDRESS><br>
config interface ip add &lt;vlan_number> &lt;IP_ADDRESS><br>
<br>
<b>#Example</b><br>
config interface ip add Loopback&lt;Number> 10.0.2.1/32<br>
config interface ip add Ethernet0 172.16.10.1/31<br>
config interface ip add Vlan100 18.0.0.1/24<Br>
</br>
<b># Command to create a  sub-interface</b> 
config interface ip add Ethernet&lt;interace_number>.&lt;vlan-id> &lt;IP_ADDRESS><br> 
</br>
<b>#Example</b><br>
config interface ip add Ethernet0.10 192.168.10.2/24<br>
</br>
<b># Validate sub-interface operational status</b><br> 
show subinterfaces status<br>

</td>
</tr>
</table>