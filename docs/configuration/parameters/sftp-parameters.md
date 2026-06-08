---
sidebar_label: 'SFTP Parameters'
title: SFTP Parameters
description: "Historical reference for the Unix Agent sftp_port parameter. SFTP-based file transfer was removed in agent version 24.0.0; this page is retained for reference when working with agent versions earlier than 24."
tags:
  - Reference
  - System Administrator
  - Agents
---

# SFTP parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Historical reference for the Unix Agent `sftp_port` parameter. SFTP-based file transfer options were removed in agent version 24.0.0 (UNIX-395). This page applies only to agent versions earlier than 24.0.0.

:::warning

The SFTP configuration options documented on this page were removed in **agent version 24.0.0**. If you are running agent version 24.0.0 or later, the `sftp_port` parameter has no effect and SFTP-based file transfer is no longer available. All file transfers use SMAFT. Refer to [SMA File Transfer Overview](../../smaft/introduction) for current file transfer capabilities.

:::

- When troubleshooting file transfer behavior on agent versions earlier than 24.0.0

### sftp_port

**Applies to:** Agent versions earlier than 24.0.0  
**Default Value**: 0

**Description**: 
	
* Enables (non-zero value)/Disables (0 value) the use of SFTP for file transfer.
* Standard SFTP uses port 22.

:::info Note 

This value must match the configured SSH port being used.

:::

* The SFTP component of SSH must be configured and enabled.
* When set, the agent attempts first to use SFTP for file transfer.
* If using SFTP for file transfer should fail, the agent will fallback to using SMAFT.

