# Replace Current Config for Devices

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
    <td><b>replaceConfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><pre>
This Rest API client call will feed the golden configuration template as input  and provides the following operational value to network operators 

 Provides difference between golden configuration and running configure and accordingly does required configure replacement operations through ONES API call also called as soft provisioning in Day2 Operations 
PUSH - This Rest API client call also provisions and append  any new Day2 operations over existing orchestrated DC fabric Sonic switches 

</pre>
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><pre><List of Device IPs > with boolean flag “only diff” = TRUE/FALSE Status, If status return is true , API call returns  difference between golden configuration and running configuration 
 If status return is false , API call returns   the parity configuration  
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td><pre>Returns  response - Difference  between running config vs golden config when network Operator chooses Soft provisioning 
Returns Response - Parity Config when  Operator chooses hard provisioned 

</pre> </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>POST /configreplace HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: 10.101.118.10:8787
Connection: close
User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
Content-Length: 61

onlydiff= <b>true</b>
</pre>
    </td>
  </tr>
</table>