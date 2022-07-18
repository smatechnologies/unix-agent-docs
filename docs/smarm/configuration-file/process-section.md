# PROCESS Section

Process-monitoring specification, via one or more ```<process> ```sections, is quite flexible. A template follows (note that this template shows all possible entities within a ```<process>``` section and that certain entities are mutually-exclusive):

```

<process>

<condition>IGNORE | MUST_RUN | MUST_NOT_RUN | CPU_CHECK</condition>

<window>____</window>

<exist_alarm>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</exist_alarm>

<exist_clear>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</exist_clear>

<name>____</name>

<UID>____</UID>

<C_alarm>[ MIN | MAX ]____</C_alarm>

<T_alarm>[ MIN | MAX ]____</T_alarm>

<log>NONE | SCANS | EVENTS</log>

<alarm_level>____</alarm_level>

<CPU_alarm>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</CPU_alarm>

<CPU_normal>

<event>____</event>

<action>____</action>

<sleep>____</sleep>

</CPU_normal>

</process>

```

All entities within ```<process>``` are optional except for ```<condition>```. Duplicate entities constitute an error.

```<alarm_level>``` is discussed below in "Multiple Alarm Levels", and may only appear if ```<condition> = CPU_CHECK```.

```<window>``` defines when the specification is to be active.

```<condition>``` specifies what is to be monitored. IGNORE means to ignore the specified processes except in counting them in determining the total number of processes in the system, and inclusion of any other entities besides ```<name>``` and ```<UID>``` constitutes an error. CPU_CHECK indicates that a specified process is to be checked for being a CPU-hog as discussed in a couple of paragraphs from now. MUST_RUN indicates that it is an alarm if a specified process does not exist, while MUST_NOT_RUN indicates that it is an alarm if a specified process does exist. A MUST_RUN ```<exist_alarm>```, discussed later under "Exception Handling", will be executed the first time an alarm occurs for any given ```<name>/<UID>``` combination, i.e., it will be executed the first scan in which a MUST_RUN process is not seen but not for each scan in which a required process is absent. Likewise, a MUST_NOT_RUN ```<exist_alarm>``` will be executed the first scan in which a MUST_NOT_RUN process is seen, and one will be executed for each unique process that creates a MUST_NOT_RUN exception. For MUST_RUN, ```<exist_clear>``` will be executed after an ```<exist_alarm>``` upon the first detection of a required process. Likewise for MUST_NOT_RUN, ```<exist_clear>``` will be executed after an ```<exist_alarm>``` upon first detection that no specified processes are executing. The event variables available within the ```<exist_alarm>``` and ```<exist_clear>``` specification for ```<condition> = MUST_NOT_RUN``` are as follows:

* ```%PID%``` = the PID of the process.
* ```%UID%``` = the UID of the process.
* ```%NAME% ```= the path/filename portion of the 'ps' CMD field for the process.
 

The event variables available within the ```<exist_alarm>``` and ```<exist_clear>``` specification for ```<condition> = MUST_RUN``` are as follows:

* ```%NAME%``` = the contents of the associated ```<name>``` tag.
* ```%UID%``` = the contents of the associated ```<UID>``` tag.
 

```<exist_alarm>``` and ```<exist_clear>``` specification may only appear if ```<condition> = MUST_RUN``` or ```MUST_NOT_RUN```.

 

```<name>``` and ```<UID>``` are used to specify the process(es) to monitor per the indicated ```<condition>``` and are combined using an implied AND conjunction, i.e., a process must match both to be processed/ignored. If neither is specified, then this ```<process>``` section applies to all processes output by a 'ps' command. Processes are monitored by executing a "ps –ef" command and capturing the output for inspection. ```<name>``` refers to the CMD field of the 'ps' output, ```<UID>``` refers to the UID field. For either, an asterisk ('*') can be used as a wildcard character at either the beginning or at the end: at the end it means "begins with", at the beginning it means "ends with", and at both ends means "contains". A lone '*' means "matches all", as does an unspecified ```<name>``` or ```<UID>```. The contents of the ```<name>``` and ```<UID>``` entities are case-sensitive. The CMD contents will be truncated at the first blank, so ```<name>``` is just the filename or pathname (as returned by a particular OS's version of 'ps'), and does not include any start parameters which might also appear in the 'ps' output.

 

```<C_alarm>``` and ```<T_alarm>```, which are integers and may only appear if ```<condition> = CPU_CHECK```, and get their default values and MIN/MAX value types from the same-named entities within the ```<config>``` section, are used to detect if a process is a CPU-hog. ```<C_alarm>``` relates to the "C" field of the 'ps' output, ```<T_alarm>``` relates to "TIME". ```<C_alarm>``` directly specifies a C value, while ```<T_alarm>``` specifies a percentage of TIME. MIN or MAX may be included with each value to set the type of the value, the default being MAX. If MIN or MAX is specified, at least one space must appear between the MIN or MAX and the value. Detection for processes being CPU-hogs works as follows:

1. When a process first appears in the 'ps' output, 10 slots are created for each C and TIME (T) value. Each C slot is set to zero, except for the first, which is set to the scanned C value. Each T slot is set to the scanned value.

2. With each new scan, the new C and T values replace the oldest values.

3. If the average of all ten "C" values meet or exceed a MAX ```<C_alarm>```, or if a MIN ```<C_alarm>``` is greater than the average, the process is considered to be a CPU-hog. (A MIN value can be used to catch a process that has quit working.)

4. If the new T value minus the oldest, as a percentage of the elapsed clock time, is greater than or equal to a MAX ```<T_alarm>```, or if a MIN ```<T_alarm>``` is greater than the difference in T values, the process is considered to be a CPU-hog. (A MIN value can be used to catch a process that has quit working.) Thus, if the scan interval is 1 second and ```<T_alarm>``` is 30, a process is considered to be a CPU-hog if it uses at least 3 seconds of CPU time within any 10-second period. If the scan interval were set to every 5 seconds and ```<T_alarm>``` to 20, then a process would be considered a CPU-hog if in any 50-second interval (10 scan cycles) it used 5 x 10 x 20% = 10 seconds of CPU time.

An event will be generated for a CPU-hog process in fewer then 10 scan cycles in relation to the extent that its C and/or T values meet or exceed (for MAX, or for MIN, are at-or-under) the specified ```<C_alarm>``` and/or ```<T_alarm>```. An event will be generated after 10 scan cycles for a CPU-hog process which barely meets one or both alarm criteria. For example, assuming a ```<C_alarm>``` of MAX 100 and a ```<T_alarm>``` of MAX 30, a process which is clocking-up CPU time at fifty percent of wall-clock time and has a C of 115 will generate an event in 6 scan cycles. (Might be 5 scan cycles, might be 7…this is not exact.) 

While accumulating time at a rate of fifty percent of wall-clock, the process will reach its alarm-value of thirty percent of 10 slot's worth of wall-clock time in 6 scan cycles — 0.50 x 6 = 0.3 x 10. (If CPU time fell way off, but the C values remained at 115, the process would generate an event in 9 scan cycles — 115 x 9 = 1035 / 10 = 103.5, which is greater than 100.) So, this will require some tuning to have SMA_RM generate events for CPU-hogs with an acceptable level of nuisance events. One indication that ```<C_alarm>``` and/or ```<T_alarm>``` need to be raised is when the same processes generate multiple events. This indicates that they go into and out of alarm as they bang hard on the CPU for a short time and then fall off to acceptable levels of CPU usage. CPU-hogs that tie-up the CPU for extended periods of time will generate fewer events because they will not [often] go into and out of alarm.

It is not expected that MIN values will be often used, as they may result in excessive generation of events if not used only for processes that are expected to consume a fair amount of CPU time.

```<log>```, which may only appear if ```<condition> = CPU_CHECK```, specifies what, if any, C and TIME values will be logged. ```<CPU_alarm>``` defines what is to occur when a process goes into alarm, and will be discussed later under "Exception Handling". Likewise with ```<CPU_normal>```, which defines what is to occur when a process returns to a normal status. The event variables available within the ```<CPU_alarm>``` and ```<CPU_normal>``` specifications, which may only appear if ```<condition> = CPU_CHECK```, are as follows:

* ```%PID%``` = the PID of the process.
* ```%UID%``` = UID of the process.
* ```%NAME%``` = the path/filename portion of the 'ps' CMD field for the process.
* ```%C%``` = the value calculated in step (3) above.
* ```%T%``` = the value calculated in step (4) above, range from 0-100.

As already mentioned, the order in which sections appear within the SMA_RM Config File is significant, as shown in the following example, which instructs SMA_RM to ignore certain processes entirely, alarm if some processes are to exist or not exist, and do CPU-hog checking on the remainder of processes in the system:

```

<process>

<condition>IGNORE</condition>

<UID>root</UID>

</process>

<process>

<condition>MUST_EXIST</condition>

<name>*data*</name>

<exist_alarm>

<event>$CONSOLE:DISPLAY,<No *data* process></event>

</exist_alarm>

<exist_clear>

<event>$CONSOLE:DISPLAY,<*data* process [%name%] now present></event>

</exist_clear>

</process>

<process>

<condition>MUST_NOT_EXIST</condition>

<name>/usr/games/*</name>

<exist_alarm>

<event>$CONSOLE:DISPLAY,<%name% is being played by %uid%></event>

</exist_alarm>

<exist_clear>

<event>$CONSOLE:DISPLAY,<No games are being played></event>

</exist_clear>

</process>

<process>

<condition>IGNORE</condition>

<name>/usr/games/*</name>

</process>

<process>

<condition>CPU_CHECK</condition>

<name>*</name>

<CPU_alarm>

<event>$CONSOLE:DISPLAY,<%name% is being played by %uid%></event>

</CPU_alarm>

<CPU_normal>

<event>$CONSOLE:DISPLAY,<No games are being played></event>

</CPU_clear>

</process>

``` 

Within each SMA_RM scan cycle, any process with a UID of 'root' will be ignored. Next, a check will be made for existence of at least one process with 'data' within its name (CMD). Next, a check will be made to see if any processes from the "/usr/games" directory are executing. And finally, with the added exclusion of any processes from the "/usr/games" directory, all other processes within the system will be inspected to see if they are CPU-hogs.