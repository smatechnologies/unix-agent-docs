# Additional Procedures

This topic describes conditions and procedures which may be required to be executed. They may apply to either a new or an upgrade installation.

## Migrate to Another SAM Socket

It may become necessary to have the LSAM communicate with the SAM on a socket different than the SAM_socket with which it was originally installed. This is easily accomplished if ```<LSAM_instance>``` was specified when the LSAM was installed. For example:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3100 prod
```

To switch to another socket, simply re-install the LSAM with the same parameters as in the original installation, except for using the new socket number. For example:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3200 prod
```

This will create a new LSAM Control Script. Then, simply stop the LSAM with the old script, and restart it with the new script. For example:

```
bin/lsam3100 stop
bin/lsam3200 start
```
 
Mark the LSAM down in the Enterprise Manager prior to issuing the stop command. In between the stop and start, set the new socket number in the Machines screen in the Enterprise Manager. After issuing the start command, mark the LSAM back up.

If ```<LSAM_instance>``` is not specified at the time the LSAM is installed, changing SAM sockets requires various operations to ensure that LSAM configuration and job-related data will be retained across the change of SAM sockets. These operations included:

* Running the LSAM Configuration program.
* Copying the job output files after setting-up the appropriate directory structure.
* Copying the job tracking files.

SMA Technologies recommends that ```<LSAM_instance>``` always be specified during the LSAM installation. If it is necessary to change SAM sockets for an LSAM installed without an explicit ```<LSAM_instance>```, please contact the SMA Technologies support representative to help accomplish the above mentioned operations.

