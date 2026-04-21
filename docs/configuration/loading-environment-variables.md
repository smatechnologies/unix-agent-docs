---
sidebar_label: 'Loading environment variables'
title: Loading Environment Variables
description: "Instructions for using SMA Technologies-provided setup scripts and the userinfo program to load a user's operating environment before the Unix Agent executes a job."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Loading environment variables

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Instructions for using SMA Technologies-provided setup scripts and the userinfo program to load a user's operating environment before the Unix Agent executes a job.

## When would you use it?

Set up environment variables when:

- A job script requires the assigned user's operating environment — including variable definitions, PATH, UMASK, or special time zone settings — before it can run correctly under that User ID.
- A job fails or produces unexpected results because environment variables such as `HOME`, `LOGNAME`, or `PATH` are not defined when the agent runs the script.

## Why would you use it?

- Loading a user's operating environment before a job runs ensures that programs and scripts behave the same way whether they are run manually by the user or run by the agent on that user's behalf.
- Using the SMA Technologies-provided setup scripts and the `userinfo` program lets a single configured script work for any valid GID/UID the agent receives, reducing per-user maintenance.

Some programs/scripts require the assigned user's operating environment (e.g., environment variable definitions, path, UMASK, special time zone settings, and so forth). A setup script must load a user's environment before the agent runs the script under the User ID.

SMA Technologies provides three setup scripts to use depending on the UNIX shell. Located in the ```<LSAM root path>/bin``` directory, the scripts are: user_setup.ksh, user_setup.csh, and user_setup.sh. SMA Technologies also provides a program, userinfo, to retrieve a user's information. The program resides in the ```<LSAM root path>/bin``` directory.

## Copy the required files

To prepare the system to use the setup scripts and userinfo program, complete the following steps:

1. Copy the appropriate script from the agent 'bin/" directory to your home directory or to another directory for setup scripts.

:::tip Example

```cp /usr/local/lsam/bin/user_setup.sh /home/john/user_setup.sh```

:::

2. Change the owner and group of user_setup script to match the relevant User ID's permissions.

:::tip Example

User "john" belongs to a group called "users." The system administrator runs the following commands to set the correct owner and group on user_setup script:

```chown john /home/john/user_setup.sh```

```chgrp users /home/john/user_setup.sh```

:::

3. Copy userinfo to the /bin directory.

:::tip Example

```cp /usr/local/lsam/bin/userinfo /bin/userinfo```

:::

The system is ready to use the setup scripts and userinfo program.

## Edit the user setup script

There are two sections of user_setup script requiring review: Setting Environment Variables, and Determining File Type.

:::caution

If your .profile or .cshrc is an interactive script, user_setup script does not work. For these cases, also review the third section Set Environmental Values. Replace the line in the third section that executes the .profile (i.e., . ./.profile) with definitions of all environment variables, aliases, and so forth that are required to run this user's scripts. The following excerpt is the portion of the script that executes the .profile.

```
# ************************************************************
# (3) Set environmental values.
#
#
#
# cd $HOME
# . ./.profile
```

:::

### Set environment variables

Under the script heading Setting Environment Variables, define the HOME and LOGNAME variables. There are two options for setting these variables:

Remove the comment symbols (#) from the HOME and LOGNAME variables using userinfo program, and enter the correct path to userinfo program. This option configures the script to be usable for any GID/UID the agent receives.

:::tip Example

On a machine with userinfo program in the /bin directory, edit the script to contain the boldface information below.

```
# Setting Environment Variables
# -----------------------------
# This script sets up the environment by allowing the
# specification of environment variables before executing the
# actual job. If the user's .profile or .cshrc is NOT
# interactive, it can be invoked here as well.
#
# The environment variables HOME, LOGNAME, and PATH should
# be set at a minimum. For example:
#
# HOME=/usr/smauser; export HOME
# LOGNAME=smauser; export LOGNAME
# PATH=/usr/bin; export PATH
#
# An alternate method of establishing an environment is to copy
# the program userinfo from the $LSAM_ROOT/bin directory to a
# common directory (for example, /bin) and make it executable by
# everyone. Environment variables can then be retrieved from
# the system. For example:
#
# n/userinfo -h`; export HOME
# LOGNAME=`/bin/userinfo -n`; export LOGNAME
#
# The path should be set as well. The path can be obtained from
# the .profile file.
#
# (file continues here)
#
# (file continues here)
```

:::

\- or \- 

Remove the comment symbols (#) from the HOME, PATH, and LOGNAME variables. Code the variable definitions.

:::tip Example

 For user named "john", edit user_setup script to contain the boldface information below.

```
# Setting Environment Variables
# -----------------------------
# This script sets up the environment by allowing the
# specification of environment variables before executing the
# actual job. If the user's .profile or .cshrc is NOT
# interactive, it can be invoked here as well.
#
# The environment variables HOME, LOGNAME, and PATH should
# be set at a minimum. For example:
#
# HOME=/home/john; export HOME
# LOGNAME=john; export LOGNAME
# PATH=/usr/bin; export PATH
#
# An alternate method of establishing an environment is to copy
# the program userinfo from the $LSAM_ROOT/bin directory to a
# common directory (for example, /bin) and make it executable by
# everyone. Environment variables can then be retrieved from
# the system. For example,
#
# HOME=`/bin/userinfo -h`; export HOME
# LOGNAME=`/bin/userinfo -n`; export LOGNAME
#
# The path should be set as well. The path can be obtained from
# the .profile file.
#
# (file continues here)
#
# (file continues here)
```

:::

## Determine the file type

Under the script heading Determining File Type, define the FILE_FIELD_NUM and SCRIPT_INDICATOR variables.

:::tip Example

On a Solaris 5.7 machine, edit the script to contain the boldface information below.

```
# Determining File Type
# ---------------------
# This script needs to determine if it is to execute a script or
# an executable program since the invocation of each is somewhat
# different. The system commands "file" and "cut" are used to
# make this determination by examining the file type of the
# object to be executed. (Therefore, file and cut must be in the
# path. Usually, these utilities are in the /bin directory.)
#
# (Documentation continues here)
#
# Some known values are:
#
#
# OS Field Number Field Value
# ________________ ____________ ___________
# AIX 3.2 2 text
# AIX 4.3 2 script
# DYNIX PTX 4.4.5 3 text
# HP-UX 10.20 2 text
# HP-UX 11 2 text
# LINUX 6.2 4 script
# LINUX 7.0 4 script
# OpenServer 5.0.5 3 text
# Solaris 5.7 3 script
#
# If this script still doesn't appear to run correctly or if the
# installation is on an operating system that is not listed, run
# the file command against a script and then against an
# executable to determine appropriate values.
# ----------------------------------------------------------------
# ****************************************************************
# (2) Set values for FILE_FIELD_NUM and SCRIPT_INDICATOR.
# THESE VALUES MUST BE OVERRIDDEN!
#
# FILE_FIELD_NUM=3
# SCRIPT_INDICATOR="script"
#
# (file continues here)
```

:::

### Enter the start image in OpCon

The Start Image line on the UNIX Details screen (in the Enterprise Manager's Job Master) must contain either the full or relative path to user_setup script or job. To specify relative path, use "." or "~username" (provided that path_to_su is enabled). For information on defining a job in the Enterprise Manager, refer to [Adding Jobs](https://help.smatechnologies.com/opcon/core/Files/UI/Enterprise-Manager/Adding-Jobs) in the Enterprise Manager online help.


:::tip Example

The Start Image in the Enterprise Manager for a job called /usr/local/payroll/timecalc would contain the following:

```/home/john/user_setup.sh /usr/local/payroll/timecalc```

:::

## Exception handling

**Job fails because `HOME`, `LOGNAME`, or `PATH` are not defined when the script runs** — The `user_setup` script has not been edited to define or retrieve these variables, leaving the environment incomplete when the agent runs the job under the assigned User ID. — Under the "Setting Environment Variables" section of the script, either hard-code the `HOME`, `LOGNAME`, and `PATH` values for the target user, or configure the script to retrieve them dynamically using `userinfo` (for example, `HOME=\`/bin/userinfo -h\`; export HOME`).

**`user_setup` script fails or produces unexpected results when sourcing `.profile`** — The user's `.profile` or `.cshrc` is an interactive script that cannot run non-interactively, as noted in the caution on this page. — Replace the line that sources `.profile` (`. ./.profile`) in section 3 of `user_setup` with explicit variable definitions for all environment variables required by that user's jobs.

**`userinfo` program is not found when the script runs** — The `userinfo` binary was not copied to a directory that is in the `PATH` used by the agent at job run time. — Copy `userinfo` from `<LSAM root path>/bin/` to a common directory such as `/bin/` and verify that the directory is included in the `PATH` variable set within the `user_setup` script.
