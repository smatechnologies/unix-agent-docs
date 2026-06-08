---
sidebar_label: 'Overview'
title: Installation Overview
description: "Overview of Installation — everything you need to install and start the Unix Agent on a supported UNIX platform."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Installation overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

This section covers the end-to-end process for installing the Unix Agent on a supported UNIX platform. It walks you through verifying hardware and software requirements, obtaining the installation files, running the installation, and completing the initial startup. System administrators responsible for deploying or upgrading the Unix Agent should start here.

## When would you use this section?

- You are installing the Unix Agent for the first time on a new machine.
- You are upgrading an existing Unix Agent installation to a newer version.
- You need to confirm that your target system meets the hardware, software, or privilege requirements before beginning an installation.
- You need to add an additional Unix Agent instance to a system that already has one running.
- You need to perform a post-installation task such as migrating the agent to a different SAM socket number.

## What is in this section?

| Topic | Description |
|---|---|
| Installation Requirements | Hardware, software, disk space, memory, and privilege requirements for installing the Unix Agent on a supported UNIX platform. |
| Supported Operating Systems | A reference table of UNIX operating systems and processor architectures supported by the Unix Agent. |
| Fetching agent Installation File | Step-by-step procedures for placing the Unix Agent installation tar file onto the target UNIX machine via DVD copy or FTP transfer. |
| Preferred Installation Procedures | Step-by-step instructions for installing, upgrading, or adding Unix Agent instances using the install_agent script. |
| Legacy Installation | Step-by-step procedures for performing a new or upgrade Unix Agent installation using the legacy manual method. |
| Initial Startup | Step-by-step procedure for starting the Unix Agent after a new or upgrade installation and verifying that all required processes are running. |
| Additional Procedures | Supplemental procedures for post-installation tasks such as migrating the Unix Agent to a different SAM socket number. |

## Frequently asked questions

**How long does the installation take?**  
A typical installation takes approximately 10 minutes.

**Do I need root access to install the agent?**  
Yes. The agent requires root or sudo access because it must call `setuid()` and `setgid()` to impersonate users when running jobs. If your account does not have root access, ask your UNIX administrator to configure sudo access for the installing account. Refer to [Preferred Installation Procedures](./preferred-installation#performing-a-sudo-installation) for the sudo installation steps.

**What is a SAM Socket Number?**  
The SAM Socket Number is the starting port number of eleven consecutive sockets the agent uses to communicate with the SAM, JORS, SMAFT, and running jobs. For example, if the SAM Socket Number is 3100, the agent uses ports 3100 through 3110. SMA Technologies recommends reserving 15 consecutive sockets.

**Can I run more than one agent instance on the same machine?**  
Yes. Each instance requires a unique SAM Socket Number and a unique `SMA_LSAM_INSTANCE` value. Refer to [Running multiple agents](../configuration/running-multiple-lsams) for the complete procedure.

**Which SSL/TLS tar file should I use?**  
Use an SSL-labeled tar file when you require TLS communication between the agent and OpCon/SAM, encrypted tokens in job arguments, or SMAFT with TLS. The SSL libraries must be installed on the target machine. Refer to [Installation Requirements](./requirements) for the library resolution procedure if startup errors reference a missing `libssl.so` file.
