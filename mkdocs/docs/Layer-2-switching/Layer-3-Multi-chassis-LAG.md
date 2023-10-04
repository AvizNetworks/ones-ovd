# Layer 3 Multi Chassis LAG

![Layre3](../img/layer3(mc-lag).png)

<div style="border: 1px solid black; padding: 10px;">
<b># Command to create PortChannel on MC LAG Pair switches</b><br> 
config portchannel add PortChannel01<br>
config portchannel add PortChannel02<br>
config portchannel add PortChannel03<br>
config portchannel member add PortChannel01 Ethernet0<br>
config portchannel member add PortChannel02 Ethernet1<br>
config portchannel member add PortChannel03 Ethernet56<br>
config portchannel member add PortChannel03 Ethernet60<br>
</div>

<br>

<div style="border: 1px solid black; padding: 10px;">
<b># Commands to Create Port Channel IPs on MC LAG pair switches</b><br> 
config interface ip add PortChannel01 192.168.11.1/24<br>
config interface ip add PortChannel02 192.168.12.1/24<br>
config interface ip add PortChannel03 192.168.10.1/24<br>
</br>
config interface ip add PortChannel01 192.168.11.1/24<br>
config interface ip add PortChannel02 192.168.12.1/24<br>
config interface ip add PortChannel03 192.168.10.2/24<br>

</div>

<br>

<div style="border: 1px solid black; padding: 10px;">
<b># command to configure MCLAG on MC LAG pair switches  (Domain ID, VLANs and MLAG members)</b><br>
config mclag add 1 192.168.10.2 192.168.10.1<br>
config mclag member add 1 PortChannel01<br>
config mclag member add 1 PortChannel02<br>
</br>
config mclag add 1 192.168.10.1 192.168.10.2<br>
config mclag member add 1 PortChannel01<br>
config mclag member add 1 PortChannel02<br>
</div>

<br>

<div style="border: 1px solid black; padding: 10px;">
<b>SONiC command to Configure IP for MCLAG Peer health check on MC LAG peers</b><br>
config interface ip add Vlan10 192.168.10.1/24<br>
config interface ip add Vlan10 192.168.10.2/24<br>
</div>

<br>

<div style="border: 1px solid black; padding: 10px;">
<b># Command to show MCLAG Status</b>
</div>
<br>
<div style="border: 1px solid black; padding: 10px;">
<b>#MC1 switch configuration -</b><br> 
show interfaces portchannel<br>
Flags: A - active, I - inactive, Up - up, Dw - Down, N/A - not available,<br>
       S - selected, D - deselected, * - not synced<br>
```
  No.  Team Dev       Protocol     Ports                          Oper Key  Admin Key    Fast Rate
-----  -------------  -----------  ---------------------------  ----------  -----------  -----------
  01  PortChannel01  LACP(A)(Up)  Ethernet0(S)                       101  auto         false
  02  PortChannel02  LACP(A)(Up)  Ethernet1(S)                       102  auto         false
  03  PortChannel03  LACP(A)(Up)  Ethernet60(S) Ethernet56(S)        103  auto         false
```
show mclag brief  
       Domain ID                    : 1
        Role                         : Active
        Session Status               : Up
       Peer Link Status             :
        Source Address               : 192.168.10.1
        Peer Address                 : 192.168.10.2
        Peer Link                    :
       Keepalive Interval           : 1 secs
        Session Timeout              : 15 secs
        System MAC                   : 00:a0:c9:00:00:00
       Number of MCLAG Interfaces   : 2
        MCLAG Interface              Local/Remote Status
        PortChannel01                Up/Up
        PortChannel02                Up/Up


MC2 switch configuration - 

admin@sonic:~$ show interfaces portchannel
Flags: A - active, I - inactive, Up - up, Dw - Down, N/A - not available,
       S - selected, D - deselected, * - not synced
  No.  Team Dev       Protocol     Ports                          Oper Key  Admin Key    Fast Rate
-----  -------------  -----------  ---------------------------  ----------  -----------  -----------
  01  PortChannel01  LACP(A)(Up)  Ethernet0(S)                       101  auto         false
  02  PortChannel02  LACP(A)(Up)  Ethernet1(S)                       102  auto         false
  03  PortChannel03  LACP(A)(Up)  Ethernet60(S) Ethernet56(S)        103  auto         false
admin@sonic:~$ show mclag brief  
       Domain ID                    : 1
        Role                         : Standby
        Session Status               : Up
        Peer Link Status             :
        Source Address               : 192.168.10.2
        Peer Address                 : 192.168.10.1
        Peer Link                    :
        Keepalive Interval           : 1 secs
        Session Timeout              : 15 secs
        System MAC                   : 00:a0:c9:00:00:00
        Number of MCLAG Interfaces   : 2
        MCLAG Interface              Local/Remote Status
        PortChannel01                Up/Up
        PortChannel02                Up/Up

</div>

<br>

<div style="border: 1px solid black; padding: 10px;">

</div>
