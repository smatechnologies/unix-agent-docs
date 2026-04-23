---
sidebar_label: 'uninstall_lsam'
title: uninstall_lsam
description: "Reference for the uninstall_lsam script, which removes a Unix Agent instance by deleting its output, tracking, and log directories along with its startup and SMAFT scripts."
tags:
  - Reference
  - System Administrator
  - Agents
---

# uninstall_lsam

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the uninstall_lsam script, which removes a Unix Agent instance by deleting its output, tracking, and log directories along with its startup and SMAFT scripts.

The uninstall_lsam script quickly removes an agent. According to the specified agent-socket combination, the script removes an agent's output, tracking, and log directories in addition to the agent startup and SMA File Transfer (SMAFT) scripts.

- You are decommissioning a Unix Agent instance and need to remove its output, tracking, log directories, and startup and SMAFT scripts in a single operation.
- You have migrated an agent instance to a new socket number and need to clean up the old control script and data directories that are no longer in use.

## Syntax

```uninstall_lsam <LSAM root directory> <SAM_Socket>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `<LSAM root directory>` | Required | Root directory path of the agent instance to remove. |
| `<SAM_Socket>` | Required | TCP/IP socket number identifying the agent instance to remove. |

## Examples

:::tip Example

The following example removes the agent instance using SAM Socket 3100 from the installation at `/usr/local/lsam`:

```
uninstall_lsam /usr/local/lsam 3100
```

**Outcome**: The output, tracking, and log directories for socket 3100, along with the `lsam3100` control script and SMAFT scripts, are removed from the agent root directory.

:::

## Glossary

**LSAM root directory** — The root directory of the Unix Agent installation (for example, `/usr/local/lsam`). Contains the `bin/`, `config/`, `log/`, and `tracking/` subdirectories used by all agent instances.

**SAM socket** — The TCP/IP port number that identifies a specific agent instance. Used to name the agent Control Script (for example, `lsam3100`) and its associated data directories.