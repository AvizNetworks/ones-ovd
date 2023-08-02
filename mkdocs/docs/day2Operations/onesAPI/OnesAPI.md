# ONES REST APIs

# Overview

ONES provides predefined REST APIs for both Day 1 and Day 2 operations. These REST APIs can easily  be integrated with customer’s  NetOps tools. All the operations via GUI can also be performed using standard REST API (Secured REST API) for Day 1 and Day 2.

ONES Application saves the complete configuration data in a real time relational database which can easily be integrated to customer’s 3rd party NetOps  tools over the Northbound plug-ins.  These plug-in feed the complete  information about various network device states enrolled with ONES application to 3rd party NetOps tools . Hence these REST APIs provide a great operational management value by integrating with customer’s desired network management open source tools .

ONES REST API modules deploy Day 1 operations like VLAN , interface , VXLAN , BGP configuration over enrolled SONiC devices and maintain all enrolled device’s  running operational and configured states. 

ONES REST API modules deploy Day 2 operations like configuration changes , modifications during maintenance windows seamlessly . These Day 2 operations may include BGP route map , policy changes done by the Data Center operators to add or remove host prefixes advertisement , may include L2-VXLAN - VNI to VLAN mapping changes , L3-VXLAN - VNI to VRF mapping changes , Switch replacement RMA operations along with image and configuration upgrades.

ONES application enables customers to integrate the Aviz Networks provided ONES Plug-in to their existing CI/CD automated operational workflow independent of programming language used by CI/CD Infrastructure like python, Java or Golang etc .

