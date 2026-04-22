---
sidebar_label: 'UNIX script requirements'
title: UNIX Script Requirements
description: "Reference for the script formatting rules that OpCon jobs executed by the Unix Agent must follow, including shell invocation, child process handling, and exit codes."
tags:
  - Reference
  - System Administrator
  - Agents
---

# UNIX script requirements

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the script formatting rules that OpCon jobs executed by the Unix Agent must follow, including shell invocation, child process handling, and exit codes.

- The Unix Agent relies on the shell invocation line in the first line of a script to determine how to run the script; without it, the agent cannot reliably start execution.
- The agent reads the exit code returned by the script to determine whether the job succeeded or failed; if the script does not supply an exit code within the valid range of -127 to +127, the agent misinterprets the result and may report incorrect job status.

Scripts run as OpCon jobs must meet the following requirements:

* A shell invocation line in the first line of the script.

:::tip Example

Depending on the UNIX shell in use, the invocation line may contain the following information:

```#!/bin/csh```

```#!/bin/ksh```

```#!/bin/sh```

Any other available shells may also be invoked.

:::

* If the script starts other scripts, the parent script must wait for all child scripts to finish.
* 
The script must supply an exit code. The valid Exit Code range is –127 to +127. The LSAM misinterprets any codes falling outside this range. If using STDOUT to communicate exit conditions, refer to [Redirecting STDOUT](redirecting-stdout).

## When these requirements apply

These requirements apply when:

- A script is defined as a Start Image in the Enterprise Manager and will be run by the Unix Agent as an OpCon job.
- A script starts child scripts or processes that must complete before the parent job is considered finished.

