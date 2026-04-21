---
sidebar_label: 'install_lsam'
title: install_lsam
description: "Reference for the install_lsam script, which creates an operational Unix Agent instance with default configuration, a tracking directory, and a properly permissioned control script."
tags:
  - Reference
  - System Administrator
  - Agents
---

# install_lsam

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the install_lsam script, which creates an operational Unix Agent instance with default configuration, a tracking directory, and a properly permissioned control script.

The install_lsam script quickly creates an operational agent without additional configuration or extensive installation steps. The script performs the following actions:

* Copies the lsam script from the specified ```<LSAM root directory>/bin``` directory to ```<LSAM root directory>/bin/lsam<SAM_Socket >```.
* Runs chgexec to ensure that the permissions are set correctly on the binary images.
* Creates an empty job tracking directory.
* Automatically configures the agent with default values.

## Syntax

```cd <LSAM root directory>```

```bin/install_lsam `pwd` <SAM_Socket> <LSAM_instance>```

(Optional) ```<SAM_Socket>``` is a parameter that can be defined to identify the TCP/IP socket number the agent instance will use. If multiple agents will be installed on the same machine to the same parent directory, be sure to specify this parameter.
(Optional) ```<LSAM_instance>``` is a parameter that can be defined to identify the name of the agent instance. 

This setting is useful for defining distinctly different operating environments (e.g., Production versus Development environments). Do not specify this parameter if fail-over agents will be installed.
If not specified, ```<LSAM_instance>```, which provides the value for environment variable ```$SMA_LSAM_INSTANCE```, defaults to ```<SAM_Socket>```.

:::info Note

If planning to install fail-over agents, SMA Technologies recommends specifying the same ```<LSAM root directory>``` and ```<SAM_socket>```, but omitting the ```<LSAM_instance>``` parameter from the install_lsam command on each machine involved in the fail-over configuration.

:::

## Migrating to another SAM socket

It may become desirable to have the agent communicate with the SAM on a socket different than the SAM_socket with which it was originally installed. This is easily accomplished if ```<LSAM_instance> ```was specified when the agent was installed. For example:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3100 prod
```

To switch to another socket, simply re-install the agent with the same parameters as in the original installation, except for using the new socket number, e.g.:

```
cd /usr/local/lsam
bin/install_lsam `pwd` 3200 prod
```

This will create a new agent Control Script. Then, simply stop the agent with the old script, and restart it with the new script, e.g.:

```
bin/lsam3100 stop
bin/lsam3200 start
```

Mark the agent down in the Enterprise Manager prior to issuing the stop command. In between the stop and start, set the new socket number in the Machine Configuration screen in the Enterprise Manager. After issuing the start command, mark the agent back up.

If ```<LSAM_instance>``` is not specified at the time the agent is installed, changing SAM sockets requires various operations to ensure that agent configuration and job-related data will be retained across the change of SAM sockets. The agent Configuration program will need to be run. 

The job output files will need to be copied after setting-up the appropriate directory structure. And, the job tracking files will need to be copied. SMA Technologies therefore recommends that ```<LSAM_instance>``` always be specified at agent installation. 

If it should become necessary to change SAM sockets for an agent installed without an explicit ```<LSAM_instance>```, please contact your SMA Technologies support representative to help you accomplish the aforementioned operations.