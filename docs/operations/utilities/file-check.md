---
sidebar_label: 'file_check'
title: file_check
description: "Reference for the file_check utility, which validates that specified files meet existence, access, size, and age criteria before an OpCon job executes."
tags:
  - Reference
  - System Administrator
  - Agents
---

# file_check

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the file_check utility, which validates that specified files meet existence, access, size, and age criteria before an OpCon job executes.

- Configure file_check as a prerun job in OpCon when a downstream job requires a specific file to exist, be readable, or meet a minimum size or age before the job starts.
- Use file_check to verify that files placed in a shared directory by an upstream process are present and fully written before a dependent job reads them.

- Running file_check as a prerun job prevents downstream jobs from failing partway through because a required file was missing or incomplete at start time.
- The utility returns structured exit codes (100–105) that map directly to specific failure conditions, making it straightforward to diagnose why a prerun check failed.

The file_check utility checks if specified file(s) meet the requested criteria. The file_check utility is useful as a prerun job in OpCon when a job requires a specific file to meet some criteria before the job runs.

:::info Note

File_check returns the correct attributes (read, write, and run) for the non-root UNIX user. For the root user, file_check will always return success for read, write, and run (with some possible exceptions in Linux) attribute check.

:::

## Syntax

```
$SMA_BINDIR/file_check -a<erwx> [-e] –f<filename(s)> or - m<filename(s)>
[-s<#>] [-t<#>]
```

:::info Note

The environment variable ```$SMA_BINDIR``` is defined for use within OpCon jobs. If run from a context other than an OpCon job, "```$SMA_BINDIR/```" must be replaced by the appropriate path.

:::

## Syntax description for file_check

```-a<erwx>```: File attributes to check:

```e```: exists
```r```: read
```w```: write
```x```: run

:::tip Example

The following example shows the command to check file attributes:

```$SMA_BINDIR/file_check –ae –f/home/john/datafile```

:::

```-e```: An optional argument to redirect filename(s) that match the specified criteria to STDOUT in environment variable format. The environment variable format is not standard format.

:::tip Example

The following example shows the both the variable and standard formats:

Variable Format: ```SMA_VAR_#=/usr/local/lsam/bin/genericpgm```

Standard Format: ```/usr/local/lsam/bin/genericpgm```

:::

```-f```: List of file(s) to check with exact filename(s). If checking multiple files, separate the files with commas (,).

:::tip Example

The following examples shows the command for checking file names:

```
$SMA_BINDIR/file_check –ae
-f /home/john/datafile1,/home/john/datafile2
```

:::

```-m```: List of filename pattern(s) to check. If not quoted, only the first file on the system with the pattern match is checked (comma delimited). User may specify how many files are checked within each pattern by specifying an optional number followed by a colon (:).

:::tip Example

The following example shows the command for checking filename patterns:

```-m "/dir/subdir/pattern","1:/anotherdir/subdir/pattern"```

:::

```-s```: An optional argument to further define the file criterion by specifying the minimum size (in bytes) of the file(s).

```-t```: An optional argument to further define the file criterion by specifying the minimum age (in seconds) of the file(s).

:::info Note

All files specified are compared to the attribute (```-a```), size (```-s```), and age (```-t```) criteria. If any of the files fail to meet the criteria, file check exits with a non-zero exit code.

:::

## file_check exit codes


### 0  

All criteria were met 

### 100

Invalid access attributes (-a) argument passed 

### 101

No files were specified to check with the -f and/or –m parameters 

### 102

* User does not have the required access attributes (-a) to the file(s) specified 
* Requested file(s) do not exist
* Requested file(s) reside on an un-mounted file system

### 103 

* User does not have access to the directory (or directories) specified by the match (-m) parameter
* Requested directory (or directories) do not exist
* Requested directory (or directories) reside on an un-mounted file system 

### 104 

The requested file(s) do not meet the size (-s) criteria 

### 105 

The requested file(s) do not meet the age (-t) criteria 

## Exception handling

**Exit code 100** — An invalid value was passed to the `-a` attribute argument. — Verify that the `-a` argument contains only the characters `e`, `r`, `w`, or `x`.

**Exit code 101** — No files were specified. — Confirm that either `-f` or `-m` (or both) is included in the command and that at least one filename or pattern is provided.

**Exit code 102** — The file does not exist, the user lacks the required access permissions, or the file resides on an unmounted file system. — Verify that the file path is correct, that the user running the job has the access specified by `-a`, and that the file system containing the file is mounted.

**Exit code 103** — The directory specified with `-m` does not exist, the user lacks access to it, or it resides on an unmounted file system. — Confirm that the directory path is correct and accessible, and that the file system is mounted.

**Exit code 104** — The file exists but is smaller than the value specified by `-s`. — Either the file has not finished being written, or the expected file content is missing. Check whether the upstream process that creates the file has completed successfully.

**Exit code 105** — The file exists but is newer than the age (in seconds) specified by `-t`. — The file was created or modified more recently than the minimum age required. Wait for the file to age sufficiently, or adjust the `-t` value to match the actual file age expectations.
