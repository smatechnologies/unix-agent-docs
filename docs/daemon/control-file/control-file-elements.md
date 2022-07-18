# Control File Elements

The bulleted outlines in this section present the supported Control File elements and their descriptions. The outline itself indicates the nested structure of elements for the files. Not all elements define data items for storage in the database. Some elements merely group a set of logically related elements together.

## Configuration

* ```<config>```: (Optional) Contains the child elements needed for describing the SMA FAD configuration.
    * ```<waittimebetweenpasses></waittimebetweenpasses>```: (Optional) In seconds, specifies the time interval between successive reads of the Control File. Valid data for this element is an integer ranging from 1 to 9999. If omitted, the data defaults to 1.
* ```</config>```

## File Activity

* ```<fileactivity>```: (Required) Contains the child elements required for describing one record block to the SMA FAD.
    * ```<id></id>```: (Required) This is a unique ID for each block of records in the control file that identify the parameters associated with monitoring one file name or file mask. It is user-defined, but they have to be unique. A check for uniqueness is made each time the daemon processes this file. Duplicates are signaled as an error. This ID is used as the name for the snapshot file containing the updated linked-list of files to be monitored and their information-like file size, modification time, etc. The location of this snapshot file is in ```LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/snapshot/<Control File>/IDn```. Record ID is a required element.
    * ```<filemask></filemask>```: (Required) Defines the file name or variable file name for monitoring. The path must be a full path which may contain wildcards.

:::tip Example

The following example shows the definition of a file name or variable file name for monitoring:

```<filemask>/usr/local/test/*.txt</filemask>```

:::

* ```<window></window>```: (Optional) Defines a time interval (using a 24-hour clock) within which the SMA FAD monitors the file(s) and triggers the events within the data block. When defined, SMA FAD ignores the record block outside the time constraints of the window. If omitted, the SMA FAD monitors the defined filemask persistently.

:::tip Example

The following example shows the definition of a time interval for monitoring:

```<window>0800–1700</window>```

:::

* ```<condition></condition>```: (Required) Defines the condition of the file(s) upon which the SMA FAD initiates events. Supported conditions include the following: CREATE, DELETE, GROWTH, SHRINK, ABSOLUTE, or MODIFY. If ABSOLUTE is specified, SMA FAD requires the file size in bytes follow the condition after a space.

:::tip Example

The following example shows the definition of a file's condition that initiates events:

```<condition>ABSOLUTE 281</condition>```

:::

* ```<mintimetowait></mintimetowait>```: (Optional) Defines the minimum amount of time in seconds the SMA FAD waits before determining if a file is still being modified (e.g., a file arriving through FTP). Between two consecutive passes, when the daemon sees that a file is modified, it uses the mintimetowait element to determine if the file is still changing. If the file changes within this time period, SMA FAD does not initiate the events. This element supplements the CREATE, MODIFY, GROWTH, and SHRINK conditions. If omitted, SMA FAD uses the value from the waittimebetweenpasses configuration element. For information on waittimebetweenpasses, refer to [Configuration](/configuration/unix-lsam-configuration) in this topic.

:::tip Example

The following example shows the definition of the waittimebetweenpasses configuration element:

```<mintimetowait>30</mintimetowait>```

:::

* ```<eofindicator></eofindicator>```: (Optional) Defines the character string that indicates that a complete file has arrived. The SMA FAD only initiates the associated events after detecting the string somewhere in the file. Because the string does not have to be at the end of the file, events can process at the exact point of the file desired. This element supplements the CREATE, MODIFY, and GROWTH conditions. If omitted, the SMA FAD processes events based on other conditions and options.

:::tip Example

The following example shows the end-of-file indicator.

```<eofindicator>END OF FILE</eofindicator>```

:::

:::info Note

The eofindicator element is mutually exclusive with the mintimetowait element. For information on mintimetowait, refer to ```<mintimetowait></mintimetowait>```: (Optional) Defines the minimum amount of time in seconds the SMA FAD waits before determining if a file is still being modified (e.g., a file arriving through FTP). Between two consecutive passes, when the daemon sees that a file is modified, it uses the mintimetowait element to determine if the file is still changing. If the file changes within this time period, SMA FAD does not initiate the events. This element supplements the CREATE, MODIFY, GROWTH, and SHRINK conditions.

If omitted, SMA FAD uses the value from the waittimebetweenpasses configuration element. For information on waittimebetweenpasses, refer to ```<waittimebetweenpasses></waittimebetweenpasses>```: (Optional) In seconds, specifies the time interval between successive reads of the Control File. Valid data for this element is an integer ranging from 1 to 9999. If omitted, the data defaults to 1.

:::

* ```<maxtimetowait></maxtimetowait>```: (Optional) Defines the maximum amount of time to wait in seconds before the SMA FAD writes an error because all of the conditions have not been met on a file(s) to trigger the event(s). This element supplements the CREATE, MODIFY, and GROWTH conditions only when the eofindicator is also specified.

:::tip Example

The following example shows the definition of the maximum time to wait:

```<maxtimetowait>300</maxtimetowait>```

:::

* ```<eventinfo>```: (Required) Contains the child elements required for describing the events for one record block to the SMA FAD.
    * ```<event></event>```: (Required) Defines the OpCon event to forward to the SAM. The event must be a valid OpCon event with a user login ID and external event password. For more information, refer to Introduction in the OpCon Events online help. The SMA FAD does not limit the number of ```<eventstr>``` elements for each ```<eventinfo>``` element. The entire ```<event></event>``` element must be on a single line.
    * ```<sleep></sleep>```: (Optional) Defines the amount of time to wait before SMA FAD initiates the next event in the same record block. The SMA FAD uses the sleep value to determine the wait time after processing the eventstr element defined on the line before the sleep element. After an event is initiated, the process waits "sleep" amount of seconds before initiating the next event in line. Although SMA Technologies does not guarantee the sequence in which events get processed by the SAM, employing the sleep element can separate the events long enough that the SAM processes the events in the desired order.
    * ```</eventinfo>```
* ```</fileactivity>```

In the example below, the SMA FAD performs the following actions:

* For record block one, SMA FAD watches for the creation of /usr/local/test/*.txt between the hours of 8:00 AM and 5:00 PM. The SMA FAD waits 5 seconds and then re-checks the file to determine if the creation is complete. After the file is complete, SMA FAD forwards to the SAM a console display, and 5 seconds later forwards a threshold update.
* For record block two, SMA FAD watches for the absolute file size of 5000 bytes for /usr/local/test/sample/*.dat between the hours of 8:00 AM and 5:00 PM. After determining the file is 5000 bytes, SMA FAD forwards to the SAM a console display and a threshold update.
* For record block three, SMA FAD watches for the modification of /usr/local/test/*.dat between the hours of 8:00 AM and 5:00 PM. The SMA FAD waits up to 1000 seconds to find the string "end of record" in the file. If the end of file indicator appears before 1000 seconds, SMA FAD forwards to the SAM a console display and a threshold update. If the end of file indicator does not appear before 1000 seconds, SMA FAD writes an error to the logfile and errfile.

:::tip Example

The following example shows an SMA FAD Control File.

 

Note: Although the ```<event>``` element is shown occupying multiple lines, it is for presentation purposes. In the actual file, it must be on a single line.

```

<config> <waittimebetweenpasses>2</waittimebetweenpasses>

</config>

 

<fileactivity>

<id>5</id>

<filemask>/usr/local/test/*.txt</filemask>

<window>0800-1700</window>

<condition>CREATE</condition>

<mintimetowait>5</mintimetowait>

<eventinfo>

<event>$CONSOLE:DISPLAY, message,BatchUser,BatchPwd </event>

<sleep>5</sleep>

<event>$THRESHOLD:SET,THRESH1,2,BatchUser,BatchPwd </event>

</eventinfo>

</fileactivity>

 

<fileactivity>

<id>10</id>

<filemask>/usr/local/test/sample/*.dat</filemask>

<window>0800-1700</window>

<condition>ABSOLUTE 5000</condition>

<eventinfo>

<event>$CONSOLE:DISPLAY,%FILEEXT% is complete,BatchUser,BatchPwd </event>

<event>$THRESHOLD:SET,%FILEROOT%,1,BatchUser,BatchPwd </event>

</eventinfo>

</fileactivity>

 

<fileactivity>

<id>15</id>

<filemask>/usr/local/test/*.dat</filemask>

<window>0800-1700</window>

<condition>MODIFY</condition>

<eofindicator>end of record</eofindicator>

<maxtimetowait>1000</maxtimetowait>

<eventinfo>

<event>$CONSOLE:DISPLAY,%FILENAME% changed,BatchUser,BatchPwd </event>

<event>$THRESHOLD:SET,%FILDROOT%,0,BatchUser,BatchPwd </event>

</eventinfo>

</fileactivity>

```

:::