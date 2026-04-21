---
slug: '/'
sidebar_label: 'Unix Agent'
hide_table_of_contents: true
displayed_sidebar: null
title: Unix Agent
description: "Documentation for the Unix Agent, an OpCon agent that schedules and runs jobs in UNIX environments."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# Unix Agent

The Unix Agent is an OpCon agent that allows OpCon to schedule and run jobs within a UNIX environment.

The agent communicates with the SAM, the Job Output Retrieval System (JORS), and SMA File Transfer (SMAFT) components over a set of sequentially numbered sockets. In addition to job scheduling, the agent includes built-in support for file transfers, directory monitoring, and system resource monitoring, each delivered through dedicated components that start alongside the agent.

**Use cases**

- Schedule and run jobs on UNIX systems under OpCon control.
- Transfer files across platforms as part of an OpCon job, with optional compression, encryption, and SFTP fallback for transfers between UNIX agents.
- Monitor directories for file changes and forward OpCon events to the SAM when changes are detected.
- Monitor system resources — including disk space, running processes, and user-defined metrics — and trigger OpCon events or local actions when alarm conditions are detected.
- Run multiple independent agent instances on a single machine to support different configurations, such as separating general-user workloads from critical-job workloads.

<div style={{display: 'flex', gap: '0.75rem', alignItems: 'flex-start', flexWrap: 'wrap', marginTop: '1rem'}}>

<div style={{flex: '1', minWidth: '160px', display: 'flex', flexDirection: 'column', gap: '0.6rem'}}>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### Overview

- [Release Notes](./release-notes.md)

</div>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### Installation

- [Requirements](./installation/requirements.md)
- [Supported Operating Systems](./installation/supported-os.md)
- [Fetch Install File](./installation/fetch-install-file.md)
- [Preferred Installation](./installation/preferred-installation.md)
- [Legacy Installation](./installation/legacy-installation.md)
- [Initial Startup](./installation/initial-startup.md)
- [Additional Procedures](./installation/additional-procedures.md)

</div>

</div>

<div style={{flex: '1', minWidth: '160px', display: 'flex', flexDirection: 'column', gap: '0.6rem'}}>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### Configuration

- [Unix Agent Configuration](./configuration/unix-lsam-configuration.md)
- [Security Configuration](./configuration/security-configuration-options.md)
- [Agent configuration file](./configuration/lsam-configuration-file.md)
- [TCP/IP Configuration](./configuration/parameters/tcp-ip-configuration.md)
- [Agent configuration parameters](./configuration/parameters/lsam-configuration-parameters.md)
- [TLS Security](./configuration/unix-tls-security.md)
- [Running multiple agents](./configuration/running-multiple-lsams.md)
- [Automatic Startup](./configuration/automatic-startup-configuration.md)
- [Time Zone](./configuration/configuring-time-zone.md)

</div>

</div>

<div style={{flex: '1', minWidth: '160px', display: 'flex', flexDirection: 'column', gap: '0.6rem'}}>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### Operations

- [Operating the agent](./operations/operating-the-lsam.md)
- [Unix Agent Commands](./operations/unix-lsam-commands.md)
- [Utilities](./operations/utilities/utilities.md)
- [Components](./operations/components.md)

</div>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### File Activity Detection Daemon

- [Overview](./daemon/file-activity-detection-daemon.md)
- [Features](./daemon/features.md)
- [Directory Structure](./daemon/directory-structure.md)
- [Control File](./daemon/control-file/control-file.md)

</div>

</div>

<div style={{flex: '1', minWidth: '160px', display: 'flex', flexDirection: 'column', gap: '0.6rem'}}>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### SMA File Transfer

- [Introduction](./smaft/introduction.md)
- [File Compression](./smaft/file-compression.md)
- [File Encryption](./smaft/file-encryption.md)
- [Stream and Record Files](./smaft/stream-and-record-files.md)

</div>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### SMA Resource Monitor

- [Introduction](./smarm/introduction.md)
- [Configuration File](./smarm/configuration-file/configuration-file.md)
- [Exception Handling](./smarm/exception-handling.md)

</div>

<div style={{background: 'var(--ifm-card-background-color)', border: '1px solid var(--ifm-color-emphasis-400)', borderRadius: '10px', padding: '0.75rem 1rem'}}>

### Reference

- [Machine Messages](./reference/machine-messages/unix-lsam-messages.md)
- [Environment Variables](./reference/system-modification/lsam-environment-variables.md)
- [Troubleshooting](./reference/troubleshooting.md)
- [Known Issues](./reference/known-issues.md)

</div>

</div>
</div>
