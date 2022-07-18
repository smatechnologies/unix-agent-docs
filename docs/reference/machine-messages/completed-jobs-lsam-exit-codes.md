# Completed Jobs and LSAM Exit Codes

When a job completes, the OpCon status changes to either Finished OK or Failed. The 20-character message text changes to include the exit codes from the job.

## LSAM Exit Codes

The following is a breakdown of the LSAM Exit Codes.

:::info Note

Do not confuse these codes with UNIX System Exit Codes. LSAM Exit Codes come from the UNIX LSAM itself while UNIX System Exit Codes come from the UNIX operating system.

:::

```
Exit Code Breakdown
+000010011:0000:N

\-------------/\-----/\--/|
            A B C

```

| Section | Exit Code | Valid Values | Description |
| ------- | --------- | ------------ | ----------- |
| A | Job Exit Codes | -999999999 to +999999999	| The first 10 characters of the exit condition consist of a plus (+) or minus (-) sign followed by nine digits indicating the job termination status - (Refer to LSAM Specific Error Codes below) |
| B	| Signals | 0000 to 9999 | If the job terminated due to the receipt of a signal from the operating system or through user intervention - the four-digit numeric value of that signal is specified here |
| C | Core Dumped | Y/N | Indicates whether or not (Y/N) a core file was created due to the termination of a job |

## LSAM-Specific Error Codes

The following is a list of the UNIX LSAM job error codes. If an exit code is not in this list, it is a UNIX-specific exit code. For information on UNIX-specific exit codes, refer to the UNIX documentation associated with the platform.

Because errors returned vary from platform to platform, it is beyond the scope of this document to try to list the possible reasons for each error. SMA Technologies recommends:

* Examine the log files for the LSAM and determine the error number reported.
* Reference the MAN page for the system call to get more information on the causes of this failure type.

| UNIX LSAM Exit Code | Failed System Call | Description |
| ------------------- | ------------------ | ----------- |
| 000010000 | ```<none>``` | The job definition does not contain a User ID |
| 000010001 | ```<none>``` | The job definition does not contain a Group ID |
| 000010002 | ```<none>``` | The job definition contains an invalid User ID |
| 000010003 | ```<none>``` | The job definition contains an invalid Group ID |
| 000010004 | ```<none>``` | - The SMANetCom sent a job status request (TX2) for a job or for a prerun process to the LSAM; The LSAM checked to see if the job was still running. <br></br> - The job was not running, but was marked as running in the tracking file |
| 000010005 | ```<none>``` | The LSAM was started and the job was shown in the tracking file to be running; however, the job was not actually running on the machine |
| 000010006 | ```<none>``` | The LSAM was started and the prerun was shown in the tracking file to be running; however, the prerun was not actually running on the machine |
| 000010007 | ```<none>``` | The job was not found in tracking file |
| 000010008 | fork() | The system function fork() failed when attempting to create a child process |
| 000010009 | ```<none>``` | - Privileged runs are not allowed <br></br> - The LSAM configuration does not allow jobs to be submitted as root |
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
| 000010299 | open() | The system function open() failed when the LSAM attempted to open the post-processing script; For more information on the post-processing script, refer to sma_ppscript |
| 000010300 | fork() | The system function fork() failed when attempting to create a process for a post-processing script |
| 000010301 | setuid() | The system function setuid() failed when attempting to set the User ID for a post-processing script |
| 000010302 | setgid() | The system function setgid() failed when attempting to set the Group ID for a post-processing script |
| 000010303 | setpgid()	| The system function setpgid() failed when attempting to set the parent Group ID for a post-processing script |
| 000010304 | `<none>` Start Image not found or insufficient privileges for the post-processing script |
| 000010305 | exec() | The system function exec() failed when attempting to initialize the process space for a post-processing script |

In many cases, a specific failure message is returned from the LSAM and viewable as field "LSAM Error Message" under the "General" tab of the Job Configuration screen. Messages begin with text generated by the LSAM, and conclude with parentheses containing an integer message ID and perhaps other test. 

If the error was the result of a system call, the additional text after the message ID would include the system-specific error number returned by the operating system, the symbolic name for this error (common to the vast majority of UNIX systems), and a brief description of the error as returned by the operating system. 

The UNIX error number and text varies from system to system. Also, a system call often has multiple failure modes, so the same message ID can be followed by a variety of error codes.

:::tip Example

The following example shows a LSAM Error Message which might be returned for a LSAM exit code of 000010205:

```
[sma_lsam] (monitor) - Unable to execute [/usr/john/job_1] for [JOB1] (120 / 2 [ENOENT] - No such file or directory)
```

In this case, the user should check what was entered for "Start Image" on the Job Details screen.

:::

## File Arrival Job Exit Codes

The following is a list of UNIX LSAM exit codes specifically for File Arrival jobs:

| Exit Code | Description |
| --------- | ----------- |
| 1	| The file is not found; Reasons include an invalid file name, the file has not arrived yet, or permissions |
| 2	| The path is not found; Reasons include an invalid path or permissions |
| 3	| A file is found but the creation date is out of range |
| 4 | Internal system error: Abnormal signal caught |