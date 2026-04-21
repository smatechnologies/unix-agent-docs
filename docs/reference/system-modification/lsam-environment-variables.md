---
title: Agent Environment Variables
description: "Reference for Unix Agent environment variables passed to jobs at runtime, including path, job identity, schedule, and file I/O variables."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Agent environment variables

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for Unix Agent environment variables passed to jobs at runtime, including path, job identity, schedule, and file I/O variables.

So a job may adapt to its environment, the agent defines several environment variables for a started job. The following references these variables:

## When would you use it?

- You are writing a job script and need to reference the agent utilities directory, configuration file path, or job identity values at runtime.
- A job fails with a "Missing environment variable" message and you need to identify what value the agent should have provided.
- You are troubleshooting a path issue in a job script and need to confirm which variable holds the correct STDOUT, STDERR, or binary directory path.
- You are configuring or reviewing an SMA File Transfer job and need to understand how the agent populates `SMA_XML_FILE`.

### SMA_BINDIR	

The path to the agent Utilities directory.

### SMA_CONFIG_FILE

The path to the configuration file used by a particular agent.

### SMA_JOBNAME

The short job name and job ID defined in OpCon.

### SMA_USER_SPECIFIED_JOBNAME

The job name displayed in the Enterprise Manager.

### SMA_SCHEDULE_DATE

The date of the schedule containing the job ```<SMA_JOBNAME>```.

### SMA_SCHEDULE_NAME

The name of the schedule containing the job ```<SMA_JOBNAME>```.

### SMA_SCHEDULE_FREQUENCY

The schedule frequency of the job ```<SMA_JOBNAME>```.

### SAM_SOCKET

The socket number the agent uses to communicate with the SAM.

### SMA_LSAM_INSTANCE

The name given to this particular instance of the agent. If no instance name was given at install, this is set to the socket number.

### SMA_STDERR

The path to the STDERR file associated with the job ```<SMA_JOBNAME>```.
If a STDERR file is not associated with the job, the variable contains "NONE".

### SMA_STDOUT

The path to the STDOUT file associated with the job ```<SMA_JOBNAME>```.
If a STDOUT file is not associated with the job, the variable contains "NONE".

### SMA_XML_FILE

Used by SMA File Transfer (SMAFT).
