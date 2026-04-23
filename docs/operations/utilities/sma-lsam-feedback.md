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

- A job needs to surface a non-job-specific error condition or status message in the agent Feedback or Detailed Job Messages field in OpCon without operators opening a log file.
- The agent encounters a condition unrelated to the job's primary function — such as a missing dependency or an unexpected environment state — and needs to surface it in OpCon without requiring operators to access the agent machine directly.

## Syntax

```$SMA_BINDIR/sma_LSAM_feedback "Message"```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `"Message"` | Required | Text to display in the agent Feedback or Detailed Job Messages field for the job. Each call to sma_LSAM_feedback creates one entry. |


## Examples

:::tip Example

The following example shows a script using the sma_LSAM_feedback utility to send a message to be displayed in the Enterprise Manager.

```
. . .

$SMA_BINDIR/sma_LSAM_feedback "Unable to open PRD file"

. . .
```

:::

## Glossary

**agent Feedback** — A field in the OpCon Job Configuration view that displays messages sent by the Unix Agent during job execution. One entry is created for each call to `sma_LSAM_feedback`.

**Detailed Job Messages** — A field in the OpCon Job Configuration view (Operations Related Information tab) that lists messages accumulated during a job's execution. Used for SMAFT-type jobs.