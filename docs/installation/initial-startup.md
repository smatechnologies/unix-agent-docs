# Initial Startup

Whether performing a new install or an upgrade, the following procedure starts the LSAM executing after installation:

1. If performing an upgrade installation, determine if any system scripts or users' jobs depend on the SAM Socket number being a part of a pathname (e.g., "```/usr/local/lsam/MSGIN/3100```"). If this is so, the ideal solution would be to edit the jobs by changing the hard-coded SAM Socket number or referencing the environment variable ```$SAM_SOCKET``` to use the environment variable ```$SMA_LSAM_INSTANCE```. If this is not practical, then do the following from the LSAM root directory:
* Enter the command ```ls –l *```
* Make a note of all occurrences of sub-directories named ```<LSAM_instance>``` (e.g., "```MSGIN/prod```"). Ignore the "```bin/```" directory.
* For each sub-directory noted in the previous step, create a symbolic link in the same parent directory to point to the ```<LSAM_instance>``` sub-directory.

:::tip Example

Assuming a ```<SAM_Socket>``` of 3100 and an ```<LSAM_instance>``` of "prod", the following example shows the syntax for creating a ```<SAM_Socket>``` symbolic link in the MSGIN directory to the ```<LSAM_instance> ```sub-directory:

```ln -s MSGIN/3100 MSGIN/prod```

:::

2. Start the LSAM. Use the following syntax: ```bin/lsam<SAM_Socket>``` start.
For information on operating the LSAM, refer to [Operating the LSAM](../operations/operating-the-lsam).

:::tip Example

The following example shows the command for starting the LSAM using SAM Socket number 3100:

```bin/lsam3100 start```

:::

:::info Note

During start-up (and in other situations) the LSAM produces output to the terminal. To make it available in resolving support issues, terminal output is automatically redirected to file "```LSAM_output_<SAM_socket>```" within the LSAM root directory. Prior to version 3.07.01 of the LSAM, the output during the LSAM's start-up would appear on the terminal in real time. Now it is delayed until the start-up procedure has been completed, at which point the LSAM_output file is dumped to the terminal. The start-up procedure normally completes in less than 30 seconds. If it takes more than five minutes, the start-up procedure may be interrupted with ```Cntrl_C``` (or the system's assigned INT sequence) and the command entered to see the terminal output that was produced.

```cat LSAM_output_<SAM_socket>```

(e.g., "```cat LSAM_output_3100```")

The LSAM output file may be inspected at any time (via the 'cat', tail', 'vi' or other text-viewing commands). The command "```tail –f LSAM_output_<SAM_socket>```" allows real-time viewing of LSAM terminal output.

:::

3. Verify the LSAM status with the following command: ```bin/lsam<SAM_Socket> status```. The command should display the following processes:
* sma_disp
* sma_log
* sma_lsam
* Any enabled, optional components:
    * sma_cronmon
    * sma_filein
    * sma_fad
    * sma_JORS

:::tip Example

The following example shows the command to verify the status of the LSAM using SAM Socket number 3100:

```bin/lsam3100 status```


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

root 1927 1 0 Oct 20 ? 0:12 /usr/local/prod/lsam/bin/sma_filein

root 1929 1 0 Oct 20 ? 0:00 /usr/local/prod/lsam/bin/sma_JORS
```

:::

:::info Note

If the LSAM processes do not start as expected, examine the logfile and the errfile files for error messages. Use the file path defined in the SMA_LOG_DIRECTORY variable in the LSAM Control Script. For information on editing the LSAM Control Script, refer to [Updating the LSAM Control Script](../configuration/updating-lsam-control-script).

:::

4. To begin using the LSAM, refer to [UNIX LSAM Configuration](../configuration/unix-lsam-configuration) to configure and operate the LSAM.

