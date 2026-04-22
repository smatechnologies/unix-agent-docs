---
title: System Impact
description: "Reference for directories and files created in the Unix Agent root directory upon initial agent startup."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# System impact

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
Reference for directories and files created in the Unix Agent root directory upon initial agent startup.

After the agent has been started, the following directories and files should be in the agent root directory:

- You are troubleshooting a startup failure and need to confirm which directories and files should be present after a successful initial run.
- Knowing which directories and files the agent creates lets you quickly identify missing or misnamed items during a startup failure.

:::info Note

The initial run of the agent creates these directories and files.

:::

![System Impact](../../../static/img/systemimpact.png)

## Examples

**Scenario:** A system administrator completes a fresh installation of the Unix Agent and starts it for the first time. After running the start command, the administrator uses the system-impact reference to confirm that all expected directories and files are present in the agent root directory. By comparing the actual directory listing against the documented structure, the administrator verifies that the initial run completed successfully and that the agent is ready to communicate with the SAM.
