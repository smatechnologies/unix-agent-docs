---
sidebar_label: 'Embedded Script Jobs'
title: Embedded Script Jobs
description: "Reference for the Unix Agent Embedded Script job type, which executes an inline script defined directly in OpCon rather than a pre-existing file on the agent machine."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Embedded Script jobs

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
The Embedded Script job type executes an inline script defined directly in OpCon rather than referencing a pre-existing file on the agent machine.

With an Embedded Script job, the script content is stored inside the OpCon job definition and sent to the Unix Agent at run time. The agent writes the script to a temporary file and executes it through the system shell. This removes the need to pre-deploy script files to agent machines before scheduling jobs.

- Use an Embedded Script job when you want to manage the script in OpCon's central repository rather than maintaining separate copies on each agent machine.
- Use an Embedded Script job for short, self-contained scripts that do not depend on files or utilities that must be installed on the agent.
- Use a Run Program job instead when the script is large, when it already exists on the agent machine, or when it requires execution permissions or a specific interpreter path set on disk.

:::info Note

The Embedded Script job type was introduced in agent version 18.1. Support for defining environment variables on Embedded Script jobs was also added in version 18.1.

:::

## How it works

1. OpCon sends the job start request to the agent. The job action field (`FC 6012`) is set to `E`, identifying the job as an Embedded Script.
2. The agent receives the script content in the start image field of the job definition.
3. The agent constructs the script as a temporary file and passes it to the system shell for execution.
4. The agent monitors the resulting process, tracks its status through the standard tracking file mechanism, and reports completion and exit code to OpCon.

## Environment variables

The agent sets the following environment variables for all jobs, including Embedded Script jobs. Your script can read these variables to access OpCon job and schedule metadata at run time.

| Variable | Description |
|---|---|
| `SMA_SCHEDULE_DATE` | The OpCon schedule date for this job run (yyyymmdd format) |
| `SMA_SCHEDULE_NAME` | The name of the OpCon schedule containing this job |
| `SMA_SCHEDULE_FREQUENCY` | The frequency name under which this job is scheduled |
| `SMA_JOBNAME` | The OpCon job ID for this job run |
| `SMA_USER_SPECIFIED_JOBNAME` | The user-defined job name as entered in the OpCon job definition |
| `SMA_USER` | The user ID the job is running as |
| `SMA_STDOUT` | The full path of the STDOUT capture file for this job run, or `NONE` if STDOUT capture is not enabled |
| `SMA_STDERR` | The full path of the STDERR capture file for this job run, or `NONE` if STDERR capture is not enabled |
| `SMA_BINDIR` | The full path to the agent `bin/` directory, allowing the script to call agent utilities without hardcoding paths |
| `SMA_LSAM_INSTANCE` | The agent instance name |
| `SMA_XML_FILE` | The path to the job's XML parameter file used by JORS |
| `SAM_SOCKET` | The SAM socket number for this agent instance |
| `SMA_CONFIG_FILE` | The full path to the agent configuration file (`lsam.conf`) for this agent instance |

:::tip Example

The following embedded script uses `SMA_SCHEDULE_DATE` to construct a date-stamped filename and writes output to the captured STDOUT file:

```bash
#!/bin/bash
OUTPUT_FILE="/data/reports/daily_${SMA_SCHEDULE_DATE}.csv"
generate_report > "${OUTPUT_FILE}"
echo "Report written to ${OUTPUT_FILE}"
```

:::

## Encrypted arguments

Encrypted property values passed in the job definition are automatically decrypted by the agent before the script is executed. The script receives the plaintext value at run time. To use encrypted tokens, the agent installation must use an SSL-enabled tar file (the agent does not need TLS communication enabled — only the SSL libraries must be present).

:::info Note

Support for encrypted arguments in Embedded Script jobs was added in agent version 19.0.0.

:::

## Exit codes

Embedded Script jobs report the exit code returned by the shell when the script finishes. The standard Unix Agent exit code rules apply:

- Exit code `0` — Success
- Non-zero exit codes — Failure (the specific value is reported to OpCon and can be used in Failure Criteria rules)
- Exit codes must be in the range `-127` to `+127`. Values outside this range may be truncated by the operating system.

## Exception handling

**Script fails with "Too many arguments" (exit code 85)** — The script content exceeds the maximum number of argument tokens the agent can parse. — Simplify the script or move complex argument construction inside the script body rather than as separate tokens.

**Script fails with "Blank start image" (exit code 86)** — The script content field in the OpCon job definition is empty. — Verify that the script body is present in the OpCon job definition and that it was saved correctly before the job ran.

**Script runs but environment variables are not set** — Embedded Script jobs receive environment variables only when the agent is configured to load them. If `path_to_su` is set to `no`, the user's login profile is not loaded, and only the variables the agent injects directly (listed above) are available. — Use the `user_setup.ksh`/`.sh`/`.csh` setup scripts to inject additional environment variables for the run-as user. Refer to [Loading Environment Variables](../../configuration/loading-environment-variables).

**Encrypted token arrives as ciphertext, not plaintext** — The agent installation does not include SSL support. Encrypted tokens require the SSL libraries to be present on the agent machine. — Install the SSL-labeled agent tar file and ensure the SSL and Crypto libraries are in the system library search path. Refer to [Installation Requirements](../../installation/requirements).

## Glossary

**Embedded Script job** — A Unix Agent job type (job action code `E`) in which the script content is provided inside the OpCon job definition and executed by the agent at run time without requiring a pre-deployed script file on the agent machine.

**Start image** — The field in the OpCon job definition that holds the script content for an Embedded Script job, or the program path for a Run Program job.
