# Job Resource-Usage Reporting

The following table lists the OpCon Field Code and description for data returned with each job when job resource-usage reporting is enabled (LSAM configuration parameter LSAM_job_statistics set to 1):

| FC | 'struct rusage' | Description |
| -- | --------------- | ----------- |
| 6801 | ru_utime | CPU usage - user code (milliseconds) |
| 6802 | ru_stime | CPU usage - system code (milliseconds) |
| 6803 | ru_maxrss | max resident set size used (kilobytes) |
| 6804 | ru_ixrss | integral shared memory size; amount of sharing of text segment memory with other processes (kilobyte-seconds) |
| 6805 | ru_idrss | integral unshared data size; amount of data segment memory used (kilobyte-seconds) |
| 6806 | ru_isrss | integral unshared stack size; amount of stack memory used (kilobyte-seconds)|
| 6807 | ru_minflt | number of page reclaims; soft page faults, i.e., those serviced by reclaiming a page from the list of pages awaiting reallocation |
| 6808 | ru_majflt | number of page faults; hard page faults, i.e., those that required I/O |
| 6809 | ru_nswap | number of swaps; times a process was swapped out of physical memory |
| 6810 | ru_inblock | number of block input operations; input operations via the file system, does not include operations with the cache |
| 6811 | ru_oublock | number of block output operations; output operations via the file system, does not include operations with the cache |
| 6812 | ru_ioch | number of characters read/written |
| 6813 | ru_msgsnd | number of IPC messages sent |
| 6814 | ru_msgrvc | number of IPC messages received |
| 6815 | ru_nsignals | number of signals received |
| 6816 | ru_nvcsw | number of voluntary context switches; times the process gave up the CPU before it had to (usually to wait for some resource to be available) |
|6817 | ru_nivcsw | number of involuntary context switches; times the process was forced to relinquish control of the CPU because a higher priority process became run able or the current process used up its time slice |
|6818 | n/a | wall-clock run time (seconds) |

Except for "wall-clock run time", which is calculated by the LSAM, text appearing in column Descriptions was compiled from #include files on various systems. The items appearing in column 'struct rusage' indicate the member names for the data structure populated by the OS with the getrusage() system call.

The above table represents the entire set of possible values which may be reported. Not all systems support the entire set. Values not supplied to the LSAM by the OS are reported as zero. At a minimum, all systems will report meaningful values for CPU usage (FC 6801 and 6802) and wall-clock run time (FC 6818).

Job resource-usage stats are returned for SMA File Transfer (SMAFT) jobs as well as regular UNIX jobs when the destination machine is a UNIX machine. The resource-usage stats will reflect those of the Agent and not include any data from the Server (even if it's another UNIX box).