---
sidebar_label: 'Release notes'
---

# Unix Agent Release Notes

## Version 22.0.0

## Version 21.2

### 2021 August

:white_check_mark: **UNIX-331**: Fixed an issue in UNIX agent where file transfers to a Windows machine failed if the Windows machine was configured with an IPv6 address.

:white_check_mark:	**UNIX-360**: Fixed an issue in UNIX agent where if the /tmp folder does not exist, then it creates one under the current installation folder.

:white_check_mark:	**UNIX-361**: Fixed an erroneous message in the UNIX agent log on core dump.

:white_check_mark:	**UNIX-375**: Fixed an issue in UNIX agent where a Symitar Print job did not run successfully due to incorrect handling of environment variable addresses.

:white_check_mark:	**UNIX-382**: Allows running of maintain_ofiles at a user configured time, when no jobs are running so it does not fail due to conflicts.

:white_check_mark:	**UNIX-388**: Fixed an issue in UNIX agent where the buffer size for environment variables was increased to 2K from 1K to accommodate larger variables.

## Version 21.0

### 2021 April

:white_check_mark:	**UNIX-386**: Fixed an issue in UNIX agent where sometimes jobs failed with STDERR: LOGNAME this variable is read only.

:white_check_mark:	**UNIX-387**: Fixed an issue in the UNIX agent where a user profile environment variable like SHELL was getting overwritten by another value by the agent.

## Version 20.0

### 2020 December

:white_check_mark:	**UNIX-378**: Fixed an issue in SMAFT wild card transfer where the specified destination file field is supposed to be a directory name, but instead it exists in the system as a regular file.

:white_check_mark:	**UNIX-377**: Fixed an issue in which "lsam refresh" command improperly auto-configures path_to_su setting to "no" on non-Symitar platforms. The work-around is to use "lsam config" to set path_to_su to "yes" and then issue a "lsam restart" command.

:white_check_mark:	**UNIX-376**: Fixed an issue where install_lsam script doesn't create the correct port number when LSAM_instance label option is specified.

:white_check_mark:	**UNIX-372**: Fixed an issue where the Control File filename length is limited to 63 characters.

:white_check_mark:	**UNIX-349**: Fixed an issue where the Installation procedure in the UNIX documentation did not specify that the install_agent script needed to be copied from the installation media/ftp site to the /tmp folder in order to update the UNIX LSAM.

## Version 19.1.25

### 2020 May

:white_check_mark:	Fixed an issue where SMAFT jobs transferring from UNIX to Windows, with the job starting at the destination (Windows), could result in excessive delay and intermittent timeouts.

:white_check_mark:	Fixed an issue where path_to_su would not be able to execute successfully. If unable to su properly, it will now default to the older user impersonation model.
 
## Version 19.1.16

### 2020 May

:eight_spoked_asterisk:  Added TLS support to SMAFT (SMA File Transfer) feature. Added a new parameter, SMAFT_TLS_socket to lsam.conf to designate that this port number is used for TLS SMAFT. Note also that parameters lsam_pem_file and lsam_private_key_file in lsam.conf need to be defined for TLS SMAFT to work.

:eight_spoked_asterisk:  Enabled starting and stopping the LSAM service using systemctl on Linux servers.

:eight_spoked_asterisk:  Changed the path_to_su default from "No" to "Yes" for executing jobs as this is the recommended default for new installations.

:white_check_mark:	Fixed an issue where filenames that have "$" embedded in them resulted in the filename being truncated after the "$" character. This problem only happened on su-submitted SMAFT jobs.

:white_check_mark:	Fixed an issue where the install_agent script that was used to install UNIX did not restart the agent after a system reboot. This was due to Debian and Ubuntu using different directories in Redhat for auto-restarting with systemd on reboot.

:white_check_mark:	Fixed an issue where multiple white spaces were trimmed in a start_image that contained an encrypted property value.

:white_check_mark:	Fixed an issue where "Received unauthorized message - discarded" messages may have caused communication to the sma_lsam process to crash, resulting in the agent being stopped/terminated. The safest course is to not print the contents of the discarded message.

:white_check_mark:	Redesigned the sma_log process to resolve an issue where the LSAM crashes intermittently on later Redhat releases.

:white_check_mark: Fixed an issue where jobs fail when UNIX LSAM starts the "main_ofiles" program. Changed main_ofiles to run once daily any time between 3 AM to 4 AM when the system is likely to be idled.
 
## Version 19.0.0

### 2019 July

:eight_spoked_asterisk:  Enhanced File Arrival jobs to now allow a total of 255 characters in the filename only (not including the path name) and 1023 characters in the path name. The previous limit for File Arrival jobs allowed for 128 characters.

:white_check_mark:	Fixed an issue where File Arrival jobs would return successfully when encountering a signal 11 error (or any other abnormal signal). It will now return exit code 4 and log the message "Internal system error: Abnormal signal caught".

:white_check_mark:  Fixed an issue where encrypted arguments in embedded script jobs were not decrypted and encrypted environment variables were not decrypted.

:white_check_mark:  Fixed an issue where the bound_NIC_adapter_ip setting in the lsam.conf file was not working.

:white_check_mark:  Fixed an issue where the UNIX LSAM would escape UNC paths of Windows filenames for SMAFT file transfer jobs that start on the UNIX side and have path_to_su enabled.

:white_check_mark:  Updated install_agent script to support LSAM instance label name.

:white_check_mark:  Fixed an issue where jobs fail when UNIX LSAM starts the "main_ofiles" program. Changed main_ofiles to run once daily any time between 3 AM to 4 AM when the system is likely to be idled.
 
## Version 18.3.0

### 2018 November

:eight_spoked_asterisk:  Updated UNIX Job Action: File Arrival performance to utilize less CPU usage.

:eight_spoked_asterisk:  The days_of_output_to_keep parameter description has been updated to clarify that setting the value to 0 will disable clean-up of STDOUT and STDERR files.

:white_check_mark:	Fixed an issue with recognizing the profile PATH environment variable when path_to_su was enabled.

:white_check_mark:	Fixed an issue where TLS communication between SAM and the Job Output Retrieval Service (JORS) was not working for the following platforms: HP-UX, SOLARIS, UBUNTU, DEBIAN, and SUSE.

:white_check_mark:	Fixed an issue where the KILL command issued from the Enterprise Manager failed to completely terminate the "non-root" user su-submitted job. This issue only affected Redhat releases RHEL6 and higher.

 
## Version 18.2.0

### 2018 September

:white_check_mark:  Fixed an issue with File Transfer jobs where files containing a wildcard going to a single file failed with an exit code 14099 "compression not supported" error.

:white_check_mark:  Fixed an issue in the Job Output Retriever where logfiles and errfiles were not written to the correct path.

 
## Version 18.1.0

### 2018 June

:eight_spoked_asterisk:  Added the ability to define Environment Variables to UNIX Job Action: Embedded Script.

:eight_spoked_asterisk:  Added the ability to parse job output for UNIX jobs to determine an exit code.

:eight_spoked_asterisk:  Added the ability to define Environment Variables to UNIX Job Action: Run Program.

:eight_spoked_asterisk:  Added the following job meta-data to STDOUT files:

* JOB_ID
* SCHEDULE_DATE
* SCHEDULE_NAME
* SCHEDULE_FREQ
* START_IMAGE
* UNIX_LSAM_ROOT_DIR
* JOB_START_TIME

:eight_spoked_asterisk:  Removed the max_burst parameter from the LSAM configuration file.

:white_check_mark:	Fixed an issue where FAD processed files that were already created.

:white_check_mark:	Fixed an issue with the UNIX LSAM where file transfers with wild cards and spaces in the file name did not work.

:white_check_mark:	Fixed an issue where SMA File Transfer successfully transferred a file into the parent folder (/) when the specified destination folder (e.g., /TMP) did not exist. The transfer will now fail with a sample message "Destination directory /TMP doesn't exist or accessible by user" when this condition is detected.

:white_check_mark:	Fixed an issue where sometimes the UNIX destination file permission was not set correctly when the UNIX LSAM would initiate an SMA File Transfer job from Windows to UNIX.

:white_check_mark:  Fixed an issue where a non-descriptive exit code 16 was given when performing a file transfer without specifying the destination file name. Now, file transfers can be transferred with no destination file name specified.

 
## Version 17.1.0

### 2017 December

:eight_spoked_asterisk:  Added support to use the newer Linux systemd service to enable auto-start of LSAM on system reboot.

:eight_spoked_asterisk:  The Prerun, Start Image, and Arguments fields in UNIX Job Details now allow up to 2000 characters.

:eight_spoked_asterisk:  Updated the UNIX SMA File Transfer (SMAFT) exit codes. These codes can be found in the agent documentation for UNIX.

:eight_spoked_asterisk:  Updated the UNIX LSAM to allow writing files larger than 2 gigabytes for SMA File Transfer on AIX platform.

:eight_spoked_asterisk:  Updated the UNIX LSAM to return the actual start command of a job back to OpCon, which can be referenced on the OpCon side using the property [[JI.$START COMMAND]].

:eight_spoked_asterisk:  Added support for Advanced Failure Criteria to UNIX Job Action: File Arrival.

:eight_spoked_asterisk:  Updated the UNIX LSAM to return new exit codes for UNIX Job Action: File Arrival.

:eight_spoked_asterisk:  Updated the UNIX LSAM to support encrypted tokens. To use encryption token capability, tarfiles that have "SSL" support must be used since encryption relies on the SSL encryption libraries. Users do not have to enable or turn on the UNIX agent's TLS communication with OpCon to take advantage of this feature, they only need to use SSL-labeled tarfiles.

:white_check_mark:	
Fixed an issue where the Time Sent field was displayed incorrectly in the Enterprise Manager Advanced Machine Properties.

:white_check_mark:
Fixed an issue where if the Start and End Time were set to zero in a File Arrival job, then the job failed even if the file was present.

:white_check_mark:	
Fixed an issue with the UNIX LSAM where the detection of duplicate job start requests for the same job from OpCon could trigger data corruption and the crash of SMANetCom.

:white_check_mark:
Fixed an issue where UNIX Job Action: File Arrival would not detect a file if the path used a symbolic link.