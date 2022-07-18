# Exception Handling/Alarm Levels

## Exception Handling

The various exception-handling specifications define what is to be done when an alarm occurs and when conditions return to normal, as discussed in the preceding sections. Each exception-handling specification may contain any number, and in any order, of ```<event>```, ```<action>```, and ```<sleep>``` specifications, to be executed from top-to-bottom within the exception-handling specification.

"```<event> event_string </event>```" specifies an OpCon event to be sent to SAM. Event_string extends from the first non-space/tab/line-feed past "```<event>```" to the last non-space/tab/line-feed before "```</event>```". Any embedded line-feeds will be discarded. If event_string contains no percent signs ('%'), it is sent exactly as specified.

If event_string contains a '%', then, either the very next character must also be a '%', in which case a single '%' will be sent to SAM at that position in event_string. Or, the '%' must be followed, without embedded spaces/tabs, by an event variable allowed within the particular type of event and terminated with a second '%', in which case, the "%variable%" will be replaced in the event sent to SAM by the appropriate value. For example, the "```<disk>…<alarm>```" event string:

```$CONSOLE:DISPLAY,<DISK [%MOUNT_POINT%] IS %USAGE%%% FULL!>```

Would get sent to SAM as:

```$CONSOLE:DISPLAY,<DISK [/usr] IS 80% FULL!>```

Assuming ```%MOUNT_POINT% = "/usr" ```and ```%USAGE% = "80"```.

"```<action> filename [ parameter(s) ] </action>```" specifies local processing to be initiated. Filename is the complete pathname of a Shell script or program to be executed. Parameter(s) is text that is to be passed to the Shell script or program as it is launched. 

As with an event_string, the '%' character must either be doubled to have a single '%' passed to the script/program, or two are used to reference an event variable. 

Embedded blanks/tabs within parameter(s) are used to break it into the actual start parameters to be passed to the script/program. The time stamp associated with the current scan will be appended to the call. For example:

```<action>/usr/act/disk %MOUNT_POINT% "Status = ALARM" %USAGE%%%<action> ```

Would, assuming ```%MOUNT_POINT% = "/usr"``` and ```%USAGE% = "80"```, result in a call to "```/usr/act/disk```" similar to:

```/usr/act/disk /usr "Status = ALARM" 80% 'Wed Mar 12 09:50:27 CDT 2017'```

"```/usr/act/disk```" would see five command-line arguments:

```

$0 = /usr/act/disk

$1 = /usr

$2 = Status = ALARM

$3 = 80%

$4 = Wed Mar 12 09:50:27 CDT 2017

```

An action is normally executed synchronously, i.e., SMA_RM will wait for it to complete. They can also be made to run asynchronously, by placing an ampersand ('&') at the very end of parameter(s), in which case the ampersand will be replaced by the time stamp and SMA_RM will not wait for the script/program to complete. 

It is analogous to using the ampersand on a UNIX Shell command line to run something in the background. The above action, coded to be executed synchronously, would be:

```<action>/usr/act/disk %MOUNT_POINT% "Status = ALARM" %USAGE%%% &<action>```

Other than to launch it and to wait on it to terminate if it is not run asynchronously, there is no interaction between an action and SMA_RM. 

"```<sleep> # </sleep>```", where '#' is a positive integer, will cause SMA_RM to delay for the specified number of seconds. This will increase the time required to complete the current scan cycle by that number of seconds.

An exception-handling specification must include at least one ```<event>``` or ```<action>``` tag.

## Multiple Alarm Levels

It may be desirable to have SMA_RM generate different events to SAM based on multiple conditions for the same monitored resource(s). For example, disk "/usr" is referenced in one ```<disk>``` specification to send one event if the usage exceeds 80 percent and in a second ```<disk>``` to send a different event if the usage exceeds 90 percent. In the first case, it may be a $JOB event to perform some clean-up, and assuming that was not sufficient and the disk's free space continued to shrink, the second event could be a $CONSOLE event to notify an operator that immediate human intervention is required. This behavior is made possible via the ```<alarm_level>``` entity.

```<alarm_level>``` is a positive integer which allows for multiple ```<disk>```, ```<process>,``` and ```<user_defined>``` sections which reference the same disk, process, or user-defined resource(s) to have events generated in a severity-based hierarchy. Such sections must appear within the SMA_RM Config File in ascending ```<alarm_level>```, with a slight change for ```<user_defined> ```sections as will be explained below.

The values chosen for ```<alarm_level>``` are arbitrary, with the provisos that a more severe condition be given a higher alarm level than a less severe condition and that alarm levels be unique within each resource. For example, two sections which reference disk "/usr" must have unique alarm levels; but, one section which references "/usr" and another section which references "/data" may both be defined to be alarm level 2. At present, SMA_RM performs no consistency checks.

Alarm level processing works as follows: when SMA_RM starts up, all resources are assumed to have an alarm level of 0 (zero – not in alarm). As each applicable ```<disk>```, ```<process>```, or ```<user_defined>``` section is executed, the resource's current alarm level is compared to that defined for the section. If the alarm level defined for the section is lower than the resource's current alarm level, any additional processing defined for this section is aborted. 

If, however, the alarm level defined for this section is at-or-above the current alarm level for the resource, then the NORMAL/ALARM status (per this section) of the resource is determined and any associated exception handling executed if the status changes. Also, if its new status is ALARM, the resource's alarm level will be set to the section's alarm level, and if it is NORMAL, the resource's alarm level will be reset to its previous setting.

Once an alarm/normal transition has occurred for any given multi-level alarm resource, further processing of that resource will be inhibited for the remainder of the current scan cycle. To see what this means, suppose that a disk is set to alarm when usage hits 70% and again at 80%. Further suppose that the current usage is at 67% (normal) and a user creates a monster file which within one scan cycle brings the usage to 82%. 

On the first scan cycle after creation of the file, SMA_RM will see disk usage as 82% and execute the 70% alarm. Assuming that disk usage remains at-or-above 80%, the 80% alarm will get executed during the following scan cycle. A similar scenario would unfold if that monster file was deleted, the 80% all-clear would be executed on the next scan, and the 70% all-clear (return to normal) on the scan after that.

Continuing with the example for disk "/usr", the applicable ```<disk>``` sections might resemble:

```

<disk>

<alarm_level>1</alarm_level>

<mount_point>/usr</mount_point>

<usage>80</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 1 -- /usr above 80%%></event>

<event>$JOB:START...</event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<CLEAR -- /usr below 80%%></event>

</normal>

</disk>

<disk>

<alarm_level>2</alarm_level>

<mount_point>/usr</mount_point>

<usage>90</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 2 -- /usr ABOVE 90%%></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 2 -- /usr below 90%%></event>

</normal>

</disk>

```

When usage hits 80%, the $JOB and 80+ $CONSOLE events gets sent. If usage hits 90%, the event gets sent. If the disk usage goes from sub-80 to 90+ in one scan, then all three events will be sent to SAM in the expected order: $JOB, 80+ $CONSOLE, 90+ $CONSOLE. When usage drops below 90%, the sub-90 $CONSOLE gets sent. When it drops below 80%, the sub-80 $CONSOLE will be sent. 

If the usage drops from 90+ to under 80 in the same scan, only the sub-90 $CONSOLE will be sent because the alarm level 1 ```<disk>``` will be skipped since the disk's alarm level is still at 2. 

If the usage remains below 80% for at least one more scan, the alarm level 1 ```<disk>``` will be executed during the next scan, at which point the sub-80 $CONSOLE will be sent to SAM. And, if it happens that the usage stays above 80%, but meanders above and below 90%, then the 90+ and sub-90 $CONSOLE events will be alternately sent until the usage drops below 80%.

It should be noted that as already inferred by the second paragraph in this section, ```<alarm_level>``` applies to the monitored resource and not to the disk ```<name> ```or ```<mount_point>```, or the process ```<name>``` or ```<UID>```. This means that two ```<disk>``` or ```<process> ```sections do not need to contain identical ```<name>```, ```<mount_point>```, or ```<UID>``` tags to reference the same resource. 

For example, suppose that it is desirable to have an event generated whenever any disk reaches 75% full, and a second event sent if "/usr" reaches 85% full, or if "/usr2" reaches 90% full. Three ```<disk>``` sections are needed:

```

<disk>

<alarm_level>1</alarm_level>

<mount_point>*</mount_point>

<usage>75</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 1 -- %MOUNT_POINT%></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<CLEAR -- %MOUNT_POINT%></event>

</normal>

</disk>

<disk>

<alarm_level>2</alarm_level>

<mount_point>/usr</mount_point>

<usage>85</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 2 -- /usr></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 2 -- /usr></event>

</normal>

</disk>

<disk>

<alarm_level>2</alarm_level>

<mount_point>/usr2</mount_point>

<usage>90</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 2 -- /usr2></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 2 -- /usr2></event>

</normal>

</disk>

```

Notice that both "/usr" and "/usr2", which are referenced by the first section, are defined to be alarm level 2. This is not contrary to the requirement that alarm levels defined for any given resource be unique. The level 1 section does indeed apply to both disks because both are referenced by the ```<mount point>``` of '\*'. On the other hand, each level 2 section is specific to each disk because each ```<mount point>``` specifies mutually-exclusive sets of resources. 

If, however, the third ```<mount point>``` had been "/usr*", then the second and third sections could not both be defined as alarm level 2 because both would reference disk "/usr". 

If it had been intended that a second event be generated for any "/usr*" reaching 85%, and a third event sent if "/usr2" reached 90%, the three sections would then need to be:

```

<disk>

<alarm_level>1</alarm_level>

<mount_point>*</mount_point>

<usage>75</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 1 -- %MOUNT_POINT%></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<CLEAR -- %MOUNT_POINT%></event>

</normal>

</disk>

<disk>

<alarm_level>2</alarm_level>

<mount_point>/usr*</mount_point>

<usage>85</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 2 -- %MOUNT_POINT%></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 2 -- %MOUNT_POINT%></event>

</normal>

</disk>

<disk>

<alarm_level>3</alarm_level>

<mount_point>/usr2</mount_point>

<usage>90</usage>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 3 -- /usr2></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 3 -- /usr2></event>

</normal>

</disk>

```

Now, multiple sections which reference the same resource are defined at unique alarm levels.

Please note that for processes, ```<alarm_level>``` only applies if ```<condition> = CPU_CHECK```. Processes defined as IGNORE cannot produce any [further] alarms. Processes defined as MUST_EXIST or MUST_NOT_EXIST either violate the condition or they do not – there are no levels of partial existence. So, it makes sense that multi-level alarms only applies to a process being a CPU-hog, and the alarm level is used to rate a process's CPU-hogging from nuisance to nightmare.

It needs to be understood that alarm level need not bare any relationship to the specified alarm boundary value. This is best understood when both MIN and MAX boundary values are defined for a disk or process. Suppose that it is desirable to keep disk "/data4" at just under half-full and to get two levels of alarm as it goes towards full or empty. The elements below could be used to accomplish this.

```

<disk>

<alarm_level>10</alarm_level>

<mount_point>/data4</mount_point>

<usage>MAX 50</usage>

<alarm>

<event>/data4 - MAX-50 ALARM %USAGE%%%</event>

</alarm>

<normal>

<event>/data4 - MAX-50 clear %USAGE%%%</event>

</normal>

</disk>

<disk>

<alarm_level>20</alarm_level>

<mount_point>/data4</mount_point>

<usage>MAX 60</usage>

<alarm>

<event>/data4 - MAX-60 ALARM %USAGE%%%</event>

</alarm>

<normal>

<event>/data4 - MAX-60 clear %USAGE%%%</event>

</normal>

</disk>

<disk>

<alarm_level>30</alarm_level>

<mount_point>/data4</mount_point>

<usage>MIN 40</usage>

<alarm>

<event>/data4 - MIN-40 ALARM %USAGE%%%</event>

</alarm>

<normal>

<event>/data4 - MIN-40 clear %USAGE%%%</event>

</normal>

</disk>

<disk>

<alarm_level>40</alarm_level>

<mount_point>/data4</mount_point>

<usage>MIN 30</usage>

<alarm>

<event>/data4 - MIN-30 ALARM %USAGE%%%</event>

</alarm>

<normal>

<event>/data4 - MIN-30 clear %USAGE%%%</event>

</normal>

</disk>

```

Notice that the alarm levels bear no direct relationship to the boundary values. The relationship that exists is to the severity of the boundary values with respect to departure from (the not directly specified) "normal". To drop to 30% usage is more severe than to drop to 40%, so the 30% section is given a higher alarm level. Likewise, it is a more severe condition for usage to reach 60% than it is to reach only 50%; therefore, the 60% section is given a higher alarm level. 

That the MIN's are given a higher alarm level than the MAX's is a non-issue because they are mutually-exclusive, i.e., they can never occur on the same side of "normal". The MIN's could have been specified first and given the lower alarm levels. 

It is very important to notice that the 40% section appears before the 30% section. If they were swapped, both sections would still get executed as usage fell from above-40 to below-30; but, in the order of 30% alarm and then the 40% alarm, and upon return-to-normal, the 40% all-clear and then the 30% all-clear.

Before moving on to a discussion specific to ```<user_defined>```, one last point can be drawn from the examples provided so far. And that is that while it is not necessary to have both alarm and return-to-normal (all-clear per this alarm level) exception handling defined for each alarm level (or in any section, regardless of alarm level also being defined), if ```$CONSOLE:DISPLAY``` or other events which provide feedback to humans are used, it is good practice to provide feedback in both directions. 

Consider that an operator receives notification of some alarm condition and begins to take action. If that resource should return to a normal status while the operator is taking required actions and a return-to-normal notification is not also sent out by SMA_RM, that operator may at best be wasting time taking no-longer-needed action, and at worst be doing things which are now detrimental.

For ```<user_defined>```, the resource is not directly referenced (as is disk "/usr" in preceding examples), so SMA_RM is, by itself, not able to see that multiple sections reference the same resource. The fact that one or more resources are monitored by multiple ```<user_defined>``` sections is indicated to SMA_RM by their having the same ```<alarm_group>```, which is an arbitrary non‑negative integer. Except that all ```<user_defined>``` with the same ```<alarm_group>``` are treated by SMA_RM as monitoring the same resource(s), no other significance is attached to alarm groups and they may appear in any order within the SMA_RM Config File. 

However, as with multiple ```<disk>``` and ```<process> ```sections which reference the same resource(s), ```<user_defined>``` sections within the same alarm group must appear within the SMA_RM Config File in ascending ```<alarm_level>``` order. SMA_RM does not currently do any consistency checks.

Monitoring of a resource(s) for multiple alarm levels will normally be done by invoking the same start image, but with parameters appropriate to effect an ALARM/NORMAL indication at the specified alarm level. And, ```<outputs>``` should be consistent within the alarm group. But, SMA_RM does not do any consistency checking within an alarm group for ```<start_image>``` or ```<outputs>```, and this "feature" may either be exploited or a cause for double-checking of the SMA_RM config file.

To be consistent with monitoring of disks and processes, user-defined monitors within each alarm group must perform only one scan of the resource per SMA_RM scan cycle. This means that the first call to the resource monitor (the ```<start_image>```) within a scan cycle—from the section with the lowest alarm level—should be coded to allow the script/program to recognize that a full scan is to be executed, and subsequent calls should be coded to use the data gathered during the first call and base their returned ALARM/NORMAL statuses on that data. 

This ensures that data will be consistent during the entire SMA_RM scan cycle as well as to keep monitoring activities from using excessive amounts of system resources. If returned data values are to be logged, the placement of ```<log>``` entities depends on what is to be logged. If data are to be logged with each scan, to prevent redundant log entries, a single "```<log>SCAN</log>```" is included in the first (lowest alarm level) ```<user_defined>```, and either no ```<log>``` entities or "```<log>NONE</log```" in higher alarm level sections. But, if data are to be logged only on NORMAL/ALARM transitions, then each ```<user_defined>``` must contain a "```<log>EVENTS</log>```".

As with ```<disk>``` and ```<process>``` resources, SMA_RM at start-up assumes that each user-defined alarm group is at alarm level zero, i.e., not in alarm. As each ```<user_defined>``` section is executed within a scan cycle, its ```<start_image>``` will be executed.

If the alarm level defined for the section is lower than the group's current alarm level, any additional processing defined for this section is aborted. If, however, the alarm level defined for this section is at-or-above the current alarm level for the group, the NORMAL/ALARM status returned by ```<start_image>``` is inspected and any associated exception handling executed if the status changes. Also, if its new status is ALARM, the alarm group's alarm level will be set to the section's alarm level, and if it is NORMAL, the group's alarm level will be reset to its previous setting. An example follows:

```

<user_defined>

<log_name>A-1</log_name>

<alarm_group>1</alarm_group>

<alarm_level>1</alarm_level>

<start_image>/usr/jobs/check_a 1</start_image>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 1 –- resource "a"></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<CLEAR –- resource "a"></event>

</normal>

</user_defined>

<user_defined>

<log_name>A-2</log_name>

<alarm_group>1</alarm_group>

<alarm_level>2</alarm_level>

<start_image>/usr/jobs/check_a 2</start_image>

<alarm>

<event>$CONSOLE:DISPLAY,<ALARM-LEVEL 2 -- resource "a"></event>

</alarm>

<normal>

<event>$CONSOLE:DISPLAY,<ALARM-CLEAR 2 -- resource "a"></event>

</normal>

</user_defined>

``` 

During each SMA_RM scan cycle, the call to "check_a 1" tells "check_a" to scan the resource and to save the data for use in subsequent calls. The follow-on call to "check_a 2" tells "check_a" to use the saved data. Since SMA_RM begins by assuming that all alarm groups are in the NORMAL state, and assuming that some scan shows the monitored resource to have a value which would place it within alarm level 2, the call to "check_a 1" will return ALARM, and the first $CONSOLE event will get sent to SAM and the group's alarm level will be set to 1. 

Next in that same scan cycle, the "check_a 2" will likewise return ALARM, and the third $CONSOLE event will get sent to SAM and the group's alarm level will be set to 2. If, in a subsequent scan, the value of the monitored resource falls to below alarm level 2 limits (but still above level 1 limits), "check_a 1" will continue to return ALARM, while "check_a 2" will return NORMAL, prompting sending of the fourth $CONSOLE to SAM and the resetting of the group's alarm level back to 1. And when it finally has a value below the alarm level 1 threshold, "check_a 1" will return NORMAL, and the second $CONSOLE will be sent and the group's alarm level reset to zero. 

If it happens that the resource's value stays above level 1 but meanders in and out of level 2 territory, then the third and fourth $CONSOLE will be alternately sent (and the group's alarm level toggled between 1 and 2 until the resource's value drops below the limit for alarm level 1.