---
sidebar_label: 'Utilities overview'
title: Utilities Overview
description: "Overview of the Unix Agent utility programs available in the agent bin directory, covering installation, job management, file checking, and status reporting tools."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Utilties Overview

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Overview of the Unix Agent utility programs available in the agent bin directory, covering installation, job management, file checking, and status reporting tools.

- Use `file_check` or `exit_codes` when you need to verify file criteria or debug the return values of a job before scheduling it in OpCon.
- Use `lsam_killjob` when a running job must be forcibly terminated and the Enterprise Manager "Allow Kill Job" parameter is not enabled.
- Use `sma_ppscript` when a job requires post-processing analysis to determine success or failure beyond what the standard Failure Criteria in Job Details supports.
- Use `sma_status` when a long-running job needs to report its current step to the Enterprise Manager so operators can monitor progress.
- Use `sma_job_step` when a job must support restart at a specific step without rerunning all preceding steps.
- Use `install_lsam` or `install_lsam_service` during initial deployment or when configuring the agent to start automatically on system reboot.
- Use `maintain_ofiles` to prevent accumulation of outdated job-related output files on the agent machine.

The programs in this section do not use the agent Control Script. All utilities are located in the ```<LSAM root path>/bin/``` directory. All require root privileges, except file_check, maintain_ofiles, sma_ppscript, and sma_status, which are available to be called from any OpCon job. 

In the table that follows, a short description of each utility is provided. 

| Utility | Short Description |
| ------- | ----------------- |
| exit_codes | Displays the return values of a process |
| file_check | Checks if specified file(s) meet certain criteria |
| genericpgm | A dummy program used to test the agent |
| get_errno | Translates a UNIX error number into meaningful text |
| install_lsam | Quickly creates an operational agent without additional configuration or extensive installation steps |
| install_lsam_service | This script creates symbolic links in the start up directory, so the agent will be started automatically when the machine is rebooted |
| lsam_killjob | Sends a SIGKILL signal to terminate specified job |
| maintain_ofiles | Prevents the accumulation of outdated job-related files |
| sma_job_step | Called to have the agent advise SAM that a Job Step is about to be run |
| sma_LSAM_feedback | Called to have agent report text to be added to a job's "Detailed Job Message" list in Enterprise Manager |
| sma_ppscript | Registers a post-processing script (ppscript) to analyze the standard out of a job |
| sma_status | Sends message for the Enterprise Manager to display after the OpCon status message |
| uninstall_lsam | Quickly removes an agent |

