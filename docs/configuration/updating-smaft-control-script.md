---
sidebar_label: 'Updating the SMAFT control script'
title: Updating the SMA File Transfer (SMAFT) Control Script
description: "Reference and procedures for reviewing and editing the SMAFT control script variables to ensure they match the Unix Agent control script settings."
tags:
  - Procedural
  - Reference
  - System Administrator
  - Agents
---

# Updating the SMA File Transfer (SMAFT) control script

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference and procedures for reviewing and editing the SMAFT control script variables to ensure they match the Unix Agent control script settings.

Update the SMAFT control script when:

- The `LSAM_ROOT`, `SAM_SOCKET`, `SMA_LSAM_INSTANCE`, or `PATH` values in the agent Control Script have changed and the SMAFT Control Script must be updated to match.
- The SMAFT Control Script has been deleted and you need to verify the values that were automatically regenerated when the agent Control Script ran.

- Confirming the `PATH` variable in the SMAFT Control Script ensures that file transfer jobs can locate the `tar` and `gzip` compression utilities required to complete transfers.

The SMA File Transfer (SMAFT) Control Script contains several variables necessary for the proper operation of SMAFT jobs. Since the installation script "install_lsam" easily creates a new Unix Agent (and updates the SMAFT Control Script), further modification of the SMAFT Control Script is not necessary. If changes need to be made, proceed as directed below under "Editing the SMAFT Control Script".

:::info Note

If the SMAFT Control Script should ever be deleted, the execution of the agent Control Script creates a new one.

:::

## SMA File Transfer control script variables

### LSAM_ROOT

**Default**: None

**Description**:

Must match definition for ```LSAM_ROOT``` in the agent Control Script.

### SAM_SOCKET

**Default**: None

**Description**:

Must match definition for ```SAM_SOCKET``` in agent Control Script.

### SMA_LSAM_INSTANCE

**Default**: None

**Description**:

Must match definition for ```SMA_LSAM_INSTANCE``` in agent Control Script.

### PATH

**Default**: None

**Description**: 

* Includes the path to the agent bin directory, and to the 'tar' and 'gzip' compression utilities if installed on the system.
* Should match the definition for ```PATH``` in agent Control Script.
* Do not modify this file if only modifying the PATH variable. Modify the agent Control Script instead. For information on editing the agent Control Script, refer to [Updating the agent Control Script](updating-lsam-control-script).


## Editing the SMAFT control script

To edit the SMAFT Control Script, complete the following steps:

1. Open the SMAFT Control Script with an ASCII editor.
2. Set the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, and ```PATH``` variables to the preferred values.

The SMAFT Control Script is updated.

:::info Note

Modifying the SMAFT Control Script is optional. The installation procedures have set default values.

:::

:::tip Example

The following example shows an excerpt from the SMAFT Control Script defining values for the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, and ```PATH variables```.

*\*The wrapping of the text in this example does not indicate the location of a carriage return; the ↵ indicates the location of a carriage return.*

```
LSAM_ROOT=/usr/local/lsam; export LSAM_ROOT ↵
SAM_SOCKET=3100; export SAM_SOCKET ↵
SMA_LSAM_INSTANCE=prod; export SMA_LSAM_INSTANCE ↵
PATH=/usr/bin:/usr/sbin:/sbin:/usr/local/lsam/bin:/usr/bin:/usr/contrib/bin; export PATH ↵
```

:::

## Exception handling

**SMAFT jobs fail because `LSAM_ROOT`, `SAM_SOCKET`, or `SMA_LSAM_INSTANCE` in the SMAFT Control Script do not match the agent Control Script** — The SMAFT Control Script was manually edited or regenerated after the agent Control Script was changed, but the values were not kept in sync. — Open both scripts side by side with an ASCII editor, verify that `LSAM_ROOT`, `SAM_SOCKET`, and `SMA_LSAM_INSTANCE` are identical in both files, then restart the agent so the updated SMAFT Control Script is used.

**The SMAFT Control Script is missing after a manual deletion and SMAFT jobs cannot run** — The script was deleted but the agent Control Script has not been run since then, so a replacement has not yet been generated. — Run the agent Control Script (for example, `lsam3100 status`) to trigger automatic regeneration of the SMAFT Control Script, then verify its contents match the agent Control Script values as described above.

**File transfer jobs cannot locate `tar` or `gzip` after the `PATH` was updated in the agent Control Script** — The `PATH` variable in the SMAFT Control Script was not updated to match, because modifying PATH must be done through the agent Control Script (not directly in the SMAFT Control Script), as noted on this page. — Follow the compression utility steps in [Updating the agent Control Script](updating-lsam-control-script) to add or remove the `#got_tar` / `#got_gzip` markers, delete the SMAFT Control Script, and let it regenerate with the correct `PATH`.
