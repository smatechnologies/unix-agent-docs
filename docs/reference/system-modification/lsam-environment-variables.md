# LSAM Environment Variables

So a job may adapt to its environment, the LSAM defines several environment variables for a started job. The following references these variables:

### SMA_BINDIR	

The path to the LSAM Utilities directory.

### SMA_CONFIG_FILE

The path to the configuration file used by a particular LSAM.

### SMA_JOBNAME

The short job name and job ID defined in OpCon.

### SMA_USER_SPECIFIED_JOBNAME

The job name displayed in the Enterprise Manager.

### SMA_SCHEDULE_DATE

The date of the schedule containing the job ```<SMA_JOBNAME>```.

### SMA_SCHEDULE_NAME

The name of the schedule containing the job ```<SMA_JOBNAME>```.

### SMA_SCHEDULE_FREQUENCY

The schedule frequency of the job ```<SMA_JOBNAME>```.

### SAM_SOCKET

The socket number the LSAM uses to communicate with the SAM.

### SMA_LSAM_INSTANCE

The name given to this particular instance of the LSAM. If no instance name was given at install, this is set to the socket number.

### SMA_STDERR

The path to the STDERR file associated with the job ```<SMA_JOBNAME>```.
If a STDERR file is not associated with the job, the variable contains "NONE".

### SMA_STDOUT

The path to the STDOUT file associated with the job ```<SMA_JOBNAME>```.
If a STDOUT file is not associated with the job, the variable contains "NONE".

### SMA_XML_FILE

Used by SMA File Transfer (SMAFT).