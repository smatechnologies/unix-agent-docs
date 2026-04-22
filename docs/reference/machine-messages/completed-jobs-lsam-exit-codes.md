---
title: Completed Jobs and Agent Exit Codes
description: "Reference for Unix Agent-specific exit codes returned when jobs complete, including agent error codes, signal values, and File Arrival job exit codes."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Completed jobs agent exit codes

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?
Reference for Unix Agent-specific exit codes returned when jobs complete, including agent error codes, signal values, and File Arrival job exit codes.

When a job completes, the OpCon status changes to either Finished OK or Failed. The 20-character message text changes to include the exit codes from the job.

- A job fails with an exit code and you need to determine whether it is an agent-specific code or a UNIX system code.
- You are interpreting the job completion status shown in the 20-character message text in Enterprise Manager.
- A File Arrival job fails and you need to identify the specific exit code returned.
- You need to understand the breakdown of the exit code sections (job exit code, signal value, and core dump indicator).

## Agent exit codes

The following is a breakdown of the agent Exit Codes.

:::info Note

Do not confuse these codes with UNIX System Exit Codes. agent Exit Codes come from the Unix Agent itself while UNIX System Exit Codes come from the UNIX operating system.

:::

```
Exit Code Breakdown
+000010011:0000:N

\-------------/\-----/\--/|
            A B C

```

| Section | Exit Code | Valid Values | Description |
| ------- | --------- | ------------ | ----------- |
| A | Job Exit Codes | -999999999 to +999999999	| The first 10 characters of the exit condition consist of a plus (+) or minus (-) sign followed by nine digits indicating the job termination status - (Refer to agent Specific Error Codes below) |
| B	| Signals | 0000 to 9999 | If the job terminated due to the receipt of a signal from the operating system or through user intervention - the four-digit numeric value of that signal is specified here |
| C | Core Dumped | Y/N | Indicates whether or not (Y/N) a core file was created due to the termination of a job |

## Agent-specific error codes

The following is a list of the Unix Agent job error codes. If an exit code is not in this list, it is a UNIX-specific exit code. For information on UNIX-specific exit codes, refer to the UNIX documentation associated with the platform.

Because errors returned vary from platform to platform, it is beyond the scope of this document to try to list the possible reasons for each error. SMA Technologies recommends:

* Examine the log files for the agent and determine the error number reported.
* Reference the MAN page for the system call to get more information on the causes of this failure type.

| Unix Agent Exit Code | Failed System Call | Description |
| ------------------- | ------------------ | ----------- |
| 000010000 | ```<none>``` | The job definition does not contain a User ID |
| 000010001 | ```<none>``` | The job definition does not contain a Group ID |
| 000010002 | ```<none>``` | The job definition contains an invalid User ID |
| 000010003 | ```<none>``` | The job definition contains an invalid Group ID |
| 000010004 | ```<none>``` | - The SMANetCom sent a job status request (TX2) for a job or for a prerun process to the agent; The agent checked to see if the job was still running. <br></br> - The job was not running, but was marked as running in the tracking file |
| 000010005 | ```<none>``` | The agent was started and the job was shown in the tracking file to be running; however, the job was not actually running on the machine |
| 000010006 | ```<none>``` | The agent was started and the prerun was shown in the tracking file to be running; however, the prerun was not actually running on the machine |
| 000010007 | ```<none>``` | The job was not found in tracking file |
| 000010008 | fork() | The system function fork() failed when attempting to create a child process |
| 000010009 | ```<none>``` | - Privileged runs are not allowed <br></br> - The agent configuration does not allow jobs to be submitted as root |
| 000010010 | ```<none>``` | Job was killed by user or system administrator |
| 000010100 | fork() | Unable to fork() a process space for the prerun process |
| 000010101 | setuid() | Unable to setuid() to the specified User ID for the prerun process |
| 000010102 | setgid() | Unable to setgid() to the specified Group ID for the prerun process |
| 000010103 | setpgid() | The system function setpgid() failed when attempting to set the parent Group ID for a prerun process |
| 000010104 | ```<none>``` | Start Image not found or insufficient privileges for the prerun process |
| 000010105 | exec() | The system function exec() failed when attempting to initialize the process space for a prerun process |
| 000010200 | fork() | Unable to fork() a process space for the job |
| 000010201 | setuid() | Unable to setuid() to the specified User ID |
| 000010202	| setgid() | Unable to setgid() to the specified Group ID |
| 000010203 | setpgid()	| The system function setpgid() failed when attempting to set the parent Group ID for a job |
| 000010204 | `<none>` | Start Image not found or insufficient privileges for the job |
| 000010205 | exec() | The system function exec() failed when attempting to initialize the process space for a job |
| 000010299 | open() | The system function open() failed when the agent attempted to open the post-processing script; For more information on the post-processing script, refer to sma_ppscript |
| 000010300 | fork() | The system function fork() failed when attempting to create a process for a post-processing script |
| 000010301 | setuid() | The system function setuid() failed when attempting to set the User ID for a post-processing script |
| 000010302 | setgid() | The system function setgid() failed when attempting to set the Group ID for a post-processing script |
| 000010303 | setpgid()	| The system function setpgid() failed when attempting to set the parent Group ID for a post-processing script |
| 000010304 | `<none>` Start Image not found or insufficient privileges for the post-processing script |
| 000010305 | exec() | The system function exec() failed when attempting to initialize the process space for a post-processing script |

In many cases, a specific failure message is returned from the agent and viewable as field "agent Error Message" under the "General" tab of the Job Configuration screen. Messages begin with text generated by the agent, and conclude with parentheses containing an integer message ID and perhaps other test. 

If the error was the result of a system call, the additional text after the message ID would include the system-specific error number returned by the operating system, the symbolic name for this error (common to the vast majority of UNIX systems), and a brief description of the error as returned by the operating system. 

The UNIX error number and text varies from system to system. Also, a system call often has multiple failure modes, so the same message ID can be followed by a variety of error codes.

:::tip Example

The following example shows a agent Error Message which might be returned for a agent exit code of 000010205:

```
[sma_lsam] (monitor) - Unable to execute [/usr/john/job_1] for [JOB1] (120 / 2 [ENOENT] - No such file or directory)
```

In this case, you should check what was entered for "Start Image" on the Job Details screen.

:::

## File arrival job exit codes

The following is a list of Unix Agent exit codes specifically for File Arrival jobs:

| Exit Code | Description |
| --------- | ----------- |
| 1	| The file is not found; Reasons include an invalid file name, the file has not arrived yet, or permissions |
| 2	| The path is not found; Reasons include an invalid path or permissions |
| 3	| A file is found but the creation date is out of range |
| 4 | Internal system error: Abnormal signal caught |
