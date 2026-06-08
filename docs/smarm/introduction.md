---
title: SMA Resource Monitor overview
description: "SMA_RM monitors system resources — including disk space, processes, and user-defined metrics — and triggers OpCon events or local actions when alarm conditions are detected."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# Introduction

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
SMA_RM monitors system resources — including disk space, processes, and user-defined metrics — and triggers OpCon events or local actions when alarm conditions are detected.

The SMA Resource Monitor (SMA_RM) monitors system resources and generates OpCon events and/or initiates local processing actions when a resource goes into or out of alarm based on user-defined conditions. A daily log records scanned values and alarm transitions. SMA_RM starts automatically at agent startup when an `SMA_RM.conf` configuration file is present in the agent's configuration directory.

:::info Note

SMA_RM.conf is located in the same directory as the agent configuration file `lsam.conf`. Changes to `SMA_RM.conf` take effect at the next scan cycle without restarting the agent. To force SMA_RM to re-read an unchanged configuration file, `touch` the file.

:::

## Log file

SMA_RM writes a daily log file to the agent's log directory under the `SMA_RM/` subdirectory — for example, `/usr/local/lsam/log/3100/SMA_RM/`. The log file is named `yyyymmdd.log`. A new log file is created at the start of each day. To prevent excessive disk usage, delete old log files using the [maintain_ofiles](../operations/utilities/maintain-ofiles) utility.

## Disk monitoring

Disk monitoring uses the standard UNIX `df` command. SMA_RM monitors either all disks reported by `df` or a user-specified set. Disks can be identified by device name (for example, `/dev/disk/c0s30t1`) or mount point (for example, `/usr`).

For each monitored disk, you specify a percent-used threshold. The boundary type defaults to MAX, meaning an alarm condition exists when the scanned value meets or exceeds the threshold. You can set the boundary type to MIN, where an alarm condition exists when the scanned value is not greater than the threshold.

Event strings for disk monitors can include event variables for the disk's name, mount point, and percent used. SMA_RM substitutes the current scanned values when forwarding the event to the SAM.

## Process monitoring

Process monitoring uses the standard UNIX `ps` command. Capabilities include:

- Checking for the existence or non-existence of a process (MUST_RUN / MUST_NOT_RUN)
- Detecting CPU-hog processes that exceed a configurable CPU usage threshold
- Alarming when the total number of processes on the system exceeds a defined limit
- Alarming when the percentage of CPU-hog processes on the system exceeds a limit (in increments of 10 percent)

Processes can be identified by name and/or UID, with support for limited wildcards. You can also specify processes to ignore when computing total process counts. Process-specific event variables are available for use in event strings forwarded to the SAM.

## User-defined monitors

User-defined monitors are scripts or programs you write and configure SMA_RM to invoke during each scan cycle. Each script performs one scan of a custom resource and returns the normal/alarm status, along with zero or more values to be logged. Data gathered by the script can be included in events forwarded to the SAM via event variables. For configuration details, refer to [User-defined section](./configuration-file/user-defined-section).

## Time windows and scan interval

SMA_RM supports daily time windows that restrict monitoring to specific hours — for example, from `0800` to `1800`. Exclusive windows are also supported, where monitoring is active outside the specified range (for example, from midnight to `0759` and from `1801` to midnight). Different windows can be applied to individual resources independently.

The scan interval defaults to one second and can be widened in increments of one second using the `<scan_interval>` configuration entity. The interval is measured from the end of one scan cycle to the start of the next, so the actual number of scans per unit of time depends on how long each scan cycle takes to complete.

- Use SMA Resource Monitor to monitor disk space and trigger an OpCon event or local action — such as a cleanup job or an operator console alert — when usage meets or exceeds a defined threshold.
- Use SMA Resource Monitor to verify that required processes are running (MUST_RUN) or that prohibited processes are not running (MUST_NOT_RUN).
- Use SMA Resource Monitor to detect CPU-hog processes and generate escalating events using multiple alarm levels for the same resource.
- Use SMA Resource Monitor to monitor custom resources — such as files in a directory, records in a database, or logged-in users — by configuring user-defined monitors that invoke your own scripts during each scan cycle.
- Use SMA Resource Monitor when monitoring should be restricted to specific daily time windows or to periods outside a specified time range.
- The log file records scanned values and alarm transitions with per-day rotation, providing an audit trail of resource behavior.

## Examples

Disk usage on the `/usr` mount point must not exceed 80 percent during business hours. An SMA_RM configuration file is created with a `<disk>` section that monitors `/usr`, sets `<usage>` to `80`, and restricts the monitoring window to `0800-1800`. When a scan cycle detects that `/usr` usage has reached or exceeded 80 percent, SMA_RM sends the event `$CONSOLE:DISPLAY,<DISK [/usr] IS 80% FULL!>` to SAM. When usage drops back below the threshold, SMA_RM sends a normal-state event. Because `<log>EVENTS</log>` is set, the transition is recorded in the daily log file in the agent's `SMA_RM/` log sub-directory.

## Glossary

**SMA Resource Monitor (SMA_RM)** — A component of the Unix Agent that monitors system resources and generates OpCon events and/or initiates local processing actions when a resource goes into or out of alarm per user-defined conditions.

**Scan interval** — The number of seconds SMA_RM waits between the end of one scan cycle and the start of the next. The minimum and default value is one second, and it can be widened in increments of one second using the `<scan_interval>` entity in the configuration file.

**Alarm level** — A positive integer assigned to a monitoring section that enables multiple sections referencing the same resource to generate events in a severity-based hierarchy, with higher values indicating more severe conditions. When a resource is in alarm at a given level, sections defined at lower levels are skipped for that resource during the current scan cycle.

**Alarm group** — A non-negative integer assigned to user-defined monitor sections to indicate to SMA_RM that multiple `<user_defined>` sections monitor the same resource, enabling multi-level alarm processing for user-defined monitors in the same way alarm levels work for disk and process monitors.

**Threshold** — The boundary value specified for a disk or process monitor (for example, the integer percent of disk space in use defined in `<usage>`) at or beyond which SMA_RM considers the resource to be in an alarm condition. The boundary type defaults to MAX (alarm if scanned value meets or exceeds the value) but can be set to MIN (alarm if scanned value is not greater than the value).

**Window** — A daily time range, specified in `hhmm-hhmm` format, during which monitoring for a resource is active. When the start time is less than the end time the window is inclusive; when the start time is greater than the end time the window is exclusive, applying from midnight to the start time and from the end time to midnight.
