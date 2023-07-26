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
    <td><b>upgradeNOSImage</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><pre>Custom Image Upgrade for  Sonic devices  . Performs custom image upgrades for specific enrolled selected  sonic devices only</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre>API Input Parameter : <Device IPs, PathToImage>
Input Parameters: one or more device ip address
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Response: True/False- 
Returns True status if image upgrade to sonic devices is successful 
Returns False Status if Image upgrade to sonic devices is unsuccessful
</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /upgradeNOSImage  HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost:8080
Connection: close
User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
Content-Length: 61

[{"ip":"10.x.x.67","pathToImage":"http://10.x.x.10:8191/mnt/ws/images/sonic-mellanox-e8daeacd.bin"}]</pre>
    </td>
  </tr>
</table>
