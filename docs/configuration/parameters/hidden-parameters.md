# Hidden LSAM Configuration Parameters

There are three LSAM configuration parameters which are not meant to be changed except under limited circumstances, and these are not displayed in the LSAM Configuration Utility. They are contained within the actual LSAM configuration file, "```$LSAM_ROOT/config/<LSAM_instance>/lsam.conf```", and can only be changed by editing this file. SMA Technologies strongly recommends that these parameters not be changed unless so-directed by an SMA Technologies Support person, and that the LSAM configuration file not otherwise be edited. The parameters are:

### lsam_root_directory

* The location of the top-level installation directory, ```$LSAM_ROOT```.

### check_CRC

* Enable/Disable CRC checking.

### close_SAM_socket

* Keep socket to SAM open across messages, or close after each message.


Each parameter in the file appears on a line by itself, of the form "Parameter = value", e.g., "check_CRC = 1". The file also contains comments, indicated by a '#', with the '#' and the remainder of the line being ignored by the LSAM as it processes the file.