# Utilties Overview

The programs in this section do not use the LSAM Control Script. All utilities are located in the ```<LSAM root path>/bin/``` directory. All require root privileges, except file_check, maintain_ofiles, sma_ppscript, and sma_status, which are available to be called from any OpCon job. 

In the table that follows, a short description of each utility is provided. 

| Utility | Short Description |
| ------- | ----------------- |
| exit_codes | Displays the return values of a process |
| file_check | Checks if specified file(s) meet certain criteria |
| genericpgm | A dummy program used to test the LSAM |
| get_errno | Translates a UNIX error number into meaningful text |
| install_lsam | Quickly creates an operational LSAM without additional configuration or extensive installation steps |
| install_lsam_service | This script creates symbolic links in the start up directory, so the LSAM will be started automatically when the machine is rebooted |
| lsam_killjob | Sends a SIGKILL signal to terminate specified job |
| maintain_ofiles | Prevents the accumulation of outdated job-related files |
| sma_job_step | Called to have the LSAM advise SAM that a Job Step is about to be executed |
| sma_LSAM_feedback | Called to have LSAM report text to be added to a job's "Detailed Job Message" list in Enterprise Manager |
| sma_ppscript | Registers a post-processing script (ppscript) to analyze the standard out of a job |
| sma_status | Sends message for the Enterprise Manager to display after the OpCon status message |
| uninstall_lsam | Quickly removes an LSAM |

