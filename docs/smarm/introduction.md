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

The SMA Resource Monitor (SMA_RM) allows for monitoring of system resources and generation of OpCon events and/or local processing actions as a resource is determined to have gone into or out of alarm per user-defined conditions. A log file is also kept in which data for monitored resources can be logged with each scanning cycle or as the determined alarm/normal status changes. Events sent to SAM and local processing actions initiated as a result of monitored conditions may also be logged. The log file is stored in the agent's log directory within sub-directory 'SMA_RM/', e.g., in "/usr/local/lsam/log/3100/SMA_RM/". The log file is named "yyyymmdd.log", where 'yyyymmdd' is the 4-digit year, 2-digit month, and 2-digit day-of-month of the current date, e.g., "20161005.log". At the beginning of every new day (if SMA_RM is in operation), the current log file will be closed and a new one, bearing the filename for the new date, will be opened. If a log file for the current day already exists when SMA_RM begins operation, data will be appended to it. To keep disk usage by log files from becoming excessive, old log files can be deleted via the agent utility 'maintain_ofiles' (refer to [maintain_ofiles](../operations/utilities/maintain-ofiles)).

The two built-in monitoring capabilities of SMA_RM are disk space monitoring and process monitoring. SMA_RM also includes "user-defined monitors", a flexible mechanism for users to define additional resources to be monitored, from the number of files within some directory, to the number of records in some database, to the number of logged-in users. For disks and processes, specified boundary values can be either a maximum, which is the default and indicates that the scanned value represents an alarm condition if it meets or exceeds the boundary value, or the specified boundary value may be a minimum, which means that an alarm condition exists if the scanned value is not greater than the boundary value. For user-defined monitors, the boundary values and comparison operator with the scanned value is internal to you-defined monitor and not directly-addressable within SMA_RM.

SMA_RM will automatically be started at agent-startup if an SMA_RM configuration file is detected. It is named "SMA_RM.conf" and is in the agent's configuration directory (same directory as the agent configuration file "lsam.conf"). Once SMA_RM has begun execution, users may make changes on-the-fly by simply updating the configuration file, and they will be incorporated at its next scheduled scan cycle. (If something external to SMA_RM needs changing to enable SMA_RM to run properly, e.g., permissions on a user-defined start image changed to allow it to run, then SMA_RM can be prompted to re-try the existing Config File by 'touching' it.) At agent start-up, all resources are assumed to be in the normal state, and if not, this will be detected in the minimum number of scans required to detect a normal-to-alarm transition. SMA_RM allows monitoring to occur within daily time windows, e.g., from 0800-1800. SMA_RM also allows for definition of "exclusive" windows, e.g., monitoring is to occur while not in the period 0800-1800 (i.e., monitor from midnight to 0759 and from 1801 to midnight). Differing windows can be applied to the monitoring of individual resources.

The minimum, and default, scan interval will be one second, and can be widened in increments of one second. When an alarm/normal transition occurs, user-defined events can be sent to SAM, e.g., ```"$CONSOLE:DISPLAY,<DISK [/usr] IS 80% FULL!>"```. It should be noted that the 1-second timer is an interval time, not an alarm timer. That is, once processing for the current scan cycle is completed, SMA_RM will sleep for the specified number of between-scan seconds before starting the next scan cycle. Also, processing time required to complete a scan cycle is not considered. It is thus quite conceivable that on a one-second scan cycle, less scans than the number of elapsed seconds will occur from time A to time B.

Disk monitoring is based on use of the standard UNIX 'df' command, and is either performed on all disks which appear in its output or on a user-specified set of disks. Users may specify disks by either their name or their mount-point on the system, e.g., name = "/dev/disk/c0s30t1", mount-point = "/usr". Users must also specify the percent used which constitutes an alarm condition for the specified disk(s). Within events to be sent to SAM, users can use event variables for the disk's name, mount-point, and percent used, and SMA_RM will replace the event variables with the scanned data.

Process monitoring uses output from the standard UNIX 'ps' command, and capabilities include simple checking for existence or non-existence of processes as well as checking for processes which are using an inordinate amount of CPU time (i.e., they are CPU-hogs). Alarm conditions can also be defined for exceeding a total number of processes on the system as well as for exceeding a percentage (in increments of 10 percent) of the total processes on the system which are CPU-hogs. Users may also specify that certain processes be ignored except in determining the total number of processes on the system. Processes can be identified, with use of limited wildcards, by process name and/or UID. Process-specific event variables are available for use in events to be sent to SAM.

User-defined monitors are user-written scripts or programs to be invoked by SMA_RM during each scan cycle to do whatever the scan requires to effect one scan of some resource and to return the normal/alarm status of the resource along with zero or more values which may be logged in the SMA_RM log file. Formatting requirements will be explained later in section "The ```<user_defined>``` Section". Data gathered by the script/program can be included via event variables in events to be sent to SAM.

- Use SMA Resource Monitor when you need to monitor disk space and trigger an OpCon event or local action — such as a cleanup job or an operator console alert — when disk usage meets or exceeds a defined percentage threshold.
- Use SMA Resource Monitor when you need to verify that required processes are running (MUST_RUN) or that prohibited processes are not running (MUST_NOT_RUN), and send an event to SAM when the condition is violated.
- Use SMA Resource Monitor when you need to detect CPU-hog processes — processes consuming an inordinate amount of CPU time — and generate escalating events as the condition worsens, using multiple alarm levels for the same resource.
- Use SMA Resource Monitor when you need to monitor custom resources beyond disk and processes — such as the number of files in a directory, the number of records in a database, or the number of logged-in users — by configuring user-defined monitors that invoke your own scripts or programs during each scan cycle.
- Use SMA Resource Monitor when you need to restrict monitoring to specific daily time windows, or to define exclusive windows so that monitoring occurs only outside a specified time period.

- SMA_RM monitors disk space, processes, and user-defined metrics continuously during each scan cycle, sending OpCon events or running local actions the moment a resource crosses a defined threshold — without requiring a separate scheduled job for each check.
- Daily time windows allow monitoring to be active only during business hours or only outside them, so alarm conditions are reported in the context where they are actionable rather than generating noise at all hours.
- User-defined monitors extend built-in disk and process monitoring to any resource that a custom script or program can measure, including the number of files in a directory, records in a database, or logged-in users, using the same alarm/normal event model as built-in monitors.
- The log file records scanned values and alarm transitions with per-day rotation, giving administrators an audit trail of resource behavior that can be reviewed after an incident.

## Examples

Disk usage on the `/usr` mount point must not exceed 80 percent during business hours. An SMA_RM configuration file is created with a `<disk>` section that monitors `/usr`, sets `<usage>` to `80`, and restricts the monitoring window to `0800-1800`. When a scan cycle detects that `/usr` usage has reached or exceeded 80 percent, SMA_RM sends the event `$CONSOLE:DISPLAY,<DISK [/usr] IS 80% FULL!>` to SAM. When usage drops back below the threshold, SMA_RM sends a normal-state event. Because `<log>EVENTS</log>` is set, the transition is recorded in the daily log file in the agent's `SMA_RM/` log sub-directory.

## Glossary

**SMA Resource Monitor (SMA_RM)** — A component of the Unix Agent that monitors system resources and generates OpCon events and/or initiates local processing actions when a resource goes into or out of alarm per user-defined conditions.

**Scan interval** — The number of seconds SMA_RM waits between the end of one scan cycle and the start of the next. The minimum and default value is one second, and it can be widened in increments of one second using the `<scan_interval>` entity in the configuration file.

**Alarm level** — A positive integer assigned to a monitoring section that enables multiple sections referencing the same resource to generate events in a severity-based hierarchy, with higher values indicating more severe conditions. When a resource is in alarm at a given level, sections defined at lower levels are skipped for that resource during the current scan cycle.

**Alarm group** — A non-negative integer assigned to user-defined monitor sections to indicate to SMA_RM that multiple `<user_defined>` sections monitor the same resource, enabling multi-level alarm processing for user-defined monitors in the same way alarm levels work for disk and process monitors.

**Threshold** — The boundary value specified for a disk or process monitor (for example, the integer percent of disk space in use defined in `<usage>`) at or beyond which SMA_RM considers the resource to be in an alarm condition. The boundary type defaults to MAX (alarm if scanned value meets or exceeds the value) but can be set to MIN (alarm if scanned value is not greater than the value).

**Window** — A daily time range, specified in `hhmm-hhmm` format, during which monitoring for a resource is active. When the start time is less than the end time the window is inclusive; when the start time is greater than the end time the window is exclusive, applying from midnight to the start time and from the end time to midnight.
