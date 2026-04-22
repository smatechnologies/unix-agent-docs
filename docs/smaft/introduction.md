---
title: SMA File Transfer overview
description: "SMAFT reliably transfers files across multiple platforms as part of an OpCon job, with support for compression, encryption, SFTP fallback, and transfers larger than 2 GB."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

# SMAFT - Introduction

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
SMAFT reliably transfers files across multiple platforms as part of an OpCon job, with support for compression, encryption, SFTP fallback, and transfers larger than 2 GB.

The SMA File Transfer (SMAFT) system reliably transfers files across multiple platforms via an OpCon job. Like file transfer protocol (ftp), SMAFT supports file compression and encryption but ensures that the file transfer completes before processing subsequent dependent jobs. SMAFT can support file transfers larger than two gigabytes as long as the underlying OS supports this feature. SMA Technologies does not recommend enabling encryption or compression for files larger than one gigabyte.

SMAFT supports Version 2 of the SMAFT specification. This allows you to select Start Transfer On Source Machine in the Enterprise Manager definition screen. The Delete Source File option is not supported and should always be set to "No."

The receiving (Agent) and sending (Server) components are installed with file-transfer-enabled agents (e.g., the Unix Agent). The Source and Destination machines must have these components for a file transfer.

After receiving instructions from the agent on the Destination machine, the Agent (also on the Destination machine) and Server (on the Source machine) determine the best method for transporting the file. After negotiating the file transfer settings with the Server, the Agent requests the file. The Server retrieves the file and sends it to the Agent according to the Agent's instructions.

The agent will perform file transfer using the open standard SFTP between UNIX agents when you have configured the agent Configuration Parameter "sftp_port" to a non-zero value. If, for whatever reason the transfer fails, the agent will fall back to using SMAFT to perform the transfer.

When the agent is installed, you have the option of choosing to use the /TMP partition or to use a TMP area in the same partition as the agent. File transfers may require anywhere from two to three times the size of the file being transferred in /TMP or TMP workspace designated when the agent was installed.

- Use SMAFT when you need to transfer files between platforms as part of an OpCon job and must ensure that the transfer completes before dependent jobs begin processing.
- Use SMAFT when transferred files require compression — for example, to reduce transfer size using the UNIX `tar` and `gzip` utilities, with the option to require compression or to prefer it and fall back gracefully if a compatible method cannot be negotiated.
- Use SMAFT when transferred files must be encrypted in transit — for example, when organizational security policies require DES, 3DES, or AES-128 encryption, with the ability to set encryption as PREFERRED or REQUIRED for each agent installation.
- Use SMAFT when transferring files from a non-UNIX platform to UNIX and then back to a non-UNIX platform, and you need to preserve the original record structure of the file so that it arrives at the destination with its record format intact.

- SMAFT ensures that file transfers complete before dependent jobs begin processing, which prevents downstream jobs from running against incomplete or missing data.
- SMAFT supports compression and encryption in a single transfer, reducing both the size of the file in transit and protecting its contents without requiring separate pre- and post-transfer steps.
- When both agents support SFTP, SMAFT uses that open standard automatically and falls back to its own protocol if the SFTP transfer fails, minimizing manual intervention.
- SMAFT can transfer files larger than two gigabytes when the underlying operating system supports it, removing size-based limitations that affect simpler transfer utilities.

## Examples

A Unix Agent is installed on both the Source and Destination machines with the `sftp_port` configuration parameter set to a non-zero value. A file transfer job is defined in OpCon between these two agents. When the job runs, the agents negotiate the transfer and use SFTP. If the SFTP transfer fails for any reason, the agents fall back to SMAFT to complete the transfer. Dependent jobs defined in OpCon do not start until the transfer completes successfully.

## Glossary

**SMAFT** — SMA File Transfer; a system that reliably transfers files across multiple platforms via an OpCon job, with support for compression, encryption, SFTP fallback, and transfers larger than 2 GB.

**Stream file** — A file maintained by the UNIX operating system as an ordered, amorphous collection of bytes, with no record structure recognized by the operating system or the Unix Agent.

**Record file** — A file in which the operating system organizes data into records of equal (fixed) or unequal (variable) length; a structure used on some non-UNIX platforms such as OS2200. When a UNIX Agent receives such a file, it can optionally store record-structure data alongside the file so that the structure can be restored when the file is transferred to a non-UNIX system.

**Compression** — Optional reduction of a file's transfer size using the UNIX `tar` and `gzip` utilities, configurable per agent installation as not used (default), PREFERRED, or REQUIRED.

**Encryption** — Optional protection of a file during transfer using a supported algorithm (DES, 3DES, or AES-128) and mode (ECB or CBC), configurable per agent installation as not used (default), PREFERRED, or REQUIRED.
