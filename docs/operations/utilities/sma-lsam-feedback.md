---
sidebar_label: 'sma_LSAM_feedback'
title: sma_LSAM_feedback
description: "Reference for the sma_LSAM_feedback utility, which sends a message from the Unix Agent to the Detailed Job Messages field in the OpCon Enterprise Manager."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_LSAM_feedback

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the sma_LSAM_feedback utility, which sends a message from the Unix Agent to the Detailed Job Messages field in the OpCon Enterprise Manager.

The sma_LSAM_feedback utility instructs the agent to send a message to be displayed for a job's "agent Feedback" or "Detailed Job Messages" (depends on job type) field of the Job Configuration. One entry will be created for each use of "sma_LSAM_feedback". 

Note that this should not be used in the place of regular job output files to log job execution data, as indiscriminate use can quickly result in large amounts of data getting added to the OpCon database – its primary use is intended to be for the agent to communicate non-job-specific error conditions to SAM.

- A job needs to communicate a non-job-specific error condition or status message to the agent, to be displayed in the agent Feedback or Detailed Job Messages field in OpCon.
- You need one entry per significant event or error in the Detailed Job Messages field for operator visibility.

- sma_LSAM_feedback writes directly to the OpCon database entry for the job, making the message visible in Solution Manager without requiring operators to open a separate log file.

## Syntax

```$SMA_BINDIR/sma_LSAM_feedback "Message"```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `"Message"` | Required | Text to display in the agent Feedback or Detailed Job Messages field for the job. Each call to sma_LSAM_feedback creates one entry. |


:::tip Example

The following example shows a script using the sma_LSAM_feedback utility to send a message to be displayed in the Enterprise Manager.

```
. . .

$SMA_BINDIR/sma_LSAM_feedback "Unable to open PRD file"

. . .
```

:::