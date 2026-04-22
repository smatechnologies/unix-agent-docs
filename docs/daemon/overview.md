---
sidebar_label: 'Overview'
title: File Activity Detection (FAD) Daemon overview
description: "Overview of the File Activity Detection (FAD) Daemon."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# File Activity Detection (FAD) Daemon overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

The File Activity Detection (FAD) Daemon is a component of the Unix Agent that monitors directories for file changes and forwards OpCon events to the SAM. It uses a control file to define which directories to watch and what events to send when file activity is detected. System Administrators configure and maintain the FAD Daemon to support event-driven job automation on Unix machines.

## When would you use this section?

- Learning what the FAD Daemon does and whether you need it
- Setting up or modifying the directories the FAD Daemon monitors
- Reviewing the file monitoring capabilities the FAD Daemon supports
- Understanding the directory layout the FAD Daemon uses for its configuration and runtime files

## What is in this section?

| Topic | Description |
|---|---|
| File Activity Detection Daemon | Overview of the SMA File Activity Detection Daemon (FAD), which monitors directories for file changes and forwards OpCon events to the SAM. |
| Features | Reference of all file monitoring capabilities supported by the SMA File Activity Detection Daemon, including file creation, deletion, size change, modification detection, and configurable event timing. |
| Directory structure | Reference for the SMA FAD directory layout, including the control, snapshot, and pid subdirectories and their roles in file monitoring and event processing. |
| Control file | Overview of the SMA FAD Control File, an XML-formatted ASCII configuration file that defines the directories to monitor and the OpCon events to forward to the SAM. |
