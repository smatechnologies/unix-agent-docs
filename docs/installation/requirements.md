---
title: Installation Requirements
description: "Hardware, software, disk space, memory, and privilege requirements for installing the Unix Agent on a supported UNIX platform."
tags:
  - Reference
  - System Administrator
  - Installation
---

# Installation requirements

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?
Hardware, software, disk space, memory, and privilege requirements for installing the Unix Agent on a supported UNIX platform.

Consult this page in the following situations:

- Before performing a new installation of the Unix Agent, to confirm that the target machine meets the minimum disk space, memory, and privilege requirements.
- Before performing an upgrade installation, to verify that root or sudo access is available and that the correct SSL and Crypto library versions are in place.
- When the agent fails to start after installation and the system displays `error while loading shared libraries` messages, to follow the SSL and Crypto library resolution procedure.

1. Installation of the agent for UNIX requires an installer with root privileges. As long as your account has a UID of ```0```, it does not matter what the account name is. You must have root access because the agent must do user impersonation (by calling ```setuid ()``` and ```setgid()``` ).
    * Installers without root privileges may be able to perform a sudo installation. For information, refer to [Performing a Sudo Installation](../installation/preferred-installation#performing-a-sudo-installation).

2. All Unix agents require a minimum of 2.10 MB disk space and 2.6 MB memory. These requirements apply to all supported operating systems regardless of version.

Use the following information to aid in the installation:

* The agent installation directory is the location of all the agent components. For example, agent version 5.20 is normally located at ```/usr/local/lsam-5.20```.

* The agent root directory is a link to the agent installation directory (e.g., ```/usr/local/lsam/```). This is the location used to access the LSAM. For example, the directory ```/usr/local/lsam/``` for LSAM version 5.20 would be linked to ```/usr/local/lsam-5.20```. This symbolic link allows access to the LSAM to stay the same through upgrades. This access is meant for system-level use (e.g., an entry in "```/etc/init.d```" used to auto-start the LSAM at boot-up). Access to LSAM utilities from within user jobs is via environment variable ```$SMA_BINDIR```, which gets defined during agent installation.

* The SAM Socket Number (```<SAM_Socket>``` when discussing agent installation/operation) is the number of the first socket of eleven sequentially numbered sockets used by the agent. For example, if the SAM Socket Number is 3100, the agent uses 3100 through 3110. Through these sockets, the agent communicates with the SAM, the Job Output Retrieval System (JORS), SMA File Transfer (SMAFT) Agents, and running jobs. For future expansion, SMA Technologies recommends reserving 15 consecutive sockets.

* The agent Instance identifies a particular installation of the agent (e.g., "devel", "prod", or "abcxyz"). For backwards compatibility, the agent Instance defaults to ```<SAM_Socket>```. Using the agent Instance enables easier reconfiguration of the SAM Socket Number, and aids in easily identifying the agent and OpCon job-related output.

    * ```<LSAM_instance>``` is limited to 24 characters consisting of case-sensitive letters, digits (0 – 9), hyphens ('-'), and underscores ('_').

* The steps to be taken after the agent Installation file is placed on the target machine depend upon whether the installation is new or an upgrade.

* To use SSL UNIX tar files, you must install and configure the appropriate SSL and Crypto libraries in the correct library path search directories.

    * If the libraries are not properly loaded upon starting up the Unix Agent, errors similar to the following may be displayed on the screen:

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

To resolve the SSL library issue, complete the following steps:

1. ```ldconfig -p | grep libssl```
2. For example, running step 1 produces this output: "```libssl.so.1.0.0 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0```". This means that the SSL library is in directory ```/usr/lib/x86_64-linux-gnu``` and it is version 1.0.0.
3. The agent's start-up message "error while loading shared libraries: ```libssl.so.0.9.8```: cannot open shared object file: No such file or directory" showed that the agent is looking for SSL library version 0.9.8, which does not exist in the system.
4. To resolve that, create a symbolic link by running "```ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib/x86_64-linux-gnu/libssl.so.0.9.8```".
5. Similarly, repeat steps 1 – 4 but use "```libcrypto```" instead of "```libssl```" to properly configure the Crypto library.

The SSL and Crypto libraries are configured correctly.

:::info Note

You must perform all operations on the target machine with SuperUser authority, either by logging-in as 'root', or by running the 'su' command.

:::

Perform the steps in sequence to install the Unix Agent properly. For a list of the files and directories installed with the agent, refer to Unix Agent Configuration. The agent installation should take approximately 10 minutes.

