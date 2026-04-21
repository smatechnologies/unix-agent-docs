---
sidebar_label: 'Security configuration options'
title: Unix Security Configuration Options
description: "Reference for configuring black list and white list security settings in the Unix Agent to control which users are permitted to run jobs."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Unix security configuration options

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for configuring black list and white list security settings in the Unix Agent to control which users are permitted to run jobs.

## When would you use it?

Configure black lists or white lists when:

- Specific user accounts must be prevented from running any jobs — including file transfer jobs — on the agent, regardless of how those jobs are submitted.
- Access to the agent must be restricted to a defined set of approved users, so that any user not explicitly listed in the white list is denied the ability to run jobs.
- The root user or another privileged account needs to be blocked from running jobs directly through the agent, and the `maintain_ofiles` program must be run through an alternative mechanism such as cron.

The Unix Agent security configuration options are White lists and Black lists. If a user is listed in the black list, they cannot run any jobs (regular or file transfer jobs). If **any** user is defined in the white list entry, then **all** users MUST be defined by a white list entry in order to run jobs referencing that user.

The black list/white list processing rules are:

* If neither black lists nor white lists are present, the agent will work the way it always has.

* If a black list is defined (one or more valid black list users are defined) and a user is present in the black list, then all jobs referencing that user will be dis-allowed.

* If a white list is defined (one or more valid white list users are defined), then each user **must** be defined in the white list to run jobs.

The black and white lists are defined in the lsam.conf file. There can be any number of black list or white list users. Each user is defined on one line with the type of check to make (black or white) and your gid/uid.

:::tip Example

```
#blacklist/whitelist parameters
blacklist_user 0/0
blacklist_user root/system
```

:::

The gid is your group id from the /etc/group file and the uid is you id from the /etc/passwd file. The agent code will automatically recognize any valid gid/uid combinations stored in any network password system supported by the operating system that is properly configured (NIS, NIS+, etc.).

The code will not use or store any invalid (i.e., non-existent) gid/uid combinations – it is if the data was never entered. A gid or uid may either be entered as a name or as a number. If your "id" program does not list all uid and gid information, then looking at /etc/passwd and /etc/group can help resolve these values.

If there is any question as to whether a specific user will be allowed or denied, it is recommended that all possible gid/uid combinations be explicitly added to the lsam.conf file. It is strongly recommended that users perform rigorous testing on the targeted operating system.

It is highly advisable to periodically review agent log files and job files for any issues/errors that may creep into the black/white lists over time. Because the black/white lists are a user configured item, SMA Technologies can give limited help/advice on what to do with particular users. If the root user is denied the right to run programs, the maintain_ofiles program will need to be run through an alternative mechanism (cron, manual runs, scripts, etc.).

:::info Note

If white lists or black lists are modified while the agent is running, the agent will need to be restarted to read the new/modified parameters.

:::
