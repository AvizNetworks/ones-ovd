# Backup Current Golden Config

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
  }

  td {
    border: 1px solid black;
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
    <td><pre>
After Sonic enabled DC fabric switches are orchestrated completely using Aviz’s ONES API  , Network operators can  take backup of running configuration on sonic switches at any time instance 

ONES application offers flexibility to network operators to trigger an  auto backup at fixed interval of time or a specified time in a given operational day in DC fabric 

ONES network operators  can leverage rest API calls to validate the available configuration snapshot  of  specific devices at any time instance .

 This  API will list the existing backups  already taken for specific devices. Operators have the option to Timestamp the  label while restoring the configuration.
</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre>Input Parameters: List of Device IP , User label defined by operator for each backup configure saved by ONES application  
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Response : true/false
Return True status , if  backup of current running configuration goes successful by ONES 
Return false  status , if  backup of current running configuration goes unsuccessful by ONES 
</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /configslisttorestore HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost:8080
Connection: close
User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
Content-Length: 61

{"devices":["10.101.118.11","10.101.118.12"],"onlylimited": true}


{
  "10.101.118.11" : {
    "configs" : [ {
      "date" : "Fri Jul 21 16:17:55 UTC 2023",
      "isbackuprecord" : false,
      "label" : "Backup 10.101.118.11_FM_Auto_Base_644791826 used.",
      "timestamp" : "21072023161755",
      "status" : "1"
    }, {
      "date" : "Fri Jul 21 16:17:55 UTC 2023",
      "isbackuprecord" : false,
      "label" : "Backup 10.101.118.11_FM_Auto_Base_644791826 used.",
      "timestamp" : "21072023161755",
      "status" : "1"
    }
  }]}
</pre>
    </td>
  </tr>
</table>
