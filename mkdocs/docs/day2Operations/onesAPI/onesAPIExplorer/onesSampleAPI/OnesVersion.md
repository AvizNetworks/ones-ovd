# Get ONES Version

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
    <td><b>getONESVersion
</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><pre>This API call enabled network operators  to retrieve  the version of ONES Fabric manager application controller and ONES fabric manager application agent which are running as container services on sonic enabled fabric devices .</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre>Input Parameters: device ip address - List of Devices IP whose Version numbers needs to be retrieved >
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Returns the current running  version of  ONES applications both controller and agent 
</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /getONESVersion HTTP/1.1
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
