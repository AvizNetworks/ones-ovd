# Intent Drift Detector

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/AvizNetworks/ncp-sdk-agents/tree/master/intent_drift_detector)

**AI-assisted detection of configuration drift between intended state and runtime state in ONES-FM–managed fabrics**

---

## Overview

**Intent Drift Detector** identifies mismatches between the **intended network configuration** (defined via user-provided YAML intents and stored in ONES-FM) and the **actual runtime configuration** deployed on network devices.

In real production environments, configuration drift occurs due to:

- Manual CLI changes outside the controller
- Partial or failed orchestration runs
- Automation bugs
- Emergency hotfixes applied directly on devices

This project automates drift detection and reduces **MTTR from hours to minutes**.

---

## Problem Statement

ONES-FM assumes that:

> The configuration stored in the database always matches the configuration running on the devices.

In practice, this assumption frequently breaks.

### Current Challenges

- No automated validation between intent and runtime
- Manual DB exports and CLI inspections
- Drift detection is slow, reactive, and error-prone
- High operational risk in large fabrics

---

## Solution Overview

The **Intent Drift Detector**:

1. Fetches **intended state** from ONES-FM
2. Collects **runtime state** from network devices
3. Normalizes both into a common data model
4. Detects configuration drift
5. Generates structured drift reports with severity and remediation hints

---

## Architecture

            +----------------------+
            |  ONES-FM MCP Server  |
            |  (Intent & Runtime)  |
            +----------+-----------+
                       |
                       v
            +----------------------+
            | FabricIntentAgent    |
            | - Intent fetch       |
            | - Runtime fetch      |
            | - Normalization      |
            +----------+-----------+
                       |
                       v
            +----------------------+
            | Drift Engine         |
            | - JSON diff          |
            | - Severity scoring   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            | ReportAgent          |
            | - Markdown / CSV     |
            | - Patch suggestions  |
            +----------------------+
