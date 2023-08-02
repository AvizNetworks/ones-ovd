# Overview Day 1 Operations 

Traditionally network operators were used to provision  Day 1 operations like interface creation , VLAN creation , BGP neighborship configuration etc using manual CLI for configuring DC Leaf and Spine switches  in 2 or 3 CLOS architecture. Configuration application to various Data Center switches through CLIs is a tedious and time consuming process for the operation teams .

The validation process of applied configuration  is also manual resulting in probability of errors during commissioning . Operators will then have to troubleshoot the complete control path and data path to isolate issues due to misconfiguration in Day 1 network entity provisioning.


## Day 1 Operations - SONiC 

The most prominently  leveraged data center fabric topology is the highly scalable Layer3  IP-CLOS network design and routing architecture commonly used in large-scale data center and cloud environments. The IP-CLOS provides a scalable and flexible solution for interconnecting multiple switches  in a hierarchical manner in leaf and spine architecture allowing efficient utilization of network resources and simplified routing.


Using Aviz network’s  Sonic Validated Designs (SVD) , commissioning of network services in Day 1 operations is automated ,  greatly simplified and reduces considerable  time to deploy services . 

SVD ensures consistency , accuracy and availability of all configurations committed in Day 1 operations through a unified fabric automation approach .




![configuration](../img/FirstImage.png)



Using an overlay architecture in the Data Center allows end users (network administrators) to place the endpoints (servers or virtual machines) anywhere in the network and remain connected to the same logical Layer 2 network enabling the virtual topology to be decoupled from the physical topology. 

This decoupling allows the data center network to be programmatically provisioned at a per-tenant level. Overlay networking generally supports both Layer 2 and Layer 3 transport between servers or VMs which  supports a much larger scale. SONiC overlay networks use a control-plane protocol (BGP-EVPN) to facilitate learning and sharing of endpoint information and uses VXLAN tunneling protocol to create the data plane for the overlay layer.

