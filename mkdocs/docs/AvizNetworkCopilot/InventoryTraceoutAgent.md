# Network Path Intelligence & Visualization Agent

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/AvizNetworks/ncp-sdk-agents/tree/master/inventory-traceroute-agent)

**Network Path Intelligence & Visualization Agent** is an AI-driven diagnostic system that automates network path discovery, live topology mapping, and actionable visualization. 

It transforms fragmented troubleshooting workflows—manual traceroutes, static diagrams, and disjointed CLI checks—into a single, validated automation pipeline. By leveraging the **Aviz NCP SDK**, this agent supports multi-vendor environments (SONiC, Arista EOS, Cisco Nexus/Catalyst) to provide real-time visibility into network behavior.

### 🚀 Key Capabilities

* **Automated Path Discovery**
    * Runs intelligent traceroutes that reflect actual packet forwarding paths.
    * Automatically resolves hostnames $\rightarrow$ Management IPs $\rightarrow$ Correct Data-Plane Interfaces.
    * Verifies interface state and IP assignments *before* running diagnostics to prevent false negatives.

* **Dynamic Topology Visualization**
    * **CLI Unicode Dashboards:** Instant, high-fidelity path visualization directly in the terminal.
    * **Mermaid.js Integration:** Renders graphical flowcharts for web-based UIs.
    * **Live Scanning:** Uses LLDP/CDP to discover and map physical cabling in real-time.

* **Intelligent Diagnostics**
    * **Configuration Audits:** Detects missing IPs, admin-down interfaces, and configuration drift.
    * **Performance Analysis:** Measures hop-by-hop latency and identifies specific "hotspot" nodes.
    * **Root Cause Classification:** Differentiates between physical link failures, routing anomalies, and logical configuration errors.

---

## Project Layout

The project follows a modular structure designed for scalability and ease of maintenance.

```text
inventory-agent/
├── ncp.toml                # Project configuration & entry points
├── requirements.txt        # Python dependencies
├── apt-requirements.txt    # Optional system packages (OS level)
├── agents/
│   └── main_agent.py       # Main agent logic and definition
└── tools/
    ├── inventory_tools.py      # Device resolution & metadata (find_device_details)
    ├── traceroute_tool.py      # Core logic (run_traceroute, find_data_interface_ip)
    ├── visualization_tool.py   # Rendering engine (create_visualization)
    ├── dynamic_topology_tool.py# Discovery engine (scan_live_topology)
    └── debug_tools.py          # Fallback utilities (run_ssh_command)
```

## Agent Definition

The agent is defined in agents/main_agent.py with strict instructions to prioritize visualization and data integrity.

```python
from ncp import Agent

agent = Agent(
    name="NetworkPathAgent",
    description="Resolves devices, validates interfaces, maps paths, and runs diagnostics",
    instructions="""
    You are the Network Path Intelligence Expert.
    Rule 1: Every successful traceroute MUST be passed to create_visualization.
    Rule 2: Always provide full traceroute JSON to the visualizer.
    Rule 3: Always perform live topology discovery when topology is required.
    """,
    tools=[ ... ]  # See Tooling Architecture below
)
```

## Tooling Architecture

The agent utilizes a suite of specialized tools located in the tools/ directory. These are implemented as NCP @tool functions.

| Tool File | Tool Name | Primary Purpose |
|----------|-----------|-----------------|
| inventory_tools.py | find_device_details | Resolve hostname → mgmt IP; gather metadata |
| traceroute_tool.py | find_data_interface_ip | **CRITICAL:** Identify the correct data-plane IP to ensure valid testing |
| traceroute_tool.py | run_traceroute | Execute traceroute and capture hop-by-hop metrics (latency, loss) |
| visualization_tool.py | create_visualization | Convert raw trace JSON into Unicode dashboards or Mermaid graphs |
| dynamic_topology_tool.py | scan_live_topology | Run LLDP/CDP scans to produce a physical neighbor map |
| debug_tools.py | run_ssh_command | Fallback for manual inspection (e.g., `show ip int brief`) |
| debug_tools.py | list_interfaces | Enumerate interface states, IPs, and attributes |
| inventory_tools.py | get_device_details | Fetch device model, OS version, and capabilities |

## Workflows & Decision Logic

- **Path Visualization Workflow**
  - Replaces manual traceroute with an intelligent, visual process.
  - **Input**
    - User requests analysis (e.g., _“Trace from Leaf1 to Leaf2”_)
  - **Resolve**
    - If a hostname is provided, call `find_device_details`
  - **Verify**
    - Call `find_data_interface_ip` to confirm a valid source interface exists and is **Up**
  - **Execute**
    - Run `run_traceroute` and collect the JSON output
  - **Visualize**
    - On success, pass the JSON to `create_visualization` to render the map
  - **Report**
    - On failure, return the specific error (e.g., _“Interface Unassigned”_)

- **Live Topology Workflow**
  - Replaces static diagrams with real-time discovery.
  - **Input**
    - User requests neighbor information or cabling maps
  - **Scan**
    - Execute `scan_live_topology` (via LLDP/CDP)
  - **Format**
    - Generate a structured table: `Local Device:Port <-> Remote Device:Port`
  - **Return**
    - Output the table and optionally a visualization

## Setup & Run Instructions

1. **Clone & Branch**
   ```bash
   git clone https://github.com/AvizNetworks/ncp-sdk-agents.git
   cd ncp-sdk-agents
   git checkout -b network-path-agent

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install ncp
   
3. **Authenticate**
   - Authenticate with the NCP platform. Credentials will be persisted in `ncp.toml`.
   ```bash
   ncp authenticate
   # Follow prompts for Platform URL, Username, and Password

4. **Validate, Package, & Deploy**
   ```bash
   # Validate code structure
   ncp validate .

   # Package the agent
   ncp package .

   # Deploy (First time)
   ncp deploy inventory-agent.ncp

   # Update existing deployment
   ncp deploy inventory-agent.ncp --update

5. **Test Interactively**
   - Use the NCP Playground to test the agent locally.
   ```bash
   ncp playground --agent inventory-agent

   # Debug mode (Show tool calls)
   ncp playground --agent inventory-agent --show-tools
   
Exit the playground with Ctrl+C.

## Example Interactions

### 🟢 Example: Path Performance Visualization

**User:**

```text
Run a trace from Arista Leaf 1 to Arista Leaf 2. Source IP: 20.20.20.2, Destination IP: 20.20.20.6
```

### Agent Response:

```plaintext
┌──────────────────────────────────────┐
│  🚀 NETWORK PATH INTELLIGENCE        │
│      Target: 20.20.20.6              │
└──────────────────────────────────────┘
          │
          ▼
┌──────────────────────────────────────┐
│  🔵 SOURCE                           │
│      IP: 20.20.20.2                  │
└──────────────────────────────────────┘
          │  ⚡ 0.328 ms
          ▼
┌──────────────────────────────────────┐
│  ⚪ INTERMEDIATE HOP                 │
│      IP: 20.20.20.1                  │
└──────────────────────────────────────┘
          │  ⚡ 0.792 ms
          ▼
┌──────────────────────────────────────┐
│  🟢 DESTINATION                      │
│      IP: 20.20.20.6                  │
└──────────────────────────────────────┘
```


#### 🔴 Example: Configuration Audit

### User:

```
Trace from Cisco Leaf 1 to Cisco Leaf 2. Source IP: 30.30.30.2
```

### ❌ Agent Response

```text
🚫 Trace Failed

The source IP 30.30.30.2 is not configured on any interface of Cisco Leaf 1.

Details:
- Interface: GigabitEthernet1/0/2
- Status: Unassigned

Action:
Configure the source IP on a valid interface and retry the trace.
```


## Configuration Files

### `ncp.toml`

Defines the agent metadata and entry point.

```toml
[project]
name = "inventory-agent"
version = "0.1.0"
description = "Network Path Intelligence & Visualization Agent"

[agents]
main = "agents.main_agent:agent"

[build]
python_version = "3.11"

```

### `requirements.txt`

Python packages required by the agent tools.

```text
requests>=2.31.0
paramiko>=3.0.0
pyyaml
```
## Troubleshooting

If you encounter issues while working with the Inventory Agent, the following table provides common problems and recommended fixes:

| Issue                 | Command / Fix                                                   |
| --------------------- | --------------------------------------------------------------- |
| Authentication Issues | Run `ncp authenticate` to re-enter credentials                  |
| Validation Errors     | Run `ncp validate .` and fix missing imports or syntax errors   |
| Deployment Failures   | Ensure `ncp package .` succeeds and verify values in `ncp.toml` |
| Connectivity Issues   | Check VPN / firewall access to the NCP platform                 |

## Future Enhancements

- **Geo-Spatial Mapping**
  - Integrate GeoIP services to visualize network paths on a world map.
- **Predictive Analytics**
  - Use historical trace data to forecast path degradation.
- **Automated Remediation**
  - Provide safe, context-aware CLI snippets to fix detected configuration gaps.
- **ITSM Integration**
  - Automatically raise incidents (e.g., ServiceNow) for persistent failures.






