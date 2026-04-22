---
sidebar_label: 'Overview'
title: System Modification and Environment Variables Overview
description: "Overview of System Modification and Environment Variables."
tags:
  - Reference
  - System Administrator
  - Agents
---

# System modification and environment variables overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

The System Modification and Environment Variables section covers how the Unix Agent affects the host system and what it provides to jobs at runtime. These pages describe the directories and files the agent creates on first startup, how to deactivate or remove agent components, and the environment variables the agent passes to every job it runs. You use this section to understand the agent's footprint, cleanly remove it, and verify what runtime context your jobs receive.

## When would you use this section?

- You want to understand which directories and files the Unix Agent creates during its first startup.
- You need to deactivate an optional agent component, such as sma_cronmon or sma_filein, without removing the agent.
- You are decommissioning a Unix system and need to completely remove the Unix Agent and its automatic startup entries.
- You need to identify the environment variables available to jobs at runtime, such as path, job identity, schedule, or file I/O variables.

## What is in this section?

| Topic | Description |
|---|---|
| System Impact | Reference for directories and files created in the Unix Agent root directory upon initial agent startup. |
| Deactivating Agent Components | Steps to deactivate the optional sma_cronmon and sma_filein components of the Unix Agent by commenting out lines in the start and stop scripts. |
| Removing the Agent | Steps to completely remove the Unix Agent from a system, including stopping the agent, deleting its directory, and disabling automatic startup. |
| Agent Environment Variables | Reference for Unix Agent environment variables passed to jobs at runtime, including path, job identity, schedule, and file I/O variables. |
