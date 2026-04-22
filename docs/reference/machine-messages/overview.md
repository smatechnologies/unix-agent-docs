---
sidebar_label: 'Overview'
title: Machine Messages Overview
description: "Overview of Machine Messages."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Machine messages overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

The Machine Messages section catalogs the messages, codes, and status indicators that the Unix Agent produces during job execution and file transfer operations. These pages cover agent log messages, running-state job information, exit codes for completed jobs, file transfer error codes, STDERR output categories, and JORS/FTServer errors. You use these references to diagnose failures and understand what the agent reported at each stage of processing.

## When would you use this section?

- A job ends in a failed or unknown state and you need to interpret the exit code or status message.
- A file transfer operation fails and you need to identify the specific SMAFT or STDOUT/STDERR error code.
- You are reviewing Unix Agent log output and need to look up a message ID or recommended corrective action.
- You need to understand what information is displayed in Enterprise Manager Operation for a running Unix Agent job.
- A JORS or FTServer process fails to start and you need to correlate the log entry to a known error condition.

## What is in this section?

| Topic | Description |
|---|---|
| Unix Agent Messages | Reference catalog of Unix Agent log and error messages, including message IDs, system error codes, and recommended corrective actions. |
| Jobs in a Running State | Reference for status messages and job information displayed in Enterprise Manager Operation while Unix Agent jobs are actively running. |
| Completed Jobs and Agent Exit Codes | Reference for Unix Agent-specific exit codes returned when jobs complete, including agent error codes, signal values, and File Arrival job exit codes. |
| UNIX File Transfer Error Codes | Reference for UNIX SMAFT exit codes returned by the Unix Agent and Server during SMA file transfer operations. |
| STDOUT Error Codes | Reference for STDOUT messages output by the Unix Agent FTAgent component during file transfer operations, including backup, transfer result, and completion messages. |
| STDERR - Pre-processing Errors | Reference for STDERR pre-processing error messages written when file transfer job requirements cannot be met before the transfer begins. |
| STDERR - Processing Errors | Reference for STDERR processing error messages output by FTServer and FTAgent during active file transfer operations, including network, file, and communication errors. |
| JORS/FTServer Errors | Reference for JORS and FTServer error messages recorded in the UNIXLSAM log file, including socket initialization and process spawning failures. |
