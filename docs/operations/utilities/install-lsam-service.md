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

## Examples

:::tip Example

The following example registers the agent using SAM Socket 3100 to start automatically on reboot. Run the commands from the agent root directory:

```
cd /usr/local/lsam
bin/install_lsam_service `pwd` 3100
```

**Outcome**: Symbolic links are created in the system startup directory. The agent instance using socket 3100 starts automatically the next time the machine is rebooted.

:::

## Glossary

**symbolic link** — A filesystem pointer that references another file or directory. `install_lsam_service` creates links in the OS startup directory pointing to the agent start script, causing the agent to start automatically on reboot.

**SAM socket** — The TCP/IP port number the Unix Agent uses to communicate with the SAM. Each agent instance on a machine uses a unique socket number specified during installation.