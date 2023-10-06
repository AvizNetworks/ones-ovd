## <b> Link Layer Discovery protocol </b> 

LLDP is a standard link-layer discovery protocol which can broadcast its capability, IP address, ID, and interface name as TLVs (Type/Length/Value) in LLDP PDUs (Link Layer Discovery Protocol Data Units).<br> 
</br>
![Link-Layer-Discovery-protocol](../img/Link-Layer-Discovery.png)<br>
</br>

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

<b>#Command to validate the  LLDP  status</b><br>
 show protocols lldp<br>
</br>
<b>#Command to Enable LLDP service:</b><br>
set protocols lldp enable true<Br>
</br>
<b>#Command to Configure LLDP information</b><br> 
set protocols lldp interface &lt;interface_name> working-mode tx_rx<br>
set protocols lldp tlv-select mac-phy-cfg true<br>
set protocols lldp tlv-select management-address true<Br>
set protocols lldp tlv-select port-description true<br>
set protocols lldp tlv-select system-capabilities true<br>

</td>
<td>

<b>#Command to Enable / Disable  LLDP globally</b><br> 
config feature state lldp enabled<br>
config feature state lldp disabled<br>

<b>#Command to Configure LLDP information</b><br>
config lldp global hello_timer &lt;timer_value><br>
config lldp global management_ip &lt;switch_mgmt_ip><br>
config lldp global system_description AS5835-Leaf1<Br>
config lldp global system_name&lt;LEAF1><br>
</br>
<b>#Command to validate the  LLDP  status</b><br>
show feature status lldp<br>
show lldp table <br>
show lldp neighbors<Br>
show lldp global<br>
</br>
<b>#Command to enable/disable LLDP over local interfaces</b><br> 
docker exec -i lldp lldpcli<Br>
configure ports Ethernet&lt;interface> lldp status disable <Br>
configure ports Ethernet&lt;interface>  lldp status enable <br>

</td>
</tr>
</table>