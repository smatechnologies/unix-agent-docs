---
sidebar_label: 'Updating the agent control script'
title: Updating the agent Control Script
description: "Reference and procedures for reviewing and editing the Unix Agent control script variables, including LSAM_ROOT, SAM_SOCKET, and PATH, after running the install_lsam installation script."
tags:
  - Procedural
  - Reference
  - System Administrator
  - Agents
---

# Updating the agent control script

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference and procedures for reviewing and editing the Unix Agent control script variables, including LSAM_ROOT, SAM_SOCKET, and PATH, after running the install_lsam installation script.

## When would you use it?

Update the agent control script when:

- You have run the `install_lsam` script and need to confirm or adjust the default values for `LSAM_ROOT`, `SAM_SOCKET`, `SMA_LSAM_INSTANCE`, `SMA_LOG_DIRECTORY`, or `PATH` to match the target environment.
- You are adding or removing compression utilities (`tar` or `gzip`) on the system and need the `PATH` variable to reflect the change so that SMA File Transfer jobs can locate those utilities.
- You are setting up multiple agent instances on a single machine and need each instance's control script to reference a unique `SAM_SOCKET` and `SMA_LSAM_INSTANCE`.

## Why would you use it?

- The control script variables define the paths and socket numbers the agent uses to locate its files and communicate with OpCon; incorrect values prevent the agent from starting or processing jobs.
- Keeping the `PATH` variable accurate ensures that SMA File Transfer operations can find the compression utilities they require, and that the SMAFT Control Script stays in sync with the agent's environment.

The agent Control Script contains several variables necessary for the proper processing of agent commands and of agent components. Since the installation script "install_lsam" easily creates a new Unix Agent (and updates the agent Control Script), further modification of the agent Control Script is not necessary. For information on the install_lsam script, refer to [install_lsam](../operations/utilities/install-lsam). SMA Technologies recommends confirming that the following variables are set to the correct values for the environment after running install_lsam. If changes need to be made, proceed as directed below under "Editing the agent Control Script."

## Agent control script variables

### LSAM_ROOT

**Default**: /usr/local/lsam

**Description**:

The location of the symbolic link to the agent's installation directory.

### SAM_SOCKET

**Default**: 3100

**Description**:

* The agent communicates with SMANetCom through this socket number.
* The Machine definition in the Enterprise Manager must contain this socket number.

### SMA_LSAM_INSTANCE

**Default**: ```$SAM_SOCKET```

**Description**:

Allows for descriptive pathnames which are not tied to a specific SAM Socket number. You can change ```$SAM_SOCKET``` without having to copy and move agent configuration and job tracking files.

### SMA_LOG_DIRECTORY

**Default**: ```$LSAM_ROOT/log/$SMA_LSAM_INSTANCE```

**Description**:

The agent writes its log files and error files to this path.

### PATH

**Description**:

* Includes the path to the agent "bin" directory.
* Includes the path(s) to the 'tar' and 'gzip' compression utilities if installed on the system.

## Editing the agent control script

:::info Note

Modifying the agent Control Script is optional. The installation procedures have set default values.

:::

With an ASCII editor, modify the agent Control Script to set the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, ```SMA_LOG_DIRECTORY```, and ```PATH``` variables to the preferred values.

:::tip Example

The following example shows an excerpt from the agent Control Script defining values for the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, ```SMA_LOG_DIRECTORY```, and ```PATH``` variables.


*\*The wrapping of the text in this example does not indicate the location of a carriage return; the ↵ indicates the location of a carriage return.*


```
LSAM_ROOT=/usr/local/lsam; export LSAM_ROOT ↵

SAM_SOCKET=3100; export SAM_SOCKET ↵

SMA_LSAM_INSTANCE=prod; export SMA_LSAM_INSTANCE ↵

SMA_LOG_DIRECTORY=$LSAM_ROOT/log/$SMA_LSAM_INSTANCE; export SMA_LOG_DIRECTORY ↵

PATH=/usr/bin:/usr/sbin:/sbin:/usr/local/lsam/bin:/usr/bin:/usr/contrib/bin; export

PATH ↵
```

:::

### Add/remove path to compression utilities

To add or remove the path to compression utilities, complete the following steps:

1. Scroll under the line "These 0 – 2 lines for creation of FTAgent script...".
2. For the tar utility:
    * If adding the tar utility path, add a line "#got_tar".
    * If removing the tar utility path, delete the line "#got_tar".
3. For the gzip utility:
    * If adding the gzip utility path, add a line "#got_gzip".
    * If removing the gzip utility path, delete the line "#got_gzip".
4. If the SMA File Transfer (SMAFT) Control Script has not been manually updated, delete it.

    ```rm SMAFTScript<SAM_Socket>```

    * Issue an LSAM 'status' command (refer to [lsam status](../operations/unix-lsam-commands#lsam-status)) to automatically update the PATH statement in the SMAFT Control Script.

    ```lsam<SAM_Socket> status```

    \- or -

    * Manually edit the ```PATH``` definition within the SMA File Transfer Control Script to match the new settings.

The agent Control Script is updated.

:::tip Example

The following example shows the bottom of an agent Control Script if the ```PATH``` variable contained the path to 'tar' but not the path to 'gzip':

```
#################-#-#-#-###################
These 0-2 lines for creation of FTAgent script...
#got_tar
#################-#-#-#-###################
```

:::

## Exception handling

**The agent fails to start and reports that it cannot find its executable or configuration files** — The `LSAM_ROOT` variable in the control script points to a path that does not exist or is not the correct symbolic link target for the installation directory. — Open the control script with an ASCII editor, verify that `LSAM_ROOT` resolves to the actual installation directory (for example, `/usr/local/lsam`), and confirm that the symbolic link exists and is not broken.

**SMA File Transfer jobs fail because `tar` or `gzip` cannot be found** — The `PATH` variable in the control script does not include the directories containing the `tar` and/or `gzip` utilities, or the `#got_tar` / `#got_gzip` marker lines were not added correctly under the "These 0 – 2 lines for creation of FTAgent script..." section. — Verify the correct paths to `tar` and `gzip` on the system, add the appropriate marker lines to the control script, delete the existing SMAFT Control Script (`rm SMAFTScript<SAM_Socket>`), and run `lsam<SAM_Socket> status` to regenerate it with the updated `PATH`.

**Changes to `SAM_SOCKET` or `SMA_LSAM_INSTANCE` in the control script do not take effect** — The agent was not stopped and restarted after the control script was edited, so the running process still uses the values it was started with. — Stop the agent using the current control script, confirm the new values are saved, then start the agent again so it reads the updated variable definitions.
