# Unix Security Configuration Options

The UNIX LSAM security configuration options are White lists and Black lists. If a user is listed in the black list, they cannot run any jobs (regular or file transfer jobs). If **any** user is defined in the white list entry, then **all** users MUST be defined by a white list entry in order to run jobs referencing that user.

The black list/white list processing rules are:

* If neither black lists nor white lists are present, the LSAM will work the way it always has.

* If a black list is defined (one or more valid black list users are defined) and a user is present in the black list, then all jobs referencing that user will be dis-allowed.

* If a white list is defined (one or more valid white list users are defined), then each user **must** be defined in the white list to run jobs.

The black and white lists are defined in the lsam.conf file. There can be any number of black list or white list users. Each user is defined on one line with the type of check to make (black or white) and the user's gid/uid.

:::tip Example

```
#blacklist/whitelist parameters
blacklist_user 0/0
blacklist_user root/system
```

:::

The gid is the user's group id from the /etc/group file and the uid is the user id from the /etc/passwd file. The LSAM code will automatically recognize any valid gid/uid combinations stored in any network password system supported by the operating system that is properly configured (NIS, NIS+, etc.).

The code will not use or store any invalid (i.e., non-existent) gid/uid combinations – it is if the data was never entered. A gid or uid may either be entered as a name or as a number. If your "id" program does not list all uid and gid information, then looking at /etc/passwd and /etc/group can help resolve these values.

If there is any question as to whether a specific user will be allowed or denied, it is recommended that all possible gid/uid combinations be explicitly added to the lsam.conf file. It is strongly recommended that users perform rigorous testing on the targeted operating system.

It is highly advisable to periodically review LSAM log files and job files for any issues/errors that may creep into the black/white lists over time. Because the black/white lists are a user configured item, SMA Technologies can give limited help/advice on what to do with particular users. If the root user is denied the right to run programs, the maintain_ofiles program will need to be run through an alternative mechanism (cron, manual runs, scripts, etc.).

:::info Note

If white lists or black lists are modified while the LSAM is running, the LSAM will need to be restarted to read the new/modified parameters.

:::