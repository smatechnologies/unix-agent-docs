---
sidebar_label: 'maintain_ofiles'
title: maintain_ofiles
description: "Reference for the maintain_ofiles utility, which deletes job output files, tracking files, and temporary agent files older than a specified number of days."
tags:
  - Reference
  - System Administrator
  - Agents
---

# maintain_ofiles

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the maintain_ofiles utility, which deletes job output files, tracking files, and temporary agent files older than a specified number of days.

The maintain_ofiles program prevents the accumulation of outdated job-related files. This program deletes files older than the specified number of days. It specifically deletes: job output files, job tracking files, and anything within the agent's tmp directory. For example, if the program's parameter indicates 10 days should be kept, it removes any job-related file older than midnight of 10 days ago.

:::tip Example

If the command is issued at 10:21 AM on Oct 20th with the number of days to retain specified as 10, all files older than 12:00 AM of Oct 10th are deleted.

:::

SMA Technologies recommends scheduling this program in OpCon and running the job daily or weekly to remove job-related files older than the configured days to retain. The default number of days to retain is 3.

:::info Note

This program will also delete any SMA Resource Monitor (SMA_RM) log files which are older than the specified number of days.

:::

## When would you use it?

- You need to prevent the accumulation of outdated job output files, tracking files, and agent temporary files on the agent machine.
- You are scheduling a recurring maintenance job in OpCon to automatically clean up files older than a configured retention period.

## Why would you use it?

- Running maintain_ofiles on a regular schedule (daily or weekly) prevents disk space from being consumed by job-related files that are no longer needed.

## Syntax

```$SMA_BINDIR/maintain_ofiles <number of days to retain>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `<number of days to retain>` | Required | Number of days of files to keep. Files older than midnight of this many days ago are deleted. Default: 3. |

:::info Note

The environment variable `$SMA_BINDIR` is defined for use within OpCon jobs. If run from a context other than an OpCon job, `$SMA_BINDIR/` must be replaced by the appropriate path.

:::



