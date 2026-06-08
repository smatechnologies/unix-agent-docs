---
sidebar_label: 'chgexec'
title: chgexec — Set Agent Binary Permissions
description: "Reference for the chgexec utility, which sets the correct ownership and permissions on Unix Agent binary executables as part of installation or maintenance."
tags:
  - Reference
  - System Administrator
  - Agents
---

# chgexec — Set agent binary permissions

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
`chgexec` sets the correct ownership (root) and permissions on the Unix Agent's binary executables and related files using a hardcoded list of programs and their required permission modes.

`chgexec` is called by the agent installation scripts. You do not normally run it directly. It is documented here to support situations where agent file permissions need to be restored after a system change or a failed installation.

## Syntax

```
chgexec
```

No arguments. `chgexec` applies a hardcoded set of permission and ownership rules to approximately 44 agent programs and files.

## Behavior

- Sets the owner of each file to root (uid 0, gid 0).
- Applies the required permission mode for each file. Common modes include:
  - `04700` (setuid, rwx for owner only) — privileged agent binaries that require setuid to run as root
  - `00755` (rwx owner, rx group and other) — general agent executables
  - `00644` (rw owner, r group and other) — configuration files
  - `0555` (rx for all, no write) — scripts
- Continues processing remaining files even if a `chmod` or `chown` operation fails on one file; errors are reported but do not abort the run.

:::info Note

`chgexec` requires that the process running it can acquire root privileges (via setuid or by running as root). It reads the agent configuration file to locate the installation directory.

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Completed — all permission changes applied (individual file errors are reported but do not change the exit code) |
