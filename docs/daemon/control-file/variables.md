---
title: Variables
description: "Reference for the SMA FAD event string variables and condition variables, including token substitutions for file path, name, and extension, as well as supported file condition types."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Variables

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the SMA FAD event string variables and condition variables, including token substitutions for file path, name, and extension, as well as supported file condition types.

The SMA FAD supports several variables in the event strings. Before sending the event string to the SAM for processing, SMA FAD replaces the variables with their current values. The variables retrieve values from the `<filemask>` element in the associated record block, allowing the forwarded OpCon events to include dynamic information — such as the full file path, the file name, or the file extension — that is only known at the time a monitored condition is detected.

- Use `%FULLNAME%` in an event string when the receiving OpCon event or SAM process needs the complete path and file name of the detected file — for example, to pass the exact file location to a downstream job.
- Use `%PATHNAME%` when only the directory path (excluding the file name and trailing slash) is needed in the event string — for example, to reference the directory in which the file was detected.
- Use `%FILENAME%` when only the file name (without the path) is needed — for example, to display or log which file triggered the event.
- Use `%FILEROOT%` when you need the base name of the file without its extension — for example, to set a threshold whose name corresponds to the file root, as shown in the `$THRESHOLD:SET,%FILEROOT%,1,BatchUser,BatchPwd` event pattern.
- Use `%FILEEXT%` when only the file extension is needed — for example, to confirm the file type in a console display event.

The following variables retrieve values from the ```<filemask>``` element in the associated record block:

* ```%FULLNAME%```: Full path and filename
* ```%PATHNAME%```: Path name of the file's location, excluding the last slash (/)
* ```%FILENAME%```: The file name alone
* ```%FILEROOT%```: Part of the filename up to but excluding the last dot (.)
* ```%FILEEXT%```: The end of the filename beginning after the last dot (.)

:::info Note 

All tokens are case sensitive.

:::

## FAD condition variables

* CREATE: Checks to see if a file has been created since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not grown in the last MINTIMETOWAIT seconds. FAD will run the associated event(s) once the file has stopped changing size.
* DELETE: Checks to see if a file has been deleted since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not been in existence in the last MINTIMETOWAIT seconds. FAD will run the associated event(s) once the file has ceased to exist.
* GROWTH: Checks to see if a file has had new bytes written to the file since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that no bytes have been written in the last MINTIMETOWAIT seconds. FAD will run the associated event(s) once the file has stopped changing size.
* SHRINK: Checks to see if a file has become smaller since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not grown smaller in the last MINTIMETOWAIT seconds. FAD will run the associated event(s) once the file has stopped changing size.
* ABSOLUTE: Checks to see if a file has exactly the specified number of bytes. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has grown/shrunk to the specified number of bytes after MINTIMETOWAIT seconds. FAD will run the associated event(s) once the file has reached the specified size.
* MODIFY: Checks to see if a file has been modified. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not been modified in the last MINTIMETOWAIT seconds. FAD will run the associated event(s) once modifications to the file have stopped.