# <b>BGP over Port Channel with Sflow enabled</b>

## <b>YAML Template</b>

```yaml
Inventory:
  SSpines: 0
  Spines: 0
  Leafs: 6
  Tors: 0
Connectivity:
  SSpine: []
  Spine: []        
  Leaf:
    - switchId: 1
      switchName: "Leaf-1"
      ipAddress: "x.x.x.13"
      ASN: 1001 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      sflow:
        enabled: true
        agent: "Loopback3"
        polling_interval: 20
      Links:
        - link: "L1_Ethernet48 | L5_Ethernet0"
          staticLink: true
          properties:
            po_group: 11
            sflow_sampling_rate: 1000
        - link: "L1_Ethernet52 | L6_Ethernet0"
          staticLink: true
          properties:
            po_group: 21
            sflow_sampling_rate: 1000
        - link: "L1_Ethernet56 |  L2_Ethernet56"
          staticLink: true
          properties:
            po_group: 33
            sflow_sampling_rate: 10000
        - link: "L1_Ethernet45 |  L3_Ethernet45"
          staticLink: true
          properties:
            po_group: 32
            sflow_sampling_rate: 10000
        - link: "L1_Ethernet46 |  L4_Ethernet45"
          staticLink: true
          properties:
            po_group: 31  
            sflow_sampling_rate: 10000                  
        - link: "L1_Ethernet0 |  H1_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 201
            mc_po_group: 201
        - link: "L1_Ethernet4 |  H2_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 202
            mc_po_group: 202
    - switchId: 2
      switchName: "Leaf-2"
      ipAddress: "x.x.x.14"
      ASN: 1002 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      sflow:
        enabled: true
        agent: "Loopback0"
        polling_interval: 20
      Links:
        - link: "L2_Ethernet48 | L5_Ethernet4"
          staticLink: true
          properties:
            po_group: 12
            sflow_sampling_rate: "default"
        - link: "L2_Ethernet52 | L6_Ethernet4"
          staticLink: true
          properties:
            po_group: 22
            sflow_sampling_rate: "default"
        - link: "L2_Ethernet56 | L1_Ethernet56"
          staticLink: true
          properties:
            po_group: 33
            sflow_sampling_rate: "default"
        - link: "L2_Ethernet45 | L3_Ethernet46"
          staticLink: true
          properties:
            po_group: 34
            sflow_sampling_rate: "default"
        - link: "L2_Ethernet46 | L4_Ethernet46"
          staticLink: true
          properties:
            po_group: 36 
            sflow_sampling_rate: "default"                   
        - link: "L2_Ethernet0 |  H1_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 203
            mc_po_group: 203
        - link: "L2_Ethernet4 |  H2_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 204
            mc_po_group: 204
    - switchId: 3
      switchName: "Leaf-3"
      ipAddress: "x.x.x.15"
      ASN: 1003 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L3_Ethernet48 | L5_Ethernet8"
          staticLink: true
          properties:
            po_group: 13
        - link: "L3_Ethernet52 | L6_Ethernet8"
          staticLink: true
          properties:
            po_group: 23
        - link: "L3_Ethernet56 | L4_Ethernet56"
          staticLink: true
          properties:
            po_group: 35
        - link: "L3_Ethernet45 | L1_Ethernet45"
          staticLink: true
          properties:
            po_group: 32
        - link: "L3_Ethernet46 | L2_Ethernet45"
          staticLink: true
          properties:
            po_group: 34                    
        - link: "L3_Ethernet0 |  H3_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 205
            mc_po_group: 205
        - link: "L3_Ethernet4 |  H4_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 206
            mc_po_group: 206
    - switchId: 4
      switchName: "Leaf-4"
      ipAddress: "x.x.x.16"
      ASN: 1004 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L4_Ethernet48 | L5_Ethernet12"
          staticLink: true
          properties:
            po_group: 14
        - link: "L4_Ethernet52 | L6_Ethernet12"
          staticLink: true
          properties:
            po_group: 24
        - link: "L4_Ethernet56 | L3_Ethernet56"
          staticLink: true
          properties:
            po_group: 35
        - link: "L4_Ethernet45 | L1_Ethernet46"
          staticLink: true
          properties:
            po_group: 31
        - link: "L4_Ethernet46 | L2_Ethernet46"
          staticLink: true
          properties:
            po_group: 36                   
        - link: "L4_Ethernet0 |  H3_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 207
            mc_po_group: 207
        - link: "L4_Ethernet4 |  H4_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 208
            mc_po_group: 208
    - switchId: 5
      switchName: "Leaf-5-Spine-1"
      ipAddress: "x.x.x.11"
      ASN: 1005 
      Credentials:
        user: "admin"
        password: "admin"
      mclag:     
      Links:
        - link: "L5_Ethernet0 | L1_Ethernet48"
          staticLink: true
          properties:
            po_group: 11
        - link: "L5_Ethernet4 | L2_Ethernet48"
          staticLink: true
          properties:
            po_group: 12
        - link: "L5_Ethernet8 | L3_Ethernet48"
          staticLink: true
          properties:
            po_group: 13
        - link: "L5_Ethernet12 | L4_Ethernet48"
          staticLink: true
          properties:
            po_group: 14
        - link: "L5_Ethernet124 | L6_Ethernet124"
          staticLink: true
          properties:
            po_group: 15           
    - switchId: 6
      switchName: "Leaf-6-Spine-2"
      ipAddress: "x.x.x.12"
      ASN: 1006 
      Credentials:
        user: "admin"
        password: "admin"
      mclag: 
      Links:
        - link: "L6_Ethernet0 | L1_Ethernet52"
          staticLink: true
          properties:
            po_group: 21
        - link: "L6_Ethernet4 | L2_Ethernet52"
          staticLink: true
          properties:
            po_group: 22
        - link: "L6_Ethernet8 | L3_Ethernet52"
          staticLink: true
          properties:
            po_group: 23
        - link: "L6_Ethernet12 | L4_Ethernet52"
          staticLink: true
          properties:
            po_group: 24
        - link: "L6_Ethernet124 | L5_Ethernet124"
          staticLink: true
          properties:
            po_group: 15
  Tor: []
BGP:
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
NTP:
  server: "x.x.x.10"
  timezone: "Asia/Kolkata"
SYSLOG:
  server: "x.x.x.10"
SNMP:
  trapserver: "x.x.x.10"
Parameters:
  vlan: "201,202,203,204,205,206,207,208"
  anycast_gateway: "x.x.x.0/23"
  hosts_per_vlan: 10
L2LS:
  enabled: false
  mode: "L2" # OverL2 and OverL3
Sflow:
  collectors:
      - id: 1
        ip: "x.x.x.10"
        port: 6343  
```

## <b>Configure, Validate & Verify through UI</b>


## <b>Show running config on sonic switch </b>

=== "Leaf1"

    ```sh
    router-id 10.10.10.0
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
    set src 10.10.10.0
    !
    vlan 201
    !
    vlan 202
    !
    interface port-channel 11
    mtu 9000
    ip address 40.0.0.0/31
    !
    interface port-channel 201
    mtu 9000
    switchport access vlan 201
    !
    interface port-channel 202
    mtu 9000
    switchport access vlan 202
    !
    interface port-channel 21
    mtu 9000
    ip address 40.0.0.2/31
    !
    interface port-channel 31
    mtu 9000
    ip address 40.0.0.8/31
    !
    interface port-channel 32
    mtu 9000
    ip address 40.0.0.6/31
    !
    interface port-channel 33
    mtu 9000
    ip address 40.0.0.4/31
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
    interface ethernet Ethernet45
    no shutdown
    mtu 9000
    channel-group 32 mode active
    sflow enable
    sflow sampling-rate 10000
    forward-error-correction none
    !
    interface ethernet Ethernet46
    no shutdown
    mtu 9000
    channel-group 31 mode active
    sflow enable
    sflow sampling-rate 10000
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 11 mode active
    sflow enable
    sflow sampling-rate 1000
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 21 mode active
    sflow enable
    sflow sampling-rate 1000
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 33 mode active
    sflow enable
    sflow sampling-rate 10000
    forward-error-correction none
    !
    interface vlan 201
    ip address x.x.x.1/26
    !
    interface vlan 202
    ip address x.x.x.65/26
    !
    interface loopback 1
    ip address 10.10.10.0/32
    !
    interface loopback 3
    ip address 10.10.10.2/32
    !
    feature sflow
    sflow collector collector1 x.x.x.10 port 6343
    sflow agent-id add interface Loopback3
    sflow polling-interval 20
    !
    router bgp 1001
    neighbor 40.0.0.1 remote-as 1005
    neighbor 40.0.0.3 remote-as 1006
    neighbor 40.0.0.5 remote-as 1002
    neighbor 40.0.0.7 remote-as 1003
    neighbor 40.0.0.9 remote-as 1004
    neighbor 40.0.0.1 capability extended-nexthop
    neighbor 40.0.0.3 capability extended-nexthop
    neighbor 40.0.0.5 capability extended-nexthop
    neighbor 40.0.0.7 capability extended-nexthop
    neighbor 40.0.0.9 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.1 allowas-in 1
    neighbor 40.0.0.3 allowas-in 1
    neighbor 40.0.0.5 allowas-in 1
    neighbor 40.0.0.7 allowas-in 1
    neighbor 40.0.0.9 allowas-in 1
    network 40.0.0.0/31
    network 40.0.0.2/31
    network 40.0.0.4/31
    network 40.0.0.6/31
    network 40.0.0.8/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```

=== "Leaf2"

    ```sh
    router-id 10.10.10.3
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
    set src 10.10.10.3
    !
    vlan 203
    !
    vlan 204
    !
    interface port-channel 12
    mtu 9000
    ip address 40.0.0.10/31
    !
    interface port-channel 203
    mtu 9000
    switchport access vlan 203
    !
    interface port-channel 204
    mtu 9000
    switchport access vlan 204
    !
    interface port-channel 22
    mtu 9000
    ip address 40.0.0.12/31
    !
    interface port-channel 33
    mtu 9000
    ip address 40.0.0.5/31
    !
    interface port-channel 34
    mtu 9000
    ip address 40.0.0.14/31
    !
    interface port-channel 36
    mtu 9000
    ip address 40.0.0.16/31
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
    interface ethernet Ethernet45
    no shutdown
    mtu 9000
    channel-group 34 mode active
    sflow enable
    forward-error-correction none
    !
    interface ethernet Ethernet46
    no shutdown
    mtu 9000
    channel-group 36 mode active
    sflow enable
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 12 mode active
    sflow enable
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 22 mode active
    sflow enable
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 33 mode active
    sflow enable
    forward-error-correction none
    !
    interface vlan 203
    ip address x.x.x.129/26
    !
    interface vlan 204
    ip address x.x.x.193/26
    !
    interface loopback 0
    ip address 10.10.10.5/32
    !
    interface loopback 1
    ip address 10.10.10.3/32
    !
    feature sflow
    sflow collector collector1 x.x.x.10 port 6343
    sflow agent-id add interface Loopback0
    sflow polling-interval 20
    !
    router bgp 1002
    neighbor 40.0.0.11 remote-as 1005
    neighbor 40.0.0.13 remote-as 1006
    neighbor 40.0.0.15 remote-as 1003
    neighbor 40.0.0.17 remote-as 1004
    neighbor 40.0.0.4 remote-as 1001
    neighbor 40.0.0.11 capability extended-nexthop
    neighbor 40.0.0.13 capability extended-nexthop
    neighbor 40.0.0.15 capability extended-nexthop
    neighbor 40.0.0.17 capability extended-nexthop
    neighbor 40.0.0.4 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.11 allowas-in 1
    neighbor 40.0.0.13 allowas-in 1
    neighbor 40.0.0.15 allowas-in 1
    neighbor 40.0.0.17 allowas-in 1
    neighbor 40.0.0.4 allowas-in 1
    network 40.0.0.10/31
    network 40.0.0.12/31
    network 40.0.0.14/31
    network 40.0.0.16/31
    network 40.0.0.4/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
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
    vlan 205
    !
    vlan 206
    !
    interface port-channel 13
    mtu 9000
    ip address 40.0.0.18/31
    !
    interface port-channel 205
    mtu 9000
    switchport access vlan 205
    !
    interface port-channel 206
    mtu 9000
    switchport access vlan 206
    !
    interface port-channel 23
    mtu 9000
    ip address 40.0.0.20/31
    !
    interface port-channel 32
    mtu 9000
    ip address 40.0.0.7/31
    !
    interface port-channel 34
    mtu 9000
    ip address 40.0.0.15/31
    !
    interface port-channel 35
    mtu 9000
    ip address 40.0.0.22/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 205 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 206 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet45
    no shutdown
    mtu 9000
    channel-group 32 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet46
    no shutdown
    mtu 9000
    channel-group 34 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 13 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 23 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 35 mode active
    forward-error-correction none
    !
    interface vlan 205
    ip address 100.10.1.1/26
    !
    interface vlan 206
    ip address 100.10.1.65/26
    !
    interface loopback 1
    ip address 10.10.10.6/32
    !
    router bgp 1003
    neighbor 40.0.0.14 remote-as 1002
    neighbor 40.0.0.19 remote-as 1005
    neighbor 40.0.0.21 remote-as 1006
    neighbor 40.0.0.23 remote-as 1004
    neighbor 40.0.0.6 remote-as 1001
    neighbor 40.0.0.14 capability extended-nexthop
    neighbor 40.0.0.19 capability extended-nexthop
    neighbor 40.0.0.21 capability extended-nexthop
    neighbor 40.0.0.23 capability extended-nexthop
    neighbor 40.0.0.6 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.14 allowas-in 1
    neighbor 40.0.0.19 allowas-in 1
    neighbor 40.0.0.21 allowas-in 1
    neighbor 40.0.0.23 allowas-in 1
    neighbor 40.0.0.6 allowas-in 1
    network 40.0.0.14/31
    network 40.0.0.18/31
    network 40.0.0.20/31
    network 40.0.0.22/31
    network 40.0.0.6/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```

=== "Leaf4"

    ```sh
    router-id 10.10.10.8
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
    set src 10.10.10.8
    !
    vlan 207
    !
    vlan 208
    !
    interface port-channel 14
    mtu 9000
    ip address 40.0.0.24/31
    !
    interface port-channel 207
    mtu 9000
    switchport access vlan 207
    !
    interface port-channel 208
    mtu 9000
    switchport access vlan 208
    !
    interface port-channel 24
    mtu 9000
    ip address 40.0.0.26/31
    !
    interface port-channel 31
    mtu 9000
    ip address 40.0.0.9/31
    !
    interface port-channel 35
    mtu 9000
    ip address 40.0.0.23/31
    !
    interface port-channel 36
    mtu 9000
    ip address 40.0.0.17/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 207 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 208 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet45
    no shutdown
    mtu 9000
    channel-group 31 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet46
    no shutdown
    mtu 9000
    channel-group 36 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet48
    no shutdown
    mtu 9000
    channel-group 14 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet52
    no shutdown
    mtu 9000
    channel-group 24 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet56
    no shutdown
    mtu 9000
    channel-group 35 mode active
    forward-error-correction none
    !
    interface vlan 207
    ip address 100.10.1.129/26
    !
    interface vlan 208
    ip address 100.10.1.193/26
    !
    interface loopback 1
    ip address 10.10.10.8/32
    !
    router bgp 1004
    neighbor 40.0.0.16 remote-as 1002
    neighbor 40.0.0.22 remote-as 1003
    neighbor 40.0.0.25 remote-as 1005
    neighbor 40.0.0.27 remote-as 1006
    neighbor 40.0.0.8 remote-as 1001
    neighbor 40.0.0.16 capability extended-nexthop
    neighbor 40.0.0.22 capability extended-nexthop
    neighbor 40.0.0.25 capability extended-nexthop
    neighbor 40.0.0.27 capability extended-nexthop
    neighbor 40.0.0.8 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.16 allowas-in 1
    neighbor 40.0.0.22 allowas-in 1
    neighbor 40.0.0.25 allowas-in 1
    neighbor 40.0.0.27 allowas-in 1
    neighbor 40.0.0.8 allowas-in 1
    network 40.0.0.16/31
    network 40.0.0.22/31
    network 40.0.0.24/31
    network 40.0.0.26/31
    network 40.0.0.8/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```

=== "Spine1"

    ```sh
    router-id 10.10.10.10
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-5-Spine-1
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.10
    !
    interface port-channel 11
    mtu 9000
    ip address 40.0.0.1/31
    !
    interface port-channel 12
    mtu 9000
    ip address 40.0.0.11/31
    !
    interface port-channel 13
    mtu 9000
    ip address 40.0.0.19/31
    !
    interface port-channel 14
    mtu 9000
    ip address 40.0.0.25/31
    !
    interface port-channel 15
    mtu 9000
    ip address 40.0.0.28/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 11 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    channel-group 14 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet124
    no shutdown
    mtu 9000
    channel-group 15 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 12 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    channel-group 13 mode active
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.10/32
    !
    router bgp 1005
    neighbor 40.0.0.0 remote-as 1001
    neighbor 40.0.0.10 remote-as 1002
    neighbor 40.0.0.18 remote-as 1003
    neighbor 40.0.0.24 remote-as 1004
    neighbor 40.0.0.29 remote-as 1006
    neighbor 40.0.0.0 capability extended-nexthop
    neighbor 40.0.0.10 capability extended-nexthop
    neighbor 40.0.0.18 capability extended-nexthop
    neighbor 40.0.0.24 capability extended-nexthop
    neighbor 40.0.0.29 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.0 allowas-in 1
    neighbor 40.0.0.10 allowas-in 1
    neighbor 40.0.0.18 allowas-in 1
    neighbor 40.0.0.24 allowas-in 1
    neighbor 40.0.0.29 allowas-in 1
    network 40.0.0.0/31
    network 40.0.0.10/31
    network 40.0.0.18/31
    network 40.0.0.24/31
    network 40.0.0.28/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```

=== "Spine2"

    ```sh
    router-id 10.10.10.12
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Leaf-6-Spine-2
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.12
    !
    interface port-channel 15
    mtu 9000
    ip address 40.0.0.29/31
    !
    interface port-channel 21
    mtu 9000
    ip address 40.0.0.3/31
    !
    interface port-channel 22
    mtu 9000
    ip address 40.0.0.13/31
    !
    interface port-channel 23
    mtu 9000
    ip address 40.0.0.21/31
    !
    interface port-channel 24
    mtu 9000
    ip address 40.0.0.27/31
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    channel-group 21 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    channel-group 24 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet124
    no shutdown
    mtu 9000
    channel-group 15 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    channel-group 22 mode active
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    channel-group 23 mode active
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.12/32
    !
    router bgp 1006
    neighbor 40.0.0.12 remote-as 1002
    neighbor 40.0.0.2 remote-as 1001
    neighbor 40.0.0.20 remote-as 1003
    neighbor 40.0.0.26 remote-as 1004
    neighbor 40.0.0.28 remote-as 1005
    neighbor 40.0.0.12 capability extended-nexthop
    neighbor 40.0.0.2 capability extended-nexthop
    neighbor 40.0.0.20 capability extended-nexthop
    neighbor 40.0.0.26 capability extended-nexthop
    neighbor 40.0.0.28 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.12 allowas-in 1
    neighbor 40.0.0.2 allowas-in 1
    neighbor 40.0.0.20 allowas-in 1
    neighbor 40.0.0.26 allowas-in 1
    neighbor 40.0.0.28 allowas-in 1
    network 40.0.0.12/31
    network 40.0.0.2/31
    network 40.0.0.20/31
    network 40.0.0.26/31
    network 40.0.0.28/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```