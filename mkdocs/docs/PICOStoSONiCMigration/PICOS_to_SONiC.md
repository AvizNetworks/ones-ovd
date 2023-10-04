# Why Migrate from PICOS to SONiC 

Existing PICOS  customers  who are looking to transition to an open networking NOS software for their network operation , SONiC is the perfect Solution. SONiC NOS brings great value for customers with deployments running PICOS. SONiC containerized architecture ensures High availability, elasticity, flexibility, innovation, resiliency of workload and applications in a Data center fabric. Multivendor ASIC support provided by Switch abstraction interface (SAI) in SONiC based green field and  brownfield fabric deployments provides customers the choice of switches of different speeds from various vendors. 

Aviz offers  SONiC support to live Data center production which helps operators reduce their TCO by 40% while bringing up Data center underlay and overlay services over a Fabric by seamlessly upgrading to SONiC NOS over any choice of vendor switches. 

This document is intended for network administrators with PICOS background. This guide will help network admins to migrate their current PICOS deployment for various Fabric architectures to SONiC.
PICOS User guide  https://docs.pica8.com/ can be used as a checklist to get started with the  migration plan from PICOS to SONiC. Following  document provides example configuration commands for comparison.

# SONiC NOS Installation from ONIE  
Before entering into ONIE install mode, operator should ensure to uninstall the PICOS
Note: Switch shall automatically enter the ONIE install mode if there's no NOS installed yet.

Step 1. Enter the ONIE install mode

GNU GRUB  version 2.02
 
+----------------------------------------------------------------------------+
|*ONIE: Install OS                                                       	|
| ONIE: Rescue                                                           	|
| ONIE: Uninstall OS                                                     	|
| ONIE: Update ONIE                                                      	|
| ONIE: Embed ONIE                                                       	|
| DIAG: Accton Diagnostic (accton_as7326_56x)                            	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
|                                                                        	|
+----------------------------------------------------------------------------+
 

<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
  }
  th{
    border: 1px solid black;
    padding: 8px;
    text-align: left;
    color: white;
    background-color:  #000080;
    
  }

  td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

 
     Use the ^ and v keys to select which entry is highlighted.
     Press enter to boot the selected OS, `e' to edit the commands
     before booting or `c' for a command-line.
     The highlighted entry will be executed automatically in 2s.

     Since switch will automatically start the ONIE Service Discovery, the ONIE-Stop command ensures the  users enter the keywords  easily. This is not a mandatory  command but it  won't affect installation no matter whether the user executes it or not though   it will enable users  to clear the ONIE running logs screen . 

  ##ONIE-stop

Step 2: Call the command to stop ONIE discovery process because DHCP server is not available 
ONIE:/ # onie-stop
discover: installer mode detected.
Stopping: discover... done.

Step 3. Setup the ip address binding to switch management port
ONIE:/ # ifconfig eth0 192.168.1.2 netmask 255.255.255.0
Caution: If user does not specific any management IP statically , Default ONIE  will get ip from DHCP server 
Step 4. Install the image from the remote URL via TFTP server IP location 
ONIE:/ # onie-nos-install tftp://192.168.1.1/SONiC.Edgecore-SONiC_20230330_091754_ec202111_352.bin
If the installation is successful, the device will reboot automatically and boot-up with SONiC.

<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
  }
  th{
    border: 1px solid black;
    padding: 8px;
    text-align: left;
    color: white;
    background-color:  #000080;
    
  }

  td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

#  # Example SONiC Image upgrade from ONIE prompt

