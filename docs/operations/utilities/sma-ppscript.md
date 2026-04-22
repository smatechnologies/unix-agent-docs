---
sidebar_label: 'sma_ppscript'
title: sma_ppscript
description: "Reference for the sma_ppscript utility, which registers a post-processing analysis script to determine job success or failure after the job's executable finishes."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_ppscript

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the sma_ppscript utility, which registers a post-processing analysis script to determine job success or failure after the job's executable finishes.

## When would you use it?

- A job's success or failure cannot be determined solely by its exit code, and the content of the job's STDOUT or STDERR output must be analyzed to make that determination.
- The standard Failure Criteria in the OpCon Job Details screen does not provide sufficient flexibility for the specific analysis the job requires.

## Why would you use it?

- sma_ppscript separates the job's executable from the logic used to evaluate its outcome, allowing you to update the analysis script independently without modifying the job's main program.
- The analysis script receives the pathnames of the job's redirected STDOUT and STDERR files as arguments, giving it direct access to the job's output for detailed inspection.

The sma_ppscript utility provides an alternative method to the Job Details screen's "Failure Criteria" for determining a job's success or failure. A Job's executable invokes sma_ppscript telling the agent the job needs post-processing with a user-supplied analysis script. 

When the job finishes, the agent runs the script. After analysis, the script returns a zero for success and a non-zero value for failure. The agent simply returns the success or failure of the job without specific details; however, the script may call the utility sma_status to provide further details to the Enterprise Manager.

## Syntax

```$SMA_BINDIR/sma_ppscript <script_command>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `<script_command>` | Required | Path and arguments for the analysis script to run after the job completes. The agent appends the pathnames of the job's redirected STDOUT and STDERR files to the end of this command when invoking the script. |

:::info Note

The environment variable `$SMA_BINDIR` is defined for use within OpCon jobs. If run from a context other than an OpCon job, `$SMA_BINDIR/` must be replaced by the appropriate path.

:::

## Analysis script

To create an Analysis Script, write a shell script (or compiled program) to do the analysis. It may take any start parameters desired, and has the pathnames of the job's redirected STDOUT and STDERR files appended to you-supplied list of start parameters. The script/program may do whatever it wishes to determine success or failure, to be indicated by its exit status.

:::info Note

If the LSAM is not configured to redirect STDOUT and/or STDERR to files, the script sees "NONE" for the/each pathname.

:::

:::tip Example

The following example shows the analysis script "/usr/home/john/check_ls" which uses the LSAM file_check utility. The script determines whether the job's redirected STDOUT exists and is of sufficient length. If so, the script exits with a zero; otherwise, the script returns a non-zero value.

```

#!/bin/sh

# $1 -- status text to display in Enterprise Manager

# $2 -- minimum acceptable file size

# $3 –- pathname of redirected STDOUT

# $4 -– pathname of redirected STDERR (not used!)

$SMA_BINDIR/sma_status $1

sleep 10

# Does STDOUT exist and at least $2 bytes long?

$SMA_BINDIR/file_check –ae -f $3 –s $2

exit $?

```

:::

## Invocation of the analysis script

Insert sma_ppscript into the job's executable for invocation of analysis script. Once the analysis script has been written, embed the command "$SMA_BINDIR/sma_ppscript ```<script_command>```" anywhere within the job's top-level script/program. For example, assuming the script is named "/usr/home/john/check_results", "$SMA_BINDIR/sma_ppscript /usr/home/john/check_results 1 a".

:::tip Example

This is the job which requires post-processing by "/usr/home/john/check_results":

```

#!/bin/sh

$SMA_BINDIR/sma_status "Registering script"

$SMA_BINDIR/sma_ppscript /usr/home/john/check_ls Checking 50

sleep 10

$SMA_BINDIR/sma_status "Listing stuff"

ls –l /usr/home/john/stuff

sleep 10

```

:::
