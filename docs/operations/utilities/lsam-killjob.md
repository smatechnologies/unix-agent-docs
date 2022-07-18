# lsam_killjob

The lsam_killjob command forcibly terminates a job. The Enterprise Manager displays the status "Failed: Killed by Sys Admin" for the terminated job.

The lsam_killjob command executes a "ps –ef" command to display every running process on the system and captures that display. For each line of the display in which the ```<Search_Text> ```appears and the associated process is determined to be the top-level process of an OpCon job, the user is presented with the line of output from the "ps" command followed by the prompt "Kill? (*n/y) =>". Respond with "y" to have the corresponding OpCon job terminated; or with "n" (or a blank line) to allow the job to continue executing. If multiple jobs with the same ```<Search_Text>``` are running concurrently, a separate display and prompt is issued for each job. Refer to the example below.

:::tip Example

The following example shows execution of lsam_killjob:

```
# lsam_killjob fail

[root 1683 1682 0 11:59:35 pts/t0 0:00 /usr/dean/fail F2]

Kill? (*n/y) => y


Killing sma_lsam's process number: 1683

 
Successfully killed sma_lsam's process number: 1683


No processes found (that were started by sma_lsam)

[dean 2222 2221 0 12:01:18 pts/t0 0:00 /usr/dean/fail F2]

Kill? (*n/y) => y


Killing sma_lsam's process number: 2222


Successfully killed sma_lsam's process number: 2222


No processes found (that were started by sma_lsam)

#
```

:::

:::info Note

Execution of this script should not be necessary if the Advanced Machine parameter "Allow Kill Job" is set to TRUE. If TRUE, users may terminate jobs via Enterprise Manager Operation.

:::

For information on this parameter, refer to [Administrative Machine Information](administrative-machine-information) in the Concepts online help. Additionally, users may also define a ```$JOB:KILL``` event. For information on this event, refer to [Job-Related Events](job-related-events) in the OpCon Events online help.

## Syntax

```lsam_killjob <Search_Text>```

* ```<Search_Text>``` specifies the job to be killed. Although anything pertaining to the job(s) to be killed, which would be displayed by a "ps –ef" command, could be specified (e.g., its PID, UID, etc.), normally, only text from the "CMD" portion of the "ps –ef" output is specified. This is the "Start Image" field from the Job Details screen in the OpCon Enterprise Manager followed by a single space and then the "Parameters" field. The entire text of "Start Image" need not be specified, only as much as is required to identify the job in question.
* If the job to be killed is a SMA File Transfer (SMAFT) job, then specify "```SMAFTScript<SAM_socket>```" for ```<Search_Text>```. For example: "```SMAFTScript3100```".
* If ```<Search_Text>``` contains embedded spaces, then enclose it in quotes. For example:
```lsam_killjob "/usr/jobs/phase-1 359 w"```
* The contents of the "CMD" field varies among the flavors of UNIX, ranging from just the filename of the executable, to its complete pathname, to the pathname plus the supplied start parameters (i.e., the "Parameters" field from the Job Details screen). Some systems also truncate "CMD" to an arbitrary length. Knowing this behavior beforehand will aid in determining what needs to be entered for ```<Search_Text>``` to either uniquely identify the job(s) or be presented with the least number of possibilities.