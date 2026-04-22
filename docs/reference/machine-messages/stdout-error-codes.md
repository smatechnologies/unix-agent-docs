---
title: STDOUT Error Codes
description: "Reference for STDOUT messages output by the Unix Agent FTAgent component during file transfer operations, including backup, transfer result, and completion messages."
tags:
  - Reference
  - System Administrator
  - Agents
---

# STDOUT error codes

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?
Reference for STDOUT messages output by the Unix Agent FTAgent component during file transfer operations, including backup, transfer result, and completion messages.

- A file transfer job completes or fails and you need to interpret the STDOUT messages written by FTAgent.
- You need to confirm whether a destination file was backed up, overwritten, appended to, or created during a transfer.
- A transfer reports "File transfer did not complete!" and you need to know to check the STDERR output for additional detail.
- You are reviewing JORS output and need to understand the transfer result messages produced by FTAgent.

## Original destination file [dest] backed-up to [backup]

**Origination**: FTAgent

Per the job's "Overwrite" option, the FTAgent backed up the Destination File prior to starting the file transfer.

## Original destination file [file] did not exist to back-up

**Origination**: FTAgent

At the job's startup, no Destination File existed to backup.

## Could not change default access permissions for destination file [dest]

**Origination**: FTAgent

Following the transfer of a new Destination file, the new file's access privileges could not be changed from the system-dependent default to:

* Full access by owner
* Read access by group
* No access by others

:::info Note 

If the Destination File existed before the file transfer, the file transfer does not modify its access permissions.

:::

## \[src_machine]src_file --> [dest_mach]dest_file

**Origination**: FTAgent

* Displays the results of the file transfer.
* The Destination File was created or overwritten.
* Shown if the job's "Overwrite" option specified appending, but the Destination File did not exist prior to the file transfer.

## \[src_machine]src_file appended --> [dest_mach]dest_file

**Origination**: FTAgent

* Displays the results of the file transfer.
* The Source File was appended to the Destination File.

## File transfer successfully completed

**Origination**: FTAgent

The job ran to completion.

## File transfer did not complete!

**Origination**: FTAgent

* The job did not run to completion. The file may or may not have been transferred.
* Refer to the job's STDERR output for details of what went wrong.
