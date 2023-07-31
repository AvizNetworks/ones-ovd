# Show Difference between golden and running config

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
    <td><b>getConfigDiff</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><pre>Leveraging this  rest API call Operators gets a view on difference between running config and committed applied config on enrolled devices</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre>API Input Parameter : < List of device IPs for which Configuration difference is required >  
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Response is the difference  of the running configuration vs configuration committed  through  ONES fabric manager 
</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /getConfigDiff HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: localhost:8080
Connection: close
User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
Content-Length: 61
Input
{ "ip": "10.x.x.66", “diff_only”: “false”}

Response: current config on device vs config done via FM
{
 "orchestrated_config": "Last login: Fri Sep 30 11:44:05 2022 from 10.x.x.150\r\r\nsave\nsave\r\n\rSN2100-Leaf1# save\r\n\rSaving Configuration\r\n\rSN2100-Leaf1# show run\show run\r\n\r configure terminal\r\nrouter-id 3.0.0.2\r\nntp add 128.138.141.172\r\nclock timezone Asia/Kolkata\r\nsyslog add 10.x.11\r\snmp-server trap modify
}
</pre>
    </td>
  </tr>
</table>
