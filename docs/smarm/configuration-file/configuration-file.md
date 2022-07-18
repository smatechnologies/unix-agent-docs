# Configuration File

The configuration file consists of one ```<config>``` section, followed in any order by any number of optional ```<disk>```, ```<process>```, or <user_defined> sections, to be discussed in that order. Although ```<disk>```,``` <process>```, or ```<user_defined>``` sections may appear in any order, the order in which they appear is significant in that their order within the file is also the order in which they are processed during each scan. 

For instance, a ```<process>``` section which specifies processes to be ignored should appear prior to ```<process>``` sections which would otherwise apply to the to-be-ignored processes. There is no interaction between ```<disk>```, ```<process>```, or ```<user_defined>``` sections.

As was previously mentioned, SMA_RM will monitor the config file for changes, and re-read it if a change to the modification time is detected. The changes are not taken to be incremental; all data from the previous version of the config file is forgotten when the new file is successfully read. If the new config file contains errors, an indication of the error will be written to the LSAM log and error files. 

If an error-free version has previously been read during this execution of SMA_RM, monitoring is continued with the previous configuration. 

The following provides an example of what will appear in the LSAM log file if SMA_RM detects an error in the [new] config file:

```

[Mon Oct 15 15:38:22 2007]

[sma_RM] Re-reading Config File (550)

[Mon Oct 15 15:38:22 2007]

[sma_RM] Line 2 - Invalid value for <scan_interval> (560)

[Mon Oct 15 15:38:22 2007]

[sma_RM] Continuing with old Config File data (611)

```

It should be noted that if the LSAM were restarted at this point, there would be no 'old' config file, since that data resides only within SMA_RM's internal, volatile memory. Upon LSAM restart, SMA_RM will attempt to read the 'new' config file, and report it as unusable.

The file is free-format, that is, spaces, tabs, and line-feeds can be used as desired to separate syntactical elements such as entity names, angle brackets, etc. It should be noted that the closing "/entity" is considered to be a single syntactical element, and so no spaces/tabs/line-feeds may appear between the '/' and the name, i.e., "< /window >" is acceptable, but "< / window >" is not.

Except as noted, letter case is insignificant. That is, "```<user_defined>```" and "```<UseR_deFIned>```" are equivalent, as are ```MUST_RUN``` and ```must_run```.

 

Comments can be included by beginning a line with a '#', as in:

```

# This line is a comment and will be ignored by SMA_RM

``` 

Common to all sections are ```<window>``` and ```<log>``` entities. A window is defined by the syntax "```<window>start-end</window>```". For example:

```<window>0600-1800</window>```

Start and end are specified in 4-digit 'hhmm' (hours and minutes) format. Leading zeros will be assumed if less than 4 digits are specified. The time is assumed to include seconds 00 to 59. When start is less than end, the window is inclusive, and applies from start thru end. 

If start is greater than end, the window is exclusive, and applies from 0000 to start, and from end to 2359, e.g., 1800-0559 would apply from midnight to (but not including) 6AM and again from 6PM until midnight. 

Start = end is an error, as are numbers outside the range 0000‑2359 and 'mm' digits greater than 59. The default window is 0000‑2359. 

```<log>``` is used to specify when, if at all, scanned values are to be entered into the SMA_RM log file. Three options are available: NONE, SCANS, and EVENTS. NONE, which is the default, results in no logging. SCANS results in values getting logged with each scan cycle. EVENTS results in values getting logged only when the scanned resource goes into or out of alarm. 

The particular values which may be logged are described below under the details for ```<config>```, ```<disk>```, ```<process>```, and ```<user_defined>```. SMA Technologies recommends that logging of scanned values be used sparingly because of the large amounts of disk space used – which can easily reach megabytes per hour. Normally, only status-change logging of values, i.e., "```<log>EVENTS</log>```", should be specified.

:::caution 

SMA Technologies recommends against more than sparing use of "```<log>SCANS</log>```" because logging values at every scan cycle can use tremendous amounts of disk space. If values are to be logged, the normal setting would be "```<log>EVENTS</log>```".

:::

Only one timestamp is written to the SMA_RM log file per scan cycle. Every time a value is to be logged, a check is made to see if the timestamp has yet been written, and it is first written if necessary. Thus, all text which appears between two timestamps was produced during and as a result of the scan cycle associated with the earlier timestamp.