# <b> Deploy ONES</b>

## <b> ONES System Requirements (v4.1)</b>

## <b> System Hardware Requirements – ONES Controller</b>

In the latest release, ONES can support managing up to 1024 devices. For ONES Application Installation, the system hardware requirements may vary based on the number of devices to manage.

| Devices | Processor and Cores        | RAM           | Storage       |
| ------- | -------------------------- | ------------- | ------------- |
| 16      | x86/x64 based, 16-core CPU | 32GB          | 80GB or more  |
| 32      | x86/x64 based, 32-core CPU | 32GB          | 160GB or more |
| 64      | x86/x64 based, 32-core CPU | 64GB          | 320GB or more |
| 128     | x86/x64 based, 32-core CPU | 96GB          | 640GB or more |
| 256     | x86/x64 based, 32-core CPU | 128GB         | 1.2TB or more |
| 512     | x86/x64 based, 64-core CPU | 256GB         | 3TB or more   |
| 1024    | x86/x64 based, 64-core CPU | 512GB or more | 6TB or more   |

**Note:** The resource sizing in the table is calculated assuming a maximum of 64 interfaces per managed entity.

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

## <b> ONES Software Requirements</b>

| Software                  | Command                               | Validation             |
| ------------------------- | ------------------------------------- | ---------------------- |
| Ubuntu Server             | Installer file (Version 18 or higher) | lsb_release -a         |
| Update to latest packages | sudo apt-get update                   | NA                     |
| Install Docker            | sudo apt-get install docker.io        | docker ps              |
| Install Docker-compose    | sudo apt-get install docker-compose   | docker-compose version |
| Install Python3           | sudo apt-get install python3          | python3 --version      |
| Install Python3-pip       | sudo apt-get install python3-pip      | pip3 --version         |
| Install Paramiko          | sudo apt-get install python3-paramiko | pip show paramiko      |
| Install SCP-Client        | sudo pip3 install scp                 | pip show scp           |

**Note:**

* ONES Application package verifies and installs dependencies automatically
* Script does not update Ubuntu to the latest version

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

## <b> ONES Controller Port Requirements</b>

### <b> Agent(Source) → Controller(Destination)</b>

| ONES Service   | Port Numbers |
| -------------- | ------------ |
| ONES Collector | 50053        |

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

### <b> Controller(Source) → Switch(Destination)</b>

| ONES Service           | Port Numbers |
| ---------------------- | ------------ |
| Switch Access over SSH | 22           |
| ONES Monitoring        | 50052        |

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

### <b> Ports to be open on ONES Controller</b>

| ONES Service               | Port Numbers      |
| -------------------------- | ----------------- |
| gNMI Gateway (Telemetry)   | 9339              |
| ONES Telemetry Database    | 5432              |
| ONES Orchestrator          | 8787              |
| ONES Orchestrator Database | 2345              |
| pty-server                 | 8885              |
| API-Server                 | 8080              |
| stream-processer           | 8093              |
| ksqldb-server              | 8088              |
| kafka-connect              | 8083              |
| schema-registry            | 8081              |
| broker                     | 29092, 9101, 9092 |
| Zookeeper                  | 2181              |
| ONES Collector             | 50053             |
| NVIDIA AIR-Model           | 8091              |

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

### <b> HTTPS Access</b>

| ONES Service | Port Numbers |
| ------------ | ------------ |
| ONES Web GUI | 443          |

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

## <b> Browser Requirements</b>

* Google Chrome version 107 or later
* Mozilla Firefox version 106 or later

## <b> ONES Multisite</b>

* Ubuntu 18.0 or later can be used for Multisite app
* ONES Multisite has to be installed on separate server
* ONES Multisite uses TCP port 443
* Ensure reachability between ONES sites and Multisite instance

## <b> Deploying VM for ONES installation</b>

Please refer the following link for deployment:

<a href="https://aviznetworks.gitbook.io/ones/">ONES Deployment Documentation</a>

## <b> Reference Documentation</b>

<a href="https://aviznetworks.gitbook.io/ones#introduction-and-overview">ONES Latest Documentation (v4.2)</a>

<a href="https://github.com/AvizNetworks/ones-ovd">OVD ONES API for Fabric Orchestration</a>

<a href="https://pypi.org/project/ones-pyapi/">ONES API for 3rd party integration</a>

<a href="https://github.com/AvizNetworks/opbnos-api">OPBNOS API for 3rd party integration</a>
