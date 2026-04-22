---
title: File Compression
description: "SMAFT supports optional file compression using the UNIX tar and gzip utilities, configurable as PREFERRED or REQUIRED for each agent installation."
tags:
  - Conceptual
  - Reference
  - System Administrator
  - Agents
---

# File Compression

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
SMAFT supports optional file compression using the UNIX tar and gzip utilities, configurable as PREFERRED or REQUIRED for each agent installation.

Both the UNIX SMA File Transfer (SMAFT) Agent and Server support file compression using the UNIX "tar" and "gzip" utilities. By default, the Server does not compress the Source File prior to its transfer to the Agent. Two additional options are available: PREFERRED and REQUIRED. If PREFERRED is selected, the file is transferred without compression if the Server and Agent are unable to negotiate a compatible compression method. If REQUIRED is selected and if a compression method cannot be negotiated, the transfer is not performed and the job fails.

:::info Note 

Although the "tar" utility may process multiple files, an OpCon File Transfer job can only transfer a single file.

:::

During the agent installation, the installation script searches the system for the "tar" and "gzip" utilities and sets compression support accordingly. You can subsequently configure each installation of the agent for compression during file transfer. Compression settings apply to both Server and Agent for an agent. If compression support is not enabled, all SMAFT jobs which reference the agent (as either Source machine or Destination machine) fail if compression is REQUIRED or FAIL-PREFERRED. 

Configuration changes take effect immediately in the Agent; however, the agent must either be restarted or refreshed for the changes to become effective in the Server.

- Enable compression when transferring large files across slow or bandwidth-limited networks, provided the `tar` and `gzip` utilities are available on both the Source and Destination machines.
- Compression reduces the size of files in transit, which can lower transfer time on slow or bandwidth-limited network connections.

## Compression options reference

SMAFT supports two non-default compression settings. The default behavior is to transfer the file without compression.

| Option | Behavior when compression cannot be negotiated |
|---|---|
| PREFERRED | Transfer proceeds without compression. |
| REQUIRED | Transfer is not performed and the job fails. |

Both the Server and Agent must have compression support enabled for negotiation to succeed. Compression support is determined at installation time: the installation script searches the system for the `tar` and `gzip` utilities and sets compression support accordingly. If compression support is not enabled on an agent, all SMAFT jobs referencing that agent fail if compression is set to REQUIRED or FAIL-PREFERRED.

Compression settings apply to both the Server and Agent roles for a given agent installation. Although `tar` can process multiple files, an OpCon File Transfer job transfers only a single file.

## Exception handling

**Symptom: SMAFT job fails with a compression-related error** — The agent's compression support is not enabled, but the job has compression set to REQUIRED or FAIL-PREFERRED. During installation, the installation script must detect the `tar` and `gzip` utilities on the system in order to enable compression support. Verify that both utilities are present, update the agent control script to include the paths to `tar` and `gzip` in the `PATH` variable, delete the SMAFT Control Script so it is regenerated, and then restart or refresh the agent so that the Server recognizes the updated compression support.

## Examples

An OpCon File Transfer job is configured to transfer a single large file from a Source machine to a Destination machine. The job has compression set to PREFERRED. The installation script on the Source machine detected `tar` and `gzip` at installation time, so compression support is enabled on the Server. The Destination machine also has compression support enabled. The Server and Agent successfully negotiate a compatible compression method, and the file is compressed using `tar` and `gzip` before transfer. If compression support had not been enabled on one of the machines, the PREFERRED setting would allow the transfer to proceed without compression rather than failing the job.

## Glossary

**Compression support** — A flag set during agent installation when the installation script detects the `tar` and `gzip` utilities on the system. If compression support is not enabled on an agent, all SMAFT jobs that reference that agent as either Source or Destination fail when compression is set to REQUIRED or FAIL-PREFERRED.

**PREFERRED** — A compression (or encryption) option that allows the transfer to proceed without the feature if the Server and Agent cannot negotiate a compatible method. Contrast with REQUIRED, which fails the job when negotiation is unsuccessful.