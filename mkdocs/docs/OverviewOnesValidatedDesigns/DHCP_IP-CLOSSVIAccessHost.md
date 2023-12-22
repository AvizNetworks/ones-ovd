# <b>DHCP IP-CLOS SVI Access Host</b>
This template enables NetOps to enable DHCP Relay on the egress  interface of a leaf switch facing server host

## <b>YAML Template</b>

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
      ASN: 1001
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
      ASN: 1001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L1_Ethernet48 | S1_Ethernet0"
          staticLink: true
          properties: null
        - link: "L1_Ethernet52 | S2_Ethernet0"
          staticLink: true
          properties: null
        - link: "L1_Ethernet0 |  H1_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 200
    - switchId: 2
      switchName: "Leaf-2"
      ipAddress: "x.x.x.14"
      ASN: 1001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L2_Ethernet48 | S1_Ethernet4"
          staticLink: true
          properties: null
        - link: "L2_Ethernet52 | S2_Ethernet4"
          staticLink: true
          properties: null
        - link: "L2_Ethernet4 |  H2_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 201
    - switchId: 3
      switchName: "Leaf-3"
      ipAddress: "x.x.x.15"
      ASN: 1001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L3_Ethernet48 | S1_Ethernet8"
          staticLink: true
          properties: null
        - link: "L3_Ethernet52 | S2_Ethernet8"
          staticLink: true
          properties: null
        - link: "L3_Ethernet0 |  H3_Ethernet0"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 200
    - switchId: 4
      switchName: "Leaf-4"
      ipAddress: "x.x.x.16"
      ASN: 1001
      Credentials:
        user: "admin"
        password: "admin"
      mclag:
      Links:
        - link: "L4_Ethernet48 | S1_Ethernet12"
          staticLink: true
          properties: null
        - link: "L4_Ethernet52 | S2_Ethernet12"
          staticLink: true
          properties: null
        - link: "L4_Ethernet4 |  H4_Ethernet1"
          staticLink: true
          properties:
            mode: "L2-Access"
            vlan: 201
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
DHCPRelay:
  server: "x.x.x.10" # can be one or more than one comma separated list
  sourceinterface: "Loopback0" #it could be any valid interface name here
Parameters:
  vlan: "200-205"
  anycast_gateway: "x.x.x.0/23"
  hosts_per_vlan: 10


```

## <b>Configure, Validate & Verify through UI</b>

![img](../img/Configure_VALIDATE_Verify.md.png)


## <b>Show running config on switch </b>
=== "Leaf1"

    ```sh
    router-id 10.10.10.2
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
    set src 10.10.10.2
    !
    vlan 200
    dhcp-relay x.x.x.10
    dhcp-relay src-interface Loopback0
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    switchport access vlan 200
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
    interface vlan 200
    ip address x.x.x.1/25
    !
    interface loopback 0
    ip address 10.10.10.10/32
    !
    interface loopback 1
    ip address 10.10.10.2/32
    !
    router bgp 1001
    neighbor 40.0.0.0 remote-as 1001
    neighbor 40.0.0.8 remote-as 1001
    neighbor 40.0.0.0 capability extended-nexthop
    neighbor 40.0.0.8 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.0 allowas-in 1
    neighbor 40.0.0.8 allowas-in 1
    network 40.0.0.0/31
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
    vlan 201
    dhcp-relay x.x.x.10
    dhcp-relay src-interface Loopback0
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    switchport access vlan 201
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
    interface vlan 201
    ip address x.x.x.129/25
    !
    interface loopback 0
    ip address 10.10.10.10/32
    !
    interface loopback 1
    ip address 10.10.10.4/32
    !
    router bgp 1001
    neighbor 40.0.0.10 remote-as 1001
    neighbor 40.0.0.2 remote-as 1001
    neighbor 40.0.0.10 capability extended-nexthop
    neighbor 40.0.0.2 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.10 allowas-in 1
    neighbor 40.0.0.2 allowas-in 1
    network 40.0.0.10/31
    network 40.0.0.2/31
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
    vlan 200
    dhcp-relay x.x.x.10
    dhcp-relay src-interface Loopback0
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    switchport access vlan 200
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
    interface vlan 200
    ip address 100.10.1.1/25
    !
    interface loopback 0
    ip address 10.10.10.10/32
    !
    interface loopback 1
    ip address 10.10.10.6/32
    !
    router bgp 1001
    neighbor 40.0.0.12 remote-as 1001
    neighbor 40.0.0.4 remote-as 1001
    neighbor 40.0.0.12 capability extended-nexthop
    neighbor 40.0.0.4 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.12 allowas-in 1
    neighbor 40.0.0.4 allowas-in 1
    network 40.0.0.12/31
    network 40.0.0.4/31
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
    vlan 201
    dhcp-relay x.x.x.10
    dhcp-relay src-interface Loopback0
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    switchport access vlan 201
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
    interface vlan 201
    ip address 100.10.1.129/25
    !
    interface loopback 0
    ip address 10.10.10.10/32
    !
    interface loopback 1
    ip address 10.10.10.8/32
    !
    router bgp 1001
    neighbor 40.0.0.14 remote-as 1001
    neighbor 40.0.0.6 remote-as 1001
    neighbor 40.0.0.14 capability extended-nexthop
    neighbor 40.0.0.6 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.14 allowas-in 1
    neighbor 40.0.0.6 allowas-in 1
    network 40.0.0.14/31
    network 40.0.0.6/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```


=== "Spine1"

    ```sh
    router-id 10.10.10.0
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Spine-1
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.0
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    ip address 40.0.0.0/31
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    ip address 40.0.0.6/31
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    ip address 40.0.0.2/31
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    ip address 40.0.0.4/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.0/32
    !
    router bgp 1001
    neighbor 40.0.0.1 remote-as 1001
    neighbor 40.0.0.3 remote-as 1001
    neighbor 40.0.0.5 remote-as 1001
    neighbor 40.0.0.7 remote-as 1001
    neighbor 40.0.0.1 capability extended-nexthop
    neighbor 40.0.0.3 capability extended-nexthop
    neighbor 40.0.0.5 capability extended-nexthop
    neighbor 40.0.0.7 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.1 allowas-in 1
    neighbor 40.0.0.3 allowas-in 1
    neighbor 40.0.0.5 allowas-in 1
    neighbor 40.0.0.7 allowas-in 1
    neighbor 40.0.0.1 route-reflector-client
    neighbor 40.0.0.3 route-reflector-client
    neighbor 40.0.0.5 route-reflector-client
    neighbor 40.0.0.7 route-reflector-client
    neighbor 40.0.0.1 next-hop-self force
    neighbor 40.0.0.3 next-hop-self force
    neighbor 40.0.0.5 next-hop-self force
    neighbor 40.0.0.7 next-hop-self force
    network 40.0.0.0/31
    network 40.0.0.2/31
    network 40.0.0.4/31
    network 40.0.0.6/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```


=== "Spine2"

    ```sh
    router-id 10.10.10.1
    ntp add x.x.x.10
    clock timezone Asia/Kolkata
    syslog add x.x.x.10
    snmp-server trap modify 2 x.x.x.10 port 161 vrf None community Public
    hostname Spine-2
    ip protocol bgp route-map RM_SET_SRC
    !
    route-map FMCLI_IPV6_NH_GLOBAL permit 1
    on-match next
    set ipv6 next-hop prefer-global
    !
    route-map RM_SET_SRC permit 10
    set src 10.10.10.1
    !
    interface ethernet Ethernet0
    no shutdown
    mtu 9000
    ip address 40.0.0.8/31
    forward-error-correction none
    !
    interface ethernet Ethernet12
    no shutdown
    mtu 9000
    ip address 40.0.0.14/31
    forward-error-correction none
    !
    interface ethernet Ethernet4
    no shutdown
    mtu 9000
    ip address 40.0.0.10/31
    forward-error-correction none
    !
    interface ethernet Ethernet8
    no shutdown
    mtu 9000
    ip address 40.0.0.12/31
    forward-error-correction none
    !
    interface loopback 1
    ip address 10.10.10.1/32
    !
    router bgp 1001
    neighbor 40.0.0.11 remote-as 1001
    neighbor 40.0.0.13 remote-as 1001
    neighbor 40.0.0.15 remote-as 1001
    neighbor 40.0.0.9 remote-as 1001
    neighbor 40.0.0.11 capability extended-nexthop
    neighbor 40.0.0.13 capability extended-nexthop
    neighbor 40.0.0.15 capability extended-nexthop
    neighbor 40.0.0.9 capability extended-nexthop
    bgp bestpath as-path multipath-relax
    no bgp ebgp-requires-policy
    address-family ipv4 unicast
    neighbor 40.0.0.11 allowas-in 1
    neighbor 40.0.0.13 allowas-in 1
    neighbor 40.0.0.15 allowas-in 1
    neighbor 40.0.0.9 allowas-in 1
    neighbor 40.0.0.11 route-reflector-client
    neighbor 40.0.0.13 route-reflector-client
    neighbor 40.0.0.15 route-reflector-client
    neighbor 40.0.0.9 route-reflector-client
    neighbor 40.0.0.11 next-hop-self force
    neighbor 40.0.0.13 next-hop-self force
    neighbor 40.0.0.15 next-hop-self force
    neighbor 40.0.0.9 next-hop-self force
    network 40.0.0.10/31
    network 40.0.0.12/31
    network 40.0.0.14/31
    network 40.0.0.8/31
    redistribute connected
    redistribute static
    !
    address-family ipv6 unicast
    redistribute connected
    redistribute static
    ```


