# Get ONES Version

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
