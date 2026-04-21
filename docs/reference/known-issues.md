---
title: Known Issues
description: "Reference for known defects and limitations in Unix Agent versions, including affected platforms, symptoms, and available workarounds."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Known issues

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?

Reference for known defects and limitations in Unix Agent versions, including affected platforms, symptoms, and available workarounds.

Issues are listed by version and include workarounds where available.

## When would you use it?

- A job, file transfer, or agent startup behaves unexpectedly and you need to determine whether the behavior is a known defect in your installed version.
- You are planning an upgrade and need to review defects and limitations in the version you are moving to or from.
- You have encountered an error and need to check whether a workaround is available before contacting SMA Technologies Support.



---

**Version 24.0.0 — Agent does not clean up zombie processes under some conditions**

- **Symptom:** :white_check_mark: **UNIX-462**: agent does not clean up zombie processes under some conditions.
- **Affected versions:** 24.0.0
- **Workaround:** None listed.

---

**Version 17.1.0 — Large file transfers from UNIX to Windows fail mid-transfer**

- **Symptom:** When transferring large files on the order of gigabytes from UNIX to Windows, the UNIX job starting at the source will fail approximately halfway through. The error from Windows will indicate that there was a socket connection failure.
- **Affected versions:** 17.1.0
- **Workaround:** None listed.

---

**Version 16.2.0 — TLS communication may not work on HP-UX, SUSE, UBUNTU, and DEBIAN**

- **Symptom:** TLS communication may not work properly for systems running HP-UX, SUSE, UBUNTU, and DEBIAN.
- **Affected versions:** 16.2.0
- **Workaround:** None listed.

---

**Version 15.00.01.23 — Compatibility issue with Windows agent in SMAFT ASCII mode transfer**

- **Symptom:** Compatibility issue in SMAFT ASCII mode transfer between UNIX and Windows agents.
- **Affected versions:** 15.00.01.23
- **Workaround:** Ensure that the latest Windows agent (version 15.3 ASCII patch) is updated before installing the latest UNIX version to resolve a compatibility issue in SMAFT ASCII mode transfer.

---

**Version 5.20.30 and higher — File transfers fail with unauthorized message error**

- **Symptom:** File transfers fail with the following error:

  ```[sma_JORS] Received unauthorized message - aborting session (759)```

- **Affected versions:** 5.20.30 and higher
- **Workaround:** If this error occurs, change the Destination Machine of the file's configuration to set redirection_stderr to a value of 1.

---

**Version 4.01.01 — sma_filein erroneously logs an error message for non-empty MSGIN files**

- **Symptom:** The utility program sma_filein was enhanced to handle multiple event strings in files dropped into the MSGIN directory. It erroneously logs an error message (even when the MSGIN file is not empty). This message looks like:

  ```[sma_filein] Empty file [/usr/local/lsam/MSGIN/<socket>/<filename>] (errno : 2)```

- **Affected versions:** 4.01.01
- **Workaround:** It can safely be ignored. The events will be sent to the core services of OpCon correctly.

---

**Version 3.08.01 — Restart Step and Job Start/End Step functions do not work properly on all UNIX/Linux flavors**

- **Symptom:** The Restart Step and Job Start/End Step functions do not work properly on all flavors of UNIX/Linux which are supported by the agent.

  It has been found that some jobs based on the "user_job_step_template" Shell script, supplied in the agent "bin/" directory, will not run properly on some flavors of UNIX/Linux. Jobs may run to completion (or through the specified ending step) and then be terminated with an "[sma_lsam] Infinite loop detected (509)" message and a numeric status code of 1. Jobs may also err-off prematurely, the error message being one with message number 508, 509, 539, 540, or 541 (and a numeric status code of 1).

  This behavior is due to differences in processing by the Shells among the various flavors of UNIX/Linux, and it is not indicative of a problem with the actual agent: users' jobs which do not make use of "user_job_step_template" will run as expected. The problems will be corrected by release of an updated version(s) of "user_job_step_template" as soon as it can be modified to account for all support Shells.

- **Affected versions:** 3.08.01
- **Workaround:** Customers who wish to create a job based on "user_job_step_template" should first create a short test job which contains three or four simple steps (e.g., "echo some_text", to determine if their system will run these types of jobs as expected).

---

**All versions prior to 3.08.01 — Agent fails to start when system PIDs reach 10,000,000**

- **Symptom:** The agent will fail to start whenever system Process IDs (PIDs, the numerical values as displayed by a 'ps' command, not the number of them) reach 10,000,000 (10 million). Jobs, however, should continue to run without problems until the agent is stopped.

  At this point, only AIX systems exhibit the problem. Solaris, Suze, Redhat, Linux/390, Unixware 7, and HP-UX systems tested to not have the problem, as their PIDs appear to not exceed the value 32768.

  The logging daemon (sma_log) start-up will be the only entry in the agent log file, or no entries from the attempted start-up will exist. PID files in the agent's PID directory "$LSAM_ROOT/pid/$SAM_SOCKET*.pid/" will have lengths of zero or contain values of zero.

- **Affected versions:** All versions prior to 3.08.01
- **Workaround:** If possible, upgrade to agent v3.08.01 or higher. Otherwise, configure the system to keep PIDs under 10 million, or if PIDs have reached 10 million, reboot the system prior to starting the agent.
