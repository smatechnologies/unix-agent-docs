# JORS and SMAFT Paramters

The following parameters reference the settings to control how the LSAM handles STDOUT and STDERR, and defines capabilities and operating parameters for the Job Output Retrieval System (JORS) and SMA File Transfer (SMAFT).

### redirect_stdout

**Default Value**: 1

**Description**:

* Enables/Disables the redirection of each job's STDOUT to a unique file. The naming convention for each file is:
```<LSAM root path>/STDOUT/<SMA_LSAM_INSTANCE>/<yyyymmdd>/<job name>_<Internal Number>.<hhmmss>```
* If set to zero, STDOUT is not redirected.
* If set to one:
    * The LSAM redirects STDOUT messages for each job.
    * The LSAM adds an environment variable to each job called SMA_STDOUT. The value for SMA_STDOUT is the complete path to the file containing this job's standard output.

### redirect_stderr

**Default Value**: 1

**Description**:

* Enables/Disables the redirection of each job's STDERR to a unique file. The naming convention for each file is:
```<LSAM root path>/STDERR/<SMA_LSAM_INSTANCE>/<yyyymmdd>/<job name>_<Internal Number>.<hhmmss>```
* If set to zero, STDERR is not redirected.
* If set to one:
    * The LSAM redirects STDERR messages for each job.
    * The LSAM adds an environment variable to each job called SMA_STDERR. The value for SMA_STDERR is the complete path to the file containing this job's standard error.

### days_of_output_to_keep

**Default Value**: 10

**Description**:

* The sma_logging process will execute maintain_ofiles to clean up STDOUT and STDERR files that were created from job executions. The value specified by days_of_output_to_keep will be used as the argument to maintain_ofiles.
* Setting the value to 0 will disable this feature. This means no clean-up of STDOUT and STDERR files will be performed by the agent. The user is responsible for its maintenance and disk usage. SMA Technologies does not recommend setting this option to 0.

### restrict_output_file

**Default Value**: 000

**Description**:

* Enables/disables restricting access to job STDOUT and STDERR output files upon a job's termination.
* Value is a standard 3-digit octal number as used on UNIX systems to set access permissions, i.e., 'ogw', where 'o', 'g', and 'w' are octal digits (digits in the range of 0 to 7) and correspond to the permissions for the file's owner, the group to which it is assigned, and everyone else. Within each octal digit, setting the 4-bit allows reading the file, setting the 2-bit allows writing to the file (including truncation and deletion), and setting the 1-bit tags the file as being executable (e.g., '764' would result in the file's owner having complete access, members of the group would be able to do everything except execute it, while everyone else would only be able to read the file).
* The default value of '000' disables access restriction, and a job's output files will be readable and writable by everyone, while the user/group will continue to be root/root – which are the settings used to create the files when the job is launched.
* A value other than '000' will result in a job's output files access permissions being set upon its termination to this value, and their user/group will be set to the User and Group specified for the job in the Enterprise Manager's Job Details screen.

### JORS_FT socket number

**Default Value**: ```<SAM_Socket> + 10```

**Description:**

* Sets the socket (port) number for communicating job output information to the Enterprise Manager.
* The Job Output Retrieval System (JORS) socket number must be configured on the Administration > Machines > Advanced screen in the Enterprise Manager. For information on configuration of JORS in the Enterprise Manager, refer to Configuring Advanced Machine Parameters and Properties in the Enterprise Manager online help.

:::caution 

For JORS to function properly, ensure that any firewall on the UNIX machine allows the JORS_FT socket number to be open.

:::

### SMAFT socket number

**Default Value**: ```<SAM_Socket> + 8```

**Description**:

* Sets the socket (port) number for SMA File Transfer (SMAFT).
* The value can be the same number as JORS_FT or a different number.
* The SMAFT socket number must be configured on the Administration > Machines > Advanced screen in the Enterprise Manager. For information on configuration of JORS in the Enterprise Manager, refer to [Configuring Advanced Machine Parameters and Properties](configuring-advanced-machine-parameters) in the Enterprise Manager online help.

:::caution 

For a File Transfer job to function properly, ensure that any firewall on the UNIX machine allows the SMAFT socket number to be open.

:::

### SMAFT TLS socket number

**Default Value**: ```<SAM_Socket> + 9```

**Description**:

* Sets the socket (port) number for SMA File Transfer (SMAFT) for TLS.
* The value should be different number than SMAFT socket number.

### max_wait_time

**Default Value**: 60

**Description**:

* For both JORS and SMAFT, sets the maximum wait time in seconds for a response during a file transfer. For information on sma_JORS, refer to sma_JORS.
* During performance of the JORS function, if the peer (SAM) side does not respond within this wait time, JORS logs the error in the LSAM log and error file.
* During execution of a SMAFT job, if the peer (FTAgent) side does not respond within this wait time, FTServer logs the error in the LSAM log and error file.
* During execution of a SMAFT job, if the peer (FTServer) side does not respond within this wait time, FTAgent exits with an error.

:::caution 

SMA Technologies does not recommend changing this parameter to less than 60 because it could cause SMAFT failure on the network experiencing heavy traffic.

:::

### max_attempts

**Default Value**: 2

**Description**:

* For both JORS and SMAFT, sets the maximum number of times a message is sent without getting a response during a file transfer. For information on sma_JORS, refer to [sma_JORS](sma-jors).
* If a message is sent this many times without receipt of a response, on the next attempt to send, JORS logs the error in the LSAM log and error file.
* If a message is sent this many times without receipt of a response, on the next attempt to send, FTAgent exits with an error.

### encryption_support

**Default Value**: All supported capabilities - Refer to [File Encryption](file-encryption)

**Description**:

* Indicates if encryption is available for use during execution of a SMAFT job.
* If encryption is available, also indicates the preferred priority order of supported capabilities. Refer to [File Encryption](file-encryption) for a complete discussion on entering this value.
* Before the file transfer, the FTServer encrypts the file. The FTAgent, on the peer side, decrypts the file before saving it to the specified location.
* If set to zero, encryption is not available.

:::info Note 

If file encryption is not required, this parameter may be set to zero although encryption is available.

:::

### max_bandwidth

**Default Value**: 65536

**Description**:

* Specifies the maximum allowed transfer rate during file transfers.
* Value is in kbps (kilo-bits per second).
* The default is 64K kilo-bps.
* Set this value to match the capabilities of the machine's network connection. For example, set it to 56 for a 56K dial-up connection.


### max_packet_size

**Default Value**: 65536

**Description**:

* Specifies the maximum message length (in bytes) to be used during a SMAFT file transfer.
    * The maximum allowed value is 65536.

