# <b>Layer2 Leaf Spine topology</b>

Layer2 Leaf-Spine architecture offers low-latency, high-bandwidth connectivity with redundancy and efficient traffic distribution. A spine-leaf architecture is data center network topology that consists of two switching layers—a spine and leaf. The leaf layer consists of access switches that aggregate traffic from servers and connect directly into the spine or network core. Spine switches interconnect all leaf switches in a full-mesh topology.

One of the main advantages of the L2LS design is that the pair of spine switches are presented to the leaf-layer switches as a single switch through the use of MLAG (Multi-chassis Link Aggregation Group), which inherently allows LAYER 2 flexibility throughout the environment. This also eliminates the dependence on spanning-tree for loop prevention and allows for full utilization of all links between the leaf and spine. It is worth noting that the scalability of the spine is limited to a total of 2 switches. By adopting a merchant silicon approach to switch design, architects are now able to design networks that have predictable traffic patterns, low latency, and minimal oversubscription. Legacy designs often incorporated more than two tiers to overcome density and oversubscription limitations. Leaf and spine switches are interconnected with LAG (802.3ad) links and each leaf has at least one connection to each spine. 


## Yaml Template

```yaml
Inventory:
  SSpines: 0
  Spines: 2
  Leafs: 4
  Tors: 0
Connectivity:
  SSpine: []
  Spine:
    - switchId: 1
      switchName: "Spine-1"
      ipAddress: "x.x.x.11"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag: 
        enabled: true
        peer: "S2"
        keepalive_vlan: 10      
      Links:
        - link: "S1_Ethernet0 | L1_Ethernet48"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "S1_Ethernet4 | L2_Ethernet48"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "S1_Ethernet8 | L3_Ethernet48"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "S1_Ethernet12 | L4_Ethernet48"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "S1_Ethernet124 | S2_Ethernet124"
          staticLink: true
          properties:
            mode: "MC-LAG"            
    - switchId: 2
      switchName: "Spine-2"
      ipAddress: "x.x.x.12"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag: 
        enabled: true
        peer: "S1"
        keepalive_vlan: 10
      Links:
        - link: "S2_Ethernet0 | L1_Ethernet52"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "S2_Ethernet4 | L2_Ethernet52"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "S2_Ethernet8 | L3_Ethernet52"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "S2_Ethernet12 | L4_Ethernet52"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "S2_Ethernet124 | S1_Ethernet124"
          staticLink: true
          properties:
            mode: "MC-LAG"         
  Leaf:
    - switchId: 1
      switchName: "Leaf-1"
      ipAddress: "x.x.x.13"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L2"
        keepalive_vlan: 10
      Links:
        - link: "L1_Ethernet48 | S1_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "L1_Ethernet52 | S2_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "L1_Ethernet56 |  L2_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L1_Ethernet0 |  H1_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 201
            mc_po_group: 201
        - link: "L1_Ethernet4 |  H2_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 202
            mc_po_group: 202
    - switchId: 2
      switchName: "Leaf-2"
      ipAddress: "x.x.x.14"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L1"
        keepalive_vlan: 10
      Links:
        - link: "L2_Ethernet48 | S1_Ethernet4"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "L2_Ethernet52 | S2_Ethernet4"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "201,202"
            mc_po_group: 501
        - link: "L2_Ethernet56 | L1_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L2_Ethernet0 |  H1_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 201
            mc_po_group: 201
        - link: "L2_Ethernet4 |  H2_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 202
            mc_po_group: 202
    - switchId: 3
      switchName: "Leaf-3"
      ipAddress: "x.x.x.15"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L4"
        keepalive_vlan: 10
      Links:
        - link: "L3_Ethernet48 | S1_Ethernet8"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "L3_Ethernet52 | S2_Ethernet8"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "L3_Ethernet56 | L4_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L3_Ethernet0 |  H3_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 203
            mc_po_group: 203
        - link: "L3_Ethernet4 |  H4_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 204
            mc_po_group: 204
    - switchId: 4
      switchName: "Leaf-4"
      ipAddress: "x.x.x.16"
      ASN: 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L3"
        keepalive_vlan: 10
      Links:
        - link: "L4_Ethernet48 | S1_Ethernet12"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "L4_Ethernet52 | S2_Ethernet12"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: "203,204"
            mc_po_group: 502
        - link: "L4_Ethernet56 | L3_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L4_Ethernet0 |  H3_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 203
            mc_po_group: 203
        - link: "L4_Ethernet4 |  H4_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Trunk"
            vlan: 204
            mc_po_group: 204
  Tor: []
BGP:
PhysicalIfCfg:
  FEC: "Off"
  MTU: 9000
  AdminStatus: "Up"
ASN:
IPv4Pool:
IPv6Pool:
NTP:
  server: "x.x.x.10"
  timezone: "Asia/Kolkata"
SYSLOG:
  server: "x.x.x.10"
SNMP:
  trapserver: "x.x.x.10"
Parameters:
  vlan: "200,201,202,203,204,501,502"
  anycast_gateway: "x.x.x.0/23"
  hosts_per_vlan: 10
L2LS:
  enabled: true
  mode: "L2" # OverL2 and OverL3
```

## <b>Configure, Validate & Verify through UI</b>



## <b>Applied Configuration on Switches</b>

=== "Leaf1"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-1
    !
    vlan 10
    !
    vlan 201
    !
    vlan 202
    !
    interface port-channel 201
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    !
    interface port-channel 202
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 202
    !
    interface port-channel 501
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 202 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.2/31
    !
    mlag domain-id 1
    peer-address 192.168.0.3
    peer-link port-channel 999
    src-address 192.168.0.2
    member port-channel 201
    member port-channel 202
    member port-channel 501
    local-interface vlan 10
    ```

=== "Leaf2"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-2
    !
    vlan 10
    !
    vlan 201
    !
    vlan 202
    !
    interface port-channel 201
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    !
    interface port-channel 202
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 202
    !
    interface port-channel 501
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 202 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.3/31
    !
    mlag domain-id 1
    peer-address 192.168.0.2
    peer-link port-channel 999
    src-address 192.168.0.3
    member port-channel 201
    member port-channel 202
    member port-channel 501
    local-interface vlan 10
    ```

=== "Leaf3"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-3
    !
    vlan 10
    !
    vlan 203
    !
    vlan 204
    !
    interface port-channel 203
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    !
    interface port-channel 204
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 204
    !
    interface port-channel 502
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 203 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 204 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.4/31
    !
    mlag domain-id 1
    peer-address 192.168.0.5
    peer-link port-channel 999
    src-address 192.168.0.4
    member port-channel 203
    member port-channel 204
    member port-channel 502
    local-interface vlan 10
    ```

=== "Leaf4"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-4
    !
    vlan 10
    !
    vlan 203
    !
    vlan 204
    !
    interface port-channel 203
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    !
    interface port-channel 204
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 204
    !
    interface port-channel 502
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 203 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 204 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.5/31
    !
    mlag domain-id 1
    peer-address 192.168.0.4
    peer-link port-channel 999
    src-address 192.168.0.5
    member port-channel 203
    member port-channel 204
    member port-channel 502
    local-interface vlan 10
    ```

=== "Spine1"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Spine-1
    !
    vlan 10
    !
    vlan 201
    !
    vlan 202
    !
    vlan 203
    !
    vlan 204
    !
    interface port-channel 501
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface port-channel 502
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet124
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.0/31
    !
    mlag domain-id 1
    peer-address 192.168.0.1
    peer-link port-channel 999
    src-address 192.168.0.0
    member port-channel 501
    member port-channel 502
    local-interface vlan 10
    ```

=== "Spine2"

    ```sh
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Spine-2
    !
    vlan 10
    !
    vlan 201
    !
    vlan 202
    !
    vlan 203
    !
    vlan 204
    !
    interface port-channel 501
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    !
    interface port-channel 502
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface port-channel 999
    mtu 9000
    switchport mode trunk
    switchport trunk allowed vlan add 10
    switchport trunk allowed vlan add 201
    switchport trunk allowed vlan add 202
    switchport trunk allowed vlan add 203
    switchport trunk allowed vlan add 204
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet124
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 501 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    channel-group 502 mode active
    forward-error-correction none
    !
    interface vlan 10
    ip address 192.168.0.1/31
    !
    mlag domain-id 1
    peer-address 192.168.0.0
    peer-link port-channel 999
    src-address 192.168.0.1
    member port-channel 501
    member port-channel 502
    local-interface vlan 10
    ```
