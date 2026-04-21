---
sidebar_label: 'Operating the agent'
title: Operating the agent
description: "Start, stop, and verify the status of the Unix Agent using agent commands from the command line."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Operating the agent

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Start, stop, and verify the status of the Unix Agent using agent commands from the command line.

The agent uses simple commands to control and check the status of the agent.

## When would you use it?

- Start the agent after a new or upgrade installation, or when the agent has been stopped for maintenance.
- Check the agent status to confirm that the required processes (sma_lsam, sma_disp, sma_log) and any configured optional components are running before jobs are submitted.
- Stop the agent when performing maintenance, applying configuration changes that require a full restart, or shutting down the host system.

## Start the agent

To start the agent, complete the following steps:

1. Log in to the UNIX system as root.
2. Change the directory to the agent's root directory. Use the following syntax:

```cd <LSAM _Root_Directory>```

:::info Note

After an upgrade installation, verify that the LSAM's tracking directory is empty before starting the LSAM.

1. List the contents of the tracking directory with the following command:
```cd ../tracking;ls```
2. If a file named ```tracking<SAM_Socket>``` exists, delete the file with the following command: ```rm tracking<SAM_Socket> E.g., rm tracking3100```
3. A directory named ```<SMA_LSAM_INSTANCE>``` may exist; if so, ensure that it is empty with the command: ```rm <SMA_LSAM_INSTANCE>/* E.g., rm prod/*```
4. Go back to the bin directory with the following command: ```cd ../bin```

:::

3. Start the agent using the following syntax:

```lsam<SAM_Socket>start```

:::tip Example

The following example shows the command for starting the LSAM using socket number 3100:

```cd /usr/local/lsam/; bin/lsam3100 start```

:::


4. The agent normally starts within 30 seconds, at which point the agent displays all terminal output from the ```LSAM_output``` file on the terminal. If it does not complete within five minutes, use the INT sequence (normally Cntrl_C) to stop the start-up procedure. 
    * Then use the command ```cat LSAM_output_<SAM_socket>``` to view the terminal output that was produced. 
    * The ```LSAM_output``` file can be viewed at any time. To see terminal output as it is produced, use the command ```tail –f LSAM_output_<SAM_socket>```.
5. Check the agent status before processing jobs. The agent is started.

## Check the agent status

To check the agent status, complete the following steps:

1. Log in to the UNIX system as root.
2. Change the directory to the agent's bin directory. Use the following syntax:

```cd <LSAM _Root_Directory>/bin```

3. Verify the LSAM status with the following command: ```lsam<SAM_Socket>status```. The command should display the following processes:
* sma_disp
* sma_log
* sma_lsam

and any of the following optional components that have been configured to run:
* sma_cronmon
* sma_filein
* sma_fad
* sma_jors

:::tip Example

The following example shows the command to verify the status of the LSAM using socket number 3100:

```
cd /usr/local/lsam/bin; ./lsam3100 status
```

If successful, the status command produces output similar to:

```
Currently running agent services:

--------------------------------

UID PID PPID C STIME TTY TIME COMMAND

root 1907 1 0 Oct 20 ? 1:10 /usr/local/prod/lsam/bin/sma_disp

root 1895 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_log

root 1901 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_lsam

root 1914 1913 0 Oct 20 ? 0:00 sh -c /usr/bin/tail -1f /var/adm/cron/log

root 1913 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_cronmon

root 1921 1 0 Oct 20 ? 0:01 /usr/local/prod/lsam/bin/sma_JORS

root 1923 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_RM

root 1925 1 0 Oct 20 ? 0:21 /usr/local/prod/lsam/bin/sma_fad fad1

root 1927 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_filein
```

:::

:::info Note

If the LSAM processes do not start as expected, examine the logfile, the errfile and the Terminal Output File files for error messages. Use the file path defined in the ```SMA_LOG_DIRECTORY``` variable. For information on the ```SMA_LOG_DIRECTORY``` variable, refer to [SMA_LOG_DIRECTORY](../configuration/updating-lsam-control-script#sma-log-directory).

:::

The agent status is displayed.

## Stop the LSAM

To stop the agent, complete the following steps:

1. Log in to the UNIX system as root.
2. Change the directory to the LSAM's bin directory. Use the following syntax:

```cd <LSAM _Root_Directory>/bin```

3. Stop the agent with the following syntax: ```lsam<SAM_Socket>``` stop.

:::tip Example

The following example shows the command for stopping the agent using SAM Socket number 3100:

```cd /usr/local/lsam/bin; ./lsam3100 stop```

:::

The agent is stopped.

## Exception handling

**The agent does not start within five minutes after running the start command.**
The startup procedure has stalled or encountered an error. Use the INT sequence (normally Ctrl+C) to stop the startup procedure, then run `cat LSAM_output_<SAM_socket>` to view the terminal output that was produced during the attempt. Examine the output for error messages and resolve the reported condition before trying again.

**The status command does not show the expected processes (sma_lsam, sma_disp, sma_log).**
One or more required processes failed to start. Examine the logfile, the errfile, and the Terminal Output File for error messages. Use the file path defined in the `SMA_LOG_DIRECTORY` variable to locate these files. Resolve any reported errors and restart the agent.

