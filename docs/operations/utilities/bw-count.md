---
sidebar_label: 'bw_count'
title: bw_count — Count Whitelist and Blacklist Entries
description: "Reference for the bw_count utility, which counts the number of whitelist and blacklist user entries in the Unix Agent configuration file."
tags:
  - Reference
  - System Administrator
  - Agents
---

# bw_count — Count whitelist and blacklist entries

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`bw_count` reads the agent configuration file and outputs the total number of `whitelist_user` and `blacklist_user` entries it contains.

Use `bw_count` to verify that the expected number of security allow list and block list entries are present after updating the configuration file, or to quickly confirm the current count without opening `lsam.conf` directly.

## Syntax

```
bw_count
```

No arguments. `bw_count` reads the configuration file path from the `SMA_CONFIG_FILE` environment variable.

## Required environment variables

| Variable | Description |
|---|---|
| `SAM_SOCKET` | The SAM socket number identifying this agent instance |
| `SMA_LSAM_INSTANCE` | The agent instance name |
| `SMA_CONFIG_FILE` | The full path to the agent configuration file (`lsam.conf`) |

:::info Note

These variables are set automatically when `bw_count` is called from within the agent Control Script environment or from an OpCon job running on the agent. If called from an external context, set these variables manually before running `bw_count`.

:::

## Output

`bw_count` prints the total count of `whitelist_user` and `blacklist_user` lines to standard output. Comment lines (starting with `#`) and blank lines are ignored.

:::tip Example

```
$ bw_count
5
```

The output `5` indicates that 5 whitelist or blacklist user entries are present in `lsam.conf`.

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success |
| `-1` | Required environment variable (`SAM_SOCKET`, `SMA_LSAM_INSTANCE`, or `SMA_CONFIG_FILE`) is not set |
