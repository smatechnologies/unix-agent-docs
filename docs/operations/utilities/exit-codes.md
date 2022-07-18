# exit_codes

The exit_codes utility executes a job and displays the return values. Helpful for debugging, this information aids in determining the expected results for a job in OpCon.

This utility displays the following information when a job completes:

* Start image
* User ID used
* Group ID used
* Job start date/time
* Job end date/time
* Numeric exit code
* Numeric exit signal
* If a core image was created. This information is displayed in binary format (i.e., 1 = Yes, 0 = No).

For dependable results, the job specified in the Start Image must explicitly perform an exit () call. Most UNIX implementations return a zero when a process completes normally; however, some UNIX implementations return 18 when a process completes normally.

## Syntax

```exit_codes -u# -g# -s"<start image>"```

```-u#```: This required parameter specifies the User ID under which the job runs.
```-g#```: This required parameter specifies the Group ID under which the job runs.
```-s"<start image>"```: This required parameter specifies the start image and arguments for the job.

:::tip Example

The following example shows the command to execute the LSAM's generic program, genericpgm, from the /usr/local/lsam/bin directory. The generic program's parameters cause the job to run for two seconds and to terminate with an exit code of three:

```
exit_codes -u0 -g0 -s"/usr/local/lsam/bin/genericpgm -t2 -e3"
```

The following output displays on the screen with the exit_codes utility processes the job:

```
/usr/local/lsam/bin/genericpgm started at Fri Oct 31 12:09:03 2003
/usr/local/lsam/bin/genericpgm - Arguments : time: 2 exit: 3 signal: 0 core : N

/usr/local/lsam/bin/genericpgm ERRORED at Fri Oct 31 12:09:05 2003

Start image : /usr/local/lsam/bin/genericpgm -t2 -e3
User-id used : 0
Group used : 0
Job started : Fri Oct 31 12:09:03 2003
Job finished : Fri Oct 31 12:09:07 2003
Exit status : 3
Exit signal : 0
Core image created : 0
```

:::