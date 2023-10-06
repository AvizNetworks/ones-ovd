# <b> QoS Configuration</b>

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

<b>#  Commands to create QoS classifiers</b><br> 
<b>#syntax</b><br>
set class-of–service classifier &lt;classifier-name><br>
delete class-of–service classifier c1<br>
<br>
<b>#Example</b><br>
creates a classifier c1 with forwarding-class f1 and code-point 3<br>
set class-of-service classifier c1 forwarding-class f1 code-point 3<br>
<br>
<br>
<b>#  Commands to create QoS schedulers</b><br> 
<b>#syntax</b><br>  
<b># Configure scheduling algorithm for queue scheduling.</b><br>
set class-of-service scheduler &lt;scheduler-name> mode &lt;SP | WRR | WFQ><br>
<b># Configure guaranteed rate and the maximum rate for the interface queue</b><br>
 set class-of-service scheduler &lt;scheduler-name> guaranteed-rate &lt;value>
 set class-of-service scheduler &lt;scheduler-name> max-rate &lt;value><br>  
<br>
<b># Configure scheduler profile associated with the configured scheduler and forwarding class.</b><br>
 set class-of-service scheduler-profile &lt;scheduler-profile-name> forwarding-class &lt;forwarding-class-name> scheduler &lt;scheduler-name></b><br>
<br>
<b>#  Configure mapping between forwarding class and local priority.</b><br>
 set class-of-service forwarding-class &lt;forwarding-class-name> local-priority &lt;int><br>
<br>
<b># Apply the scheduler profile to an egress interface.</b><br>
 set class-of-service interface &lt;interface-name> scheduler-profile &lt;scheduler-profile-name><br>

</td>
<td>

<b>#  Commands to create QoS classifiers ( Edge core SONiC Platform - AS9716-32D)</b><br>
<b>#Syntax</b><br>  
Create a profile for DOT1P/DSCP mapped  to TC(Traffic Class).<br>
<br>
<b>#Example for DSCP</b><br>
<br>
config qos dscp-tc add DSCP_TC --dscp 7 --tc 1<br>
<br>
<b>#Modify the existing Dot1p/DSCP to TC profile.</b><br>
<b>#Example for DOT1P:</b><br>
config qos dot1p-tc update 1p_tc --dot1p 1 --tc 2<br>
<br>
<b>#Validate  the profile for  DOT1P/DSCP to Traffic class.</b><br>
<b># DOT1P to TC:</b><br>
show qos dot1p-tc<br> 
<br>
<b>#Validate Queue mapping from DSCP queue  to Traffic class</b><br>
show qos dscp-tc <br>
<br>
<b># Create a profile for traffic class and map it to  Queue</b><br>
config qos tc-queue add TC_Q --tc 1 --queue 2<br>
<br>
<b># Validate  the profile of Traffic class  to Queue.</b><br>
show qos tc-queue <br>
<br>
<b>#Binding the mapping table to the specified interface.</b><br>
config interface qos dscp-tc bind Ethernet0 DSCP_TC<br>
<br>
<b>#Validate  the binding table.</b><br>
show interfaces qos <br>
<br>
<b># Clear the queue counter</b><br>
sonic-clear queue counters<br>
<br>
<b>#Check Specific ethernet port  (egress port) queue counters</b><br>
show queue counters Ethernet8<br>
<br>
<b># Marking configuration</b><br>
<b>#Create a profile for DOT1P remarking.</b><br>
<b>#Example for Dot1P:</b><br>
config qos remark dot1p add remark_dot1p --tc 0 --dot1p 1<br>
<br>
<b># Validate  the remark profile.</b><br>
 show qos remark dot1p<br>
<br>
<b># Bind  the remark table to the egress interface.</b><br>
config interface qos remark dot1p bind Ethernet8 remark_dot1p<br>
<br>
<b>#Validate  the binding table.</b><br>
show interfaces qos<br>
<br>
<br>
<b># Scheduler Configuration(Edge Core SONiC platform - AS7326-56X)</b><br>
<b># Set the scheduler mode.</b><br>
config scheduler add strict_mode --sched_type STRICT<br>
<br>
<b># Validate  scheduler status.</b><br>
show scheduler<br>
<br>
<b># Bind  the scheduler to ethernet sub- interface.</b><br> 
<b>>#Example</b><br>
config interface scheduler bind queue Ethernet 5.3 strict_mode<br>
<br>
<b>#Command to unbind the scheduler from ethernet interface</b><br>
config interface scheduler unbind queue Ethernet 5.3<br>
<br>
<b>#Validate scheduler  status.</b><br>
show interfaces scheduler<br>
<br>
<b>#Validate Scheduler queues</b><br>
show queue counters Ethernet5<br>
<br>
<b>#  Set the scheduler mode</b><br>
<b>#Example</b><br>
config scheduler add wrr_7 --sched_type WRR --weight 7<br>
config scheduler add wrr_3 --sched_type WRR --weight 3<br>
<br>
<b>#validate scheduler  status.</b><br>
show scheduler<br>
<br>
<b># Bind  the scheduler to ethernet  interface.</b><br> 
<b>#Example</b><br>
config interface scheduler bind queue Ethernet5 3 wrr_7<br>
config interface scheduler bind queue Ethernet5 4 wrr_3<br>
<br>
<b># validate scheduler  status.</b><br>
show interfaces scheduler<br>

</td>
</tr>
</table>