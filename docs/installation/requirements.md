# Installation Requirements

1. Installation of the LSAM for UNIX requires an installer with root privileges. As long as the user account has a UID of ```0```, it does not matter what the "prod" of the account is. Root access is required because the LSAM must do user impersonation (by calling ```setuid ()``` and ```setgid()``` ).
    * Installers without root privileges may be able to perform a sudo installation. For information, refer to [Performing a Sudo Installation](../installation/preferred-installation#performing-a-sudo-installation).

2. All UNIX LSAM's require a minimum of 2.10 MB disk space and 2.6 MB memory. These requirements apply to all supported operating systems regardless of version.

Use the following information to aid in the installation:

* The LSAM installation directory is the location of all the LSAM components. For example, LSAM version 5.20 is normally located at ```/usr/local/lsam-5.20```.

* The LSAM root directory is a link to the LSAM installation directory (e.g., ```/usr/local/lsam/```). This is the location used to access the LSAM. For example, the directory ```/usr/local/lsam/``` for LSAM version 5.20 would be linked to ```/usr/local/lsam-5.20```. This symbolic link allows access to the LSAM to stay the same through upgrades. This access is meant for system-level use (e.g., an entry in "```/etc/init.d```" used to auto-start the LSAM at boot-up). Access to LSAM utilities from within user jobs is via environment variable ```$SMA_BINDIR```, which gets defined during LSAM installation.

* The SAM Socket Number (```<SAM_Socket>``` when discussing LSAM installation/operation) is the number of the first socket of eleven sequentially numbered sockets used by the LSAM. For example, if the SAM Socket Number is 3100, the LSAM uses 3100 through 3110. Through these sockets, the LSAM communicates with the SAM, the Job Output Retrieval System (JORS), SMA File Transfer (SMAFT) Agents, and running jobs. For future expansion, SMA Technologies recommends reserving 15 consecutive sockets.

* The LSAM Instance identifies a particular installation of the LSAM (e.g., "devel", "prod", or "abcxyz"). For backwards compatibility, the LSAM Instance defaults to ```<SAM_Socket>```. Using the LSAM Instance enables easier reconfiguration of the SAM Socket Number, and aids in easily identifying the LSAM and OpCon job-related output.

    * ```<LSAM_instance>``` is limited to 24 characters consisting of case-sensitive letters, digits (0 – 9), hyphens ('-'), and underscores ('_').

* The steps to be taken after the LSAM Installation file is placed on the target machine depend upon whether the installation is new or an upgrade.

* In order to use the SSL UNIX tar files, the appropriate SSL and Crypto libraries need to be installed or configured properly in the correct library path search directories.

    * If the libraries are not properly loaded upon starting up the UNIX LSAM, errors similar to the following may be displayed on the screen:

:::tip Example

/usr/lib/lsam-17.1.26/bin/validate_startup: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

Pre-start validation completed.

 

--- Starting logging daemon

/usr/lib/lsam-17.1.26/bin/sma_log: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

--- Starting lsam daemon

/usr/lib/lsam-17.1.26/bin/sma_lsam: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

--- Starting dispatcher daemon

/usr/lib/lsam-17.1.26/bin/sma_disp: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

--- Starting CronMon

/usr/lib/lsam-17.1.26/bin/sma_cronmon: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

--- Starting Filein

/usr/lib/lsam-17.1.26/bin/sma_filein: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

--- Starting sma_JORS

/usr/lib/lsam-17.1.26/bin/sma_JORS: error while loading shared libraries: libssl.so.0.9.8: cannot open shared object file: No such file or directory

:::

Users need to log in as root and perform the following steps to resolve this issue:
1. ```ldconfig -p | grep libssl```
2. For example, running step 1 produces this output: "```libssl.so.1.0.0 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0```". This means that the SSL library is in directory ```/usr/lib/x86_64-linux-gnu``` and it is version 1.0.0.
3. The agent's start-up message "error while loading shared libraries: ```libssl.so.0.9.8```: cannot open shared object file: No such file or directory" showed that the agent is looking for SSL library version 0.9.8, which does not exist in the system.
4. To resolve that, create a symbolic link by running "```ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib/x86_64-linux-gnu/libssl.so.0.9.8```".
5. Similarly, repeat steps 1 – 4 but use "```libcrypto```" instead of "```libssl```" to properly configure the Crypto library.

:::info Note

All operations on the target machine are to be executed with SuperUser authority, either by logging-in as 'root', or by executing the 'su' command.

:::

Perform the steps in sequence to install the UNIX LSAM properly. For a list of the files and directories installed with the LSAM, refer to UNIX LSAM Configuration. The LSAM installation should take approximately 10 minutes.

