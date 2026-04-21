---
title: Preferred Installation Procedures
description: "Step-by-step instructions for installing, upgrading, or adding Unix Agent instances using the install_agent script."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Preferred installation procedures

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?

Step-by-step instructions for installing, upgrading, or adding Unix Agent instances using the install_agent script.

:::info Note

The procedures in this section describe the preferred method for installing the Unix Agent. For the legacy method, refer to [Legacy Installation Procedures](../installation/legacy-installation).

:::

The Unix Agent installation is initiated by the install_agent script. The script lets you install, upgrade, or add one or more instance(s) of the agent at the same time.

## When would you use it?

Use the procedures on this page in the following situations:

- When performing a new Unix Agent installation on a UNIX machine, to create one or more agent instances using the install_agent script.
- When upgrading from an older version of the agent to a newer version, to stop the existing agent, convert the configuration file format, and carry forward existing configuration and job data.
- When adding another agent instance to an existing agent version, to create an additional agent instance with a new SAM socket number on the same machine.
- When the installing account does not have root privileges and the system administrator has configured sudo access, to perform the installation using the sudo command.

## Transferring the installation files

Transferring the installation files is the preferred installation method. For the initial release, you will need to transfer the script to the target machine. To transfer the installation files, complete the following steps:

1. Transfer the script and binary tar file (e.g., ```LSAM_15.00.01.24_Redhat_AS_5_0.tar```) to the UNIX machine. For the recommended file transfer procedures, refer to [Fetching the agent Installation File](../installation/fetch-install-file).

:::info Note

The install_agent script is included in the Unix Agent image in version 05.20.30 or later.

:::

2. Remove any excess ```.tar``` files from the current working directory.

:::info Note

To reduce the number of command arguments, there is not an option to specify the lsamexe.tar file. Instead, the script is designed to look for the file with the .tar extension and not a specific filename, and will expect to find only one such file type in the working directory.

:::

The installation files are transferred to the UNIX machine.

## Preparing for the installation

### Configure installation parameters

Prior to running the script, you can optionally configure the installation parameters for the platform. A text editor (e.g., vi) lets you edit the install_agent script.

:::tip Example

The following example identifies the default settings:

```
#---------------------------------------------------------------------

# User changeable installation parameters

#---------------------------------------------------------------------

START_AGENT=YES # if YES then start LSAM after installation

START_SERVICE=YES # if YES then auto start LSAM on system reboot

COPY_LOGFILE=YES # if YES then copy over STDOUT, STDERR and log dirs

USE_SYMLINK=YES # if YES then use symbolic link for LSAM ROOT/tmp dir

LSAM_BIN=*.tar # name of LSAM tar file

LSAM_LINK=/usr/local/lsam # default symbolic link to LSAM dir

INSTALL_LOG=/usr/local/install_agent.log # installation logfile

#---------------------------------------------------------------------
```
:::

During the installation, the script will perform the following actions:

* Create the symbolic link ```LSAM_LINK``` to the new version folder.
* Create the symbolic link ```LSAM_LINK.old.YYYYMMDD``` pointing to the version being updated. This provides a convenient link to when the upgrade was performed.
* Create a private key file (```sma_id_rsa```) and a public key file (```sma_id_rsa.pub```) under the root's .ssh directory, and then append the public key file to the root's .ssh/authorized_keys file. The purpose of the key is to allow SFTP to work without prompting you for a password. If you doesn't want to use SFTP for an OpCon File Transfer job, they can remove the appropriate entry in ```~root/.ssh/authorized_keys```.

START_AGENT and START_SERVICE, as configured in the install_agent script.

### Checking script permissions

Before you run the script, ensure that it has run permission by using the following syntax:

```chmod +x install_agent```

:::info Note

For version 05.20.30 or higher, the script should have the appropriate permission and you can invoke it directly from the ```LSAM_ROOT/```bin directory.

:::

## Running the script

You can use the install_agent script to perform a new install, an upgrade, or an add, depending on the type of installation that you require.

:::info Note

During the install, the script expects absolute pathname for the directories.

:::

### Performing a new installation

The "new" option not only allows you to create a new LSAM installation, but also create multiple agent instances at once. To perform a new installation, use syntax:

```./install_agent [new]```

:::tip Example

The following example shows the syntax for installing a new version with the agent instance number 3100:

```./install_agent new /usr/local/lsam-15.00.01 3100```


If installing multiple instances at once, add the additional instance numbers to the end of the string:

```./install_agent new /usr/local/lsam-15.00.01 3100 4100 5100```

:::

The new LSAM installation is created.

### Performing an upgrade installation

:::info Note

During the upgrade, the script also checks to make sure the second specified directory parameter points to an existing agent version.

:::

The "upgrade" options allows you to upgrade from an older version of the agent. To upgrade, use syntax:

```./install_agent [upgrade]```

:::tip Example

The following example shows the syntax for upgrading from version 05.20.01 of the LSAM to version 15.00.01:

```./install_agent upgrade /usr/local/lsam-15.00.01 /usr/local/lsam-05.20.01```

:::

During an upgrade, the script will perform the following actions:

* Stop the existing agent.
* Convert the agent's lsam.conf to the correct format as new parameters/options had been added to that file to accommodate new features in the latest releases.
* Copy over the agent's cronmon.conf and SMA_RM.conf (if they exist).
* Copy over everything under fad/AGENT_INSTANCE (e.g., fad/3100 folder) and ppscripts directories (if they exist).

The agent is upgraded to the new version.

### Performing an add installation

The "add" option allows you to add another instance of the agent to an existing version. To add another instance, use syntax:

```./install_agent [add]```

:::tip Example

The following example shows the syntax for adding another agent instance 6100 to version 15.00.01 of the LSAM:

```./install_agent add /usr/local/lsam-15.00.01 6100```

:::

:::info Note

The "add" option will not work for versions 05.20.01 or older since those versions prompt you for inputs for some of the configuration settings (such as symbolic linking of the tmp directory and STDOUT/STDERR file capture for JORS). This was done starting with release 05.20.20 to allow for non-interactive (i.e., without any user's input) agent installation. The default action is to create a symbolic link of LSAM_ROOT/tmp to /tmp directory and enable STDOUT/STDERR file capture by JORS. The rational for doing a symbolic link to /tmp is that there is more ample disk space allocated there under the typical UNIX file system. If this is not the case, you can manually remove the symbolic link and create the tmp directory under LSAM_ROOT folder, as follows:

1. ```rm LSAM_ROOT/tmp```
2. ```mkdir LSAM_ROOT/tmp```
3. ```chmod 1777 LSAM_ROOT/tmp```

For proper operation of agent (e.g., SMAFT file transfer between different UNIX user's accounts), the tmp directory needs to have read/write/run permission for everyone. The sticky bit ("t") is shown being set to avoid deletion of a folder by other users.

:::

The new agent instance is added to the existing version.

### Verifying the installation

You can check the output of the log file (```$INSTALL_LOG```) to check the status (success or failure) of the installation.

### Performing a sudo installation

The UNIX agent code was designed to be installed by a root account. If the installer does not have root privileges, the UNIX administrator must set up you account to use the sudo command.

To perform a sudo installation, complete the following steps:

1. Copy the install_agent script and lsamexe.tar file to a directory.
2. Perform the installation by prepending 'sudo' to the syntax, as in:

```sudo ./install_agent [upgrade | new | add]```


:::tip Example

The following example shows the syntax for installing a new version with the agent instance number 6000:

```sudo ./install_agent new /usr/local/lsam-new 6000```

:::

The installation completes with sudo privileges.

## Exception handling

**`install_agent: Permission denied` when running the script** — The install_agent script does not have execute permission. — Run `chmod +x install_agent` before invoking the script.

**`error while loading shared libraries: libssl.so.x.x.x: cannot open shared object file: No such file or directory`** — The SSL or Crypto library version the agent was built against is not present in the system library path. This error appears for each agent daemon (`sma_log`, `sma_lsam`, `sma_disp`, etc.) that fails to start. — Run `ldconfig -p | grep libssl` to locate the installed SSL library version, then create a symbolic link from the expected version name to the installed version (for example, `ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib/x86_64-linux-gnu/libssl.so.0.9.8`). Repeat the same steps using `libcrypto` in place of `libssl` to resolve the Crypto library. See [Installation Requirements](../installation/requirements) for the complete procedure.

**Script fails or behaves unexpectedly when locating the tar file** — More than one `.tar` file is present in the working directory. The install_agent script searches for a single file with the `.tar` extension rather than a specific filename. — Remove any extra `.tar` files from the working directory before running the script, leaving only the agent binary tar file.

**`EACCES - Permission denied` or `EPERM - Not owner` during installation** — The account running the script does not have the required privileges. The agent installation requires root authority because the agent must call `setuid()` and `setgid()`. — Run the script as root, or use `sudo ./install_agent` if the system administrator has configured sudo access for the installing account.

**`EADDRINUSE - Address already in use` after installation** — The SAM Socket number chosen during installation is already bound by another process. The agent uses eleven consecutive sockets starting from the specified `<SAM_Socket>` value. — Identify the conflicting process with a command such as `netstat -an | grep <SAM_Socket>`, resolve the conflict, or reinstall the agent specifying a different `<SAM_Socket>` number.
