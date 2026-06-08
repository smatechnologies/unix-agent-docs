---
sidebar_label: 'sma_delete_file'
title: sma_delete_file — Permission-Aware File Deletion
description: "Reference for the sma_delete_file utility, which changes file ownership before deleting to allow deletion of files owned by a different user."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_delete_file — Permission-aware file deletion

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`sma_delete_file` switches to a specified user/group identity before deleting a file, enabling deletion of files owned by a different user without requiring root to run `rm` directly.

Use `sma_delete_file` from an OpCon job when the file to delete is owned by a user other than the job's run-as user, and when standard file deletion tools do not have the required permissions.

## Syntax

```
sma_delete_file <gid>/<uid> <file_to_delete>
```

| Argument | Description |
|---|---|
| `<gid>/<uid>` | The group ID and user ID to switch to before attempting deletion, separated by `/`. Accepts either numeric IDs (for example, `0/500`) or names (for example, `dba/oracle`). |
| `<file_to_delete>` | The full path of the file to delete. |

## Behavior

1. `sma_delete_file` looks up the specified user and group identities.
2. The process switches to the specified user/group.
3. The file's permissions are set to full access (read/write/execute for all) to ensure deletion can proceed regardless of the original permissions.
4. The file is deleted.

:::info Note

If the user lookup fails but the group is valid, `sma_delete_file` logs a warning and continues with the deletion attempt using the available identity. If neither the user nor the group is found, the deletion attempt still proceeds.

:::

:::tip Example

The following command deletes a file owned by user `oracle` (uid 500, gid 501):

```bash
sma_delete_file 501/500 /data/incoming/processed_file.dat
```

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success — the file was deleted |
| `-1` | The file does not exist, or the `unlink` call failed |
| `10` | Invalid argument count, user/group change failed, or other fatal error |
