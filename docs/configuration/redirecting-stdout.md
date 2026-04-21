---
sidebar_label: 'Redirecting STDOUT'
title: Redirecting STDOUT
description: "Reference for redirecting STDOUT output from Unix Agent jobs, including use of the captureSTDOUT script and behavior differences based on the path_to_su parameter."
tags:
  - Procedural
  - Reference
  - System Administrator
  - Agents
---

# Redirecting STDOUT

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for redirecting STDOUT output from Unix Agent jobs, including use of the captureSTDOUT script and behavior differences based on the path_to_su parameter.

## When would you use it?

Redirect STDOUT when:

- The `path_to_su` parameter is set to No and a job must write its output to a specific file, because in this configuration the agent does not correctly interpret a redirection character (`>`) in a Start Image received from the Enterprise Manager.
- A job's output would otherwise accumulate in the `LSAM_output_<SAM_socket>` file in the agent root directory, making it difficult to identify or archive output for individual jobs.

## Why would you use it?

- Redirecting STDOUT to a dedicated output file keeps job output separate from agent diagnostic output, making it easier to review results and diagnose job failures.
- Using the `captureSTDOUT` script or a wrapper script provides a consistent, maintainable approach to output handling that works for any job without modifying the individual scripts themselves.

## How to implement it

To redirect STDOUT for Unix Agent jobs, complete the following steps:

- [Review the `path_to_su` setting](#redirecting-stdout) — if `path_to_su` is set to Yes, redirection in the Start Image works directly; if it is set to No, use the `captureSTDOUT` script or embed redirection logic inside the job script.
- [Use the `captureSTDOUT` script](#syntax) — pass the output file path and the script path as arguments so the agent routes job output to the specified file rather than the `LSAM_output_<SAM_socket>` file in the agent root directory.

## Exception handling

**Job output is written to `LSAM_output_<SAM_socket>` instead of the specified file** — The `path_to_su` parameter is set to No and the redirection character (`>`) was placed in the Start Image rather than inside a script or handled by `captureSTDOUT`. — Either embed the output redirection within the job script itself, or set the Start Image to invoke `captureSTDOUT` with the output file path and script path as arguments as described in the [Syntax](#syntax) section.

**`captureSTDOUT` script fails or produces errors for the current shell** — The script template is written for the Korn shell; running it under a different shell without modification causes syntax errors or unexpected behavior. — Edit `captureSTDOUT` in `<LSAM root path>/bin/` to match the syntax of the shell in use on the system before referencing it in job definitions.

**Output file is not created at the specified path** — The directory path supplied as the first argument to `captureSTDOUT` does not exist, or the agent's user does not have write permission to that directory. — Verify that the target directory exists and that the user identity under which the job runs has write access to it.

If the parameter ```path_to_su``` is set to Yes, redirecting ```STDOUT``` in the start image received from the Enterprise Manager will work fine.

If the parameter ```path_to_su``` is set to No, redirecting ```STDOUT``` must take place within a script. Because of its design, the LSAM does not correctly interpret a redirection character (>) in a Start Image received from the Enterprise Manager. Each script must contain the code to redirect ```STDOUT```, or a wrapper script can receive each script and handle the redirection. If the output is not redirected, it will be sent to the ```LSAM_output``` file, ```LSAM_output_<SAM_socket>``` in the agent root directory.

SMA Technologies provides a generic script ```captureSTDOUT``` that redirects ```STDOUT``` for any script. The ```captureSTDOUT``` script resides in the ```<LSAM root path>/bin``` directory. This script is a working template, and is open to modification by a system programmer to contain more detailed information. The template is for use with the Korn shell; therefore, be sure to adjust the script according to the shell in use.

For information on analyzing standard out to determine exit conditions, refer to [sma_ppscript]../../operations/utilities/sma-ppscript).

## Syntax

```<path>/captureSTDOUT <path to output file> <path to script>```

The ```<path>``` points to the LSAM "```bin/```" directory (e.g., "```/usr/local/lsam/bin```").

:::tip Example

An example UNIX job has the following characteristics:

The job to run has the following path: ```/usr/local/payroll/timecalc```
The standard output from the job goes to the following file: ```/usr/local/payroll/finished/timecalc.datetime.```
Assuming the ```captureSTDOUT``` file is in the LSAM ```/bin``` directory, the Start Image and Parameters on the UNIX Details screen (in the Enterprise Manager's Job Master) for the above job would contain the following:

Start Image: ```/usr/local/lsam/bin/captureSTDOUT```

Parameters: ```/usr/local/payroll/finished/timecalc.datetime/usr/local/payroll/timecalc```

:::

For more information, refer to [UNIX Job Details](https://help.smatechnologies.com/opcon/core/job-types/unix) in the Concepts online help.
