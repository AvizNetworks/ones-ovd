# Device Reboot

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

    POST /rebootRequest HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: localhost:8080
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61
    Input
    ["10.x.x.236"]
    Response:
    True

</pre>
    </td>
  </tr>
</table>
