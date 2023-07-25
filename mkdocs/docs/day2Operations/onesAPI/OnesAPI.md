# ONES APIs

ONES provides predefined APIs for both Day 1 and Day 2 operations, these APIs can be easily integrated with Customers NetOps tools. All the operations via GUI can also be performed using standard API (Secured REST API) for Day 1. 

ONES Application saves the complete configuration data in post gres database which can be easily integrated to customer’s 3rd party network operations tools over Northbound plugs-in . These plugs-in feed the information about various network devices states enrolled with ONES server to 3rd party netops tool and hence provides a great operational management value by integrating with customer’s desired network management open source tools .

ONES API modules deploy Day1 operations like VLAN , interface , VXLAN , BGP configuration over Enrolled SONiC devices and maintain all enrolled devices running operational and configured states in a secure database.  ONES applications support Day2 operations like configuration changes , modifications during maintenance windows seamlessly through ONES APIs 

These Day2 operations may include BGP route map , policy changes done by DC operations to add or remove host prefixes advertisement , May include VXLAN VNI to VLAN mapping changes , VXLAN VNI to VRF mapping changes , Switch replacement RMA operations with image and config upgrades.
ONES enabled customers to integrate Aviz provided ONES APIs and plug-ins into their existing CI/CD automated operational workflow independent of programming language used by CI/CD Infrastructure like python, Java or Golang etc 
