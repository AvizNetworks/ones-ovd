# ZTP Upgrade 

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
    border: 1px solid black;
  }
  th {
    border: 1px solid black;
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
    <td><b>enableZTPUpgrade</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><pre>ZTP upgrade - Perform SONiC ZTP upgrade for image and configuration .
To support image management, There are two options for network operators running sonic fabric 
Image Upgrade with ZTP 
Custom image management via ONES application.
                 ONES application  needs the following information as the input -
List of devices (IP address or host name) to upgrade images
Image path , user credentials to scp server

Both ZTP and Custom image upgrades enables the  network operators to change  the version of the operating NOS during maintenance window</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre>API Input parameter : <Input Device IPs>
Both ZTP and Custom image upgrades enable  network operators  to change  the version of the Sonic  NOS during the maintenance window . . Following  are the  rest API call  signatures for the same.

API: enableZTPAndRunRequest
Type: POST
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Response: true/False
Returns status true if ZTP enabled upgrade to sonic enrolled devices is successful
Returns status false if ZTP enabled upgrade to sonic enrolled devices is unsuccessful
</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /enableZTPUpgrade HTTP/1.1
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
