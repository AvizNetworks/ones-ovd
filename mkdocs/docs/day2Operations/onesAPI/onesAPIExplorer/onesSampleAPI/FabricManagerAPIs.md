# <b>Fabric Manager orchestration Sample APIs</b>

## <b> ONES Sample REST APIs</b>
Fabric manager Command line interface provides a network operator an  interface to configure all the open standard protocols and is user-friendly. Network operators can run Fabric Manager CLI (FMCLI)  commands on the device to enter into  the configuration mode and can configure interfaces,  protocols or other required features to bring up services over a data center fabric .


### <b>Prerequisites</b>

- Network operators are required to construct a complete configuration yaml  file including new incremental configuration section and not only the incremental change in the fabric configuration while doing incremental configuration as a part of Day2 Operations over the ONES enrolled Data center switches 
- ONES Enrolled Devices will be on-boarded by a Fabric Manager Controller application called ONES  . Following rest API is first called which ensures network operator does not share the login  credentials with a re-occurrence 
- This API call is well encrypted  which ensures ONES enrolled devices access credentials are not exposed in a  plain text to avoid any security compromise 
- All these APIs use python script
```py
import requests
import json
```
`print(result)`, will show the verification status <br />
`print(result.text)` , will show the applied status

- Config Status or VerificationStatus <br />
```py
0-Fail, 1-Pass, 2-Inprogress, 3-Notstarted
```


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
    <td><b>addDeviceFacts</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>
      Allows the user to add device facts like Enrolled Device Management IP , username and Password to the Fabric Manager database. This is a one time operation and is required to be done before making any other API call. This API will add the device username, password and IP address to the Fabric Manager database and will be used for all other API calls. This API will also validate the device credentials and will return an error if the credentials are not valid.
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>1. Device IP (Mgmt IP/SSH IP) <br />
2. Userid (required for ssh) <br />
3. Password (required for ssh) <br />
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>true/false</td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
addDeviceFacts_url = 'http://10.20.0.74:8787/addDeviceFacts'
payload = [{"ip":"10.20.3.11","user":"admin","password":"YourPaSsWoRd"},{"ip":"10.20.3.12","user":"admin","password":"YourPaSsWoRd"},{"ip":"10.20.3.14","user":"admin","password":"YourPaSsWoRd"},{"ip":"10.20.3.15","user":"admin","password":"YourPaSsWoRd"},{"ip":"10.20.3.16","user":"admin","password":"YourPaSsWoRd"},{"ip":"10.20.3.192","user":"admin","password":"YourPaSsWoRd"}]
call_api = requests.post (addDeviceFacts_url, json = payload)
print(call_api)
print(call_api.text)
</pre>
    </td>
  </tr>
</table>

### <b> Simplified Day 1 Orchestration</b>

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
    <td>
    <pre>
    upload_url = 'http://10.20.0.74:8787/uploadDay1Config'
    template = '/home/aviz/VXLAN.yaml'
    file_upload = {'file': open(template, 'rb')}
    getdata = requests.post(upload_url, files=file_upload)
    print(getdata)
    print(getdata.text)
    #track_id = 'i-BGP-IPv4-CLOS-L2-host.yaml_20230629130445'
    </pre>
    </td>
  </tr>
</table>



### <b>Get Day 1 Operational Status</b>

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

Input Parameter for the API call -  Intent ID for the intent configuration for the complete  fabric switches enrolled with ONES 
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
    url= 'http://10.20.0.74:8787/getDay1ConfigStatus'
    track_id = 'VXLAN.yaml_20240311054856'
    payload = {'intentName': track_id}
    result = requests.get(url = url, params = payload)
    print ('Debug info: url = {} ; payload = {}'.format(url,payload))
    print(result.text)
        </pre>
    </td>
  </tr>
</table>


### <b>Custom Upgrade SONiC NOS Image</b>

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
    imageUpgradeRequest = 'http://10.20.0.74:8787/upgradeNOSImage'
    payload = [{"ip":"10.20.3.14","pathToImage":"http://10.20.0.11:8080/ztp/Edgecore-SONiC_20231006_073817_ec202111_575.bin"}]
    result = requests.post(url = imageUpgradeRequest, json = payload)
    print ('debug :: imageUpgradeRequest -- {}'.format(result.json()))
    print(result.text)
</pre>
    </td>
  </tr>
</table>


### <b>Device Reboot</b>

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

    import requests
    url = 'http://10.20.0.74:8787/rebootRequest'
    call_api = requests.post (url, json = ['10.20.3.12'])
    print (call_api.text)
    print (call_api)


</pre>
    </td>
  </tr>
</table>


### <b>Show Difference between golden and running config</b>

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
    url = 'http://10.20.0.74:8787/getConfigDiff'
    call_api = requests.post (url, json = {'ip' : '10.20.3.192'})
    print (call_api.text)

    Readable format
    url = 'http://10.20.0.74:8787/getConfigDiff'
    call_api = requests.post (url, json = {'ip' : '10.20.3.192'})
    parse = json.loads(call_api.text)
    print (parse['orchestrated_config'])

</pre>
    </td>
  </tr>
</table>


### <b>Get Current Devcice Configuration</b>
<!-- ## New table added -->

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
    <td><b>getConfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Leveraging this API call, Operators get a view on the running configuration on enrolled devices
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b> API Input Parameter : < List of device IPs for which Configuration  is required > </b>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>API Response is the running configuration  through  ONES fabric manager </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    url = 'http://10.20.0.74:8787/getconfig'
    payload = {'deviceip': '10.20.3.192'}
    result = requests.get(url = url, params = payload)
    parse = result.json()
    print (parse['current_config'])

</pre>
    </td>
  </tr>
</table>




### <b>Get ONES Version</b>

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
    getVersion = 'http://10.20.0.74:8787/getVersion'
    ip_list = ['10.20.3.192']
    result = requests.post(url = getVersion, json = ip_list)
    print(result.text)

</pre>
    </td>
  </tr>
</table>


### <b>Backup Current running Config</b>

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
    backupconfig = 'http://10.20.0.74:8787/backupConfig'
    payload = [{"ip": "10.20.3.192", "label": "Demo_backup"}]
    result = requests.post(url = backupconfig, json = payload)
    print(result.text)


</pre>
    </td>
  </tr>
</table>

### <b>Get the List of all Backedup Configuration</b>
<!-- ## New table added -->

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
    <td><b>configlistrestore</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Leveraging this API call, Operators get a view on all the backed-up configuration taken by user
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b> API Input Parameter : < List of device IPs for which Configuration  is required > </b>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>API Response is the List of configuration  through  ONES fabric manager </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    url = 'http://10.20.0.74:8787/configslisttorestore'
    payload = {'devices': ['10.20.3.192'], 'onlylimited': False}
    result = requests.post(url = url, json = payload)
    print(result.text)


</pre>
    </td>
  </tr>
</table>


### <b>Restore old backup configuration</b>
<!-- ## New table added -->

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
    <td><b>restoreconfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Leveraging this API call, Operators can choose any backed-up configuration to restore 
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b> API Input Parameter : < List of device IPs for which Configuration  is required and the label name of the backed-up config > </b>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>API Response is the success or failure of the API </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    url = 'http://10.20.0.74:8787/restoreconfig'
    payload = [{'ip': '10.20.3.11', 'label': 'test'}]
    result = requests.post(url = url, json = payload)
    print(result.text)


</pre>
    </td>
  </tr>
</table>

### <b>Replace Current Config for Devices</b>

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
 - User needs to feed .cfg file containing the new config changes, a FMCLI standard CLI configuration format can be used
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
    
    device = '10.20.3.192'
    url = 'http://10.20.0.74:8787/replaceConfig'
    config_file = '/home/aviz/fmcli_db.cfg'

<b>Check Incremental Config</b>
    #This API will check the incremental config before applying it to device
    diff_flag = True 
    cfg_file_upload = {'file': open(config_file, 'rb')}
    values = {'deviceip' : device , 'onlydiff':diff_flag}
    getdata = requests.post(url, files=cfg_file_upload, data=values)
    print(json.dumps(getdata.json(), indent = 3))


<b>Applying Incremental Config</b>
    #This API will apply the incremental config
    diff_flag = False 
    cfg_file_upload = {'file': open(config_file, 'rb')}
    values = {'deviceip' : device , 'onlydiff':diff_flag}
    getdata = requests.post(url, files=cfg_file_upload, data=values)
    print(json.dumps(getdata.json(), indent = 3))

</pre>
    </td>
  </tr>
</table>

### <b>ZTP Upgrade SONiC NOS Image</b>

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
    enableZTPAndRunRequest = 'http://10.20.0.74:8787/enableZTPUpgrade'
    ip_list = ['10.20.3.14']
    result = requests.post(url = enableZTPAndRunRequest, json = ip_list)
    print(result.text)

</pre>
    </td>
  </tr>
</table>

### <b>Image status after SONiC NOS Image upgrade</b>
<!-- ### New table Added -->

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
    <td><b>getimgmgmtStatus</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Image Status - Status of Image after SONiC upgrade using ZTP mechanism.<br /><br />
    
  </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>REST API Input parameter : `<`Input Device IPs`>`</b>
    
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
    getImgmgmtStatus = 'http://10.20.0.74:8787/getImgmgmtStatus'
    ip_list = ['10.20.3.12']
    result = requests.post(url = getImgmgmtStatus, json = ip_list)
    print(result.text)

</pre>
    </td>
  </tr>
</table>
