# LSAM Configuration Parameters

## Configuration Parameters

The following parameters reference basic LSAM settings for job handling.

### max_number_of_jobs_to_run

**Default Value**: 50

**Description**:
	
* Defines the maximum number of jobs the LSAM can simultaneously manage.
* The value for this parameter must be numeric and greater than zero.

:::info Note 

The machine's capabilities (e.g., memory, processor speed, and so forth) determine this maximum.

:::

* Typical customer usage ranges from 10 to 30 jobs.
* The LSAM can detect a change to this setting when the LSAM is refreshed with the lsam ```<SAM_Socket>``` refresh command. For information on the LSAM refresh command, refer to [lsam refresh](/operations/unix-lsam-commands#lsam-refresh).

:::warning

If setting the MAX_NUMBER_OF_JOBS_TO_RUN parameter to a high value (i.e., greater than 50), ensure that your system can manage the load; otherwise, the system may hang. The minimum number of processes which are generated is 10 + (2 * MAX_NUMBER_OF_JOBS_TO_RUN). For example, if set to 200, then the system must be able to handle at least 410 processes.

:::

### allowed_privileged_runs

**Default Value**: 1

**Description**:

* Enables/Disables the processing of jobs submitted as root ```(0/0)```.
* If set to zero, the LSAM does not process jobs submitted as root ```(0/0)```.
* If set to one, the LSAM processes jobs submitted as root ```(0/0)```.

### require_HOME_directory

**Default Value**: 0

**Description**: 

* Enables/Disables the requirement that all users who submit OpCon jobs have $HOME directories on the system.
* If set to zero, the LSAM attempts to issue a UNIX "cd $HOME" command before starting a job. The job proceeds without indicating if the "cd" command was successful. This is the traditional behavior of the LSAM. If the "cd" command fails, the job executes at the root ("/").
* If set to one, the LSAM aborts jobs submitted by a user with no $HOME directory (i.e., the "cd $HOME" command fails).

### LSAM_job_statistics

**Default Value**: 0

**Description**:

* Enables/Disables reporting of resource-usage statistics for users' jobs.
* If set to zero, the LSAM does not report resource-usage statistics for users' jobs.
* If set to one, the LSAM reports resource-usage statistics for users' jobs.
* This applies to all jobs. Note that this can result in creation of a large amount of data on the SAM machine, which can adversely affect SAM's performance.

### monitor_LSAM_health

**Default Value**: 60

**Description**:

* The period (in seconds) the LSAM performs self-monitoring for signs of malfunction.
* Zero disables LSAM self-monitoring.
* The parameter requires a minimum of 30 seconds.

### LSAM_malfunction_action

**Default Value**: 1

**Description**: 

* This parameter determines, if self-monitoring is enabled (refer to above), the action to be taken upon detection of an LSAM malfunction:
* If set to one, the LSAM terminates itself.
* If set to two, the LSAM sends an event (i.e., the first line of file "```$LSAM_ROOT/config/<SMA_LSAM_INSTANCE>/LSAM_malfunction_event```") to the SAM-SS.
    * Ensure that "LSAM_malfunction_event" contains a valid OpCon event. For more information, refer to [Introduction](https://help.smatechnologies.com/opcon/core/events/introduction) in the OpCon Events online help.
    * To prevent the generation of recurring events, the LSAM disables self-monitoring upon detection of a malfunction.

### LSAM_0_255

**Default Value**: yes

**Description**:

This is the global configuration setting for how the LSAM will impersonate users when executing jobs. For a full discussion of the options, please refer to "Considerations for path_to_su" below this table.

 

The options for this setting include:

* no: Setting the value to no causes the LSAM to use the legacy method of user impersonation for all jobs.
* yes or the full path to the su program: Setting the value to yes or the full path to su causes the LSAM to use the su method of user impersonation for all jobs.

Full path Examples:

```/usr/bin/su```
```/bin/su```
```/sbin/su```

## Considerations for path_to_su

Before deciding to change from the default of "No" for the path_to_su configuration setting, it is important to consider the differences in behavior between the options.

:::caution

When switching the value for path_to _su, be sure to retest all jobs running through this LSAM. Differences in behavior can cause jobs to start failing that previously were finishing OK.

:::

When path_to_su is set to No, the LSAM will not load the user profile when a job is executed. The LSAM will use only the user name/id and group name/id passed with the job to determine permissions for the job execution. If a user is a member of multiple groups, only the group defined in the job will be honored. You can also configure the user_setup script to emulate a profile script for all things except interactive commands. For more information refer to [Edit the user_setup Script](/configuration/loading-environment-variables#edit-user_setup-script).

If you set path_to_su to yes, the LSAM will search in default directories for the su program at startup and log the location where it is found. If either su method is used, all jobs will execute calling "su -" to perform the user impersonation. The LSAM will load the profile for the user's default shell as well as the user's full group list. The su utility will then handle all command line interpretation, including special characters. Since the LSAM is not running as a logged in user, any command in the profile that requires a console to be logged in may not execute successfully.

:::tip Example

Jack Henry provides for AIX servers for running Episys with a standard profile configuration with settings that require the UNIX LSAM to be configured with path_to_su set to no.

:::

:::info Note

If the LSAM is configured to use "su" to run the jobs, and the su executable is not found on start up, the LSAM will log an error and stop.

:::