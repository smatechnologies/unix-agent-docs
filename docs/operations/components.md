---
sidebar_label: 'Components'
title: Components
description: "Describes the continuous daemon processes that make up the Unix Agent, including their roles in job submission, communication, logging, file monitoring, and job output retrieval."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# Components

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

Describes the continuous daemon processes that make up the Unix Agent, including their roles in job submission, communication, logging, file monitoring, and job output retrieval.

## When would you use it?

- You are troubleshooting a missing or unexpectedly stopped process (for example, sma_disp, sma_log, or sma_lsam) and need to understand what each process is responsible for.
- You are planning a deployment and need to decide which optional components (sma_fad, sma_filein, sma_cronmon, sma_JORS, sma_RM) to enable based on the features you require.
- You are deactivating an optional component and need to confirm which processes are safe to remove without affecting core agent operation.

## Why would you use it?

- The agent is composed of interdependent processes. Knowing the role of each component helps you identify the source of a problem without restarting the entire agent unnecessarily.
- The Required/Optional distinction lets you make informed decisions about which processes to include in your deployment, reducing resource usage on systems that do not need features such as file-event triggering (sma_fad), MSGIN event submission (sma_filein), or job output retrieval (sma_JORS).

## Process dependencies

The table below summarizes which processes are always required and which are optional. The three required processes — sma_lsam, sma_disp, and sma_log — must run for the agent to submit jobs, communicate with the SAM, and write log entries. The remaining processes are optional and only need to run when their specific feature is in use.

| Process | Required | Purpose |
| ------- | -------- | ------- |
| sma_lsam | Yes | Job submission and monitoring |
| sma_disp | Yes | Communication with the SAM; sma_log must be active for sma_disp to function |
| sma_log | Yes | Continuous logging for all agent processes |
| sma_fad | No | File-activity-based event triggering |
| sma_filein | No | External event submission via the MSGIN directory |
| sma_cronmon | No | Cron-log-based event triggering |
| sma_JORS | No | Job output retrieval and SMA File Transfer server |
| sma_RM | No | Resource monitoring and event triggering |

## Common characteristics

All of the agent components have the following characteristics:

* The processes read the agent configuration file to initialize system parameters.
* The processes run as daemon processes with root authority.
* The processes should always be started from within the agent Control Script with the start argument. For information on agent commands, refer to [Unix Agent Commands](../operations/unix-lsam-commands).
* All output bound for the terminal is redirected to file ```"LSAM_output_<SAM_socket>"``` in the agent root directory.

The table below lists the continuous processes of the agent with a short description of each component. Click on the link for a more in-depth discussion of the component.

agent Continuous Processes

| Process | Required | Short Description |
| ------- | -------- | ----------------- |
| sma_lsam | Yes | This process submits jobs to the operating system as instructed by the SAM and monitors the jobs' progress |
| sma_disp | Yes | This process manages all communication between the agent and the SAM |
| sma_log | Yes | This process provides continuous and dependable logging for the agent |
| sma_fad | No | This process(es) is a mechanism allowing the agent to trigger events based on the satisfaction of file dependencies - SAM then processes these events |
| sma_filein | No | This process allows events to be submitted to the SAM from the agent machine |
| sma_cronmon | No | This process provides a mechanism to allow the agent to trigger events for processing by SAM based on cron-activated processes |
| sma_JORS | No | This process enables you to view Unix Agent job output from the Enterprise Manager, and acts as FTServer during execution of SMA File Transfer (FT) jobs |
| sma_RM | No | This process is the mechanism by which disk, process, and user-defined resources are monitored and events triggered based upon the state of these resources. SAM then processes these events |

### sma_lsam 

The sma_lsam submits jobs to the operating system as instructed by the SAM and monitors the jobs' progress. For normal job processing, the agent resolves process status requests by searching the job's tracking file, ```"<LSAM root path>/tracking/<SMA_LSAM_INSTANCE>/<Job_ID>"```. If the file is not found, the agent reports the job as Failed to the SAM.

The sma_lsam process works in the following way:

1. If a start request is received from the SAM, a child process (also called sma_lsam) is spawned to monitor the job.
2. After spawning the job, the monitor process sends a message to the parent sma_lsam containing start information. The monitor process then sleeps until the job terminates.
3. When the job completes, the UNIX operating system wakes the monitor process. Before exiting, the monitor process sends a message to the parent sma_lsam containing completion information.

#### Characteristics

The sma_lsam rereads the agent configuration parameter max_number_of_jobs_to_run from the configuration file when the agent Control Script is run with the refresh argument. For information on the agent Control Script, refer to [Updating the agent Control Script](../configuration/updating-lsam-control-script).

### sma_disp

The message dispatcher (sma_disp) is responsible for communication with the sma_lsam process and with SMANetCom. Communication with SMANetCom is sent on the SAM Socket Number specified in the agent Control Script.

#### Characteristics

Uses the SAM_SOCKET variable in the agent Control Script to communicate with SMANetCom.

:::info Note 

If the agent receives no communication on a socket after the time specified by the msg_timeout_in_seconds parameter, the agent considers the socket inactive and closes it.

:::

You must have the logging system (sma_log) active.

### sma_log

The sma_log process provides continuous and dependable logging of the agent.

#### Characteristics

* Logs messages containing a date/time-stamp, the machine name, and the process ID (pid) number.
* By default, writes all informational messages to the ```<LSAM root path>/log/<SMA_LSAM_INSTANCE>/logfile```. The SMA_LOG_DIRECTORY variable contains this directory.
* By default, writes all error messages to the: ```<LSAM root path>/log/<SMA_LSAM_INSTANCE>/errfile```. The SMA_LOG_DIRECTORY variable contains this directory.
* If the size of the logfile or errfile reaches the log_file_rollover_size (read from the configuration file), the sma_log renames the file to a unique name and creates a new file.

### sma_fad

The sma_fad process enables the agent to send external events to the SAM when certain files meet defined criteria. Additionally, sma_fad offers more features and a dramatic increase in event throughput. For a list of valid OpCon Events, refer to [Introduction](https://help.smatechnologies.com/opcon/core/events/introduction) in the OpCon Events online help. For more information on the SMA File Activity Detection Daemon, refer to [SMA File Activity Detection Daemon](../daemon/file-activity-detection-daemon).


#### Characteristics

This process is optional. For information on [Deactivating agent Components](../reference/system-modification/deactivating-lsam-components), refer to Deactivating agent Components. It reads all of the file dependency criteria and events from a Control File:

```LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/<Control file>```

The sma_disp process sends the event(s) to the SAM when files meet defined criteria.

### sma_filein

The sma_filein process monitors a MSGIN directory for files containing valid OpCon events to be sent to the SAM. The location of the directory is ```<LSAM root path>/MSGIN/<SMA_LSAM_INSTANCE>``` on the machine where the UNIX LSAM resides. Any external program/application may generate and place an ASCII file in this directory. For the SAM to process the event, these ASCII files must contain a properly formatted OpCon event with a User Login ID and event password. For a list of valid OpCon Events, refer to [Introduction](https://help.smatechnologies.com/opcon/core/events/introduction) in the OpCon Events online help.

:::info Note 

An event file can only contain one event. Place the event in the first line of the ASCII file.

:::

The sma_filein process watches the MSGIN directory for any text file. Following detection, the process reads the file, passes the text to the SAM for processing, and finally deletes the text file. If the SAM receives an invalid event, the SAM documents the error in the SAM Critical log file.

#### Characteristics

* The sma_filein process is optional. For information on Deactivating LSAM Components, refer to [Deactivating LSAM Components](../reference/system-modification/deactivating-lsam-components).
* Reads the sma_filein_sleep_time from the configuration file to determine the time to wait between file checks.
* Processes and deletes all files in the MSGIN directory.
* After sma_filein reads the file, the sma_disp process sends the event to the SAM.

### sma_cronmon

The sma_cronmon process enables the LSAM to send external events to the SAM based on cron-activated processes. This process searches the cron log for a user-defined string and then sends a user-defined event to SAM.

The cronmon.conf file contains all cron search strings and events. When editing the cronmon.conf file, use the following syntax:

```<regular expression search string>#e#<event string>```

Characteristics
The sma_cronmon process is optional. For information on Deactivating agent Components, refer to [Deactivating agent Components](../reference/system-modification/deactivating-lsam-components).
Reads all of the process dependency criteria from the cronmon.conf file:
```<LSAM root path>/config/<SMA_LSAM_INSTANCE>/cronmon.conf```
Searches for the ```<regular expression search string>``` in the following possible locations for the cron log: ```/var/log/cron```, ```/var/cron/log```, and ```/var/adm/cron/log```.

When the search string is found, the sma_disp process sends the event to the SAM. For a list of valid OpCon Events, refer to [Introduction](https://help.smatechnologies.com/opcon/core/events/introduction) in the OpCon Events online help.

:::tip Example

The following example shows a cronmon.conf file:

```

/dev/null#e#$THRESHOLD:SET,thresholdnull,1

jobtest#e#$THRESHOLD:SET,findtest,3

```

:::

### sma_JORS

The sma_JORS (Job Output Retrieval System) process allows you to view UNIX LSAM job output from the Enterprise Manager, and acts as FTServer during execution of SMA File Transfer (SMAFT) jobs.

#### Characteristics

* Regarding job output, the only available output files are for the last execution.
* If the UNIX LSAM is not configured with STDOUT and/or STDERR capture turned on, no job output is available for users to view; consequently, users receive a message indicating the absence of STDOUT and STDERR files when attempting to view job output in the Enterprise Manager. For more information on LSAM STDOUT and STDERR redirection setting, refer to [JORS and SMAFT Parameters](../configuration/parameters/jors-and-smaft-parameters).
* The socket number specified in the configuration file must match both the JORS Port Number and the File Transfer Port Number specified in the Enterprise Manager.

##### Configure the JORS and file transfer ports in the Enterprise Manager

For the Enterprise Manager to connect to the LSAM for job output and/or File Transfer, configure the JORS and File Transfer Port Numbers to match the JORS_FT Socket configured through the LSAM.

:::info Note 

By default, the LSAM sets the JORS_FT Socket number to the sum of ten plus the LSAM's socket number.

:::

To configure the JORS and file transfer ports, complete the following steps:

1. Use menu path: Start > Programs > OpConxps > Enterprise Manager. The OpCon Login screen displays.
2. In the Username text box, enter a case-sensitive User Login ID (e.g., ocadm).
3. In the Password text box, enter the case-sensitive password for you.
4. In the Profile drop-down list, select the Profile.
5. Select the Login button to log in to the Enterprise Manager.
6. Double-click on Machines. The Machines screen displays.
7. In the Select Machine list, select the UNIX Machine.
8. Select Open Advanced Settings Panel. The Advanced Machine Properties window displays.
9. Select the Communication Settings tab.
10. Select the JORS Port Number parameter.
11. Enter the same value entered for the JORS Socket in the LSAM Configuration in the Modify Parameter frame at the bottom of the screen. For information on the JORS Socket in the LSAM Configuration, refer to [JORS_FT socket number](../configuration/parameters/jors-and-smaft-parameters#jors-ft-socket-number).

:::caution 

For JORS and a File Transfer job to function properly, ensure that any firewall on the UNIX machine allows the JORS Port Number (and the matching File Transfer Port Number below) to be open.

:::

12. Select the Update button.
13. Select the File Transfer Settings tab in the Advanced Properties window.
14. Select the File Transfer parameter.
15. Select the desired operating mode (None, Send Only, Receive Only, or Two-way) from the drop-down list in the frame below the Advanced Machine Properties.
16. Select the Update button.
17. Select the File Transfer IP Address parameter in the File Transfer Settings tab.
* Enter the machine's IP address.
* Select the Update button.
18. Select the File Transfer Port Number parameter in the File Transfer Settings tab.
* Enter the same value entered for JORS Port Number in step 10-a.
* Select the Update button.
19. Select the Save button to save and close the Advanced Settings Panel. The JORS and file transfer ports are configured.
20. *(Optional)* Start communication with the machine by:
* Right-clicking over the graphic to enable the menu in the Communication Status frame.
* Selecting Start Communication from the menu.
21. Select the x to the right of the Machines tab to close the Machines screen.

##### View job output in the Enterprise Manager

To view job output, complete the following steps:

1. Under the Operation topic, double-click on List.
2. Select the arrow to expand the specific date.
3. Select the arrow to expand the specific schedule.
4. Right-click on the desired job.
5. Select View Job Output from the menu. The Job Output Retriever window displays.
6. Double-click on the Output File(s) name to retrieve the output file information. The Log Viewer window displays.
7. *(Optional)* Select the Copy To Clipboard button.
8. *(Optional)* Select the Open external editor button to open the file in an external editor (e.g., Notepad).
9. Select the Close button to close the "Log Viewer" window.
10. Select the Close button to close the "Job Output Retriever" window. The job output is displayed.

### sma_RN

The sma_RM process enables the LSAM to send external events to the SAM when certain resource-related criteria are met. For a list of valid OpCon Events, refer to Introduction in the OpCon Events online help. For more information on the SMA Resource Monitor, refer to [SMA Resource Monitor (SMA_RM)](../smarm/introduction).

:::info Note 

The SMA Resource Monitor is a beta program.

:::

#### Characteristics

This process is optional. For information on Deactivating LSAM Components, refer to [Deactivating LSAM Components](../reference/system-modification/deactivating-lsam-components). It reads all of the file dependency criteria and events from its Control File:

```LSAM_ROOT/config/<SMA_LSAM_INSTANCE>/SMA_RM.conf```

The sma_disp process sends the event(s) to the SAM when the resource-related criteria defined within the Control File are met.

## Examples

**Scenario:** A system administrator is deploying the Unix Agent on a host that runs automated cron jobs and needs OpCon to react when those jobs fire, but the host does not require job output retrieval.

The administrator enables the three required processes — sma_lsam, sma_disp, and sma_log — to handle job submission and SAM communication. Because the host's cron log is at `/var/log/cron`, the administrator also enables sma_cronmon and configures `cronmon.conf` with a search string matching the cron job name and a `$THRESHOLD:SET` event. The sma_JORS and sma_fad components are left deactivated because job output retrieval and file-activity triggering are not needed on this host. After starting the agent, the administrator runs `lsam3100 status` and confirms that sma_lsam, sma_disp, sma_log, and sma_cronmon are listed as running, while the unneeded processes are absent from the output.

## Glossary

**sma_disp** — The message dispatcher process responsible for all communication between the Unix Agent and SMANetCom. It must be active for the agent to receive job requests from the SAM and return job status.

**sma_lsam** — The core agent process that submits jobs to the Unix operating system as instructed by the SAM and monitors each job's progress through its tracking file. It is required for any job processing to occur.

**MSGIN directory** — A monitored directory (`<LSAM root path>/MSGIN/<SMA_LSAM_INSTANCE>`) into which external programs place ASCII files containing valid OpCon events. The sma_filein process reads, forwards, and deletes each file.

**daemon process** — A background process that runs continuously with root authority, reads the agent configuration file to initialize system parameters, and redirects all terminal output to the `LSAM_output_<SAM_socket>` file in the agent root directory.
