---
sidebar_label: 'Overview'
title: Reference Overview
description: "Overview of Reference."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Reference overview

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?

The Reference section provides lookup material for the Unix Agent, including error codes, system messages, known issues, and environment details. You use these pages to identify the cause of a failure, understand what the agent reports, and verify system state. The content is organized for quick lookup rather than sequential reading.

## When would you use this section?

- A job fails and you need to identify the error code or message returned by the Unix Agent.
- You want to check whether a reported behavior is a known issue with a documented workaround.
- You need to review the fields included in job resource-usage reports.
- You are diagnosing communication or file transfer failures and need to cross-reference machine messages.
- You need to understand how the Unix Agent modifies the system or what environment variables it passes to jobs.

## What is in this section?

| Topic | Description |
|---|---|
| UNIX Troubleshooting | Reference for common UNIX system error symbols returned by the Unix Agent, including probable causes and corrective actions for each error condition. |
| Known Issues | Reference for known defects and limitations in Unix Agent versions, including affected platforms, symptoms, and available workarounds. |
| Job Resource-Usage Reporting | Reference for OpCon field codes and descriptions returned per job when Unix Agent resource-usage reporting is enabled via the LSAM_job_statistics configuration parameter. |
| Machine Messages | Reference catalogs for Unix Agent log messages, job status messages, exit codes, file transfer error codes, and JORS/FTServer errors returned during job and transfer operations. |
| System Modification and Environment Variables | Reference and procedural content covering the directories and files created by the Unix Agent, how to deactivate or remove agent components, and the environment variables passed to jobs at runtime. |
