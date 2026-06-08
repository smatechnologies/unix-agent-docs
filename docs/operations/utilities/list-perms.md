---
sidebar_label: 'list_perms'
title: list_perms — Generate File Permissions Baseline
description: "Reference for the list_perms utility, which reads filenames from stdin and outputs a permissions baseline for use with compare_perms."
tags:
  - Reference
  - System Administrator
  - Agents
---

# list_perms — Generate file permissions baseline

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`list_perms` reads filenames from standard input and writes each file's permissions, group ID, user ID, and name to standard output in the four-line format required by [`compare_perms`](./compare-perms).

Use `list_perms` to capture a permissions baseline for the agent installation that you can later compare against using `compare_perms`.

## Syntax

```
list_perms < file_list
```

`list_perms` reads filenames from standard input, one per line. Pipe a file list to it — typically from `find`.

## Output format

For each input filename, `list_perms` writes four lines to standard output:

```
<octal_mode>
<gid>
<uid>
<filename>
```

Files that cannot be `stat`'d are silently skipped.

:::tip Example

Generate a baseline of all files in the current agent installation directory:

```bash
find . -name "*" | list_perms > /tmp/agent_baseline.txt
```

The resulting `agent_baseline.txt` can be used as the input to `compare_perms CHECK` or `compare_perms CORRECT`. Refer to [compare_perms](./compare-perms) for the full workflow.

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success |
