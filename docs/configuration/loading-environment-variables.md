# Loading Environment Variables

Some programs/scripts require the assigned user's operating environment (e.g., environment variable definitions, path, UMASK, special time zone settings, and so forth). A setup script must load a user's environment before the LSAM runs the script under the User ID.

SMA Technologies provides three setup scripts to use depending on the UNIX shell. Located in the ```<LSAM root path>/bin``` directory, the scripts are: user_setup.ksh, user_setup.csh, and user_setup.sh. SMA Technologies also provides a program, userinfo, to retrieve a user's information. The program resides in the ```<LSAM root path>/bin``` directory.

## Copy the Required Files

To prepare the system to use the setup scripts and the userinfo program, perform the following steps:

1. Copy the appropriate script from the LSAM 'bin/" directory to the user's home directory or to another directory for setup scripts.

:::tip Example

```cp /usr/local/lsam/bin/user_setup.sh /home/john/user_setup.sh```

:::

2. Change the owner and group of the user_setup script to match the relevant User ID's permissions.

:::tip Example

The user "john" belongs to a group called "users." The system administrator executes the following commands to set the correct owner and group on the user_setup script:

```chown john /home/john/user_setup.sh```

```chgrp users /home/john/user_setup.sh```

:::

3. Copy userinfo to the /bin directory

:::tip Example

```cp /usr/local/lsam/bin/userinfo /bin/userinfo```

:::

## Edit the User Setup Script

There are two sections of the user_setup script requiring review: Setting Environment Variables, and Determining File Type.

:::caution

If the user's .profile or .cshrc is an interactive script, the user_setup script does not work. For these cases, also review the third section Set Environmental Values. Replace the line in the third section that executes the .profile (i.e., . ./.profile) with definitions of all environment variables, aliases, and so forth that are required to run this user's scripts. The following excerpt is the portion of the script that executes the .profile.

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

### Set Environment Variables

Under the script heading Setting Environment Variables, define the HOME and LOGNAME variables. There are two options for setting these variables:

Remove the comment symbols (#) from the HOME and LOGNAME variables using the userinfo program, and enter the correct path to the userinfo program. This option configures the script to be usable for any GID/UID the LSAM receives.

:::tip Example

On a machine with the userinfo program in the /bin directory, edit the script to contain the boldface information below.

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

 For the user named "john", edit the user_setup script to contain the boldface information below.

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

## Determine the File Type

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

### Enter the Start Image in OpCon

The Start Image line on the UNIX Details screen (in the Enterprise Manager's Job Master) must contain either the full or relative path to the user_setup script or job. To specify relative path, use "." or "~username" (provided that path_to_su is enabled). For information on defining a job in the Enterprise Manager, refer to [Adding Jobs](adding-jobs) in the Enterprise Manager online help.


:::tip Example

The Start Image in the Enterprise Manager for a job called /usr/local/payroll/timecalc would contain the following:

```/home/john/user_setup.sh /usr/local/payroll/timecalc```

:::