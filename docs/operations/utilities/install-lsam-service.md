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

## Syntax

```
cd <LSAM root directory>

bin/install_lsam_service `pwd` <SAM_Socket>
```

```<SAM_Socket>``` is a parameter that identifies the TCP/IP socket number the LSAM instance was installed to use.