---
sidebar_label: 'Overview'
title: Operations overview
description: "Overview of Unix Agent operations."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Operations overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

The Operations section covers how to manage the Unix Agent after installation. It provides instructions for starting and stopping the agent, describes the daemon processes that make up the agent, and documents the command-line tools and utilities available to System Administrators.

## When would you use this section?

- Starting or stopping the Unix Agent on a machine
- Verifying the running status of the agent and its components
- Looking up a specific agent command or utility program
- Identifying which daemon processes are running and what each one does

## Why would you use this section?

- The Operations section consolidates the procedures and reference material needed to manage the agent after installation. Starting and stopping the agent, identifying daemon processes, and running utility programs are the routine tasks that System Administrators perform to keep the agent running and to respond to job failures.

## What is in this section?

| Topic | Description |
|---|---|
| Operating the agent | Start, stop, and verify the status of the Unix Agent using agent commands from the command line. |
| Unix Agent commands | Complete reference of all Unix Agent control script parameters, including start, stop, status, certificate management, and troubleshooting commands. |
| File Arrival jobs | Reference for the File Arrival job type, which monitors a directory for files matching a pattern and reports success when a matching, stable file is found within a defined time window. |
| Embedded Script jobs | Reference for the Embedded Script job type, which executes an inline script defined directly in OpCon without requiring a pre-deployed script file on the agent machine. |
| Components | Describes the continuous daemon processes that make up the Unix Agent, including their roles in job submission, communication, logging, file monitoring, and job output retrieval. |
| Utilities overview | Overview of the Unix Agent utility programs available in the agent bin directory, covering installation, job management, file checking, and status reporting tools. |

## Frequently asked questions

**How do I start the agent?**  
Log in as root, change to the agent's root directory, and run `lsam<SAM_Socket> start`. For example: `cd /usr/local/lsam/; bin/lsam3100 start`. Refer to [Operating the agent](./operating-the-lsam) for the full procedure including how to verify that all required processes started.

**How do I know which version of the agent is running?**  
Run `lsam<SAM_Socket> version` from the agent's `bin/` directory. For example: `bin/lsam3100 version`.

**Which processes must be running for the agent to work?**  
Three processes are required: `sma_lsam` (job submission), `sma_disp` (SAM communication), and `sma_log` (logging). If any of these are missing from the output of `lsam<SAM_Socket> status`, the agent is not operational. The remaining processes (`sma_fad`, `sma_filein`, `sma_cronmon`, `sma_JORS`, `sma_RM`) are optional.

**What do I do if the agent won't start?**  
Run `cat LSAM_output_<SAM_socket>` to view terminal output from the failed startup, then check the `logfile` and `errfile` in the `SMA_LOG_DIRECTORY` path for error messages. Common causes are missing SSL libraries (see [Installation Requirements](../installation/requirements)) and port conflicts (`EADDRINUSE`). Refer to [Troubleshooting](../reference/troubleshooting) for a full error symbol reference.

**How do I stop the agent without losing running jobs?**  
Use `lsam<SAM_Socket> stop`. The stop command systematically stops all agent processes. Jobs already submitted to the operating system continue to run, but the agent will not receive their completion status until it is restarted.
