# UNIX Troubleshooting

## UNIX Error Messages

The following table provides help in finding solutions to errors most commonly reported by UNIX system routines. The error messages displayed in the Enterprise Manager, LSAM log file, and/or LSAM error file appear as follows:

LSAM-generated text (ID / errno [SYMBOL] - description)

The numbers ID and errno are not discussed here, but may be requested by SMA Technologies Support. SYMBOL and description are listed in the first column under "Error".

System-generated SYMBOL and description are not specific to any particular system routine, so the "Possible Cause/Fix" needs to be considered in the context in which the UNIX error appears. In most cases involving a resource (e.g., file, directory, socket, etc.), the particular resource is noted in the LSAM-generated-text portion of the message.

:::info Note 

The description may be presented in a language other than English.

:::

### EPERM 

- Not owner	

* **CAUSE**: The user is not listed as the "owner" of the indicated resource and the user cannot be given the access requested.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if access can be granted.


### ENOENT - No such file or directory

* **CAUSE**: The indicated file or directory does not exist on the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors.

### E2BIG - Arg list too long

* **CAUSE**: The combined "Start Image" and "Parameters" of the Job.
* **FIX**: The Job Details field (in the Enterprise Manager) is too long, or there are too many individual items in the combination.

### EAGAIN - Resource temporarily unavailable

* **CAUSE**: The LSAM cannot access a resource.
* **FIX**: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### ENOMEM - Not enough space

* **CAUSE**: The system is low on memory.
* **FIX**: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### EACCES - Permission denied

* **CAUSE**: The user is not authorized for the access requested for the indicated resource.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if access can be granted.

### EBUSY - Device busy	

CAUSE: The LSAM cannot access a hardware device.
FIX: Re-run the job at a later time. If the error persists, consult the System Administrator to determine the cause.

### EEXIST - File exists

* **CAUSE**: An attempt was made to create a file which already exists on the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or delete the file.

### ENFILE - File table overflow

* **CAUSE**: The file system appears to be full.
* **FIX**: Consult the System Administrator to determine the cause.

### EMFILE - Too many open files

* **CAUSE**: An attempt was made to open more files than allowed.
* **FIX**: Consult the System Administrator to determine if the allowed number of open files can be increased.

### EFBIG - File too large

* **CAUSE**: An attempt was made to create a file larger than allowed.
* **FIX**: Consult the System Administrator to determine if the allowed maximum size of files can be increased.

### ENOSPC - No space left on device

* **CAUSE**: The device (normally a hard disk) is full.
* **FIX**: Either remove files or find another device with sufficient space. Re-run the job.

### EROFS - Read-only file system

* **CAUSE**: An attempt was made to create new data or to modify existing data on a file system marked as "read-only".
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if write access may be granted.

### ENAMETOOLONG - File name too long

* **CAUSE**: The file name (or a directory name embedded within the pathname) is longer than allowed by the system.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the System Administrator to determine if the allowed maximum size of file names can be increased.

### EADDRINUSE - Address already in use

* **CAUSE**: The indicated network resource is already in use.
* **FIX**: Either determine which process uses one of the LSAM sockets (e.g., 3100 – 3105) and resolve the conflict, or reinstall the LSAM with a different ```<SAM_Socket>``` (e.g., 5100 instead of the default 3100).
* **FIX**: Ensure the LSAM is at or near the end of the system boot-up sequence.

### ENETDOWN - Network is down	

* **CAUSE**: The LSAM can't access the network.
* **FIX**: Consult the System Administrator to determine the cause.

### ENETUNREACH - Network is unreachable

* **CAUSE**: The LSAM can't access the network.
* **FIX**: Consult the System Administrator to determine the cause.

### ECONNRESET - Connection reset by peer

* **CAUSE**: The process on a remote machine is no longer connected. The process probably terminated abnormally.
* **FIX**: If the error persists, consult the remote machine's System Administrator to determine the cause.

### ETIMEDOUT - Connection timed out

* **CAUSE**: The process on a remote machine is not sending data as expected. Unless the network is experiencing heavy traffic, the process probably terminated abnormally.
* **FIX**: If the error persists, consult the remote machine's System Administrator to determine the cause.

### ECONNREFUSED - Connection refused

* **CAUSE**: No process exists on the remote machine to accept a connection from this machine.
* **FIX**: Check the Job Details (in the Enterprise Manager) for errors and/or consult the remote machine's System Administrator to determine the cause.

### EHOSTDOWN - Host is down

* **CAUSE**: The LSAM can't access the network.
* **FIX**: Consult the remote machine's System Administrator to determine the cause.

### EHOSTUNREACH - No route to host

* **CAUSE**: Part of the network is either down or mis-configured.
* **FIX**: Consult the System Administrator to determine the cause.