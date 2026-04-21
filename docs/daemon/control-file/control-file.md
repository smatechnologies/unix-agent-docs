---
title: Control File
description: "Overview of the SMA FAD Control File, an XML-formatted ASCII configuration file that defines the directories to monitor and the OpCon events to forward to the SAM."
tags:
  - Conceptual
  - Reference
  - System Administrator
  - Agents
---

# Control File

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

Overview of the SMA FAD Control File, an XML-formatted ASCII configuration file that defines the directories to monitor and the OpCon events to forward to the SAM.

The Control File contains all the parameters the daemon needs to monitor the directories and initiate the SAM external events. As a single ASCII text file, the Control File is configurable with standard editors (e.g., vi). The Control File has the following characteristics:

## When would you use it?

- Create a Control File when you need to set up a new instance of the SMA FAD — each Control File in the `control` subdirectory identifies a unique daemon instance with its own configuration.
- Create an additional Control File when different directories must be monitored at different intervals — multiple Control Files can coexist in the control directory, each configuring an independent daemon instance.
- Modify a Control File when the directories to monitor, the conditions to detect, the events to forward, or the timing settings for an existing daemon instance need to change.
- Modify the Control File when you need to add, remove, or adjust record blocks — each block targets a specific file mask and condition, so changes to monitoring scope require editing the file directly.

## Why would you use it?

- The Control File provides a single, human-readable XML configuration point for all parameters an SMA FAD instance needs — the directories to watch, the conditions to detect, the external events to forward to the SAM, and the timing controls.
- Storing configuration in a plain ASCII text file means any standard editor (for example, vi) can be used to create or modify it without specialized tooling.
- Supporting multiple Control Files in the same `control` subdirectory allows independent monitoring instances to run with different configurations, giving administrators granular control over how different directories are monitored.
- Commenting out lines with a `#` as the first non-blank character lets administrators disable individual lines for testing or troubleshooting without deleting content.

## Creating a Control File

To create a Control File and activate it, complete the following steps:

1. Use a standard text editor (for example, vi) to create an XML-formatted ASCII text file. Structure the file using the supported Control File elements, with at least one `<fileactivity>` block containing a unique `<id>`, a `<filemask>`, a `<condition>`, and at least one `<event>` within an `<eventinfo>` block.
2. Save the file with a name of 63 characters or fewer (excluding the pathname) to the following directory: `LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/`.
3. From the `<LSAM_Root_Directory>` directory, stop the daemon by issuing the following command: `bin/stop_fad`
4. Start the daemon by issuing the following command: `bin/start_fad`

:::info Note

The agent must be restarted before modifications to an existing Control File take effect, and before a newly copied Control File is recognized. The startup script starts one daemon instance for each file in the control directory.

:::

* The Control File resides in the following directory: ```LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/```. The filename has a limit of 63 characters (excluding the pathname).
* The Control File consists of blocks of records that are processed one at a time.
* The Control File is an XML type file, and all the elements are defined within their tags.
* A "#" sign as the first non-blank character on a line comments out the whole line.
* Multiple Control Files can exist in the control directory.
    * Each Control File identifies a unique instance of the file activity detection daemon.
    * Each Control File also serves as a configuration file for the associated instance of the daemon.
    * Using the Control File names as identifiers, the FAD daemon startup script (like the agent startup script) starts one instance of the daemon for each file in the control directory.

:::info Note

For most sites, a single instance of the SMA FAD is sufficient; nevertheless, multiple instances of SMA FAD can monitor different directories at different intervals.

:::

* The agent must be restarted before modifications take effect, or after the new control file has been copied into the Control Directory. Issue a bin/stop_fad command followed by a bin/start_fad command from the ```<LSAM _Root_Directory>``` directory.

## Examples

**Scenario:** A system administrator needs to monitor two separate directories — one for incoming payroll files and one for nightly report files — each at a different polling interval and each triggering a different OpCon event.

**Configuration:** The administrator creates two separate Control Files in `LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/`. The first Control File contains a `<fileactivity>` block with a `<filemask>` targeting the payroll directory and an `<eventinfo>` block that forwards a job-start event to the SAM. The second Control File contains its own `<fileactivity>` block targeting the report directory with a different polling interval and a separate `<eventinfo>` block. Each file is named with 63 characters or fewer.

**Expected outcome:** When the daemon is started with `bin/start_fad`, the startup script reads both files in the control directory and starts one daemon instance per Control File. Each instance monitors its assigned directory independently, forwarding the configured OpCon event to the SAM when the defined condition is detected.

## Glossary

**Control File** — An XML-formatted ASCII text file stored in the `LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/` directory. It contains all parameters a single SMA FAD instance needs to monitor directories and initiate SAM external events. Each Control File identifies and configures one unique daemon instance.

**Record block** — A set of XML elements within a Control File, bounded by an `<id>` tag, that defines the monitoring parameters for a specific file mask and condition. Each record block targets one set of files and specifies the event to forward when the condition is met.

**SAM** — The OpCon Schedule Activity Monitor. The SAM receives the external events forwarded by SMA FAD and acts on them within the OpCon schedule.