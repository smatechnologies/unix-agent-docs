---
title: Removing the Agent
description: "Steps to completely remove the Unix Agent from a system, including stopping the agent, deleting its directory, and disabling automatic startup."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Removing the agent

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Steps to completely remove the Unix Agent from a system, including stopping the agent, deleting its directory, and disabling automatic startup.

## When would you use it?

- You are decommissioning a host and need to ensure the Unix Agent and all of its files are fully removed before the system is retired or repurposed.
- You need to perform a clean reinstallation and want to eliminate any residual directories or configuration files from the previous installation before installing again.

To completely remove an agent, complete the following steps:

1. Stop the relevant agent.
2. Remove the contents of the /usr/local/lsam directory.
3. Remove the /usr/local/lsam directory itself.
4. If automatic startup at boot time is configured for the agent, reconfigure the system to disable this option.

The agent is fully removed from the system.

## Exception handling

**The `/usr/local/lsam` directory cannot be deleted because files are in use.**
The agent is still running. Stop the relevant agent before attempting to remove the directory, then retry the remove commands.

**After removal, the agent restarts automatically at the next system boot.**
The automatic startup configuration was not disabled. If the system uses a boot-time startup mechanism (such as an entry in `/etc/rc` or an init script), locate and remove or disable the relevant entry so the agent does not attempt to start from a directory that no longer exists.
