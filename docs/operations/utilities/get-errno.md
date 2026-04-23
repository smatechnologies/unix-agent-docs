---
sidebar_label: 'get_errno'
title: get_errno
description: "Reference for the get_errno utility, which translates a numeric UNIX error code into its symbolic constant and descriptive text for use in job debugging."
tags:
  - Reference
  - System Administrator
  - Agents
---

# get_errno

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the get_errno utility, which translates a numeric UNIX error code into its symbolic constant and descriptive text for use in job debugging.

The get_errno program translates the numeric error indicator (returned by UNIX system calls) into meaningful text. Text includes the standard symbolic constant # defined for the error and a brief description. Output is written to STDOUT. 

Additionally, if run as an OpCon job, the utility writes to the Enterprise Manager in the Detailed Job Messages field in the Job Information screen>Configuration Tab>Operations Related Information Tab. For additional information, refer to [Job Information](https://help.smatechnologies.com/opcon/core/Files/UI/Enterprise-Manager/Job-Information) in the Enterprise Manager online help.

- A job fails with a numeric UNIX error code and you need to identify the corresponding symbolic constant and description before consulting the troubleshooting reference.
- You are writing an OpCon job script and need to surface a UNIX error number as human-readable text in the Detailed Job Messages field.

## Syntax

```get_errno error_number```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `error_number` | Required | Numeric UNIX error indicator returned by a system call. |

:::info Note

 If run from within a user's OpCon job, "```$SMA_BINDIR/```" must be preface the command (e.g., "```$SMA_BINDIR/get_errno error_number```").

:::

## Examples

:::tip Example

The following example shows the use of get_errno for retrieving two error codes.

```
# get_errno 75

75 [EISCONN] - Socket is already connected

# get_errno 77

77 [ESHUTDOWN] - Can't send after socket shutdown
```

:::

:::tip Example

The following example shows get_errno clarifying error information on different systems. Note, although the error numbers differ, they are the same error.

```
AIX# get_errno 79

79 [ECONNREFUSED] - Connection refused

...

HP-UX$ get_errno 239

239 [ECONNREFUSED] - Connection refused
```

:::

:::tip Example

The following example shows get_errno within an OpCon job retrieving detailed exist status information on a command. The command returns the UNIX error number (i.e., errno) as its exit value.

```
...

$HOME/some_command p1 p2 p3 pn

$SMA_BINDIR/get_errno $?

...
```

:::

## Exception handling

**`Command not found` when running get_errno as an OpCon job** — The utility was invoked without the `$SMA_BINDIR/` prefix. When run as an OpCon job, the agent does not add the `bin` directory to the `PATH` automatically. — Prefix the command with `$SMA_BINDIR/`: `$SMA_BINDIR/get_errno error_number`.

**Same error condition returns different errno numbers on different platforms** — UNIX errno values are not standardized across operating systems. The same error (for example, `ECONNREFUSED`) may have different numeric values on AIX versus HP-UX. — Use `get_errno` to translate the numeric value to its symbolic constant, then look up the symbolic constant in the troubleshooting reference rather than the numeric value.

## Glossary

**errno** — A numeric error indicator returned by UNIX system calls when an operation fails. The numeric value is platform-specific but maps to a symbolic constant that is consistent across platforms.

**symbolic constant** — A human-readable identifier (such as `EACCES` or `ECONNREFUSED`) that represents a specific UNIX error condition. `get_errno` translates numeric errno values to their symbolic constants and descriptions.