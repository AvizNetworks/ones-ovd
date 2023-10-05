## BGP Routing 

![BGP-Routing ](../img/BGP-Routing.png)

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

<br></br>

<table>
<tr>
<th>PICOS</th>
<th>SONiC</th>
</tr>
<tr>
<th colspan='2'>BGP Routing</th>
</tr>
<tr>
<td>

<b>#Command to configure BGP routing -</b><br>
set protocols bgp router-id &lt;System_loopback_IP><br>
 set protocols bgp local-as &lt;LOCAL_AS_NUMBER><br>
 set protocols bgp local-as &lt;LOCAL_AS_NUMBER><Br>
 set protocols bgp neighbor &lt;Neighbor_IP> remote-as &lt;REMOTE_AS_NUMBER><br>
 set protocols bgp local-as &lt;LOCAL_AS_NUMBER><br>
 set protocols bgp neighbor &lt;Neighbor_IP>  remote-as &lt;REMOTE_AS_NUMBER><br>
 set protocols bgp peer-group &lt;LEAF_NAME><br>
 set protocols bgp neighbor &lt;LEAF_NAME><br>
 remote-as external<br>
 set protocols bgp neighbor &lt;Neighbor_IP> peer-group &lt;LEAF_NAME><br>
 set protocols bgp neighbor &lt;Neighbor_IP>  peer-group &lt;LEAF_NAME><br>
Commit<br>
</br>
<b>#Example BGP routing configuration</b><br>
 set protocols bgp router-id 1.1.1.1<br>
 set protocols bgp local-as 100<Br>
 set protocols bgp local-as 100<br>
 set protocols bgp neighbor 192.168.49.1 remote-as 200<br>
 set protocols bgp local-as 100<br>
 set protocols bgp neighbor 192.168.49.1 remote-as 100<br>
 set protocols bgp peer-group Leaf1<br>
 set protocols bgp neighbor leaf1 remote-as external<br>
 set protocols bgp neighbor 10.10.0.1 peer-group Leaf1<br>
 set protocols bgp neighbor 10.10.0.12 peer-group Leaf1<br>
commit<br>
</br>
<b>#Command to show BGP routes summary</b><br>
run show bgp route &lt;ip>

</td>
<td>

<b>#vtysh sonic command  to configure BGP routing -</b><br>
router bgp &lt;ASN_NUMBER><br>
bgp router-id &lt;System_loopback_IP><br>
no bgp ebgp-requires-policy<br>
bgp bestpath as-path multipath-relax<br>
neighbor FABRIC peer-group<br>
neighbor FABRIC capability extended-nexthop<br>
neighbor &lt;Neighbor_IP>  remote-as &lt;REMOTE_ASN_NUMBER><br>
neighbor &lt;Neighbor_IP>  peer-group FABRIC<br>
</br>
<b>#Example BGP routing configuration</b><br>
router bgp 65001<br>
bgp router-id 10.0.2.1<br>
no bgp ebgp-requires-policy<br>
bgp bestpath as-path multipath-relax<br>
neighbor FABRIC peer-group<br>
neighbor FABRIC capability extended-nexthop<br>
neighbor 172.16.10.0 remote-as 2001<br>
neighbor 172.16.10.0 peer-group FABRIC<br>
neighbor 172.16.10.8 remote-as 2002<br>
neighbor 172.16.10.8 peer-group FABRIC<br>
neighbor 192.168.3.1 remote-as 2003<br>
neighbor 192.168.3.1 peer-group FABRIC<br>
</br>
<b>#Command to show BGP routes summary</b><br>
show ip bgp summary<br>
show ip bgp neighbors<br>
show ip bgp network<br>
</br>
show ipv6 bgp summary</br>
show ipv6 bgp neighbors<br>
show ipv6 bgp network<Br>
</br>
</td>
</tr>
</table>