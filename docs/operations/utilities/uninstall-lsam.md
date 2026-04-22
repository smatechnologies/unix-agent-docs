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

## Syntax

```uninstall_lsam <LSAM root directory> <SAM_Socket>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `<LSAM root directory>` | Required | Root directory path of the agent instance to remove. |
| `<SAM_Socket>` | Required | TCP/IP socket number identifying the agent instance to remove. |