# CONFIG Section

A template ```<config>``` section follows:

```

<config>

<scan_interval>____</scan_interval>

<C_alarm>[ MIN | MAX ]____</C_alarm>

<T_alarm>[ MIN | MAX ]____</T_alarm>

<user_defined_monitor>

<max_run_time>____</max_run_time>

<event>____</event>

</user_defined_monitor>

<window>____</window>

<CPU_hogs>[ MIN | MAX ]____</CPU_hogs>

<total_processes>[ MIN | MAX ]____</total_processes>

<log>NONE | SCANS | EVENTS</log>

<log_events>YES | NO</log_events>

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

</config>

``` 

All entities within the ```<config>``` are optional, and defaults will be as noted in the discussion of each entity. Duplicate entities constitute an error. Thus, since all ```<config>``` entries are optional, and a ```<config>``` section is the only required section within an SMA_RM config file, the minimum content of the file is:

```<config>```

```</config>```

Thus, this "empty" config file can be used to effectively disable execution of SMA_RM without needing to delete the SMA_RM config file and re-start the entire LSAM. To resume normal operation of SMA_RM, simply overwrite the empty file with the normal one.

For the four entities which may include a MIN or MAX designator, at least one space must appear between the MIN or MAX and the value. MAX is the default.

```<scan_interval>``` is an integer number of seconds, with a default of 1. SMA_RM will execute each ```<disk>```, ```<process>```, and ```<user_defined>``` specification every ```<scan_interval>``` number of seconds.

```<log_events>``` determines whether or not SMA_RM-generated OpCon events from ```<event>``` entities will be logged in the SMA_RM log file as they are sent to SAM. The default setting is NO. If set to YES, the SMA_RM log file will contain all events sent to SAM, i.e., the event strings defined by ```<event>``` entities with the event variables replaced by the referenced scanned values. It will also contain indications of each ```<sleep>``` entity as it is executed.

```<C_alarm>``` and ```<T_alarm>``` are global process alarm values, and will be discussed with local entities of the same name within the ```<process>``` specification. MIN or MAX may be included with the value to set the type of the value. Their default values are MAX 10 and MAX 20, respectively.

```<user_defined_monitor>``` defines what is a reasonable amount of time that a user-defined monitor may take to complete one scan, and the event to be sent to SAM if one should fail to complete within the allotted time. They are expected to run for only milliseconds, and SMA_RM waits for them to complete. The default behavior is that no checking of execution time will be performed for user-defined monitors. If ```<user_defined_monitor>``` is specified, then both```<max_run_time>``` and ```<event>``` must also be included. ```<max_run_time>``` specifies the maximum amount of time, in seconds, that a user-defined monitor should take to complete one scan. ```<event>``` is triggered if a user-defined monitor continues to execute after ```<max_run_time>``` has elapsed, and it is coded as described for other ```<event>``` entities as covered later under "Exception Handling". The single event variable available within ```<event>``` is %LOG_NAME%, which is the contents of the ```<log_name>``` entity in the to-be-discussed ```<user-defined>``` specification. Note that except for issuance of the event to SAM, a run-away user-defined monitor will still continue to execute and cause SMA_RM to hang. User intervention will be required to address a run-away.

```<CPU_hogs>``` is the percentage of the number of CPU-hog processes to the total number of processes in the system which constitutes an alarm condition. (Processes which qualify as CPU-hogs are specified in ```<process>``` sections, and include non-working processes as caught with a MIN comparison of the specified boundary value.) Likewise, ```<total_processes>``` is the point at which the total number of processes is considered to constitute an alarm condition. MIN or MAX may be included with each value to set the type of the value. Defaults for these, which are both integers, are MAX 25 for ```<CPU_hogs>``` and MAX 1000 for ```<total_processes>```. ```<log>``` specifies what, if any, values for the count of CPU-hogs and total processes in the system will be logged. ```<alarm>``` defines what is to occur when an alarm has been noted, and will be discussed later under "Exception Handling". Likewise with ```<normal>``` which defines what is to occur upon a return to normal. The event variables available within the ```<alarm>``` and ```<normal>``` specifications are as follows:

* ```%CPU_HOGS%``` = the percentage of processes which are CPU-hogs.
* ```%TOTAL_PROCESSES%``` = the total number of processes in the system.

```<window>``` defines when ```<CPU_hogs>``` and ```<total_processes>``` will be monitored and ```<alarm>``` and ```<normal>``` executed.

