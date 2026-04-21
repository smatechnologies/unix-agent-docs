---
title: JORS/FTServer Errors
description: "Reference for JORS and FTServer error messages recorded in the UNIXLSAM log file, including socket initialization and process spawning failures."
tags:
  - Reference
  - System Administrator
  - Agents
---

# JORS/FTServer errors

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?

Reference for JORS and FTServer error messages recorded in the UNIXLSAM log file, including socket initialization and process spawning failures.

The UNIXLSAM.log file contains these errors:

## When would you use it?

- You are reviewing the UNIXLSAM.log file and need to identify a JORS or FTServer error entry.
- A file transfer or JORS request fails and you need to determine whether the socket initialization or child-process spawning failed.
- You are diagnosing communications channel errors reported by FTServer during startup or operation.



* **Unable to open master socket (return : return errno : errno)**
* **Select on master socket failed (errmo : errno)**
* **Accept on master socket failed (errno : errno)**
* **Could not set buffer size**

**Origination**: FTServer

* The communications channel could not be initialized.
* The return and errno fields provide the specific reason.

---

* **fork() failed (errno : errno)**	

**Origination**:FTServer

* A child process to handle the JORS/FTServer duties could not be spawned.
* The errno field provides the specific reason.
