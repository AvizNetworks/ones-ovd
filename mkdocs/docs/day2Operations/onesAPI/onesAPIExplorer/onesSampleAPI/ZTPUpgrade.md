# ZTP Upgrade SONiC NOS Image

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
    <td><b>enableZTPUpgrade</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>ZTP upgrade - Perform SONiC upgrade using ZTP mechanism for a specific  image and configuration file.<br /><br />
    Use Case is to support image management for network operators running SONiC fabric <br /><br />

    Both ZTP image upgrade  enables  network operators to change  the version of the operating Sonic NOS during maintenance window
  </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>REST API Input parameter : `<`Input Device IPs`>`</b>
    ZTP  enable  image upgrade by network operators use case is to change  the version of the Sonic  NOS during the maintenance window  . Following  are the  REST API call  signatures for the same.

    REST API: enableZTPUpgrade
    Type: POST
  </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    Response: true/False <br /><br />
    Returns status true,  if ZTP enabled upgrade to SONiC enrolled devices is successful<br /><br />
    Returns status false,  if ZTP enabled upgrade to SONiC enrolled devices is unsuccessful<br /><br />

</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /enableZTPUpgrade HTTP/1.1</b>
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
