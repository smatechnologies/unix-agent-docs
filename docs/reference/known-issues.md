# Known Issues

### Version 17.1.0

When transferring large files on the order of gigabytes from UNIX to Windows, the UNIX job starting at the source will fail approximately halfway through. The error from Windows will indicate that there was a socket connection failure.

### Version 16.2.0

TLS communication may not work properly for systems running HP-UX, SUSE, UBUNTU, and DEBIAN.

### Version 15.00.01.23

Ensure that the latest Windows LSAM (version 15.3 ASCII patch) is updated before installing the latest UNIX version to resolve a compatibility issue in SMAFT ASCII mode transfer.

### Version 5.20.30 and Higher

File transfers fail with the following error:

 ```[sma_JORS] Received unauthorized message - aborting session (759)```

If this error occurs, change the Destination Machine of the file's configuration to set redirection_stderr to a value of 1.

### Version 4.01.01

The utility program sma_filein was enhanced to handle multiple event strings in files dropped into the MSGIN directory. It erroneously logs an error message (even when the MSGIN file is not empty). This message looks like:

```[sma_filein] Empty file [/usr/local/lsam/MSGIN/<socket>/<filename>] (errno : 2)```

It can safely be ignored. The events will be sent to the core services of OpCon correctly.

### Version 3.08.01

The Restart Step and Job Start/End Step functions do not work properly on all flavors of UNIX/Linux which are supported by the LSAM.

*Discussion*:

It has been found that some jobs based on the "user_job_step_template" Shell script, supplied in the LSAM "bin/" directory, will not execute properly on some flavors of UNIX/Linux. Jobs may run to completion (or through the specified ending step) and then be terminated with an "[sma_lsam] Infinite loop detected (509)" message and a numeric status code of 1. Jobs may also err-off prematurely, the error message being one with message number 508, 509, 539, 540, or 541 (and a numeric status code of 1).

This behavior is due to differences in processing by the Shells among the various flavors of UNIX/Linux, and it is not indicative of a problem with the actual LSAM: users' jobs which do not make use of "user_job_step_template" will execute as expected. The problems will be corrected by release of an updated version(s) of "user_job_step_template" as soon as it can be modified to account for all support Shells.

Customers who wish to create a job based on "user_job_step_template" should first create a short test job which contains three or four simple steps (e.g., "echo some_text", to determine if their system will execute these types of jobs as expected).

### All Versions Prior to 3.08.01

The LSAM will fail to start whenever system Process IDs (PIDs, the numerical values as displayed by a 'ps' command, not the number of them) reach 10,000,000 (10 million). Jobs, however, should continue to run without problems until the LSAM is stopped.

*Affected Systems*:

At this point, only AIX systems exhibit the problem. Solaris, Suze, Redhat, Linux/390, Unixware 7, and HP-UX systems tested to not have the problem, as their PIDs appear to not exceed the value 32768.

*Symptoms*:

The logging daemon (sma_log) start-up will be the only entry in the LSAM log file, or no entries from the attempted start-up will exist. PID files in the LSAM's PID directory "$LSAM_ROOT/pid/$SAM_SOCKET*.pid/" will have lengths of zero or contain values of zero.

*Workaround*:

If possible, upgrade to LSAM v3.08.01 or higher. Otherwise, configure the system to keep PIDs under 10 million, or if PIDs have reached 10 million, reboot the system prior to starting the LSAM.