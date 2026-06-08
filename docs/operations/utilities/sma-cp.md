---
sidebar_label: 'sma_cp'
title: sma_cp — Lock-Safe File Copy
description: "Reference for the sma_cp utility, which safely copies a file to a lock-managed destination such as FAD or SMA_RM configuration files."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_cp — Lock-safe file copy

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`sma_cp` copies a file to a lock-managed destination, acquiring a write lock on the target before copying to prevent conflicts when another process is simultaneously reading the file.

Use `sma_cp` in place of the standard `cp` command when updating files that the agent reads at runtime — specifically the FAD control file and the SMA_RM configuration file — to avoid crashes caused by a read/write race condition.

- Use `sma_cp` when updating a FAD control file that is actively monitored by a running `sma_fad` process.
- Use `sma_cp` when updating `SMA_RM.conf` while the `sma_RM` process is running.
- Use the standard `cp` command for all other file copy operations. `sma_cp` is only needed for lock-managed agent configuration files.

## Syntax

```
sma_cp <from_file> <to_file>
```

| Argument | Description |
|---|---|
| `<from_file>` | Full path to the source file to copy from |
| `<to_file>` | Full path of the destination file to copy to. The destination must be a lock-managed file. |

## Behavior

1. `sma_cp` acquires a write lock (`F_WRLCK`) on the destination file.
2. If the lock is not available within 5 seconds, `sma_cp` exits with an error.
3. Once the lock is held, the source file is copied to the destination byte-by-byte.
4. The destination file is truncated to the source file size after copying.
5. The lock is released when the destination file is closed.

:::tip Example

The following command replaces an active FAD control file with an updated version:

```bash
sma_cp /tmp/control_new.xml $LSAM_ROOT/fad/$SMA_LSAM_INSTANCE/control/control.xml
```

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success — file copied successfully |
| `-1` | Error — destination stat failed, file open failed, lock acquisition timed out, truncate failed, or copy failed |

## Exception handling

**`sma_cp` returns `-1` with no file copied** — The write lock on the destination could not be acquired within 5 seconds. Another process is holding the lock. — Wait for the lock-holding process to release the file, then retry. If the condition persists, check that `sma_fad` or `sma_RM` is running normally.
