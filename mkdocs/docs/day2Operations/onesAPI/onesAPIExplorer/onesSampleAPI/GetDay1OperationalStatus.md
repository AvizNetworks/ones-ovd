# Get Day1 Operational Status

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
    <td><b>getDay1ConfigStatus</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>Show Generic Status - Retrieve Generic Intent Status for provisioning on sonic enabled fabric switches . This restful API allows network  operators  to  get the status of orchestration progress on a specific switch in sonic fabric  enrolled with ONES application 
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>Input: `<`Intent ID`>` Output: JSON (status)
        Input Parameter for the Rest API call -  Template file for the intent configuration for the whole fabric switches enrolled with ONES 
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td> Return  the Intent Status for the Day 1 orchestration. </td>
  </tr>
  <tr>
    <th>Example</th>
    <td> 
    <pre>
    GET /getIntentStatus?intentName=configure_az_1.yaml_20230223115541 HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: 10.x.x.6:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    Response
    [
        {
        "intentName": "SNMPServer",
        "ip": "10.x.x.69",
        "verification_status": "1",
        "config_status": "1",
        "logs": ""
        },
    ]
    </pre>
    </td>
  </tr>
</table>
