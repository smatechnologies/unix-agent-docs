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

## Examples

:::tip Example

The following example runs genericpgm for 5 seconds and exits with code 1 to verify an OpCon job's Failure Criteria threshold:

```
genericpgm -t5 -e1
```

**Outcome**: The program sleeps for 5 seconds, then exits with code 1. Use this with the `exit_codes` utility to confirm that OpCon reports the job as Failed when the Failure Criteria threshold is set to flag non-zero exit codes.

:::

## Glossary

**exit code** — A numeric value (in the range -127 to 127) returned by the program when it exits. The Unix Agent reads this value to determine job success or failure.

**signal disposition** — A numeric value specifying whether the program simulates termination by a Unix signal. A value of 0 means the program exits normally without signal termination.

**sleep time** — The number of seconds the program waits before exiting. Controls how long the simulated job appears to run.