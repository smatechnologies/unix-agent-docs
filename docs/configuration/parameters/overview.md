---
sidebar_label: 'Overview'
title: Agent Configuration Parameters Overview
description: "Overview of Agent Configuration Parameters — a reference guide to all Unix Agent lsam.conf parameter groups and their settings."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Agent configuration parameters overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

This section provides a complete reference for all Unix Agent configuration parameters stored in the lsam.conf file. Parameters are organized by functional group — covering job handling, logging, dispatcher behavior, file transfer, tracing, and TCP/IP communication. System administrators who need to tune, troubleshoot, or verify the Unix Agent's configuration settings should consult this section.

## When would you use this section?

- You need to look up the name, default value, or accepted values for a specific configuration parameter.
- You are troubleshooting agent behavior and need to understand what a parameter controls.
- You are enabling or tuning a specific feature such as TLS, SFTP, SMAFT, JORS, or File Activity Detection.
- You need to identify which parameters are hidden and must be edited directly in the lsam.conf file rather than through the configuration program.
- You are reviewing TCP/IP settings such as allowed SMANetCom IP addresses or NIC binding.

## What is in this section?

| Topic | Description |
|---|---|
| agent Configuration Parameters | Reference for Unix Agent configuration parameters covering job handling, user impersonation, health monitoring, and privilege settings. |
| Logging Configuration Parameters | Reference for Unix Agent logging configuration parameters, including log file rollover size and maximum archived log file count settings. |
| Dispatcher Configuration Parameters | Reference for Unix Agent dispatcher configuration parameters, including the message timeout setting that controls TCP/IP socket behavior when SMANetCom communication is delayed. |
| JORS and SMAFT Parameters | Reference for Unix Agent JORS and SMAFT parameters, including settings that control STDOUT and STDERR redirection and Job Output Retrieval System and SMA File Transfer behavior. |
| sma_filein Parameters | Reference for the Unix Agent sma_filein parameter that defines the sleep interval between checks of the MSGIN directory. |
| Trace Option Parameters | Reference for Unix Agent trace option parameters that enable or disable diagnostic tracing for the dispatcher, agent, and other internal processes. |
| SFTP Parameters | Reference for the Unix Agent SFTP parameter that configures the port used for SFTP-based file transfer, including fallback behavior to SMAFT. |
| FAD Parameters | Reference for the Unix Agent FAD parameter that controls whether the File Activity Detection monitor detects files created while the agent was down. |
| Hidden agent Configuration Parameters | Reference for Unix Agent hidden configuration parameters, including lsam_root_directory, check_CRC, and close_SAM_socket, which are only editable directly in the lsam.conf file. |
| TCP/IP Configuration Parameters | Reference for Unix Agent TCP/IP configuration parameters, including allowed SMANetCom IP addresses, NIC binding, and TLS certificate settings. |
