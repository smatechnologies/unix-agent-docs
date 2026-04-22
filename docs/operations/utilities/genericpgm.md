---
sidebar_label: 'genericpgm'
title: genericpgm
description: "Reference for the genericpgm utility, a dummy test program that sleeps for a configurable duration and exits with a specified exit code and signal disposition."
tags:
  - Reference
  - System Administrator
  - Agents
---

# genericpgm

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the genericpgm utility, a dummy test program that sleeps for a configurable duration and exits with a specified exit code and signal disposition.

The genericpgm program sleeps for the requested time (default 10 seconds) and then exits with the requested exit code (default zero [0]) and signal disposition (default zero [0]). Valid UNIX exit codes are restricted to the range -127 to 127.

- You are configuring or testing the agent and need a job that runs for a predictable duration and exits with a specific code, without requiring a real workload.
- You are using exit_codes to test Failure Criteria and need a controlled program whose exit code and sleep duration you can specify precisely.

## Syntax

```genericpgm [-e#] [-s#] [-t#]```

## Parameters

| Parameter | Required | Default | Description |
|---|---|---|---|
| `-e#` | Optional | `0` | Exit code the program returns on completion. Valid range: -127 to 127. |
| `-s#` | Optional | `0` | Signal disposition. |
| `-t#` | Optional | `10` | Sleep time in seconds before the program exits. |