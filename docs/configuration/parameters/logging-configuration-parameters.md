---
sidebar_label: 'Logging Configuration Parameters'
title: Logging Configuration Parameters
description: "Reference for Unix Agent logging configuration parameters, including log file rollover size and maximum archived log file count settings."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Logging configuration parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for Unix Agent logging configuration parameters, including log file rollover size and maximum archived log file count settings.

The following parameters reference the logging settings for troubleshooting the Unix Agent. These settings control log file rollover size and the maximum number of archived log and error files retained on the system.

- When troubleshooting agent behavior that requires reviewing log file retention settings

### log_file_rollover_size

**Default Value**: 1000000
**Change Required**: N

**Description**:

* In bytes, sets the maximum size for the logfile and errfile before they are archived.
* When archiving, the agent renames the logfile to ```<ten-digit unique number>```.log.
* When archiving, the agent renames the errfile to ```<ten-digit unique number>```.err.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log messages in a single file.

### log_file_max_count

**Default Value**: 5
**Change Required**: N

**Description**:

* Sets the maximum number of archived log files.
* Also sets the maximum number of archived error files.
* When the maximum is reached for either the archived log files or error files, the agent deletes the oldest archived file and creates a new one.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log files.

### enable_logging

**Default Value**: 1

**Description**:

* Enables/Disables the messages that agent processes send to the agent log.
* If set to one, agent processes write their messages to the logfile and errfile.
* If set to zero, agent processes stop sending messages to the log. Leave this set to one: with logging off, agent problems cannot be diagnosed from the log.

### enable_unix_sockets_for_logging

**Default Value**: 1

**Description**:

* Selects how agent processes connect to the agent's logging process.
* If set to one, they connect through UNIX domain sockets on the local machine.
* If set to zero, they connect over TCP/IP to the logging ports. For the related binding settings, refer to `bind_localhost_LOGGING` and `bind_localhost_JOB_LOGGING` in [TCP/IP configuration](./tcp-ip-configuration.md).

### maintain_ofile_start_time

**Default Value**: 00:00

**Description**:

* The time of day, in 24-hour `HH:MM` format from 00:00 to 23:59, at which the agent runs [maintain_ofiles](../../operations/utilities/maintain-ofiles.md) each day to delete job output older than [days_of_output_to_keep](./jors-and-smaft-parameters.md#days_of_output_to_keep).
* The agent runs this clean-up only when `days_of_output_to_keep` is greater than zero.
* If the value is not a valid time, the agent logs an error and uses 03:00.