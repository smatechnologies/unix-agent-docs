---
title: UNIX Troubleshooting
description: "Reference for common UNIX system error symbols returned by the Unix Agent, including probable causes and corrective actions for each error condition."
tags:
  - Reference
  - System Administrator
  - Agents
---

# UNIX Troubleshooting

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?

Reference for common UNIX system error symbols returned by the Unix Agent, including probable causes and corrective actions for each error condition.

## When would you use it?

- An error symbol (such as ENOENT, EACCES, or ETIMEDOUT) appears in the Enterprise Manager, agent log file, or agent error file and you need to identify its probable cause and corrective action.
- A job fails with a UNIX system error and the agent-generated message includes an errno symbol you do not recognize.
- You are diagnosing network, file, permission, or resource errors reported by the agent.
- You need a quick-reference index to locate a specific error symbol by category before reading its full entry.

## UNIX error messages

The following table provides help in finding solutions to errors most commonly reported by UNIX system routines. The error messages displayed in the Enterprise Manager, agent log file, and/or agent error file appear as follows:

agent-generated text (ID / errno [SYMBOL] - description)

The numbers ID and errno are not discussed here, but may be requested by SMA Technologies Support. SYMBOL and description are listed in the first column under "Error".

System-generated SYMBOL and description are not specific to any particular system routine, so the "Possible Cause/Fix" needs to be considered in the context in which the UNIX error appears. In most cases involving a resource (e.g., file, directory, socket, etc.), the particular resource is noted in the agent-generated-text portion of the message.

Each error entry below follows the format ID / errno [SYMBOL] - description. The errno number and SYMBOL are the key identifiers to match against your log file. Because errors are context-dependent, review the agent-generated text surrounding the error for the specific resource involved. Check the agent log file for the exact error string before consulting this page.

:::info Note 

The description may be presented in a language other than English.

:::

## Quick-reference index

| Symbol | Category | Description |
|---|---|---|
| EAGAIN | Resource errors | Resource temporarily unavailable |
| EACCES | Permission and access errors | Permission denied |
| EADDRINUSE | Network and communication errors | Address already in use |
| EBUSY | File and I/O errors | Device busy |
| ECONNREFUSED | Network and communication errors | Connection refused |
| ECONNRESET | Network and communication errors | Connection reset by peer |
| EEXIST | File and I/O errors | File exists |
| EFBIG | File and I/O errors | File too large |
| EHOSTDOWN | Network and communication errors | Host is down |
| EHOSTUNREACH | Network and communication errors | No route to host |
| EMFILE | Resource errors | Too many open files |
| ENAMETOOLONG | File and I/O errors | File name too long |
| ENETDOWN | Network and communication errors | Network is down |
| ENETUNREACH | Network and communication errors | Network is unreachable |
| ENFILE | Resource errors | File table overflow |
| ENOENT | File and I/O errors | No such file or directory |
| ENOMEM | Resource errors | Not enough space |
| ENOSPC | Resource errors | No space left on device |
| EPERM | Permission and access errors | Not owner |
| EROFS | Permission and access errors | Read-only file system |
| ETIMEDOUT | Network and communication errors | Connection timed out |
| E2BIG | File and I/O errors | Arg list too long |

## Network and communication errors

### EADDRINUSE - Address already in use

* **CAUSE**: The indicated network resource is already in use.
* **FIX**: Either determine which process uses one of the agent sockets (e.g., 3100 – 3105) and resolve the conflict, or reinstall the agent with a different ```<SAM_Socket>``` (e.g., 5100 instead of the default 3100).
* **FIX**: Ensure the agent is at or near the end of the system boot-up sequence.

### ECONNREFUSED - Connection refused

* **CAUSE**: No process exists on the remote machine to accept a connection from this machine.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the remote machine's System Administrator to determine the cause.

### ECONNRESET - Connection reset by peer

* **CAUSE**: The process on a remote machine is no longer connected. The process probably terminated abnormally.
* **FIX**: If the error persists, consult the remote machine's System Administrator to determine the cause.

### EHOSTDOWN - Host is down

* **CAUSE**: The agent can't access the network.
* **FIX**: Consult the remote machine's System Administrator to determine the cause.

### EHOSTUNREACH - No route to host

* **CAUSE**: Part of the network is either down or mis-configured.
* **FIX**: Consult the System Administrator to determine the cause.

### ENETDOWN - Network is down	

* **CAUSE**: The agent can't access the network.
* **FIX**: Consult the System Administrator to determine the cause.

### ENETUNREACH - Network is unreachable

* **CAUSE**: The agent can't access the network.
* **FIX**: Consult the System Administrator to determine the cause.

### ETIMEDOUT - Connection timed out

* **CAUSE**: The process on a remote machine is not sending data as expected. Unless the network is experiencing heavy traffic, the process probably terminated abnormally.
* **FIX**: If the error persists, consult the remote machine's System Administrator to determine the cause.

## Permission and access errors

### EACCES - Permission denied

* **CAUSE**: You is not authorized for the access requested for the indicated resource.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if access can be granted.

### EPERM 

- Not owner	

* **CAUSE**: You is not listed as the "owner" of the indicated resource and you cannot be given the access requested.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if access can be granted.

### EROFS - Read-only file system

* **CAUSE**: An attempt was made to create new data or to modify existing data on a file system marked as "read-only".
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if write access may be granted.

## File and I/O errors

### E2BIG - Arg list too long

* **CAUSE**: The combined "Start Image" and "Parameters" of the Job.
* **FIX**: The Job Details field (in the Enterprise Manager) is too long, or there are too many individual items in the combination.

### EBUSY - Device busy	

CAUSE: The agent cannot access a hardware device.
FIX: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### EEXIST - File exists

* **CAUSE**: An attempt was made to create a file which already exists on the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or delete the file.

### EFBIG - File too large

* **CAUSE**: An attempt was made to create a file larger than allowed.
* **FIX**: Consult the System Administrator to determine if the allowed maximum size of files can be increased.

### ENAMETOOLONG - File name too long

* **CAUSE**: The file name (or a directory name embedded within the pathname) is longer than allowed by the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if the allowed maximum size of file names can be increased.

### ENOENT - No such file or directory

* **CAUSE**: The indicated file or directory does not exist on the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors.

## Resource errors

### EAGAIN - Resource temporarily unavailable

* **CAUSE**: The agent cannot access a resource.
* **FIX**: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### EMFILE - Too many open files

* **CAUSE**: An attempt was made to open more files than allowed.
* **FIX**: Consult the System Administrator to determine if the allowed number of open files can be increased.

### ENFILE - File table overflow

* **CAUSE**: The file system appears to be full.
* **FIX**: Consult the System Administrator to determine the cause.

### ENOMEM - Not enough space

* **CAUSE**: The system is low on memory.
* **FIX**: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### ENOSPC - No space left on device

* **CAUSE**: The device (normally a hard disk) is full.
* **FIX**: Either remove files or find another device with sufficient space. Re-run the job.
