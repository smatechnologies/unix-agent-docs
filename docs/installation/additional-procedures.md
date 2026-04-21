---
title: Additional Procedures
description: "Supplemental procedures for post-installation tasks such as migrating the Unix Agent to a different SAM socket number."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Additional procedures

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?

Supplemental procedures for post-installation tasks such as migrating the Unix Agent to a different SAM socket number.

## When would you use it?

Use the procedures on this page in the following situations:

- After a new or upgrade installation, when it becomes necessary to have the agent communicate with the SAM on a socket number different from the one specified during the original installation.
- When the agent was originally installed with an explicit `<LSAM_instance>` parameter, enabling a straightforward socket migration by re-running the install_lsam script with the same instance name and the new socket number.
- When setting up multiple agent instances on the same machine with different SAM socket numbers, to create separate agent control scripts for each instance.

This topic describes conditions and procedures which may be required to be run. They may apply to either a new or an upgrade installation.

## How to implement it

**Prerequisites:** The Unix Agent must already be installed. To use the socket migration procedure with the re-run method, the agent must have been originally installed with an explicit `<LSAM_instance>` parameter. If the agent was installed without an explicit `<LSAM_instance>`, contact SMA Technologies support before proceeding, as additional manual operations are required to retain agent configuration and job-related data. The agent must be marked down in the Enterprise Manager before stopping it, and the new socket number must be set in the Machines screen in the Enterprise Manager before starting the agent with the new script.

To migrate the agent to a different SAM socket number, complete the following steps:

## Migrate to another SAM socket

It may become necessary to have the agent communicate with the SAM on a socket different than the SAM_socket with which it was originally installed. This is easily accomplished if ```<LSAM_instance>``` was specified when the agent was installed. For example:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3100 prod
```

To switch to another socket, simply re-install the agent with the same parameters as in the original installation, except for using the new socket number. For example:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3200 prod
```

This will create a new agent Control Script. To complete the switch, complete the following steps:

1. Stop the agent with the old script.
2. Restart the agent with the new script. For example:

```
bin/lsam3100 stop
bin/lsam3200 start
```
 
Mark the agent down in the Enterprise Manager prior to issuing the stop command. In between the stop and start, set the new socket number in the Machines screen in the Enterprise Manager. After issuing the start command, mark the agent back up.

If ```<LSAM_instance>``` is not specified at the time the agent is installed, changing SAM sockets requires various operations to ensure that agent configuration and job-related data will be retained across the change of SAM sockets. These operations included:

* Running the agent Configuration program.
* Copying the job output files after setting-up the appropriate directory structure.
* Copying the job tracking files.

SMA Technologies recommends that ```<LSAM_instance>``` always be specified during the LSAM installation. If it is necessary to change SAM sockets for an LSAM installed without an explicit ```<LSAM_instance>```, please contact the SMA Technologies support representative to help accomplish the above mentioned operations.

## Exception handling

**Agent was installed without an explicit `<LSAM_instance>` and socket migration is required** — The re-run method for changing SAM sockets depends on the `<LSAM_instance>` parameter having been specified at original installation time. Without it, the agent's configuration and job-related data cannot be automatically carried forward, and running `install_lsam` with only the new socket number will not produce a correct migration. — Contact the SMA Technologies support representative. The representative will assist with the required manual operations: running the agent Configuration program, setting up the appropriate directory structure, and copying job output files and job tracking files.

**Agent does not respond after switching to the new socket number** — The new socket number was not updated in the Enterprise Manager Machines screen before restarting the agent, or the agent was not marked down before the stop command was issued. The Enterprise Manager continues to communicate on the old socket number, so the agent and SAM cannot establish a connection. — Stop the agent with the new script. In the Enterprise Manager, mark the agent down, then update the socket number in the Machines screen to the new value. Start the agent with the new script, then mark the agent back up in the Enterprise Manager.
