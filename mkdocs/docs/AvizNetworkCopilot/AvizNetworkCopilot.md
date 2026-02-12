# Aviz Network Copilot SDK Documentation
[![Documentation](https://img.shields.io/badge/Documentation-Read%20Docs-blue?logo=readthedocs)](https://pypi.org/project/ncp-sdk/)
# NCP SDK User Guide

Comprehensive Guide to Network Copilot SDK for AI Agent Development

The NCP SDK enables developers to create sophisticated AI agents and deploy them on the NCP platform. This guide covers everything from basic setup to advanced features like background agents, memory systems, and MCP integrations.

## Table of Contents

1. Getting Started
   * Prerequisites
   * Installation
   * Quick Verification
2. Core Concepts
   * Tools
   * Agents
   * Project Structure
3. Advanced Features
   * MCP Integration
   * Data Connectors
4. Dependency Management
   * Python Dependencies
   * System Dependencies
5. SDK Workflow
   * Project Initialization
   * Development
   * Validation
   * Packaging
   * Deployment

---

## Getting Started

### Prerequisites

#### Python Version

* Python 3.8 or higher is required  
* Python 3.9+ recommended for better type support

#### Platform-Specific Setup

##### macOS

```

# Install Python via Homebrew (recommended)

brew install python@3.11

# Or use pyenv for version management

brew install pyenv
pyenv install 3.11.0
pyenv global 3.11.0

```

##### Linux (Ubuntu/Debian)

```

# Update package list

sudo apt update

# Install Python and pip

sudo apt install python3.11 python3.11-pip python3.11-venv

# Verify installation

python3.11 --version

```

##### Windows

1. Download Python from python.org  
2. Run installer and check "Add Python to PATH"  
3. Open Command Prompt or PowerShell to verify:

```sh
python --version
pip --version
```

#### Virtual Environment

```sh
# Already included with Python 3.3+
python -m venv --help
```

### Installation

#### Step 1: Create Virtual Environment

Using venv:

```sh
# Create virtual environment
python -m venv .venv
# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
# Verify activation (should show .venv in prompt)
which python
```

#### Step 2: Install NCP SDK

```sh
# Install from PyPI

pip install ncp-sdk
```

#### Step 3: Verify Installation

```sh
# Check if NCP CLI is available

ncp --help

# Check Python import

python -c "from ncp import Agent, tool; print('NCP SDK installed successfully!')"
```

### Quick Verification

Create a simple test to ensure everything works:

```python
# test_ncp.py
from ncp import Agent, tool

@tool
def hello_world(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

# This should work without errors

agent = Agent(
    name="TestAgent",
    description="A simple test agent",
    instructions="You are a test agent. Be helpful.",
    tools=[hello_world]
    )

print("✅ NCP SDK is working correctly!")
```
Run the test:

```sh
python test_ncp.py
```

---

## Core Concepts

### Tools

Tools are the building blocks that give your agents capabilities. They're Python functions decorated with `@tool` that agents can call to perform actions.

#### Basic Tool Creation

```python
from ncp import tool
@tool
def ping_device(ip_address: str, timeout: int = 5) -> dict:
    [...]
```

#### Async Tools

```python
import asyncio
import aiohttp

@tool
async def backup_device_config(device_ip: str, backup_type: str = "running") -> dict:
    [...]
```

#### Tool Documentation Best Practices

```python
@tool
def search_documents(
    query: str,
    max_results: int = 10,
    include_metadata: bool = True
) -> List[dict]:
    [...]
```

### Agents

Agents are AI entities that use tools to accomplish tasks. They combine language models with your custom tools to create powerful automation.

#### Basic Agent Configuration

```python

from ncp import Agent

agent = Agent(
    name="NetworkMonitorBot",
    description="AI assistant for network monitoring and diagnostics",
    instructions="""
    [...]
    """,
    tools=[ping_device, get_interface_status, backup_device_config]
)

```

#### LLMConfig Parameters

```python
from ncp import LLMConfig

config = LLMConfig(
    model="llama-3.3-70b",
    [...],
)
```

### Project Structure

Standard project layout:

```sh
my-agent-project/
├── ncp.toml
├── requirements.txt
├── apt-requirements.txt
├── agents/
│   └── main_agent.py
├── tools/
└── **init**.py
```

---

## Advanced Features

### MCP Integration

Model Context Protocol (MCP) enables agents to connect to external services and data sources.

Example MCP setup:

```python
from ncp import Agent, MCPConfig

filesystem_server = MCPConfig(
transport_type="stdio",
command="mcp-server-filesystem /path/to/files"
)
```

Add multiple MCP servers:

```python
agent = Agent(
    name="MultiServiceAgent",
    [...]
    mcp_servers=[...]
    )
```

### Data Connectors

Data connectors allow agents to access external data sources configured in the NCP platform.

```python
from ncp import Agent, tool

@tool
def analyze_logs(query: str) -> dict:
    [...]
    agent = Agent(
    name="LogAnalyzer",
    [...]
    connectors=["splunk-prod"]
)
```

---

## Dependency Management

### Python Dependencies

Example `requirements.txt`:

```sh
pandas>=1.5.0
numpy>=1.21.0
requests>=2.28.0
```

#### Version Pinning

```sh
requests==2.28.2
pandas==1.5.3
```

### System Dependencies

Example `apt-requirements.txt`:

```sh
curl
wget
git
```

---

## SDK Workflow

### Project Initialization

```sh
ncp init my-agent-project
cd my-agent-project
```

### Development Best Practices

1. Start Simple  
2. Test Locally  
3. Use Type Hints  
4. Document Everything  
5. Handle Errors

### Packaging

```sh
ncp package .
```

### Deployment

```sh
ncp authenticate
ncp deploy my-agent-project.ncp

#Interactive Playground mode:
ncp playground
```
