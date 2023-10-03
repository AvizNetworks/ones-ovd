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