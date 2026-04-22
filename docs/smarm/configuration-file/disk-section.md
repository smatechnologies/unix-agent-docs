---
title: DISK Section
description: "Reference for the SMA_RM DISK section, which specifies disk monitoring parameters including name, mount point, usage thresholds, alarm levels, and event variables."
tags:
  - Reference
  - System Administrator
  - Agents
---

# DISK Section

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the SMA_RM DISK section, which specifies disk monitoring parameters including name, mount point, usage thresholds, alarm levels, and event variables.

- Configure a `<disk>` section when you need SMA_RM to send an OpCon event or run a local action when a specific disk's usage meets or exceeds a defined percentage threshold — for example, to trigger a cleanup job before a file system fills up.
- Configure a `<disk>` section with a MIN threshold when you need to detect a disk that has dropped below a minimum expected usage level, such as monitoring a disk that should always contain data.
- Configure multiple `<disk>` sections for the same mount point with ascending `<alarm_level>` values when you need graduated responses — for example, sending a cleanup job at 80 percent usage and an operator console alert at 90 percent.
- Configure a `<disk>` section with a `<window>` entity when disk monitoring should be active only during specific hours of the day, such as during business hours or during batch processing windows.

Disk monitoring is specified via one or more ```<disk>``` sections, as shown in the following template:

```

<disk>

<alarm_level>____</alarm_level>

<window>____</window>

<name>____</name>

<mount_point>____</mount_point>

<usage>[ MIN | MAX ]____</usage>

<log>NONE | SCANS | EVENTS</log>

<alarm>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</alarm>

<normal>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</normal>

</disk>

``` 

All entities within ```<disk>``` are optional except for ```<usage>```. Duplicate entities constitute an error.

```<alarm_level>``` is discussed below in "Multiple Alarm Levels".

```<name> ```specifies the name of the disk(s) as displayed by a UNIX 'df' command. ```<mount_point>``` likewise specifies the mount point for the disk(s) as displayed by a 'df' command. Both specify the disk(s) to monitor and are combined using an implied AND conjunction, i.e., a disk must match both to be processed. For either, you can use an asterisk ('\*') as a wildcard character at either the beginning or at the end: at the end it means "begins with", at the beginning it means "ends with", and at both ends means "contains". 

A lone '*' means "matches all", as does an unspecified ```<name>``` or ```<mount_point>```. The contents of the ```<name>``` and ```<mount_point> ```entities are case-sensitive. If neither is specified, then this ```<disk>``` section applies to all disks output by a 'df' command. ```<window>``` defines when the disk(s) will be monitored.

```<usage>``` is the integer percent of total disk space in use which constitutes an alarm. MIN or MAX may be included with the value to set the type of the value, which has a default type of MAX. If MIN or MAX is specified, at least one space must appear between the MIN or MAX and the value. 

```<log>``` specifies what, if any, values for disk usage will be logged. ```<alarm>``` defines what is to occur when disk usage goes into alarm, and will be discussed later under "Exception Handling". Likewise with ```<normal>``` which defines what is to occur when disk usage returns to a normal status. The event variables available within the ```<alarm>``` and ```<normal>``` specifications are as follows:

* ```%NAME% ```= the name of the disk.
* ```%MOUNT_POINT%``` = the mount point for the disk.
* ```%USAGE%``` = the percent of space in use.

## Examples

The following example monitors the `/usr` mount point and sends a console event when usage exceeds 80 percent. When usage returns to normal, a separate console event is sent. The `<log>` entity is set to EVENTS so that the percent-used value is logged only when the alarm status changes.

```

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

```