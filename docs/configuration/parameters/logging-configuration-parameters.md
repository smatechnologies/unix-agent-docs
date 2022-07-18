# Logging Configuration Parameters

The following parameters refernce the logging settings for troubleshooting the UNIX LSAM.

## log_file_rollover_size

**Default Value**: 600000
**Change Required**: N

**Description**:

* In bytes, sets the maximum size for the logfile and errfile before they are archived.
* When archiving, the LSAM renames the logfile to ```<ten-digit unique number>```.log.
* When archiving, the LSAM renames the errfile to ```<ten-digit unique number>```.err.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log messages in a single file.

### log_file_max_count

**Default Value**: 20
**Change Required**: N

**Description**:

* Sets the maximum number of archived log files.
* Also sets the maximum number of archived error files.
* When the maximum is reached for either the archived log files or error files, the LSAM deletes the oldest archived file and creates a new one.
* The value for this parameter must be numeric and greater than zero.
* Prevents the accumulation of log files.