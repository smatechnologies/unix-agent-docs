# Operating the LSAM

The LSAM uses simple commands to control and check the status of the LSAM.

## Start the LSAM

1. Log in to the UNIX system as root.
2. Change the directory to the LSAM's root directory. Use the following syntax:

```cd <LSAM _Root_Directory>```

:::info Note

After an upgrade installation, verify that the LSAM's tracking directory is empty before starting the LSAM.

1. List the contents of the tracking directory with the following command:
```cd ../tracking;ls```
2. If a file named ```tracking<SAM_Socket>``` exists, delete the file with the following command: ```rm tracking<SAM_Socket> E.g., rm tracking3100```
3. A directory named ```<SMA_LSAM_INSTANCE>``` may exist; if so, ensure that it is empty with the command: ```rm <SMA_LSAM_INSTANCE>/* E.g., rm prod/*```
4. Go back to the bin directory with the following command: ```cd ../bin```

:::

3. Start the LSAM using the following syntax:

```lsam<SAM_Socket>start```

:::tip Example

The following example shows the command for starting the LSAM using socket number 3100:

```cd /usr/local/lsam/; bin/lsam3100 start```

:::


4. The LSAM normally starts within 30 seconds, at which point all of the terminal output produced and redirected to the ```LSAM_output``` file will be dumped to the terminal. If it does not complete within five minutes, use the INT sequence (normally Cntrl_C) to stop the start-up procedure. 
    * Then use the command ```cat LSAM_output_<SAM_socket>``` to view the terminal output that was produced. 
    * The ```LSAM_output``` file can be viewed at any time. To see terminal output as it is produced, use the command ```tail –f LSAM_output_<SAM_socket>```.
5. Check the LSAM status before processing jobs.

## Check the LSAM Status

1. Log in to the UNIX system as root.
2. Change the directory to the LSAM's bin directory. Use the following syntax:

```cd <LSAM _Root_Directory>/bin```

3. Verify the LSAM status with the following command: ```lsam<SAM_Socket>status```. The command should display the following processes:
* sma_disp
* sma_log
* sma_lsam

and any of the following optional components that have been configured to run:
* sma_cronmon
* sma_filein
* sma_fad
* sma_jors

:::tip Example

The following example shows the command to verify the status of the LSAM using socket number 3100:

```
cd /usr/local/lsam/bin; ./lsam3100 status
```

If successful, the status command produces output similar to:

```
Currently running LSAM services:

--------------------------------

UID PID PPID C STIME TTY TIME COMMAND

root 1907 1 0 Oct 20 ? 1:10 /usr/local/prod/lsam/bin/sma_disp

root 1895 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_log

root 1901 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_lsam

root 1914 1913 0 Oct 20 ? 0:00 sh -c /usr/bin/tail -1f /var/adm/cron/log

root 1913 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_cronmon

root 1921 1 0 Oct 20 ? 0:01 /usr/local/prod/lsam/bin/sma_JORS

root 1923 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_RM

root 1925 1 0 Oct 20 ? 0:21 /usr/local/prod/lsam/bin/sma_fad fad1

root 1927 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_filein
```

:::

:::info Note

If the LSAM processes do not start as expected, examine the logfile, the errfile and the Terminal Output File files for error messages. Use the file path defined in the ```SMA_LOG_DIRECTORY``` variable. For information on the ```SMA_LOG_DIRECTORY``` variable, refer to [SMA_LOG_DIRECTORY](/configuration/updating-lsam-control-script#sma-log-directory).

:::

## Stop the LSAM

1. Log in to the UNIX system as root.
2. Change the directory to the LSAM's bin directory. Use the following syntax:

```cd <LSAM _Root_Directory>/bin```

3. Stop the LSAM with the following syntax: ```lsam<SAM_Socket>``` stop.

:::tip Example

The following example shows the command for stopping the LSAM using SAM Socket number 3100:

```cd /usr/local/lsam/bin; ./lsam3100 stop```

:::