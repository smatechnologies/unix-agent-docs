---
sidebar_label: 'Configuring time zone'
title: Configuring the Time Zone in the Root Profile
description: "Instructions for setting the TZ environment variable in the root profile or agent startup script to ensure the Unix Agent uses the correct time zone."
tags:
  - Procedural
  - System Administrator
  - Agents
---

# Configuring the time zone in the root profile

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Instructions for setting the TZ environment variable in the root profile or agent startup script to ensure the Unix Agent uses the correct time zone.

Configure the time zone when:

- The `TZ` environment variable is not set in the root user's environment and you need the agent to use a time zone other than the default of `EST5EDT`.
- The system operates in a time zone that differs from the default, and jobs must be scheduled or logged using the correct local time.

- Setting `TZ` in the agent startup script or the root profile ensures the agent always starts with the correct time zone regardless of how the system-wide default is configured.

## How to implement it

To configure the time zone for the Unix Agent, complete the following steps:

- [Set `TZ` in the root user profile](#configuring-the-time-zone-in-the-root-profile) — edit the root user's `.profile` or `.cshrc` to export the `TZ` variable, or set it system-wide through the appropriate system configuration file for your UNIX variant.
- [Set `TZ` in the agent startup script](#configuring-the-time-zone-in-the-root-profile) — add a `TZ=<identifier>; export TZ` line to the `lsam<SAM_Socket>` file in `$LSAM_ROOT/bin/` so the agent always starts with the correct time zone regardless of the user environment.

## Exception handling

**Agent logs and job start times appear in the wrong time zone after setting `TZ`** — The `TZ` variable was set in the root profile but the agent was already running when the change was made, so it inherited the previous value. — Stop the agent, confirm the `TZ` variable is set correctly in the current shell by running `env | grep TZ`, then restart the agent so it picks up the updated value.

**`TZ` identifier is rejected or the agent still defaults to `EST5EDT`** — The time zone identifier supplied is not valid for the UNIX variant in use; identifier formats differ across AIX, Linux, Solaris, and HP-UX. — Consult the system administrator for a list of valid identifiers for the installed UNIX version, or check the system's `zoneinfo` database (typically located in `/usr/share/zoneinfo/`).

**Setting `TZ` in `.profile` has no effect when the agent starts automatically** — When the agent starts through the init system at boot, it may not source the root user's `.profile`, so the profile-level `TZ` setting is never applied. — Set the `TZ` variable directly in the agent startup script (`lsam<SAM_Socket>` in `$LSAM_ROOT/bin/`) to ensure the value is always present regardless of how the agent is started.

Before starting the Unix Agent, set the TZ (time zone) environment variable in the root user's environment. To verify the current setting, log in as the root user and enter "env". If the TZ environment variable is not set, the agent uses a default time zone of EST5EDT.

* To set the TZ environment variable for root, edit the .profile (or .cshrc depending on which shell is used) file in the home directory of the root user.

* To set the TZ environment variable for all users, consult the system administrator. The system wide setting for the TZ environment variable is different for different versions of UNIX. (For example, AIX keeps its system wide environment settings in /etc/environment. Linux keeps its system wide environment settings in /etc/profile.)

* To set the TZ environment variable in the agent startup script, edit the ```lsam<SAM_Socket>``` file in the $LSAM_ROOT/bin directory. Add a line to the agent startup script that looks like the following:

```TZ=xxxxxxxxxx; export TZ```
    
* xxxxxxxxx is the identifier for the desired time zone.

:::info Note

Time zone identifiers vary on different versions of UNIX. For a list of valid identifiers, see the system administrator.

:::
