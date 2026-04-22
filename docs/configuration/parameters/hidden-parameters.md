---
sidebar_label: 'Hidden Agent Configuration Parameters'
title: Hidden agent Configuration Parameters
description: "Reference for Unix Agent hidden configuration parameters, including lsam_root_directory, check_CRC, and close_SAM_socket, which are only editable directly in the lsam.conf file."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Hidden agent configuration parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for Unix Agent hidden configuration parameters, including lsam_root_directory, check_CRC, and close_SAM_socket, which are only editable directly in the lsam.conf file.

- When directed by SMA Technologies Support to modify a hidden parameter directly in the `lsam.conf` file
- When reviewing the `lsam.conf` file to understand the location of the installation directory, CRC checking status, or SAM socket behavior

There are three agent configuration parameters which are not meant to be changed except under limited circumstances, and these are not displayed in the agent Configuration Utility. They are contained within the actual agent configuration file, "```$LSAM_ROOT/config/<LSAM_instance>/lsam.conf```", and can only be changed by editing this file. SMA Technologies strongly recommends that these parameters not be changed unless so-directed by an SMA Technologies Support person, and that the agent configuration file not otherwise be edited. The parameters are:

### lsam_root_directory

* The location of the top-level installation directory, ```$LSAM_ROOT```.

### check_CRC

* Enable/Disable CRC checking.

### close_SAM_socket

* Keep socket to SAM open across messages, or close after each message.


Each parameter in the file appears on a line by itself, of the form "Parameter = value", e.g., "check_CRC = 1". The file also contains comments, indicated by a '#', with the '#' and the remainder of the line being ignored by the agent as it processes the file.
