---
sidebar_label: 'Running multiple agents'
title: Running Multiple agents on One Machine
description: "Instructions for simultaneously running multiple Unix Agent instances on a single system, covering environment variable configuration and OpCon machine registration for each instance."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Running multiple agents on one machine

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Instructions for simultaneously running multiple Unix Agent instances on a single system, covering environment variable configuration and OpCon machine registration for each instance.

## When would you use it?

Run multiple agents on one machine when:

- You need to test a new agent release while the current production agent continues to process jobs on the same host.
- Different job workloads require separate configurations — for example, one instance with a small `max_number_of_jobs` and low `max_bandwidth` for general users, and a second instance with full system utilization reserved for critical jobs.
- You want to grant OpCon users access to a specific workload tier without granting access to all jobs on the host, by restricting access to a named machine definition in OpCon.

## How to implement it

To run multiple agents on one machine, complete the following steps:

- [Set up environment variables](#environmental-variables) — assign a unique `$SAM_SOCKET` and `$SMA_LSAM_INSTANCE` to each agent instance, and confirm `$LSAM_ROOT` points to the correct installation directory.
- [Register each instance in OpCon central components](#opcon-central-components) — add a separate machine definition for each agent instance and ensure all machine names resolve to the host's IP address in DNS or the OpCon server's hosts file.

## Scenarios

Multiple agents may be simultaneously run on a single system. It is possible to run different versions of the agent (Scenario 1) as well as the same versions with different configurations (Scenario 2). An example of the first scenario would be testing a new release while continuing to operate the most current release. An example of the second scenario is running agents with differing SMA File Transfer (SMAFT) max_bandwidth parameters.

## Environmental variables

Environment variables ```$LSAM_ROOT```, ```$SAM_SOCKET```, and ```$SMA_LSAM_INSTANCE``` define each instance of an LSAM. ```$LSAM_ROOT``` specifies the root location of the executable, configuration, and data files. ```$SAM_SOCKET``` identifies the socket number over which the LSAM communicates with the SAM. Since the socket used by SAM to communicate with an LSAM must be unique to a host system, no two running LSAMs can share the same ```$SAM_SOCKET```. ```$SMA_LSAM_INSTANCE``` identifies the location within ```$LSAM_ROOT``` of a particular instance of the agent's configuration and data files.

| Variable | Purpose | Example value |
|---|---|---|
| `$LSAM_ROOT` | Root location of the agent's executable, configuration, and data files | `/usr/local/lsam` |
| `$SAM_SOCKET` | Socket number over which the agent communicates with the SAM; must be unique per host | `3100` |
| `$SMA_LSAM_INSTANCE` | Identifies the instance-specific configuration and data directory within `$LSAM_ROOT` | `general` |
| `$SMA_BINDIR` | Points to the `bin/` directory containing agent utilities; lets jobs resolve the correct agent version | `/usr/local/lsam/bin` |

If two agents share the same ```$LSAM_ROOT```, they run the same code. To operate multiple versions of the LSAM (Scenario 1), place the LSAMs in separate directories and set the respective ```$LSAM_ROOT``` variable to the appropriate path (e.g., ```/usr/local/prod-lsam/``` and ```/usr/local/dev-lsam/```). To implement multiple configurations of a single version of the LSAM (Scenario 2), run the "install_lsam" script, specifying the appropriate ```$SAM_SOCKET``` and ```$SMA_LSAM_INSTANCE```, e.g., "```install_lsam `pwd` 3100 general```" and "```install_lsam `pwd` 3200 critical```".

:::tip Example

Assume that one instance of the agent operating on host "unix_system" is for general users (configured with a small max_number_of_jobs and small max_bandwidth). A second instance of the agent is configured to allow full system utilization for critical jobs.

The OpCon machine names could be named "unix_general" and "unix_critical". Access to "unix_critical" is restricted to the OpCon users with the correct privileges. Both "unix_general" and "unix_critical" would resolve to the IP address of "unix_system". A job available to both "unix_general" and "unix_critical" could query environment variable ```$SMA_LSAM_INSTANCE``` to determine on which LSAM instance it is currently running (Is the value of ```$SMA_LSAM_INSTANCE``` "general" or "critical"?) and act accordingly.

:::

The environment variable ```$SMA_BINDIR``` is defined within each instance of an agent to point to the "bin/" directory containing the utilities file_check, maintain_ofiles, sma_ppscript, and sma_status. This allows user jobs, running these utilities, to get the correct agent version under which the job is running.

## OpCon central components

From the point of view of the OpCon central components, multiple instances of an agent are different machines. Each instance of an agent must be identified in the Enterprise Manager on the Machines Screen (Navigation path: Administration>Machines). This requires all machine names associated with the same IP address to be listed in the DNS or to be in the "hosts" file on the OpCon server. For more information, refer to the [Machines](https://help.smatechnologies.com/opcon/core/objects/machines) section in the Concepts online help.

## Exception handling

**`EADDRINUSE - Address already in use` when starting an agent instance** — The socket number assigned to `$SAM_SOCKET` is already bound by another process on the system. This can happen when two agent instances are configured with the same `$SAM_SOCKET` value, or when another service on the host has claimed that port. — Identify the process holding the socket (for example, using `netstat -an | grep <SAM_Socket>`). Either resolve the conflict or reinstall the agent instance with a different `$SAM_SOCKET` (for example, `5100` instead of the default `3100`). Verify that no two running agent instances on the same host share the same `$SAM_SOCKET` value.
