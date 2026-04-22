---
sidebar_label: 'lsam_killjob'
title: lsam_killjob
description: "Reference for the lsam_killjob command, which forcibly terminates a running OpCon job on the Unix Agent by sending a SIGKILL signal to the identified process."
tags:
  - Reference
  - System Administrator
  - Agents
---

# lsam_killjob

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the lsam_killjob command, which forcibly terminates a running OpCon job on the Unix Agent by sending a SIGKILL signal to the identified process.

- A running job must be terminated immediately and the Advanced Machine parameter "Allow Kill Job" is not set to TRUE, so termination through the Enterprise Manager Operation view is not available.
- You need to terminate an SMA File Transfer (SMAFT) job that cannot be stopped through the normal OpCon job kill mechanism.
- lsam_killjob presents an interactive confirmation prompt for each matching process before sending the SIGKILL signal, giving you the opportunity to confirm the correct process before terminating it.

The lsam_killjob command forcibly terminates a job. The Enterprise Manager displays the status "Failed: Killed by Sys Admin" for the terminated job.

The lsam_killjob command runs a "ps –ef" command to display every running process on the system and captures that display. For each line of the display in which the ```<Search_Text> ```appears and the associated process is determined to be the top-level process of an OpCon job, you are presented with the line of output from the "ps" command followed by the prompt "Kill? (*n/y) =>". Respond with "y" to have the corresponding OpCon job terminated; or with "n" (or a blank line) to allow the job to continue running. If multiple jobs with the same ```<Search_Text>``` are running concurrently, a separate display and prompt is issued for each job. Refer to the example below.

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

Running this script should not be necessary if the Advanced Machine parameter "Allow Kill Job" is set to TRUE. If TRUE, users may terminate jobs via Enterprise Manager Operation.

:::

For information on this parameter, refer to [Administrative Machine Information](https://help.smatechnologies.com/opcon/core/objects/machines#administrative-machine-information) in the Concepts online help. Additionally, users may also define a ```$JOB:KILL``` event. For information on this event, refer to [Job-Related Events](https://help.smatechnologies.com/opcon/core/job-components/events) in the OpCon Events online help.

## Syntax

```lsam_killjob <Search_Text>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `<Search_Text>` | Required | Text used to identify the job to terminate. Matched against the output of `ps -ef`; typically the Start Image and Parameters from the OpCon Job Details screen. Only as much text as needed to identify the job is required. Enclose in quotes if the text contains embedded spaces. For SMAFT jobs, specify `SMAFTScript<SAM_socket>` (for example, `SMAFTScript3100`). |
