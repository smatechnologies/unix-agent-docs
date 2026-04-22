---
title: Features
description: "Reference of all file monitoring capabilities supported by the SMA File Activity Detection Daemon, including file creation, deletion, size change, modification detection, and configurable event timing."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Features

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference of all file monitoring capabilities supported by the SMA File Activity Detection Daemon, including file creation, deletion, size change, modification detection, and configurable event timing.

The SMA File Activity Detection Daemon supports the following features.

- Use file name recognition with wildcards when a directory receives files with variable names that share a common pattern — for example, monitoring `/usr/local/test/*.txt` for any new text files rather than a single known filename.
- Use file creation detection when downstream processing must begin as soon as an expected file arrives — the SMA FAD treats file existence the same as file creation, so the event fires whether the file is brand new or already present.
- Use file deletion detection when an alert or job must trigger upon the removal of a required file — the SMA FAD treats file absence the same as file deletion.
- Use change in file size detection when you need to react to any growth or shrinkage of a monitored file, and events should fire as soon as the file size changes.
- Use file modification detection when you need to detect that a file's content has changed independently of its size — the SMA FAD processes modification events separately from size change events.
- Use time-window support when external events must only be forwarded to the SAM during a defined period — for example, restricting monitoring to business hours using the `<window>` Control File element.
- Use the configurable sleep interval when multiple events must fire for the same file condition and you need a pause between them to allow the SAM to process them in the intended order.
- Use the configurable control file read interval when the default one-second polling rate is too frequent or too slow for your environment.

## SMA File Activity Daemon features and descriptions

### Recognition of file names

* The SMA FAD recognizes individual file names and masks containing wildcards.
* The SMA FAD allows overlapping file names or wildcard specifications to support processing of different events.
* Refer to the ```<filemask>``` Control File element.

### Recognition of file creation

* The SMA FAD checks for file creation.
* The SMA FAD treats file existence the same as file creation.
* Refer to the ```<condition>``` Control File element.

### Recognition of file deletion

* The SMA FAD checks for file deletion.
* The SMA FAD treats file absence the same as file deletion.
* Refer to the ```<condition>``` Control File element.

### Recognition of change in file size

* The SMA FAD checks for any changes in the file size (i.e., increase or decrease) and initiates the associated events.
* Refer to the ```<condition>``` Control File element.

### Recognition of file modification
	
* The SMA FAD recognizes when a file has been modified.
* Refer to the ```<condition>``` Control File element.

:::info Note 

The SMA FAD processes events for file modification separately from events for change in file size.

:::

### Support the initiation of events in specified time slots only

* If specified in the control file, the SMA FAD triggers the external events only if the conditions are met within a specific period of time.
* Refer to the ```<window>``` Control File element.

### Ability to specify a time interval between initiation of events

* If configured to trigger multiple events upon certain file criteria, the SMA FAD can wait a user-defined number of seconds between events.
* Refer to the ```<sleep>``` Control File element.

### Read the control file at a configurable interval

* By default, the SMA FAD reads the control file every one second; however, the administrator can configure other intervals.
* Refer to the ```<waittimebetweenpasses>``` Control File element.

## Glossary

**SMA FAD** — The SMA File Activity Detection Daemon; a daemon that monitors directories for relevant file changes and forwards defined OpCon events to the SAM.

**Control File** — An XML-formatted ASCII text file residing in the `control` subdirectory of the FAD directory structure. It contains all parameters the daemon needs to monitor directories and initiate SAM external events, including the file masks to watch, the conditions to detect, the events to forward, and timing settings.

**`<filemask>`** — A required Control File element that defines the full path and file name or wildcard pattern for monitoring.

**`<condition>`** — A required Control File element that defines the file state (CREATE, DELETE, GROWTH, SHRINK, ABSOLUTE, or MODIFY) that causes the SMA FAD to initiate events.

**`<window>`** — An optional Control File element that restricts event initiation to a defined time interval using a 24-hour clock. When omitted, the SMA FAD monitors persistently.

**`<sleep>`** — An optional Control File element within `<eventinfo>` that defines the number of seconds the SMA FAD waits before initiating the next event in the same record block.

**`<waittimebetweenpasses>`** — An optional Control File element that specifies the interval in seconds between successive reads of the Control File. Defaults to 1 second if omitted.