---
sidebar_label: 'validate_startup'
title: validate_startup — Validate Socket Availability
description: "Reference for the validate_startup utility, which verifies that the required TCP sockets are available before the Unix Agent starts its daemon processes."
tags:
  - Reference
  - System Administrator
  - Agents
---

# validate_startup — Validate socket availability

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`validate_startup` tests whether the consecutive TCP sockets required by the agent are available before the agent starts its daemon processes. It is called automatically by the agent Control Script during `lsam<SAM_Socket> start`.

You do not normally call `validate_startup` directly. It is documented here to explain the pre-start validation phase that appears in agent startup output and to support troubleshooting of `EADDRINUSE` errors during startup.

## Syntax

```
validate_startup [port_number]
```

| Argument | Description |
|---|---|
| `[port_number]` | Optional. When provided, `validate_startup` binds to the specified port and pauses indefinitely. This mode is used only for socket debugging. |

## Behavior

- `validate_startup` attempts to bind to each of the agent's required consecutive sockets starting from the `SAM_socket` value in `lsam.conf`.
- Each socket is tested with a 5-second timeout.
- If all sockets are available, `validate_startup` closes them and exits with code `0`, allowing the agent start to proceed.
- If any socket is unavailable, `validate_startup` exits with code `1`, and the agent start is aborted.

:::info Note

`validate_startup` disables agent logging internally during the socket check. Any errors are reported to the terminal output file (`LSAM_output_<SAM_socket>`), not the agent log.

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | All required sockets are available — agent startup can proceed |
| `1` | One or more required sockets are unavailable — agent startup is aborted |

## Exception handling

**Agent startup fails with `EADDRINUSE` and validate_startup exits `1`** — The SAM socket number or one of the consecutive ports is already in use by another process. — Identify the conflicting process using `netstat -an | grep <SAM_Socket>`, resolve the conflict (stop the conflicting process or choose a different `SAM_socket` number), then retry the agent start.
