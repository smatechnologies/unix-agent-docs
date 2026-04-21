---
sidebar_label: 'Automatic startup configuration'
title: Automatic Startup Configuration for the agent
description: "Instructions for configuring the Unix Agent to start and stop automatically during system boot and shutdown using symbolic links to init.d and rc directories."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Automatic startup configuration for the agent

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Instructions for configuring the Unix Agent to start and stop automatically during system boot and shutdown using symbolic links to init.d and rc directories.

## When would you use it?

Configure automatic startup when:

- The Unix Agent must resume operation without manual intervention after a system reboot or scheduled maintenance window.
- The production environment requires the agent to be available as soon as the operating system reaches multi-user mode, without waiting for an administrator to issue a start command.

## Why would you use it?

- Configuring automatic startup ensures the agent is consistently available after any reboot, reducing the risk of missed job schedules caused by a forgotten manual start.
- Placing the agent near the end of the system boot sequence (and near the beginning of the shutdown sequence) prevents erratic behavior that can occur when the agent starts before dependent system services are ready.

To ensure that the agent automatically starts and stops, create a symbolic link from the agent Control Script (e.g., lsam3100) to the system's init.d directory. Then make symbolic links from the init.d link to the rc<#>.d directories.

:::info Note

To ensure that the agent automatically starts and stops, create a symbolic link from the agent Control Script (e.g., lsam3100) to the system's init.d directory. Then make symbolic links from the init.d link to the rc<#>.d directories.

:::

When creating the links to the rc<#>.d directories, appropriately place the agent in the sort order. This order should cause the agent to be one of the last items started and one of the first items stopped.

:::warning

If the agent startup is not one of the final steps in the system boot sequence, erratic behavior may result. If this erratic behavior disappears with a manual restart of the agent, move the agent startup further down in the system's boot sequence.

:::


:::tip Example

The following example shows the commands, on a Solaris machine, to automatically stop and start the lsam3100 control script if the machine is booted in multi-user mode.

To configure automatic startup on Solaris, complete the following steps:

```
ln -s /usr/local/lsam/bin/lsam3100 /etc/init.d/lsam3100

ln -s /etc/init.d/lsam3100 /etc/rc2.d/K02lsam3100

ln -s /etc/init.d/lsam3100 /etc/rc2.d/S98lsam310
```

The agent is configured to start and stop automatically during system boot and shutdown.

:::

## Exception handling

**The agent does not start at boot even though the symbolic links are in place** — The symbolic link in `init.d` may point to an incorrect path, or the target control script does not have execute permissions. — Verify that the symbolic link target resolves to the correct control script (for example, `ls -l /etc/init.d/lsam3100`), confirm the control script is executable (`chmod +x`), and test it manually by running the script with the `start` argument.

**The agent starts but exhibits erratic behavior immediately after boot** — The agent is starting before dependent system services (such as networking or the file system containing `$LSAM_ROOT`) are fully available, as described in the warning on this page. — Move the agent's start link further toward the end of the boot sequence by renaming the `S` link in the `rc<#>.d` directory to a higher sort number (for example, change `S98lsam3100` to `S99lsam3100`), then reboot and confirm the behavior disappears.

**The agent does not stop cleanly at system shutdown** — The shutdown symbolic link (`K` link) in the `rc<#>.d` directory may be missing or may have a sort number that places it too late in the shutdown sequence, after dependent services have already stopped. — Verify that a `K` link exists in the appropriate `rc<#>.d` directory and that its sort number places it near the beginning of the shutdown sequence (a low number, such as `K02lsam3100`).
