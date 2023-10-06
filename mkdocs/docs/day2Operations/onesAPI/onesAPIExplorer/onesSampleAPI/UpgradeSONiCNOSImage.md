# <b>Custom Upgrade SONiC NOS Image</b>

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
