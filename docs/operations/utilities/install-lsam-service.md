---
sidebar_label: 'install_lsam_service'
title: install_lsam_service
description: "Reference for the install_lsam_service script, which creates symbolic links in the system startup directory so the Unix Agent starts automatically on reboot."
tags:
  - Reference
  - System Administrator
  - Agents
---

# install_lsam_service

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the install_lsam_service script, which creates symbolic links in the system startup directory so the Unix Agent starts automatically on reboot.

The install_lsam_service script creates symbolic links in the start up directory, so the agent will be started automatically when the machine is rebooted. This script is valid on the following UNIX platforms: Linux, AIX, HP-UX, and Solaris.

- You are deploying a Unix Agent on Linux, AIX, HP-UX, or Solaris and need the agent to start automatically when the machine is rebooted.
- You have already run install_lsam and now need to register the agent with the system startup sequence.

## Syntax

```
cd <LSAM root directory>

bin/install_lsam_service `pwd` <SAM_Socket>
```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `pwd` | Required | Root directory of the agent installation, passed using the shell `pwd` command. |
| `<SAM_Socket>` | Required | TCP/IP socket number the agent instance was installed to use. |