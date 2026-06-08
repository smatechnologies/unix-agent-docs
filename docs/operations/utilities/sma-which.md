---
sidebar_label: 'sma_which'
title: sma_which — Locate Executable in PATH
description: "Reference for the sma_which utility, which searches the PATH environment variable to return the full path of a specified executable program."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_which — Locate executable in PATH

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`sma_which` searches the directories listed in the `PATH` environment variable to locate the full path of a specified executable, and prints the result to standard output.

Use `sma_which` in OpCon job scripts when you need to confirm the resolved path of a program before calling it, or to make scripts portable across machines where executables may be installed in different locations.

## Syntax

```
sma_which <program_name>
```

| Argument | Description |
|---|---|
| `<program_name>` | The name of the executable to locate. Can be a bare name (`bash`), a relative path (`./myscript`), or an absolute path (`/usr/bin/python3`). |

## Behavior

- If `<program_name>` is an absolute path, `sma_which` verifies that the file exists and returns the path directly.
- If `<program_name>` is a relative path (starts with `./`), `sma_which` resolves it relative to the current directory.
- Otherwise, `sma_which` searches each directory in the `PATH` environment variable in order and returns the first match found.
- The full path is printed to standard output.

:::tip Example

The following script uses `sma_which` to locate `python3` before calling it:

```bash
PYTHON=$(sma_which python3)
if [ $? -ne 0 ]; then
    echo "python3 not found in PATH"
    exit 1
fi
$PYTHON /data/scripts/process.py
```

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success — the executable was found; full path printed to stdout |
| `10` | The executable was not found in PATH or at the specified path |
