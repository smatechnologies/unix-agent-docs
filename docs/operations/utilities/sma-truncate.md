---
sidebar_label: 'sma_truncate'
title: sma_truncate — Truncate Agent Trace Files
description: "Reference for the sma_truncate utility, which truncates Unix Agent trace files to zero length for log management and diagnostic workflows."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_truncate — Truncate agent trace files

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`sma_truncate` truncates a specified Unix Agent trace file to zero length, allowing the file to continue receiving new trace output without accumulating old entries.

Use `sma_truncate` as part of a log and trace file management routine, or before enabling tracing to ensure a clean file before capturing a diagnostic session.

- Use `sma_truncate` before capturing a trace for SMA Technologies Support to ensure the trace file contains only current diagnostic output.
- Use `sma_truncate` in a scheduled OpCon job to prevent trace files from growing unboundedly on agents where tracing is left enabled.

## Syntax

```
sma_truncate <trace_type>
```

| Argument | Description |
|---|---|
| `<trace_type>` | The trace file to truncate. Must be one of the values listed in the table below. |

## Trace type values

| Value | File(s) truncated |
|---|---|
| `DISP_trace` | `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/sma_disp.trace` |
| `LSAM_trace` | `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/sma_lsam.trace` |
| `JORS_FT_trace` | `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/sma_JORS.trace` and `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/SMAFTAgent.trace` |
| `RM_trace` | `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/sma_RM.trace` |
| `FAD_trace` | `$LSAM_ROOT/log/$SMA_LSAM_INSTANCE/sma_FAD.trace` |

:::info Note

`sma_truncate` requires the `LSAM_ROOT` and `SMA_LSAM_INSTANCE` environment variables to be set. These are set automatically when you invoke `sma_truncate` from within the agent Control Script environment or from a job running on the agent.

:::

:::tip Example

The following command truncates the dispatcher trace file before starting a new diagnostic capture:

```bash
sma_truncate DISP_trace
```

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success — the specified trace file was truncated to zero length |
| `1` | Error — invalid trace type argument, or the truncate operation failed |
