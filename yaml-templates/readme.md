# Network Fabric Configuration / Supported YAML files for day 1 operations.
## Overview

This repository contains a structured configuration for deploying a network fabric. It is designed to describe devices, connectivity, and network parameters in a scalable and automated manner.

## Purpose

The configuration can be used for:

* Network simulation and testing
* Automated deployment of network topologies
* Validation of connectivity and design principles

## Topology

The topology is defined using a modular approach and may include:

* Spine, Leaf, and/or ToR switches
* Inter-switch connectivity
* Host-facing interfaces

The design supports flexible architectures such as Layer-2, Layer-3, or hybrid fabrics.

## Features

* Device-level configuration (IP, ASN, credentials)
* Link definitions with port-channel support
* VLAN-based segmentation
* Optional features like MC-LAG, sFlow, and monitoring
* Scalable IP address management (IPv4/IPv6 pools)

## Configuration Sections

* **Inventory**: Defines number and type of devices
* **Connectivity**: Describes links between devices
* **Protocols**: Includes routing and switching configurations
* **IP Pools**: Allocates address ranges for different roles
* **System Services**: NTP, Syslog, SNMP, etc.

## Usage

Modify the configuration file to match your topology and requirements. This file can be consumed by automation tools to deploy or validate the network.


