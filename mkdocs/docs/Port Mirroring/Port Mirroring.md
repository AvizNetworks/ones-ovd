 # Port Mirroring

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
  <tr>
  <td>
<b>#Configuring port as port mirroring</b>
<b>#Syntax </b>

set interface ethernet-switching-options analyzer 111 output ge-&lt;x/y/z>

<b># Configure Monitor the flows of ingress port</b>
set interface ethernet-switching-options analyzer &lt;number> input ingress ge-x/y/z

<b># Configure Monitor the Flows of Egress Port</b>
set interface ethernet-switching-options analyzer &lt;number> input egress ge-&lt;x/yz>


<b>#Configuring Mirroring on Egress or Ingress Port</b>
 set interface ethernet-switching-options analyzer &lt;number> input ingress ge-&lt;x/y/z>
 set interface ethernet-switching-options analyzer <number> input egress ge-<x/yz>

  </td>
  <td>
<b>#Create a mirror session</b>
<b>#Syntax</b>
config mirror_session add ts1_everflow &lt;Source_Ip_address> 
&lt;destination_Ip_Address>  &lt;dscp_number> &lt;queue_number>


<b># Command to create  ACL table</b>
 config acl add table ACL_Mirror MIRROR --description 'mirror' --stage ingress --ports Ethernet0

<b># Command  an ACL JSON file and load it to the configuration database for everflow.</b>
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
config load acl.json -y</b>

<b>#Command to verify  the mirror status</b>
 show mirror_session

<b># Command to create  a mirror session for SPAN</b>
<b>#Syntax</b>
config mirror_session span add &lt;session_name> &lt;Destination_interface_Analyzer> &lt;Source_intertface_switch>


<b># Command to create a mirror session for Remote SPAN</b>
config mirror_session erspan add &lt;session_name> &lt;src_ip> &lt;dst_ip> &lt;dscp> &lt;ttl> [gre_type] [queue] [src_port] [direction]

<b>#Command to create  a mirror session and  ACL table</b>
config mirror_session span add &lt;session_name>  &lt;Destination_port> &lt;Source_port> &lt;Direction>

<b># Example</b> 
config acl add  table Test MIRROR -p Ethernet8 -s ingress

<b>#Command to verify  the mirror table</b>
show mirror_session

<b># Create ACL JSON file and load it to the configuration database for Mirror</b>
cat acl.json
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
<b># Command to load the json file with ACL config applied</b> 
config load acl.json -y 
config  save -y

<b>#Command to check  the status of ACL table and mirror session</b> 
show mirror_session
show acl table

  </td>
  </tr>
</table>