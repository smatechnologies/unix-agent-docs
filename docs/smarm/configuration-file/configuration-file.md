---
title: Configuration File
description: "The SMA_RM configuration file defines the structure and rules for disk, process, and user-defined monitoring sections, including window, log, and comment syntax."
tags:
  - Conceptual
  - Reference
  - System Administrator
  - Agents
---

# Configuration File

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
The SMA_RM configuration file defines the structure and rules for disk, process, and user-defined monitoring sections, including window, log, and comment syntax.

- Edit the configuration file to add, modify, or remove `<disk>`, `<process>`, or `<user_defined>` monitoring sections when your organization's monitoring requirements change — for example, when new disks are mounted, new processes must be tracked, or user-defined monitors are added.
- Edit the configuration file to change global parameters in the `<config>` section, such as the `<scan_interval>`, `<C_alarm>`, `<T_alarm>`, or `<user_defined_monitor>` timeout settings, when the current values no longer reflect your monitoring needs.
- Edit the configuration file to replace its contents with an empty `<config></config>` block when you need to temporarily disable SMA_RM without stopping the agent, then overwrite it with the full configuration when you are ready to resume monitoring.

- SMA_RM starts automatically at agent startup only if the configuration file is present and readable; configuring the file is required to activate disk, process, and user-defined monitoring without restarting the agent.
- SMA_RM monitors the configuration file for changes and re-reads it when a change to its modification time is detected, allowing monitoring configuration to be updated on the fly without an agent restart; if the new file contains errors, SMA_RM logs the error and continues with the previous valid configuration.
- The order in which sections appear in the configuration file controls the order in which they are processed during each scan cycle, which is significant for process sections — for example, `<process>` sections that ignore certain processes must appear before sections that would otherwise apply to those processes.

The configuration file consists of one ```<config>``` section, followed in any order by any number of optional ```<disk>```, ```<process>```, or <user_defined> sections, to be discussed in that order. Although ```<disk>```,``` <process>```, or ```<user_defined>``` sections may appear in any order, the order in which they appear is significant in that their order within the file is also the order in which they are processed during each scan. 

For instance, a ```<process>``` section which specifies processes to be ignored should appear prior to ```<process>``` sections which would otherwise apply to the to-be-ignored processes. There is no interaction between ```<disk>```, ```<process>```, or ```<user_defined>``` sections.

As was previously mentioned, SMA_RM will monitor the config file for changes, and re-read it if a change to the modification time is detected. The changes are not taken to be incremental; all data from the previous version of the config file is forgotten when the new file is successfully read. If the new config file contains errors, an indication of the error will be written to the agent log and error files. 

If an error-free version has previously been read during this execution of SMA_RM, monitoring is continued with the previous configuration. 

The following provides an example of what will appear in the agent log file if SMA_RM detects an error in the [new] config file:

```

[Mon Oct 15 15:38:22 2007]

[sma_RM] Re-reading Config File (550)

[Mon Oct 15 15:38:22 2007]

[sma_RM] Line 2 - Invalid value for <scan_interval> (560)

[Mon Oct 15 15:38:22 2007]

[sma_RM] Continuing with old Config File data (611)

```

It should be noted that if the agent were restarted at this point, there would be no 'old' config file, since that data resides only within SMA_RM's internal, volatile memory. Upon agent restart, SMA_RM will attempt to read the 'new' config file, and report it as unusable.

The file is free-format, that is, you can use spaces, tabs, and line-feeds as desired to separate syntactical elements such as entity names, angle brackets, etc. It should be noted that the closing "/entity" is considered to be a single syntactical element, and so no spaces/tabs/line-feeds may appear between the '/' and the name, i.e., "< /window >" is acceptable, but "< / window >" is not.

Except as noted, letter case is insignificant. That is, "```<user_defined>```" and "```<UseR_deFIned>```" are equivalent, as are ```MUST_RUN``` and ```must_run```.

 
Comments can be included by beginning a line with a '#', as in:

```

# This line is a comment and will be ignored by SMA_RM

``` 

Common to all sections are ```<window>``` and ```<log>``` entities. A window is defined by the syntax "```<window>start-end</window>```". For example:

```<window>0600-1800</window>```

Start and end are specified in 4-digit 'hhmm' (hours and minutes) format. Leading zeros will be assumed if less than 4 digits are specified. The time is assumed to include seconds 00 to 59. When start is less than end, the window is inclusive, and applies from start thru end. 

If start is greater than end, the window is exclusive, and applies from 0000 to start, and from end to 2359, e.g., 1800-0559 would apply from midnight to (but not including) 6AM and again from 6PM until midnight. 

Start = end is an error, as are numbers outside the range 0000‑2359 and 'mm' digits greater than 59. The default window is 0000‑2359. 

```<log>``` specifies when, if at all, scanned values are to be entered into the SMA_RM log file. Three options are available: NONE, SCANS, and EVENTS. NONE, which is the default, results in no logging. SCANS results in values getting logged with each scan cycle. EVENTS results in values getting logged only when the scanned resource goes into or out of alarm. 

The particular values which may be logged are described below under the details for ```<config>```, ```<disk>```, ```<process>```, and ```<user_defined>```. SMA Technologies recommends that logging of scanned values be used sparingly because of the large amounts of disk space used – which can easily reach megabytes per hour. Normally, only status-change logging of values, i.e., "```<log>EVENTS</log>```", should be specified.

:::caution 

SMA Technologies recommends against more than sparing use of "```<log>SCANS</log>```" because logging values at every scan cycle can use tremendous amounts of disk space. If values are to be logged, the normal setting would be "```<log>EVENTS</log>```".

:::

Only one timestamp is written to the SMA_RM log file per scan cycle. Every time a value is to be logged, a check is made to see if the timestamp has yet been written, and it is first written if necessary. Thus, all text which appears between two timestamps was produced during and as a result of the scan cycle associated with the earlier timestamp.

## Examples

The following example shows a minimal but functional SMA_RM configuration file containing one `<config>` section, one `<disk>` section, and one `<process>` section. Comments are introduced with `#`. The `<config>` section sets a 30-second scan interval. The `<disk>` section monitors the `/usr` mount point and sends a console event when usage exceeds 80 percent. The `<process>` section alarms if no process with `data` in its name is running.

```

# SMA_RM configuration file

<config>

<scan_interval>30</scan_interval>

<log_events>YES</log_events>

</config>

<disk>

<mount_point>/usr</mount_point>

<usage>80</usage>

<log>EVENTS</log>

<alarm>

<event>$CONSOLE:DISPLAY,<DISK [%MOUNT_POINT%] IS %USAGE%%% FULL!></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<DISK [%MOUNT_POINT%] USAGE BACK TO %USAGE%%%></event>

</normal>

</disk>

<process>

<condition>MUST_RUN</condition>

<name>*data*</name>

<exist_alarm>

<event>$CONSOLE:DISPLAY,<No *data* process running></event>

</exist_alarm>

<exist_clear>

<event>$CONSOLE:DISPLAY,<*data* process restored></event>

</exist_clear>

</process>

```

## Glossary

**`<window>` entity** — A configuration element that restricts a monitoring section to a specific daily time range, specified in `hhmm-hhmm` format. When the start value is less than the end value the window is inclusive; when the start value is greater than the end value the window is exclusive, applying from midnight to the start time and from the end time to midnight. The default window is `0000-2359` (all day).

**`<log>` entity** — A configuration element that controls when scanned values are written to the SMA_RM log file. Three options are available: `NONE` (default, no logging), `SCANS` (log every scan cycle), and `EVENTS` (log only when the resource transitions into or out of alarm). SMA Technologies recommends `EVENTS` for normal use because `SCANS` can consume large amounts of disk space.