# Day 1 Orchestration example

This illustration demonstrates the deployment of the configuration using an intent-based YAML template, while also offering a practical instance of checking the status of the intent operation.

## Importing ONES Fabric Manager Agent

```py
from client import FMClient
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:<port_number>") 
#usually <port_number> will be 8787
```

## Deploy Config 
This method takes Yaml file as input, and will be used by the fabric manager to orchestrate the network. There are pre-validated templates for various data center fabric deployments using SONiC, listed below. Yaml templates can be found [here](https://github.com/AvizNetworks/ones-pyapi/tree/master/examples/day1fm/yaml-templates)

- BGP-IP-CLOS
- DCL-L2-VXLAN-EVPN-MC LAG
- DCL-L3-VXLAN-EVPN-Sym-IRB
- DCL-L3-VXLAN-EVPN-Asym-IRB



```py
# Deploy Config
file = "<Path of Yaml file>"
result = conn.day1_intent_ovd_template(file)
```

## Intent Status
This method retrieve Generic Intent Status for provisioning on SONiC enabled fabric switches . This method allows network  operators  to  get the status of orchestration progress on a specific switch in SONiC fabric  enrolled with ONES application.
```py
result = conn.get_intent_status()
```

 ### Note - 
 Day 1 orchestration calls are synchronous. We need to await the command's completion status, determined using **get_intent_status()**, before proceeding with any subsequent commands.
