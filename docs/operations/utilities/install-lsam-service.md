# install_lsam_service

The install_lsam_service script creates symbolic links in the start up directory, so the LSAM will be started automatically when the machine is rebooted. This script is valid on the following UNIX platforms: Linux, AIX, HP-UX, and Solaris.

## Syntax

```
cd <LSAM root directory>

bin/install_lsam_service `pwd` <SAM_Socket>
```

```<SAM_Socket>``` is a parameter that identifies the TCP/IP socket number the LSAM instance was installed to use.