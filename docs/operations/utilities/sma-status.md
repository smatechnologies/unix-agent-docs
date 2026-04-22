---
sidebar_label: 'sma_status'
title: sma_status
description: "Reference for the sma_status utility, which sends a short status message from a running job to the OpCon Enterprise Manager to display alongside the job's status."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_status

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the sma_status utility, which sends a short status message from a running job to the OpCon Enterprise Manager to display alongside the job's status.

- A job runs multiple discrete steps and operators monitoring the Enterprise Manager need to know which step is currently running without examining log files.
- A job invokes sma_ppscript and the analysis script needs to report a human-readable status to the Enterprise Manager alongside the pass/fail result.

- The status message remains visible in the Enterprise Manager until the job status changes or the job terminates, giving operators continuous visibility into a long-running job's progress.
- Embedding sma_status calls at key points in a job script reduces the need for operators to consult log files to determine how far a job has progressed.

The sma_status utility sends a message for the Enterprise Manager to display after the OpCon status message. The message's maximum is twenty-characters. Without warning you, the agent truncates messages longer than the maximum.

## Syntax

```$SMA_BINDIR/sma_status "<message>"```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `"<message>"` | Required | Status text to display in the Enterprise Manager after the OpCon status message. Maximum 20 characters; messages longer than 20 characters are truncated without warning. |

:::info Note

The environment variable `$SMA_BINDIR` is defined for use within OpCon jobs. If run from a context other than an OpCon job, `$SMA_BINDIR/` must be replaced by the appropriate path.

The job status posted by this command remains in the Enterprise Manager until the job status changes or the job terminates.

:::

:::tip Example

The following example shows a script using the sma_status utility. The script sends a message when each step of the job begins processing.

```

#!/bin/sh

# Job status in Enterprise Manager currently shows "Job Running:Pid = pid"

$SMA_BINDIR/sma_status "Starting Step 1"

# Job status in Enterprise Manager now shows "Job Running:Starting Step 1"

do_step 1

$SMA_BINDIR/sma_status "Starting Step 2"

do_step 2

# Job status in Enterprise Manager now shows "Job Running:Starting Step 2"

```

:::