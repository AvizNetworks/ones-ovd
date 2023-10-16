 # <b> Port Mirroring</b>

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
  <tr>
  <td>
  
<b>#Configuring port as port mirroring</b><br>
<b>#Syntax </b><br>
</br>
set interface ethernet-switching-options analyzer 111 output ge-&lt;x/y/z><br>
</br>
<b># Configure Monitor the flows of ingress port</b><br>
set interface ethernet-switching-options analyzer &lt;number> input ingress ge-x/y/z<br>
</br>
<b># Configure Monitor the Flows of Egress Port</b><br>
set interface ethernet-switching-options analyzer &lt;number> input egress ge-&lt;x/yz><br>
</br>
<b>#Configuring Mirroring on Egress or Ingress Port</b><br>
 set interface ethernet-switching-options analyzer &lt;number> input ingress ge-&lt;x/y/z><br>
 set interface ethernet-switching-options analyzer <number> input egress ge-<x/yz>

  </td>
  <td>

<b>#Create a mirror session</b><br>
<b>#Syntax</b><br>
config mirror_session add ts1_everflow &lt;Source_Ip_address><br> 
&lt;destination_Ip_Address>  &lt;dscp_number> &lt;queue_number><br>
</br>
<b># Command to create  ACL table</b><br>
 config acl add table ACL_Mirror MIRROR --description 'mirror' --stage ingress --ports Ethernet0<br>
</br>
<b># Command  an ACL JSON file and load it to the configuration database for everflow.</b><br>
cat acl.json
```
{
    "ACL_RULE": {
        "ACL_Mirror|ACE_Mirror": {
            "PRIORITY": "55",
            "IP_TYPE": "ipv4any",
            "MIRROR_ACTION": "ts1_everflow"
        }
    }
}
```
<b># Command to load the acl.json with new config related to ACL applied 
config load acl.json -y</b><br>
</br>
<b>#Command to verify  the mirror status</b><br>
 show mirror_session<br>
</br>
<b># Command to create  a mirror session for SPAN</b><Br>
<b>#Syntax</b><br>
config mirror_session span add &lt;session_name> &lt;Destination_interface_Analyzer> &lt;Source_intertface_switch><br>
<br>
<b># Command to create a mirror session for Remote SPAN</b><br>
config mirror_session erspan add &lt;session_name> &lt;src_ip> &lt;dst_ip> &lt;dscp> &lt;ttl> [gre_type] [queue] [src_port] [direction]<br>
</br>
<b>#Command to create  a mirror session and  ACL table</b><br>
config mirror_session span add &lt;session_name>  &lt;Destination_port> &lt;Source_port> &lt;Direction><br>
</br>
<b># Example</b> <br>
config acl add  table Test MIRROR -p Ethernet8 -s ingress<br>
</br>
<b>#Command to verify  the mirror table</b><br>
show mirror_session<br>
</br>
<b># Create ACL JSON file and load it to the configuration database for Mirror</b><br>
cat acl.json<br>
```
{
"ACL_RULE": {
        "Test|Forward": {
                "PRIORITY": "2",
                "MIRROR_ACTION": "test",
                "VLAN_ID": "20"
                }
        }
}
```
<b># Command to load the json file with ACL config applied</b><br> 
config load acl.json -y <br>
config  save -y<br>
</br>
<b>#Command to check  the status of ACL table and mirror session</b><br> 
show mirror_session<br>
show acl table<br>

  </td>
  </tr>
</table>