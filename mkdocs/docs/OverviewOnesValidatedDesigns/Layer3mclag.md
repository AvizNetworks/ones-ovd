# <b>Layer3  MC-LAG </b>
This enables NetOps to configure dual homing of Server host  upstreaming  to 2 Leaf switches through MC-LAG protocol over Layer 3 interfaces thus offering protection to Server Hosted applications 


![img](../img/Layer3MclagDeployment.png)

## <b> YAML Template </b>

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
      ASN: 1001
      Credentials:
        user: "admin"
        password: "admin"
      mclag: null
      Links:
        - link: "S1_Ethernet0 | L1_Ethernet48"
          staticLink: true
          properties: null
        - link: "S1_Ethernet4 | L2_Ethernet48"
          staticLink: true
          properties: null
        - link: "S1_Ethernet8 | L3_Ethernet48"
          staticLink: true
          properties: null
        - link: "S1_Ethernet12 | L4_Ethernet48"
          staticLink: true
          properties: null
    - switchId: 2
      switchName: "Spine-2"
      ipAddress: "x.x.x.12"
      ASN: 1002
      Credentials:
        user: "admin"
        password: "admin"
      mclag: null
      Links:
        - link: "S2_Ethernet0 | L1_Ethernet52"
          staticLink: true
          properties: null
        - link: "S2_Ethernet4 | L2_Ethernet52"
          staticLink: true
          properties: null
        - link: "S2_Ethernet8 | L3_Ethernet52"
          staticLink: true
          properties: null
        - link: "S2_Ethernet12 | L4_Ethernet52"
          staticLink: true
          properties: null
  Leaf:
    - switchId: 1
      switchName: "Leaf-1"
      ipAddress: "x.x.x.13"
      ASN: 2001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L2"
        keepalive_vlan: 10
        isoverl3: true
      Links:
        - link: "L1_Ethernet48 | S1_Ethernet0"
          staticLink: true
          properties: null
        - link: "L1_Ethernet52 | S2_Ethernet0"
          staticLink: true
          properties: null  
        - link: "L1_Ethernet64 |  L2_Ethernet64"
          staticLink: true
          properties: null               
        - link: "L1_Ethernet56 |  L2_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L1_Ethernet0 |  H1_Ethernet0"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 200
        - link: "L1_Ethernet4 |  H2_Ethernet0"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 201
    - switchId: 2
      switchName: "Leaf-2"
      ipAddress: "x.x.x.14"
      ASN: 2001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L1"
        keepalive_vlan: 10
        isoverl3: true
      Links:
        - link: "L2_Ethernet48 | S1_Ethernet4"
          staticLink: true
          properties: null
        - link: "L2_Ethernet52 | S2_Ethernet4"
          staticLink: true
          properties: null
        - link: "L2_Ethernet64 |  L1_Ethernet64"
          staticLink: true
          properties: null           
        - link: "L2_Ethernet56 | L1_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L2_Ethernet0 |  H1_Ethernet1"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 200
        - link: "L2_Ethernet4 |  H2_Ethernet1"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 201
    - switchId: 3
      switchName: "Leaf-3"
      ipAddress: "x.x.x.15"
      ASN: 2002
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L4"
        keepalive_vlan: 10
        isoverl3: true
      Links:
        - link: "L3_Ethernet48 | S1_Ethernet8"
          staticLink: true
          properties: null
        - link: "L3_Ethernet52 | S2_Ethernet8"
          staticLink: true
          properties: null
        - link: "L3_Ethernet60 |  L4_Ethernet60"
          staticLink: true
          properties: null           
        - link: "L3_Ethernet56 | L4_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L3_Ethernet0 |  H3_Ethernet0"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 200
        - link: "L3_Ethernet4 |  H4_Ethernet0"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 201
    - switchId: 4
      switchName: "Leaf-4"
      ipAddress: "x.x.x.16"
      ASN: 2002
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
        enabled: true
        peer: "L3"
        keepalive_vlan: 10
        isoverl3: true
      Links:
        - link: "L4_Ethernet48 | S1_Ethernet12"
          staticLink: true
          properties: null
        - link: "L4_Ethernet52 | S2_Ethernet12"
          staticLink: true
          properties: null
        - link: "L4_Ethernet60 |  L3_Ethernet60"
          staticLink: true
          properties: null            
        - link: "L4_Ethernet56 | L3_Ethernet56"
          staticLink: true
          properties:
            mode: "MC-LAG"
        - link: "L4_Ethernet0 |  H3_Ethernet1"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 200
        - link: "L4_Ethernet4 |  H4_Ethernet1"
          staticLink: true
          properties:
            mode: "L3-V4"
            mc_po_group: 201
  Tor: []
BGP:
  BGP_U: false
  ND_RA: 30
PhysicalIfCfg:
  FEC: "Off"
  MTU: 9000
  AdminStatus: "Up"
ASN:
  SSpine: "10000-20000"
  Spine: "21000-50000"
  Leaf: "51000-60000"
  Tor: "61000-70000"
IPv4Pool:
  Loopback: "10.10.10.0/24"
  LeafSpine: "40.0.0.0/24"
  LeafTor: "39.0.0.0/24"
  Host: "49.0.0.0/24"
IPv6Pool:
  LeafSpine: null
  LeafTor: null
  Host: null
NTP:
  server: "x.x.x.10"
  timezone: "Asia/Kolkata"
SYSLOG:
  server: "x.x.x.10"
SNMP:
  trapserver: "x.x.x.10"
Parameters:
  hosts_per_l3_subnet: 10
```

## <b>Configure, Validate & Verify through UI</b>
![img](../img/Configure_VALIDATE_Verify.md.png)

## <b>Running config on Sonic Switch </b>

=== "Leaf-1"

    ```sh
    router-id 10.10.10.3
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-1
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.3
    !
    interface port-channel 200
    mtu 9000
    ip address 49.0.0.0/27
    !
    interface port-channel 201
    mtu 9000
    ip address 49.0.0.32/27
    !
    interface port-channel 999
    mtu 9000
    ip address 192.168.0.0/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 200 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    ip address 40.0.0.1/31
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    ip address 40.0.0.9/31
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet64
    no shutdown
    mtu 9000
    ip address 40.0.0.16/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.3/32
    !
    router bgp 2001
    neighbor 40.0.0.0 remote-as 1001
    neighbor 40.0.0.17 remote-as 2001
    neighbor 40.0.0.8 remote-as 1002
    neighbor 40.0.0.0 capability extended-nexthop
    neighbor 40.0.0.17 capability extended-nexthop
    neighbor 40.0.0.8 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.0 allowas-in 1
    neighbor 40.0.0.17 allowas-in 1
    neighbor 40.0.0.8 allowas-in 1
    network 40.0.0.0/31
    network 40.0.0.16/31
    network 40.0.0.8/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    !
    !
    mlag domain-id 1
    peer-address 192.168.0.1
    peer-link port-channel 999
    src-address 192.168.0.0
    member port-channel 200
    member port-channel 201
    ```

=== "Leaf2"

    ```sh
    router-id 10.10.10.4
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-2
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.4
    !
    interface port-channel 200
    mtu 9000
    ip address 49.0.0.0/27
    !
    interface port-channel 201
    mtu 9000
    ip address 49.0.0.32/27
    !
    interface port-channel 999
    mtu 9000
    ip address 192.168.0.1/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 200 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    ip address 40.0.0.3/31
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    ip address 40.0.0.11/31
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet64
    no shutdown
    mtu 9000
    ip address 40.0.0.17/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.4/32
    !
    router bgp 2001
    neighbor 40.0.0.10 remote-as 1002
    neighbor 40.0.0.16 remote-as 2001
    neighbor 40.0.0.2 remote-as 1001
    neighbor 40.0.0.10 capability extended-nexthop
    neighbor 40.0.0.16 capability extended-nexthop
    neighbor 40.0.0.2 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.10 allowas-in 1
    neighbor 40.0.0.16 allowas-in 1
    neighbor 40.0.0.2 allowas-in 1
    network 40.0.0.10/31
    network 40.0.0.16/31
    network 40.0.0.2/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    !
    !
    mlag domain-id 1
    peer-address 192.168.0.0
    peer-link port-channel 999
    src-address 192.168.0.1
    member port-channel 200
    member port-channel 201
    ```

=== "Leaf3"

    ```sh
    router-id 10.10.10.6
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-3
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.6
    !
    interface port-channel 200
    mtu 9000
    ip address 49.0.0.64/27
    !
    interface port-channel 201
    mtu 9000
    ip address 49.0.0.96/27
    !
    interface port-channel 999
    mtu 9000
    ip address 192.168.0.2/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 200 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    ip address 40.0.0.5/31
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    ip address 40.0.0.13/31
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet60
    no shutdown
    mtu 9000
    ip address 40.0.0.22/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.6/32
    !
    router bgp 2002
    neighbor 40.0.0.12 remote-as 1002
    neighbor 40.0.0.23 remote-as 2002
    neighbor 40.0.0.4 remote-as 1001
    neighbor 40.0.0.12 capability extended-nexthop
    neighbor 40.0.0.23 capability extended-nexthop
    neighbor 40.0.0.4 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.12 allowas-in 1
    neighbor 40.0.0.23 allowas-in 1
    neighbor 40.0.0.4 allowas-in 1
    network 40.0.0.12/31
    network 40.0.0.22/31
    network 40.0.0.4/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    !
    !
    mlag domain-id 1
    peer-address 192.168.0.3
    peer-link port-channel 999
    src-address 192.168.0.2
    member port-channel 200
    member port-channel 201
    ```

=== "Leaf4"

    ```sh
    router-id 10.10.10.7
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-4
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.7
    !
    interface port-channel 200
    mtu 9000
    ip address 49.0.0.64/27
    !
    interface port-channel 201
    mtu 9000
    ip address 49.0.0.96/27
    !
    interface port-channel 999
    mtu 9000
    ip address 192.168.0.3/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 200 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 201 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    ip address 40.0.0.7/31
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    ip address 40.0.0.15/31
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 999 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet60
    no shutdown
    mtu 9000
    ip address 40.0.0.23/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.7/32
    !
    router bgp 2002
    neighbor 40.0.0.14 remote-as 1002
    neighbor 40.0.0.22 remote-as 2002
    neighbor 40.0.0.6 remote-as 1001
    neighbor 40.0.0.14 capability extended-nexthop
    neighbor 40.0.0.22 capability extended-nexthop
    neighbor 40.0.0.6 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.14 allowas-in 1
    neighbor 40.0.0.22 allowas-in 1
    neighbor 40.0.0.6 allowas-in 1
    network 40.0.0.14/31
    network 40.0.0.22/31
    network 40.0.0.6/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    !
    !
    mlag domain-id 1
    peer-address 192.168.0.2
    peer-link port-channel 999
    src-address 192.168.0.3
    member port-channel 200
    member port-channel 201
    ```

