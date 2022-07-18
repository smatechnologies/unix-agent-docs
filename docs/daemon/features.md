# Features

The SMA File Activity Detection Daemon supports the following features.

## SMA File Activity Daemon Features and Descriptions

### Recognition of file names

* The SMA FAD recognizes individual file names and masks containing wildcards.
* The SMA FAD allows overlapping file names or wildcard specifications to support processing of different events.
* Refer to the ```<filemask>``` Control File element.

### Recognition of file creation

* The SMA FAD checks for file creation.
* The SMA FAD treats file existence the same as file creation.
* Refer to the ```<condition>``` Control File element.

### Recognition of file deletion

* The SMA FAD checks for file deletion.
* The SMA FAD treats file absence the same as file deletion.
* Refer to the ```<condition>``` Control File element.

### Recognition of change in file size

* The SMA FAD checks for any changes in the file size (i.e., increase or decrease) and initiates the associated events.
* Refer to the ```<condition>``` Control File element.

### Recognition of file modification
	
* The SMA FAD recognizes when a file has been modified.
* Refer to the ```<condition>``` Control File element.

:::info Note 

The SMA FAD processes events for file modification separately from events for change in file size.

:::

### Support the initiation of events in specified time slots only

* If specified in the control file, the SMA FAD triggers the external events only if the conditions are met within a specific period of time.
* Refer to the ```<window>``` Control File element.

### Ability to specify a time interval between initiation of events

* If configured to trigger multiple events upon certain file criteria, the SMA FAD can wait a user-defined number of seconds between events.
* Refer to the ```<sleep>``` Control File element.

### Read the control file at a configurable interval

* By default, the SMA FAD reads the control file every one second; however, the administrator can configure other intervals.
* Refer to the ```<waittimebetweenpasses>``` Control File element.