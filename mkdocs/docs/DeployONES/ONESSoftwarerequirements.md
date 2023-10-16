# <b> ONES Software Requirements</b>

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
















