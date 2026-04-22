---
title: STDERR - Pre-processing Errors
description: "Reference for STDERR pre-processing error messages written when file transfer job requirements cannot be met before the transfer begins."
tags:
  - Reference
  - System Administrator
  - Agents
---

# STDERR - Pre-processing errors

**Theme:** Troubleshoot  
**Who Is It For?** System Administrator

## What is it?
Reference for STDERR pre-processing error messages written when file transfer job requirements cannot be met before the transfer begins.

Pre-processing errors are written to a job's STDERR file when the job requirements could not be met.

- A file transfer job fails before the transfer begins and you need to identify the pre-processing error written to the job's STDERR file.
- A transfer is aborted due to access, permission, or path issues on the source or destination file.
- Compression or encryption settings cannot be met by both machines and you need to understand the resulting error message.
- You need to determine why a file transfer job was aborted before any data was transferred.

### User does not have required access to Source File [file]	

**Origination**: FTServer

The file transfer was aborted because you did not have Read access to the Source File.

### User does not have required access to Destination File [file]	

**Origination**: FTAgent

The file transfer was aborted because you did not have Write access to the Destination File, or Create access to the Destination directory.

### Invalid path component in Destination File [file]	

**Origination**: FTAgent

The file transfer was aborted because you specified a non-existent directory within the path portion of the Destination File, i.e., that portion of the Destination File prior to the final '/' in the filename.

### Destination File [file] already exists and overwrite not allowed	

**Origination**: FTAgent

The file transfer was aborted because the Destination File already existed and you specified "Do Not Overwrite" for the job's "Overwrite" option.

### Could not back-up Destination File [file] (indicator)	

**Origination**: FTAgent

* The file transfer was aborted because the Destination File could not be backed up as you specified for the job's "Overwrite" option.
* The indicator field provides the specific reason.

### Compression REQUIRED but not supported by both machines	

**Origination**: FTAgent

The file transfer was aborted because compatible forms of file compression were not available on both the Source and Destination machine.

### Compression is FAIL-PREFERRED but not supported by both machines -- Continuing without compression - job status will be FAILED...

**Origination**: FTAgent

* The file transfer was initiated without file compression.
* If it was successful, the Enterprise Manager reported the job as Failed because you checked the "Send fail..." box under Failure Criteria in the Job Details screen.

### Compression is not supported by both machines -- Continuing without compression...

**Origination**: FTAgent

The file transfer was initiated without file compression.

### Encryption REQUIRED but not supported by both machines	

**Origination**: FTAgent

The file transfer was aborted because compatible forms of file encryption were not available on both the Source and Destination machine.

### Encryption is FAIL-PREFERRED but not supported by both machines -- Continuing without encryption - job status will be FAILED...

**Origination**: FTAgent

* The file transfer was initiated without file encryption.
* If it was successful, the Enterprise Manager reported the job as Failed because you checked the "Send fail..." box under Failure Criteria in the Job Details screen.

### Encryption is not supported by both machines -- Continuing without encryption...

**Origination**: FTAgent

The file transfer was initiated without file encryption.

### Unsupported Data Type [type]	

**Origination**: FTServer or FTAgent

The file transfer was aborted because the indicated data type is not supported.

### Cannot process ```<CommonCharSet>``` of [charset]	

**Origination**: FTAgent

FTAgent is unable to translate the intermediate character set chosen by the FTServer to affect the transfer when source and destinations data types differ.

