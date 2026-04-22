---
title: Stream and Record Files
description: "SMAFT includes a UNIX-specific feature that preserves the record structure of files transferred from non-UNIX platforms, enabling round-trip transfers with record structure intact."
tags:
  - Conceptual
  - Reference
  - System Administrator
  - Agents
---

# Stream and Record Files

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
SMAFT includes a UNIX-specific feature that preserves the record structure of files transferred from non-UNIX platforms, enabling round-trip transfers with record structure intact.

Files on a UNIX system are maintained by the operating system as streams (i.e., ordered, amorphous collection of bytes). For example, the 114th will result in return of the same data as long as the file has not been updated. Although various applications (e.g., a database manager) might organize the data into a different structure, neither the operating system nor any other non-specific application (including the Unix Agent) will have any knowledge of this structure. In contrast, operating systems on some platforms (e.g., OS2200) organize files into records. Records within a file may be of equal (fixed) or of unequal (variable) length. Records may be separated based on their length or by some particular sequence of data (e.g., a linefeed character). Applications read and write entire records at once, rather than individual bytes as with UNIX.

When a UNIX Agent receives a file, its default behavior is to ignore any record structure transmitted by the Server and to store the file as a stream file, as described in the preceding paragraph. If the file is subsequently requested to be transferred to its original system, or to any other system which supports the concept of records, it will be transferred as a structure-less stream of bytes. The receiving Server will do its best to give it some structure, but it may not be correct for the intended application.

A feature of SMAFT specific to UNIX platforms allows for retention of record structure so that files may be sent to a UNIX system from a non-UNIX system, and later retrieved by a (possibly different) non-UNIX system with the record structure intact. This feature is agent-specific and will not be usable by any application which may reside on the same system. If some application supports multiple platforms, it should include an import utility to make a file transferred from a non-UNIX system usable to it – and you will need to run it whether or not the SMAFT feature being described here was used to transfer the file.

This feature is invoked by pre-pending an equals sign ('=') to either the Source or Destination filename when filling in the Job Details screen in the Enterprise Manager (e.g., "=/usr/FMS/data/tn465.dat"). It should be noted here that only absolute pathnames are allowed (e.g., "./stuff.txt" and "~/this/that/other.data" are not allowed). As a visual indicator, the '=' sort of looks like: "divided into lines".

When '=' is pre-pended to the Source filename, it instructs the Server to send the record-structure data with the file. This means that the file must have first been transferred to the system and processed by the Agent as a record file (so that an ".idx" file exists). If the Server detects that this is not the case, it will abort the transfer with an appropriate message to the requesting Agent (which will be shared in some form with you). The file may still be sent as a stream file by not pre-pending an equal sign to the Source filename.

- Use the `=` prefix on the Destination filename when receiving a file from a non-UNIX platform and you need to preserve the record structure for a later transfer back to a non-UNIX system.
- Use the `=` prefix on the Source filename when retrieving a file that was previously stored on UNIX with record-structure data (when an `.idx` file exists alongside the data file) and the destination system requires the record structure.
- Preserving record structure on round-trip transfers ensures the receiving system can reconstruct the file in the format its applications expect, rather than receiving a structureless stream of bytes.

## Examples

A file named `tn465.dat` originates on OS2200, a platform that uses fixed-length records. You need to stage the file on a UNIX system and later retrieve it for use on another non-UNIX system.

**Transfer to UNIX:** Set the Destination filename to `=/usr/FMS/data/tn465.dat`. The Agent stores the file as a stream file and also writes an `.idx` file containing the record-structure data alongside it.

**Transfer from UNIX:** Set the Source filename to `=/usr/FMS/data/tn465.dat`. The Server detects the `.idx` file and sends the record-structure data with the file. If the Server detects that no `.idx` file exists, it aborts the transfer with an appropriate message. The file can always be sent as a stream file by omitting the `=` prefix from the Source filename.

## Glossary

**Stream file** — A file maintained by the UNIX operating system as an ordered, amorphous collection of bytes with no record structure recognized by the operating system or the Unix Agent. This is the default storage format for all files received by a Unix Agent unless the `=` prefix is used.

**`.idx` file** — A file written by the Unix Agent alongside a data file when the `=` prefix is applied to the Destination filename. The `.idx` file stores the record-structure data transmitted by the Source Server so that the structure can be sent with the data file when it is later transferred to a non-UNIX system. If no `.idx` file exists when the `=` prefix is applied to the Source filename, the Server aborts the transfer.