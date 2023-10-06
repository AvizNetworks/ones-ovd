# <b>Show Difference between golden and running config</b>

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
