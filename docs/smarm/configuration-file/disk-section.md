# DISK Section

Disk monitoring is specified via one or more ```<disk>``` sections, as shown in the following template:

```

<disk>

<alarm_level>____</alarm_level>

<window>____</window>

<name>____</name>

<mount_point>____</mount_point>

<usage>[ MIN | MAX ]____</usage>

<log>NONE | SCANS | EVENTS</log>

<alarm>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</alarm>

<normal>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</normal>

</disk>

``` 

All entities within ```<disk>``` are optional except for ```<usage>```. Duplicate entities constitute an error.

```<alarm_level>``` is discussed below in "Multiple Alarm Levels".

```<name> ```specifies the name of the disk(s) as displayed by a UNIX 'df' command. ```<mount_point>``` likewise specifies the mount point for the disk(s) as displayed by a 'df' command. Both are used to specify the disk(s) to monitor and are combined using an implied AND conjunction, i.e., a disk must match both to be processed. For either, an asterisk ('\*') can be used as a wildcard character at either the beginning or at the end: at the end it means "begins with", at the beginning it means "ends with", and at both ends means "contains". 

A lone '*' means "matches all", as does an unspecified ```<name>``` or ```<mount_point>```. The contents of the ```<name>``` and ```<mount_point> ```entities are case-sensitive. If neither is specified, then this ```<disk>``` section applies to all disks output by a 'df' command. ```<window>``` defines when the disk(s) will be monitored.

```<usage>``` is the integer percent of total disk space in use which constitutes an alarm. MIN or MAX may be included with the value to set the type of the value, which has a default type of MAX. If MIN or MAX is specified, at least one space must appear between the MIN or MAX and the value. 

```<log>``` specifies what, if any, values for disk usage will be logged. ```<alarm>``` defines what is to occur when disk usage goes into alarm, and will be discussed later under "Exception Handling". Likewise with ```<normal>``` which defines what is to occur when disk usage returns to a normal status. The event variables available within the ```<alarm>``` and ```<normal>``` specifications are as follows:

* ```%NAME% ```= the name of the disk.
* ```%MOUNT_POINT%``` = the mount point for the disk.
* ```%USAGE%``` = the percent of space in use.