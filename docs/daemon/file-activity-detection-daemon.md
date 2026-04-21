---
title: File Activity Detection Daemon
description: "Overview of the SMA File Activity Detection Daemon (FAD), which monitors directories for file changes and forwards OpCon events to the SAM."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# Introduction

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

Overview of the SMA File Activity Detection Daemon (FAD), which monitors directories for file changes and forwards OpCon events to the SAM.

The SMA File Activity Detection Daemon (SMA FAD) monitors directories specified for any relevant changes and forwards defined OpCon events to the SAM. The Control File contains the directories to be monitored and contains the external events to be forwarded to the SAM. SMA FAD writes all logging information through the sma_log process. For information on sma_log, refer to [sma_log](../operations/components#sma_log).

## When would you use it?

- Use FAD when you need to trigger OpCon events in response to file creation or deletion — for example, to start a dependent job as soon as an expected file arrives or to raise an alert when a required file is removed.
- Use FAD when you need to monitor for changes in file size or file modification, and initiate associated events — for example, to detect when an in-progress file has stopped growing before allowing downstream processing to begin.
- Use FAD when you need to restrict event initiation to specific time slots — for example, to forward external events to the SAM only during a defined processing window, using the `<window>` Control File element.
- Use FAD when multiple directories require independent monitoring at different intervals — because multiple Control Files can exist in the control directory, each identifying a unique instance of the daemon with its own configuration.

## Why would you use it?

- FAD removes the need for polling scripts or manual checks — it monitors directories continuously and forwards OpCon events to the SAM the moment a defined condition is detected, reducing the lag between a file event and the downstream job that depends on it.
- Because FAD writes all logging information through the sma_log process, monitoring and troubleshooting activity is consolidated in the same logging infrastructure used by the rest of the agent, keeping operational overhead low.
- Using the `<window>` element in the Control File, administrators can restrict when events are forwarded to the SAM, preventing unintended job triggers outside defined processing windows without modifying the schedule in OpCon.
- Multiple Control Files — and therefore multiple independent daemon instances — can coexist in the control directory, which means a single agent installation can monitor multiple directories at different intervals without additional software or separate agent deployments.

## Examples

**Scenario:** A system administrator needs to start an OpCon job as soon as a daily data feed file arrives in a designated drop directory, but only during a defined processing window.

**Configuration:** A Control File is created in `LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/` with a `<fileactivity>` block that targets the drop directory using a `<filemask>` matching the expected filename pattern. The `<condition>` is set to detect file creation. A `<window>` element is included to restrict event forwarding to the defined processing hours. An `<eventinfo>` block specifies the OpCon job-start event to forward to the SAM. The daemon is started with `bin/start_fad`.

**Expected outcome:** When the data feed file appears in the drop directory during the processing window, SMA FAD detects the creation event and forwards the configured OpCon event to the SAM. The SAM receives the event and starts the dependent job. Activity is recorded through the sma_log process. If the file arrives outside the processing window, the event is not forwarded.

## Glossary

**FAD** — The SMA File Activity Detection Daemon (SMA FAD); a daemon that monitors directories specified for any relevant changes and forwards defined OpCon events to the SAM.

**Control File** — An XML-formatted ASCII text file that resides in the `control` subdirectory of the FAD directory structure. It contains all the parameters the daemon needs to monitor directories and initiate SAM external events, including the directories to watch, the conditions to detect, the events to forward, and timing settings. Each Control File identifies a unique instance of the file activity detection daemon and serves as its configuration file.
