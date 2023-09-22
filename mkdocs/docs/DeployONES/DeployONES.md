# Deploy ONES
## ONES System Requirements

### System Hardware Requirements – ONES Application

In the latest release, ONES can support managing up to 1024 devices. For ONES Application Installation, the system hardware requirements may vary based on the number of devices to manage.


|Devices       |Processor and Cores                      |RAM         |Storage                |
|--------------|-----------------------------------------|------------|-----------------------|
|64            |x86/x64 based, 2-core CPU                |16GB        |160GB/320GB/640GB/1.2 TB|
|128           |INTEL(E5-1607 v2)/AMD, 4 cores           |32GB        |3 TB or more            |
|256           |x86/x64 based 8-core CPU                 |64GB        |6 TB or more            |
|512           |INTEL(E5-1607 v2)/AMD, 16 cores or higher|64GB        |12 TB or more           |
|1024          |INTEL(E5-1607 v2)/AMD, 32 cores or higher|128GB       |20 TB or more           |

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
  }
  th{
    border: 1px solid black;
    padding: 8px;
    text-align: left;
    color: white;
    background-color:  #000080;
    
  }

  td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>

# ONES Software Requirements

|Software            |Command                                |Validation|
|--------------------|----------------------------------------|----------|
|Ubuntu Server       |Installer file (Version 18 or higher)   |lsb_release -a|
|Update to latest packages|sudo apt-get update                |NA         |
|Install Docker           |sudo apt-get install docker.io     |docker ps​  |
|Install Docker-compose   |sudo apt-get install docker-compose |docker-compose version​|
|Install Python3          |sudo apt-get install python3        |python3 –-version|
|Install Python3-pip      |sudo apt-get install python3-pip    |pip3 –-version   |
|Install Paramiko         |sudo apt-get install python3-paramiko|​pip show paramiko|
|Install SCP-Client        |sudo pip3 install scp                |pip show scp|

<!-- markdownlint-disable MD033 -->
<style>
  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 400px;
  }
  th{
    border: 1px solid black;
    padding: 8px;
    text-align: left;
    color: white;
    background-color:  #000080;
  }

  td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
    vertical-align: middle;
    word-wrap: break-word;
  }
</style>


<br />

## Browser Requirements

- Google Chrome version 107 or later
- Mozilla Firefox version 106 or later

<br />

## Deploying VM for ONES installation 

Please refer the following link for deployment of a virtual machine as a host for ONES application installation

<a href="https://aviznetworks.gitbook.io/ones/ones-ga-v1.3/getting-started/deploy-the-vm">https://aviznetworks.gitbook.io/ones/ones-ga-v1.3/getting-started/deploy-the-vm</a>

<br />

## Reference Documentation

<a href="https://aviznetworks.gitbook.io/ones/ones-ga-v1.3/ones-web-gui-administration/ones-orchestration">https://aviznetworks.gitbook.io/ones/ones-ga-v1.3/ones-web-gui-administration/ones-orchestration</a> - ONES Orchestration Configuration Guide

<a href="https://github.com/AvizNetworks/ones-ovd">https://github.com/AvizNetworks/ones-ovd</a> - OVD's ONES API for orchestration 

<a href="https://github.com/AvizNetworks/ones-pyapi">https://github.com/AvizNetworks/ones-pyapi</a> - ONES API for 3rd party integration

<a href="https://github.com/AvizNetworks/opbnos-api">https://github.com/AvizNetworks/opbnos-api</a> - OPBNOS API for 3rd party integration
