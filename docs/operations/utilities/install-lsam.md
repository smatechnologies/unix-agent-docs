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

- You are deploying a new Unix Agent instance and need an operational agent quickly without running the full installation procedure.
- You are installing multiple agent instances on the same machine and need to assign each a distinct socket number and instance name.
- You are configuring a fail-over agent pair and need to ensure both instances share the same root directory and socket without an explicit instance name.
- Specifying `<LSAM_instance>` at installation time makes it straightforward to migrate the agent to a different SAM socket later without additional manual configuration.

## Syntax

```cd <LSAM root directory>```

```bin/install_lsam `pwd` <SAM_Socket> <LSAM_instance>```

## Parameters

| Parameter | Required | Description |
|---|---|---|
| `pwd` | Required | Root directory of the agent installation, passed using the shell `pwd` command. |
| `<SAM_Socket>` | Optional | TCP/IP socket number the agent instance will use. Required when installing multiple agent instances on the same machine to the same parent directory. |
| `<LSAM_instance>` | Optional | Name of the agent instance. Sets the `$SMA_LSAM_INSTANCE` environment variable. Defaults to `<SAM_Socket>` if not specified. Do not specify for fail-over agent installations. |

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

## Glossary

**SAM socket** — The TCP/IP port number the Unix Agent uses to communicate with the SAM. Specified as `<SAM_Socket>` in the `install_lsam` command and used to name the agent Control Script (for example, `lsam3100`).

**agent instance** — A single running installation of the Unix Agent identified by its `$SMA_LSAM_INSTANCE` environment variable. Multiple agent instances can run on the same machine using different socket numbers and instance names.

**fail-over configuration** — An agent deployment in which two instances on different machines share the same root directory and socket number. Omit the `<LSAM_instance>` parameter when installing agents intended for fail-over to avoid configuration conflicts during switchover.