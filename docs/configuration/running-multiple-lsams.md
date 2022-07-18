# Running Multiple LSAMs on One Machine

## Scenarios

Multiple LSAMs may be simultaneously executed on a single system. It is possible to execute different versions of the LSAM (Scenario 1) as well as the same versions with different configurations (Scenario 2). An example of the first scenario would be testing a new release while continuing to operate the most current release. An example of the second scenario is running LSAMs with differing SMA File Transfer (SMAFT) max_bandwidth parameters.

## Environmental Variables

Environment variables ```$LSAM_ROOT```, ```$SAM_SOCKET```, and ```$SMA_LSAM_INSTANCE``` define each instance of an LSAM. ```$LSAM_ROOT``` specifies the root location of the executable, configuration, and data files. ```$SAM_SOCKET``` identifies the socket number over which the LSAM communicates with the SAM. Since the socket used by SAM to communicate with an LSAM must be unique to a host system, no two running LSAMs can share the same ```$SAM_SOCKET```. ```$SMA_LSAM_INSTANCE``` identifies the location within ```$LSAM_ROOT``` of a particular instance of the LSAM's configuration and data files.

If two LSAMs share the same ```$LSAM_ROOT```, they execute the same code. To operate multiple versions of the LSAM (Scenario 1), place the LSAMs in separate directories and set the respective ```$LSAM_ROOT``` variable to the appropriate path (e.g., ```/usr/local/prod-lsam/``` and ```/usr/local/dev-lsam/```). To implement multiple configurations of a single version of the LSAM (Scenario 2), execute the "install_lsam" script, specifying the appropriate ```$SAM_SOCKET``` and ```$SMA_LSAM_INSTANCE```, e.g., "```install_lsam `pwd` 3100 general```" and "```install_lsam `pwd` 3200 critical```".

:::tip Example

Assume that one instance of the LSAM operating on host "unix_system" is for general users (configured with a small max_number_of_jobs and small max_bandwidth). A second instance of the LSAM is configured to allow full system utilization for critical jobs.

The OpCon machine names could be named "unix_general" and "unix_critical". Access to "unix_critical" is restricted to the OpCon users with the correct privileges. Both "unix_general" and "unix_critical" would resolve to the IP address of "unix_system". A job available to both "unix_general" and "unix_critical" could query environment variable ```$SMA_LSAM_INSTANCE``` to determine on which LSAM instance it is currently executing (Is the value of ```$SMA_LSAM_INSTANCE``` "general" or "critical"?) and act accordingly.

:::

The environment variable ```$SMA_BINDIR``` is defined within each instance of an LSAM to point to the "bin/" directory containing the utilities file_check, maintain_ofiles, sma_ppscript, and sma_status. This allows user jobs, executing these utilities, to get the correct LSAM version under which the job is running.

## OpCon Central Components

From the point of view of the OpCon central components, multiple instances of an LSAM are different machines. Each instance of an LSAM must be identified in the Enterprise Manager on the Machines Screen (Navigation path: Administration>Machines). This requires all machine names associated with the same IP address to be listed in the DNS or to be in the "hosts" file on the OpCon server. For more information, refer to the [Machines](machines) section in the Concepts online help.