# <b>Replace Current Config for Devices</b>

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
  }
</style>

<table>
  <tr>
    <th>API</th>
    <td><b>replaceConfig</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td>
This Rest API client call will feed the golden configuration template as input  and provides the following operational value to network operators <br /></br />

 - Provides difference between golden configuration and running configure and accordingly do the  required configure replacement operations through ONES API call also called as soft provisioning in Day 2 Operations <br />
 - PUSH - This Rest API client call also provisions and append  any new Day 2 operations over existing orchestrated DC fabric Sonic switches 

    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td><b>&lt;List of Device IPs &gt; with boolean flag “only diff” = TRUE/FALSE Status,</b> If status return is true , API call returns  difference between golden configuration and running configuration <br /><br />
    If status return is false , API call returns  the parity configuration 
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>
    - Returns  response - Difference  between running config vs golden config when network Operator chooses Soft provisioning <br /><br />
    - Returns Response - Returns the appended configuration to the existing running baseline configuration<br />
 </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    
    POST /replaceConfig HTTP/1.1
    Content-Type: application/json; charset=utf-8
    Host: 100.100.10.10:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61

    file: goldenconfigfile
    onlydiff: true/false

</pre>
    </td>
  </tr>
</table>
