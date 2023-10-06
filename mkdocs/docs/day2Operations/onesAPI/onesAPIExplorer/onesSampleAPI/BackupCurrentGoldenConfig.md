# <b>Backup Current running Config</b>

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
