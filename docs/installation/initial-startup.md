---
title: Initial Startup
description: "Step-by-step procedure for starting the Unix Agent after a new or upgrade installation and verifying that all required processes are running."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Initial startup

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?
Step-by-step procedure for starting the Unix Agent after a new or upgrade installation and verifying that all required processes are running.

Use this procedure in the following situations:

- After completing a new Unix Agent installation, to start the agent and confirm that all required processes (`sma_disp`, `sma_log`, `sma_lsam`, and any enabled optional components) are running.
- After completing an upgrade installation, to start the agent and verify that the upgrade was successful, including resolving any symbolic link dependencies on the old SAM Socket number in pathnames.
- Whenever the agent has been stopped for maintenance or reconfiguration and must be restarted and verified.

## How to implement it

**Prerequisites:** The Unix Agent must be installed (new or upgrade) and the agent Control Script must be configured. The `SMA_LOG_DIRECTORY` variable in the agent Control Script defines the path to the log file and error file used to diagnose start-up failures. For information on editing the agent Control Script, refer to [Updating the agent Control Script](../configuration/updating-lsam-control-script).

To start the agent and verify that all required processes are running, complete the following steps:

1. If performing an upgrade installation, determine if any system scripts or users' jobs depend on the SAM Socket number being a part of a pathname (e.g., "```/usr/local/lsam/MSGIN/3100```"). If this is so, the ideal solution would be to edit the jobs by changing the hard-coded SAM Socket number or referencing the environment variable ```$SAM_SOCKET``` to use the environment variable ```$SMA_LSAM_INSTANCE```. If this is not practical, then do the following from the agent root directory:
* Enter the command ```ls –l *```
* Make a note of all occurrences of sub-directories named ```<LSAM_instance>``` (e.g., "```MSGIN/prod```"). Ignore the "```bin/```" directory.
* For each sub-directory noted in the previous step, create a symbolic link in the same parent directory to point to the ```<LSAM_instance>``` sub-directory.

:::tip Example

Assuming a ```<SAM_Socket>``` of 3100 and an ```<LSAM_instance>``` of "prod", the following example shows the syntax for creating a ```<SAM_Socket>``` symbolic link in the MSGIN directory to the ```<LSAM_instance> ```sub-directory:

```ln -s MSGIN/3100 MSGIN/prod```

:::

2. Start the LSAM. Use the following syntax: ```bin/lsam<SAM_Socket>``` start.
For information on operating the LSAM, refer to [Operating the LSAM](../operations/operating-the-lsam).

:::tip Example

The following example shows the command for starting the LSAM using SAM Socket number 3100:

```bin/lsam3100 start```

:::

:::info Note

During start-up (and in other situations) the agent produces output to the terminal. To make it available in resolving support issues, terminal output is automatically redirected to file "```LSAM_output_<SAM_socket>```" within the LSAM root directory. Prior to version 3.07.01 of the LSAM, the output during the LSAM's start-up would appear on the terminal in real time. Now it is delayed until the start-up procedure has been completed, at which point the LSAM_output file is dumped to the terminal. The start-up procedure normally completes in less than 30 seconds. If it takes more than five minutes, the start-up procedure may be interrupted with ```Cntrl_C``` (or the system's assigned INT sequence) and the command entered to see the terminal output that was produced.

```cat LSAM_output_<SAM_socket>```

(e.g., "```cat LSAM_output_3100```")

The LSAM output file may be inspected at any time (via the 'cat', tail', 'vi' or other text-viewing commands). The command "```tail –f LSAM_output_<SAM_socket>```" allows real-time viewing of LSAM terminal output.

:::

3. Verify the LSAM status with the following command: ```bin/lsam<SAM_Socket> status```. The command should display the following processes:
* sma_disp
* sma_log
* sma_lsam
* Any enabled, optional components:
    * sma_cronmon
    * sma_filein
    * sma_fad
    * sma_JORS

:::tip Example

The following example shows the command to verify the status of the LSAM using SAM Socket number 3100:

```bin/lsam3100 status```


If successful, the status command produces output similar to:

```
Currently running LSAM services:

--------------------------------

UID PID PPID C STIME TTY TIME COMMAND

root 1907 1 0 Oct 20 ? 1:10 /usr/local/prod/lsam/bin/sma_disp

root 1895 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_log

root 1901 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_lsam

root 1914 1913 0 Oct 20 ? 0:00 sh -c /usr/bin/tail -1f /var/adm/cron/log

root 1913 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_cronmon

root 1927 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_filein

root 1929 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_JORS
```

:::

:::info Note

If the agent processes do not start as expected, examine the logfile and the errfile files for error messages. Use the file path defined in the SMA_LOG_DIRECTORY variable in the agent Control Script. For information on editing the agent Control Script, refer to [Updating the agent Control Script](../configuration/updating-lsam-control-script).

:::

4. To begin using the agent, refer to [Unix Agent Configuration](../configuration/unix-lsam-configuration) to configure and operate the agent.

The agent is started and all required processes are running.

## Exception handling

**`Process [x] did not start`** — The agent health monitor determined that a required process (`sma_disp`, `sma_log`, `sma_lsam`, or another component) did not start or started and immediately terminated. — Stop the agent. Review the agent log file and error file (at the path defined in `SMA_LOG_DIRECTORY` in the agent Control Script) for preceding error messages that indicate the cause. After correcting the cause, restart the agent. If no cause can be determined, wait five minutes and restart; if the condition was momentary, the agent should start and run properly.

**`Process [x] has terminated`** — The agent health monitor detected that a running agent process terminated abnormally. — Stop the agent. Review the log and error files for messages that preceded the termination. Correct the identified cause, then restart the agent. If no cause can be determined, wait five minutes before restarting.

**`EADDRINUSE - Address already in use` at startup** — The socket number the agent is configured to use is already bound by another process on the system. — Identify the process holding the socket (for example, using `netstat -an | grep <SAM_Socket>`), resolve the conflict, or reconfigure the agent with a different `<SAM_Socket>` number. If the system boots multiple services simultaneously, ensure the agent starts near the end of the boot sequence so earlier services have time to release or claim their sockets before the agent starts.

**Start-up hangs for more than five minutes with no output** — The `LSAM_output_<SAM_socket>` file is not being written to the terminal until start-up completes, and the procedure may be stalled. — Interrupt start-up with `Ctrl+C` and inspect the captured output: `cat LSAM_output_<SAM_socket>`. Address any errors reported in that file before attempting to restart.

**Agent fails to start; PID files in `$LSAM_ROOT/pid/` are zero-length or contain zero values** — On AIX systems running agent versions prior to 3.08.01, the agent fails to start when system Process IDs have reached or exceeded 10,000,000. Only the `sma_log` start-up entry appears in the log file, or no start-up entries appear at all. — Upgrade to agent version 3.08.01 or higher. If upgrading is not possible, configure the system to keep PIDs below 10 million, or reboot the system to reset PIDs before starting the agent.
