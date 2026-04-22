---
sidebar_label: 'Overview'
title: Configuration Overview
description: "Overview of Configuration — all steps required to configure the Unix Agent after installation, including control scripts, security, startup, and job execution settings."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Configuration overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

This section covers the configuration tasks required to make the Unix Agent operational after installation. It includes guidance on editing the agent configuration file and control scripts, setting up security controls, configuring the time zone and automatic startup, running multiple agent instances, and preparing the environment for job execution. System administrators who have completed installation and need to configure the agent for their environment should start here.

## When would you use this section?

- You have completed installation and need to configure the Unix Agent before placing it into production.
- You need to update the agent or SMAFT control script variables after running the installation script.
- You want to restrict which users are permitted to run jobs by configuring security allow lists or block lists.
- You need to configure the agent to start and stop automatically when the system boots or shuts down.
- You are setting up multiple Unix Agent instances on a single machine.
- You need to understand script formatting requirements, environment variable loading, or STDOUT redirection behavior for jobs.
- You need to enable TLS-secured communication between the agent and OpCon.

## What is in this section?

| Topic | Description |
|---|---|
| Unix Agent configuration | Overview of the configuration steps required to set up the Unix Agent, including the control script, configuration file, and root profile. |
| Unix Security Configuration Options | Reference for configuring black list and white list security settings in the Unix Agent to control which users are permitted to run jobs. |
| Agent Configuration File | Step-by-step instructions for modifying the Unix Agent configuration file using the LSAM configuration program. |
| Updating the agent Control Script | Reference and procedures for reviewing and editing the Unix Agent control script variables, including LSAM_ROOT, SAM_SOCKET, and PATH, after running the install_lsam installation script. |
| Updating the SMA File Transfer (SMAFT) Control Script | Reference and procedures for reviewing and editing the SMAFT control script variables to ensure they match the Unix Agent control script settings. |
| Configuring the Time Zone in the Root Profile | Instructions for setting the TZ environment variable in the root profile or agent startup script to ensure the Unix Agent uses the correct time zone. |
| Automatic Startup Configuration for the agent | Instructions for configuring the Unix Agent to start and stop automatically during system boot and shutdown using symbolic links to init.d and rc directories. |
| Running Multiple agents on One Machine | Instructions for simultaneously running multiple Unix Agent instances on a single system, covering environment variable configuration and OpCon machine registration for each instance. |
| UNIX Script Requirements | Reference for the script formatting rules that OpCon jobs run by the Unix Agent must follow, including shell invocation, child process handling, and exit codes. |
| Loading Environment Variables | Instructions for using SMA Technologies-provided setup scripts and the userinfo program to load a user's operating environment before the Unix Agent runs a job. |
| Redirecting STDOUT | Reference for redirecting STDOUT output from Unix Agent jobs, including use of the captureSTDOUT script and behavior differences based on the path_to_su parameter. |
| UNIX TLS Security Procedures | Procedures for enabling and configuring TLS-secured communication between the Unix Agent and OpCon/SAM, including certificate creation and lsam.conf file changes. |
