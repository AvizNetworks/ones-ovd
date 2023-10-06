# <b> ACL Configuration</b>

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

<b>#  Command to create ACL rules</b><br> 
<b>#syntax</b><br>  
set firewall filter MyFilter sequence <number> from destination-mac-address &lt;mac_address><br>
 set firewall filter &lt;filter-name>  sequence &lt;number>  then action discard<br>
 set firewall filter &lt;filter-name>  sequence &lt;number>  from destination-address-ipv6 &lt;ipv6_address><br>
 set firewall filter &lt;filter-name>  sequence &lt;number> then action forward<br>
<br>
 set firewall filter&lt;filter-name1> sequence &lt;number1>  from source-address-ipv4 &lt;source_ip_address><br>
 set firewall filter bad-net sequence &lt;number1> then action discard

</td>
<td>

<b># Command to create ACL Tables</b><br>
<b># Syntax </b><br>
config acl add table &lt;ACL_table_name> L3 --description 'ACL_Test1' --stage 'ingress' --ports 'Ethernet&lt;number>’'<br>
<br>
<br>
<b># Example</b><br>
config acl add table ACL_Test1 L3V6 --description 'ACL_Test1' --stage 'egress' --ports 'Ethernet16'<br>
<br>
<b>#Command to delete ACL tables</b><br>
config acl remove table &lt;ACL_Table_Name><br>
<br>
<b>#Command to create ACL Rule with source_ip_address</b><br>
<b>#Example</b><br>
config acl add rule --src-ip4 100.0.0.1 --priority 3 ACL_Test1 deny<br>
<br>
<b>#  Commands to verify  ACL  table and rule  created -</b><br>
show acl table<br>
show acl rule<br>

</td>
</td>
</table>