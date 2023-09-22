# ONES ‘s Sample REST APIs

## Simplified Day 1 Orchestration

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>uploadDay1Config</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><b>Intent Driven orchestration</b> -Performs Day 1 fabric orchestration for various Data Center topologies.This method will initiate the Day-1 orchestration depending on  the topology and intent supplied via template file. This  REST API  allows network operators  to upload an entire intent file (yaml-based) and orchestrate the entire fabric in a desired intent based underlay and overlay. For example, if customers  want to provision  BGP as an underlay and  VXLAN as an overlay ,they can operate the template form and provide minimum parameter inputs , with the rest of the derivation and parameters handled by the ONES application.
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>
    <b>&lt;Intent YAML file- Path to Template file &gt; Output:< Intent ID></b>

Input Parameter for the REST API call -  Template file for the intent configuration for the whole fabric switches enrolled with ONES 
 
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>Returns  the intent ID which is an unique tag mapped to the specific intended input configuration desired by the network operator  while defining the intended configuration with only specific desired network entities </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /uploadDay1Config HTTP/1.1</b>
    Content-Type: application/json; charset=utf-8
    Host: 10.x.x.6:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61
    Input
    configure_az_1.yaml
    Response:
    configure_az_1.yaml_20230223115541
</pre>
    </td>
  </tr>
</table>


<br />

## Get Day 1 Operational Status

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>getDay1ConfigStatus</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><b>getDay1ConfigStatus</b>- Retrieve Generic Intent Status for provisioning over SONiC enabled fabric switches . This  REST API allows network  operators  to  get the status of orchestration progress on a specific switch in a SONiC fabric  enrolled with ONES application 
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>Input: &lt;Intent ID&gt;  Output: JSON (status)</b>

Input Parameter for the Rest API call -  Intent ID for the intent configuration for the complete  fabric switches enrolled with ONES 
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td> Return  the Intent Status for the Day 1 orchestration.  </td>
  </tr>
  <tr>
    <th>Example</th>
    <td> 
    <pre>
    <b>GET/getDay1ConfigStatus?intentID=configure_az_1.yaml_20230223115541</b>
    HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: 10.x.x.6:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    Response
    [
      {
        "intentName": "SNMPServer",
        "ip": "10.x.x.69",
        "verification_status": "1",
        "config_status": "1",
        "logs": ""
      },
    ]
    </pre>
    </td>
  </tr>
</table>


<br />

## ZTP Upgrade SONiC NOS Image

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }


  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>enableZTPUpgrade</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>ZTP upgrade - Perform SONiC upgrade using ZTP mechanism for a specific  image and configuration file.<br /><br />
    Use Case is to support image management for network operators running SONiC fabric <br /><br />

    Both ZTP image upgrade  enables  network operators to change  the version of the operating Sonic NOS during maintenance window
  </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>REST API Input parameter : `<`Input Device IPs`>`</b>
    ZTP  enable  image upgrade by network operators use case is to change  the version of the Sonic  NOS during the maintenance window  . Following  are the  REST API call  signatures for the same.

    REST API: enableZTPUpgrade
    Type: POST
  </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    Response: true/False <br /><br />
    Returns status true,  if ZTP enabled upgrade to SONiC enrolled devices is successful<br /><br />
    Returns status false,  if ZTP enabled upgrade to SONiC enrolled devices is unsuccessful<br /><br />

</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /enableZTPUpgrade HTTP/1.1</b>
    Content-Type: application/json; charset=utf-8
    Host: localhost:8080
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    ["10.x.x.10", "10.x.x.11"]

</pre>
    </td>
  </tr>
</table>


<br />

## Custom Upgrade SONiC NOS Image

<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>upgradeNOSImage</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>
    Custom Image Upgrade for  Sonic devices  . Performs custom image upgrades for specific enrolled  sonic devices only.<br /><br />
    Custom image management via ONES application. ONES application  needs the following #information as the input -<br /><br />

    - List of devices (IP address or host name) for the upgrade image operation.
    - Image path and  user credentials to scp server
  </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>
    <b>REST API Input Parameter : <Device IPs, PathToImage></b> <br />
    Input Parameters: one or more device ip address
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    Response: True/False- <br /><br />
    Returns True status , if  image upgrade to SONiC devices is successful <br /><br />
    Returns False Status , if  Image upgrade to SONiC devices is unsuccessful <br /><br />

 </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
   <b>POST /upgradeNOSImage  HTTP/1.1</b>
  Content-Type: application/json; charset=utf-8
  Host: localhost:8080
  Connection: close
  User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
  Content-Length: 61

  [{"ip":"10.x.x.67","pathToImage":"http://10.x.x.10:8191/mnt/ws/<br />
  images/SONiC-mellanox-e8daeacd.bin"}]</pre>
    </td>
  </tr>
</table>


<br />

## Device Reboot

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>rebootDevice</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>This REST API performs ONES  enrolled SONiC device reboot . Network operators can reboot SONiC devices  enrolled through ONES application via REST API calls
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>REST API Input Parameter : < List of device IPs to be rebooted> </b>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    Response: True/False <br /><br />
    Returns True status , if  Device reboot is successful and ONES receives an acknowledge for the same <br /><br />
    Returns False  status , if Device reboot is unsuccessful and ONES receives an acknowledge for the same <br /><br />

</td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>

    POST /rebootRequest HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: localhost:8080
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61
    Input
    ["10.x.x.236"]
    Response:
    True

</pre>
    </td>
  </tr>
</table>

<br />

## Show Difference between golden and running config

<!-- markdownlint-disable MD033 -->
<style>
 table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }
  
  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>getConfigDiff</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Leveraging this  REST API call, Operators get a view on difference between running configuration and applied configuration on enrolled devices
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>REST API Input Parameter : < List of device IPs for which Configuration difference is required > </b>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>API Response is the difference  of running configuration vs Applied configuration  through  ONES fabric manager </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
<b>POST /getConfigDiff HTTP/1.1</b>
Content-Type: application/json; charset=utf-8
Host: localhost:8080
Connection: close
User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
Content-Length: 61
Input
{ "ip": "10.x.x.66", “diff_only”: “false”}

Response: current config on device vs config done via FM
{
 "orchestrated_config": "Last login: Fri Sep 30 11:44:05 2022 <br/>
 from 10.x.x.150\r\r\nsave\nsave\r\n\rSN2100-Leaf1# save\r\n\r<br /> 
 Saving Configuration\r\n\rSN2100-Leaf1# show run\show run\r\n\r <br />
 configure terminal\r\nrouter-id 3.0.0.2\r\nntp add 128.138.141.172\<br />
 r\nclock timezone Asia/Kolkata\r\nsyslog add 10.x.11\r\snmp-server<br />
  trap modify
}
</pre>
    </td>
  </tr>
</table>


<br />

## Get ONES Version

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>getONESVersion
</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>This REST API call enables network operators  to retrieve  versions of both the ONES Fabric manager application and ONES Fabric manager agent application which are running as container services on SONiC enabled fabric devices .
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>
    <b>Input Parameters: Device ip address - List of Devices IP </b>whose Version numbers needs to be retrieved 
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>Returns the current running  version of  ONE'S controller as well as agent application</td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /getONESVersion HTTP/1.1</b>
    Content-Type: application/json; charset=utf-8
    Host: 10.1.1.8:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61


    ["10.x.x.79"]


    [
      {
        "Version": "v1.3.16/1.3.25",
        "IP": "10.x.x.61"
      }
    ]


</pre>
    </td>
  </tr>
</table>


<br />

## Backup Current running Config

<!-- markdownlint-disable MD033 -->
<style>
 table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }


  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>backupConfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>
After Sonic enabled DC fabric switches are orchestrated completely using Aviz’s ONES REST API  , Network operators can  take the backup of running configuration on SONiC switches at any time instance <br /><br />

ONES network operators  can leverage REST API calls to validate the available configuration snapshot  of  specific devices at any time instance . <br /><br />

This  REST API will list the existing backups  already taken for specific devices. Operators have the option to Timestamp the  label while restoring the configuration<br /><br />
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>Input Parameters: List of Device IP , User label</b> defined by operator for each backup configure saved by ONES application
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    Response : True/false <br /><br />
    Return True status , If  backup of current running configuration goes successful by ONES <br /><br />
    Return false  status , If   backup of current running configuration goes unsuccessful by ONES <br />
    </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /backupConfig HTTP/1.1</b>
    Content-Type: application/json; charset=utf-8
    Host: localhost:8080
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    [{"ip":"10.x.x.10","label":"test label"}]


</pre>
    </td>
  </tr>
</table>


<br />

## Replace Current Config for Devices

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: .1rem  solid #0000001f;
  }
  th, tr {
    border: .1rem solid #0000001f;
  }

  td {
    border: .1rem solid #0000001f;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>replaceConfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>
This Rest API client call will feed the golden configuration template as input  and provides the following operational value to network operators <br /></br />

 - Provides difference between golden configuration and running configure and accordingly do the  required configure replacement operations through ONES API call also called as soft provisioning in Day 2 Operations <br />
 - PUSH - This Rest API client call also provisions and append  any new Day 2 operations over existing orchestrated DC fabric Sonic switches 

    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>&lt;List of Device IPs &gt; with boolean flag “only diff” = TRUE/FALSE Status,</b> If status return is true , API call returns  difference between golden configuration and running configuration <br /><br />
    If status return is false , API call returns  the parity configuration 
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    - Returns  response - Difference  between running config vs golden config when network Operator chooses Soft provisioning <br /><br />
    - Returns Response - Returns the appended configuration to the existing running baseline configuration<br />
 </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    
    POST /replaceConfig HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: 10.101.118.10:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    file: goldenconfigfile
    onlydiff: true/false

</pre>
    </td>
  </tr>
</table>


