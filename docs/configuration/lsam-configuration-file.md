---
sidebar_label: 'Agent configuration file'
title: Agent Configuration File
description: "Step-by-step instructions for modifying the Unix Agent configuration file using the LSAM configuration program."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Agent configuration file

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Step-by-step instructions for modifying the Unix Agent configuration file using the LSAM configuration program.

## When would you use it?

Modify the agent configuration file when:

- You need to adjust job-handling settings such as `max_number_of_jobs_to_run` to match the machine's capabilities or workload requirements.
- You need to change TCP/IP settings — for example, the socket number or communication parameters — after the initial installation.
- You need to enable, disable, or tune optional agent components (for example, health monitoring or user impersonation settings).
- You are applying a configuration change after an upgrade and the existing settings no longer reflect the intended operating parameters.

## Modify the configuration file

To modify the agent configuration file, complete the following steps:

1. Log in to the UNIX system as root.
2. Change the directory to the agent's bin directory. Use the following syntax: ```cd $LSAM_ROOT/bin```.

:::tip Example

The following example shows the syntax for getting to the agent's bin directory, assuming that ```$LSAM_ROOT``` is ```/usr/local/lsam```:

```cd /usr/local/lsam/bin```

:::

3. Start the LSAM configuration program. Use the following syntax: ```./lsam<SAM_Socket> config```

:::tip Example

The following example shows the syntax for starting the LSAM configuration program. The LSAM's SAM Socket number (```<SAM_Socket>```) is 3100:

```./lsam3100 config```

:::

4. Select an option from the menu and make any necessary modifications to the displayed values. For complete information on the lsam.conf settings, refer to the [TCP/IP Configuration Parameters](../configuration/parameters/tcp-ip-configuration) tables.
5. Repeat step 3 until all agent options are set correctly.
6. Enter s to save the configuration changes.
7. Enter q to quit the configuration program.
8. If the agent was running when performing step 3, refresh the agent after saving the configuration file. For information on refreshing the agent, refer to [lsam refresh](../operations/unix-lsam-commands#lsam-refresh).

The agent configuration file is saved.

## Exception handling

**The configuration program will not start** — The `$LSAM_ROOT` environment variable is not set, or the working directory is not the agent's `bin/` directory when invoking `./lsam<SAM_Socket> config`. — Confirm that `$LSAM_ROOT` is correctly defined in the agent Control Script and that you have changed to the `$LSAM_ROOT/bin` directory before running the command. For information on verifying these variables, refer to [Updating the agent Control Script](updating-lsam-control-script).

**`EADDRINUSE - Address already in use` after saving a socket number change** — The new socket number is already bound by another process on the system. — Identify the process using the socket (for example, with `netstat -an | grep <SAM_Socket>`), resolve the conflict, or choose a different socket number. After resolving the conflict, restart the agent.
