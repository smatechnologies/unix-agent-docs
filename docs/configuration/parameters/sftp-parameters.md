---
sidebar_label: 'SFTP Parameters'
title: SFTP Parameters
description: "Reference for the Unix Agent SFTP parameter that configures the port used for SFTP-based file transfer, including fallback behavior to SMAFT."
tags:
  - Reference
  - System Administrator
  - Agents
---

# SFTP parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the Unix Agent SFTP parameter that configures the port used for SFTP-based file transfer, including fallback behavior to SMAFT.

The following parameters reference the SFTP setting for the Unix Agent. This setting controls whether SFTP is enabled for file transfers and specifies the port used, with automatic fallback to SMAFT if SFTP fails.

## When would you use it?

- When enabling SFTP-based file transfer for the agent
- When configuring the SSH port used for SFTP connections
- When troubleshooting file transfer behavior, including SFTP-to-SMAFT fallback

### sftp_port

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
