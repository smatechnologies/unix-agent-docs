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

- When configuring log file size limits to prevent accumulation of log messages in a single file
- When setting the maximum number of archived log and error files to manage disk usage
- When troubleshooting agent behavior that requires reviewing log file retention settings

## log_file_rollover_size

**Default Value**: 600000
**Change Required**: N

**Description**:

* In bytes, sets the maximum size for the logfile and errfile before they are archived.
* When archiving, the agent renames the logfile to ```<ten-digit unique number>```.log.
* When archiving, the agent renames the errfile to ```<ten-digit unique number>```.err.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log messages in a single file.

### log_file_max_count

**Default Value**: 20
**Change Required**: N

**Description**:

* Sets the maximum number of archived log files.
* Also sets the maximum number of archived error files.
* When the maximum is reached for either the archived log files or error files, the agent deletes the oldest archived file and creates a new one.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log files.