# ONES Sample REST APIs
## Simplified Day 1 Orchestration

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
    <td><b>uploadDay1Config</b></td>
  </tr>
  <tr>
    <th>Description</th>
    <td><b>Intent Driven orchestration</b> -Performs Day 1 fabric orchestration for various Data Center topologies.This method will initiate the Day-1 orchestration depending on  the topology and intent supplied via template file. This  REST API  allows network operators  to upload an entire intent file (yaml-based) and orchestrate the entire fabric in a desired intent based underlay and overlay. For example, if customers  want to provision  BGP as an underlay and  VXLAN as an overlay ,they can operate the template form and provide minimum parameter inputs , with the rest of the derivation and parameters handled by the ONES application.
    </td>
  </tr>
  <tr>
    <th>Parameters</th>
    <td>
    <b>&lt;Intent YAML file- Path to Template file &gt; Output:< Intent ID></b>

Input Parameter for the REST API call -  Template file for the intent configuration for the whole fabric switches enrolled with ONES 
 
</pre>
    </td>
  </tr>
  <tr>
    <th>Response</th>
    <td>Returns  the intent ID which is an unique tag mapped to the specific intended input configuration desired by the network operator  while defining the intended configuration with only specific desired network entities </td>
  </tr>
  <tr>
    <th>Example</th>
    <td><pre>
    <b>POST /uploadDay1Config HTTP/1.1</b>
    Content-Type: application/json; charset=utf-8
    Host: 10.x.x.6:8787
    Connection: close
    User-Agent: Paw/3.4.0 (Macintosh; OS X/12.3.0) GCDHTTPRequest
    Content-Length: 61
    Input
    configure_az_1.yaml
    Response:
    configure_az_1.yaml_20230223115541
</pre>
    </td>
  </tr>
</table>
