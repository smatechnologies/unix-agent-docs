# Jobs in a Running State

Once jobs are built, the Enterprise Manager Operation screen contains different information depending on a job's status. In many cases, a specific failure message is returned from the LSAM and viewable in the Detailed Job Messages parameter in the Job Information screen>Configuration Tab>Operations Related Information Tab. For more information, refer to [Job Information](https://help.smatechnologies.com/opcon/core/Files/UI/Enterprise-Manager/Job-Information) in the Enterprise Manager online help. When UNIX jobs are processing, the status information includes the Process ID (pid) number or any optional status messages.

:::info Note

Scripts using the sma_status utility can use the 20-character message area to display any desired text; otherwise, the PID displays in the message area. For further information, refer to the example that shows a script using the sma_status utility on [sma_status](../../operations/utilities/sma-status).

:::

UNIX jobs in Enterprise Manager Operation appear in the following format:

```<JobName> (<Frequency Name>) (<OpCon Status> - <twenty-character message>)```

:::tip Example

The following example shows UNIX job (Ujob1) running in Enterprise Manager Operation without a user-defined status message:

```

Ujob1 (Daily) (Job Running – PID = 29613)

```


:::

:::tip Example

The following example shows a UNIX job (Ujob2) running in Enterprise Manager Operation with a user-defined status message:

```

Ujob2 (Daily) (Job Running – Starting Step 1)

```

:::

## Status Messages 

### [x] multiply-defined	

The indicated step [STARTING_STEP, ENDING_STEP, RESTART_STEP] was found to be included more than once. Check "Start Image" and "Parameters" in the job's Job Details screen.

:::info Note 

The [x] multiply-defined message text applies only to jobs based on the SMA Technologies-supplied template job script discussed in the Source - UNIX LSAM Details DOC.

:::

### Invalid job step [x]	

Shell variable 'next_step' set to a non-existent job Step Label as displayed. Check all settings of 'next_step' – especially for use of incorrect letter case.

:::info Note 

The Invalid job step [x] applies only to jobs based on the SMA Technologies-supplied template job script discussed in the Source - UNIX LSAM Details DOC.

:::

### Infinite loop detected	

The job experienced 'number_of_steps' iterations and was terminated. Check the following:
* Starting or Restart Step comes after Ending step in script
* Step gets repeated, possibly via intervening steps
* Job logic correct but 'number_of_steps' set too small

:::info Note

The Infinite loop detected applies only to jobs based on the SMA Technologies-supplied template job script discussed in the Source - UNIX LSAM Details DOC.

:::

### Unable to change access for [x]	

Access permissions for the indicated job stdout/dtderr output file could not be restricted per the LSAM Configuration setting.

### Unable to change ownership for [x]	

Ownership of the indicated job stdout/dtderr output file could not be changed from 'root/root' per the LSAM Configuration setting.

### Process [x] did not start	

The LSAM health monitor has determined that the indicated LSAM process did not start (or started but then immediately terminated). Stop the LSAM. If the cause for the lost process cannot be determined from other error messages, corrected, and the LSAM successfully re-started, then wait five minutes and re-start the LSAM. It should then start and run properly if the cause was of a momentary nature.

### Process [x] has terminated	

The LSAM health monitor has determined that the indicated LSAM process abnormally terminated. Stop the LSAM. If the cause for the lost process cannot be determined from other error messages, corrected, and the LSAM successfully re-started, then wait five minutes and re-start the LSAM. It should then start and run properly if the cause was of a momentary nature.

### Sending SIGUSR1 (die) to all LSAM processes	

The "```bin/lsam<SAM_Socket> stop```" command was given; this message is confirmation that the LSAM is in normal termination processing.

### Unable to find [x]	

"[x]" cannot be located for processing.

### Unable to create [x]	

"[x]" cannot be created for processing.

### Unable to open [x]	

"[x]" cannot be opened for processing.

### Unable to read [x]	

Data cannot be read from "[x]".

### Unable to write [x]	

Data cannot be written to "[x]".

### Deleting [x]	

"[x]" was deleted. This is normally just an informational message, and not indicative of a problem unless "[x]" is later referenced in an "Unable to ..." message.

### Unable to connect to [x]	

A socket-based connection cannot be made to the indicated remote service or system. Determine if the indicated system or service is up-and-running, and/or if the network is operational, and correct the condition.

### Unable to send [x1] to [x2]	

A message "[x1]" cannot be sent over the socket-based connection to the indicated remote service or system ("[x2]"). Determine if the indicated system or service is up-and-running, and/or if the network is operational, and correct the condition.

### LSAM health monitor operating	

Informational message to confirm that the LSAM started with the LSAM health monitor in proper operation.

### No LSAM health monitor	

Informational message to confirm that the LSAM started without the LSAM health monitor in proper operation. Execute the LSAM Configuration program to confirm that LSAM health monitoring has been disabled.

### LSAM health monitor disabled	

The LSAM health monitor has ceased operation. This is normal after issuance of the "LSAM stop" command.

### Sender not allowed by the LSAM configuration	

The portion of the LSAM which communicates with the SAM has received a message over a socket-based connection from an address not configured to be acceptable. The received message was ignored. It may be necessary to run the LSAM Configuration program to update the LSAM's configuration.

### Received unauthorized message	

Some portion of the LSAM has received a message over a socket-based connection from an unexpected address. The received message was ignored. It may be necessary to run the LSAM Configuration program to update the LSAM's configuration.

### Received a message with a blank machine name	

The portion of the LSAM which communicates with the SAM has received a message without the required machine name which identifies to the LSAM the intended recipient for the message. Mark the LSAM down in the Enterprise Manager and stop the LSAM. Wait five minutes, then re-start the LSAM and mark it back up in the Enterprise Manager.

### Received a message from SAM with invalid action specified	

The portion of the LSAM which communicates with the SAM has received a message with an invalid action specified. Mark the LSAM down in the Enterprise Manager and stop the LSAM. Wait five minutes, then re-start the LSAM and mark it back up in the Enterprise Manager.

### Received a duplicate message from SAM	

The LSAM has received a duplicate message from SAM. If this happens only occasionally, it indicates timing issues which sometimes arise in distributed processing systems like OpCon, and is not indicative of a problem. If it happens in a series over a few minutes, it indicates an acute problem with the SAM or the intervening network hardware.

### Missing environment variable [x]	

The indicated UNIX shell environment variable is not defined. The variable may be either expected to be defined at the system level, or it may be an LSAM-defined variable which is not getting passed around as required.

### Environment variable [x] is not defined	

The indicated UNIX shell environment variable is not defined. The variable may be either expected to be defined at the system level, or it may be an LSAM-defined variable which is not getting passed around as required.

### Received a SIGUSR1	

Each process in the LSAM should output this message during normal termination of the LSAM. If the "bin/lsam<SAM_Socket> stop" command was not given, then some process or user on the system issued a "kill" command on the indicated process.

### Received order to stop LSAM health monitor	

This message is output during normal termination processing.

### [x] Operational	

Each process in the LSAM should output this message during normal start-up of the LSAM.

### Too many arguments for [x]	

The addition of the text for "Start Image" and "Parameters" in the Enterprise Manager resulted in > 100 arguments. An "argument" is any text but a space. For example, the Start Image/Parameters combination "/usr/john/job x y abc123 1", the start image is "/usr/john/job", and the four arguments are "x", "y", "abc123", and "1". (It is possible to include parameters in the "Start Image" text box in the Enterprise Manager.)

### Blank start image for [x]	

The indicated job contained no start image, i.e., script or program to execute. Check the Job Details screen in the Enterprise Manager.

### Job [x] contained no UID	

The indicated job had no User ID.

### Job [x] contained no GID	

The indicated job had no Group ID.

### Job [x1] contained an invalid UID [x2]	

The indicate User ID for the indicated job was either non-existent or incorrectly formatted.

### Job [x1] contained an invalid GID [x2]	

The indicate Group ID for the indicated job was either non-existent or incorrectly formatted.

### Not allowed to start job [x] as 'root'	

The LSAM is configured to not allow jobs to execute with 'root' privileges. This can be changed by running the LSAM Configuration program.

### Unable to access start image [x1] for [x2]	The indicated Start Image could not be executed for the indicated job. The parenthesized portion of the message provides additional details, on which corrective action can be based.

### Unable to execute [x1] for [x2]	

The indicated item could not be executed for the indicated job. The parenthesized portion of the message provides additional details, on which corrective action can be based.

### Unable to exec() [x1] to start [x2]	

The indicated Start Image could not be executed for the indicated job. The parenthesized portion of the message provides additional details, on which corrective action can be based. If the LSAM determines that this was caused by an invalid reference to a shell/interpreter, e.g., the first line of the job script reads "!#/bin/bogus", an additional message will be generated to indicate this possibility.

### Unable to 'cd' to $HOME for [x]	

LSAM configuration parameter require_HOME_directory is enabled and the indicated job cannot be executed within the associated user's HOME directory. The most likely cause is an error defining the HOME directory when the user was added to the system, or that the HOME directory was either never created or it was deleted.

### Received TX0 for pid = [x] - [x]	

This is an informational message output to confirm receipt of a command from SAM to terminate the indicated job after the user executed the "Kill Job" command from the Enterprise Manager. This does not indicate that the job actually was terminated; that event/inability will be confirmed in a subsequent message.

### Can't fork() for [x] - decrementing max jobs to [x]	

The LSAM is unable to create a process in which to run the indicated job, and is decreasing the number of jobs it will attempt to simultaneously run in an effort to preclude further fork() errors. If this is a recurring problem, the LSAM Configuration program can be executed to lower the number of allowed jobs and/or the OS may need tuning to handle the load.

### Job [x] completed	

Informational message upon proper termination of an OpCon job – doesn't reflect the OK/Failed termination status.

### Data has not arrived in [x] seconds - closing socket	

The LSAM has not received any communication from the SAM in the indicated amount of time. The LSAM will close the connection in preparation for SAM initiating a new connection. "[x]" can be set with the LSAM Configuration program.