# Preferred Installation Procedures

:::info Note

The procedures in this section describe the preferred method for installing the UNIX LSAM. For the legacy method, refer to [Legacy Installation Procedures](../installation/legacy-installation).

:::

The UNIX LSAM installation is initiated by the install_agent script. The script can be executed to install, upgrade, or add one or more instance(s) of the LSAM at the same time.

## Transferring the Installation Files

Transferring the installation files is the preferred installation method. For the initial release, you will need to transfer the script to the target machine. Follow the steps provided in this section to do so.

1. Transfer the script and binary tar file (e.g., ```LSAM_15.00.01.24_Redhat_AS_5_0.tar```) to the UNIX machine. For the recommended file transfer procedures, refer to [Fetching the LSAM Installation File](../installation/fetch-install-file).

:::info Note

The install_agent script is included in the UNIX LSAM image in version 05.20.30 or later.

:::

2. Remove any excess ```.tar``` files from the current working directory.

:::info Note

To reduce the number of command arguments, there is not an option to specify the lsamexe.tar file. Instead, the script is designed to look for the file with the .tar extension and not a specific filename, and will expect to find only one such file type in the working directory.

:::

## Preparing for the Installation

### Configure Installation Parameters

Prior to running the script, you can optionally configure the installation parameters for the platform. A text editor (e.g., vi) can be used to edit the install_agent script.

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
* Create a private key file (```sma_id_rsa```) and a public key file (```sma_id_rsa.pub```) under the root's .ssh directory, and then append the public key file to the root's .ssh/authorized_keys file. The purpose of the key is to allow SFTP to work without prompting the user for a password. If the user doesn't want to use SFTP for an OpCon File Transfer job, they can remove the appropriate entry in ```~root/.ssh/authorized_keys```.

START_AGENT and START_SERVICE, as configured in the install_agent script.

### Checking Script Permissions

Before you run the script, ensure that it has execute permission by using the following syntax:

```chmod +x install_agent```

:::info Note

For version 05.20.30 or higher, the script should have the appropriate permission and can be invoked directly from the ```LSAM_ROOT/```bin directory.

:::

## Executing the Script

You can use the install_agent script to perform a new install, an upgrade, or an add, depending on the type of installation that you require.

:::info Note

During the install, the script expects absolute pathname for the directories.

:::

### Performing a New Installation

The "new" option not only allows you to create a new LSAM installation, but also create multiple agent instances at once. To perform a new installation, use syntax:

```./install_agent [new]```

:::tip Example

The following example shows the syntax for installing a new version with the agent instance number 3100:

```./install_agent new /usr/local/lsam-15.00.01 3100```


If installing multiple instances at once, add the additional instance numbers to the end of the string:

```./install_agent new /usr/local/lsam-15.00.01 3100 4100 5100```

:::

### Performing an Upgrade Installation

:::info Note

During the upgrade, the script also checks to make sure the second specified directory parameter points to an existing LSAM version.

:::

The "upgrade" options allows you to upgrade from an older version of the LSAM. To upgrade, use syntax:

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

### Performing an Add Installation

The "add" option allows you to add another instance of the LSAM to an existing version. To add another instance, use syntax:

```./install_agent [add]```

:::tip Example

The following example shows the syntax for adding another agent instance 6100 to version 15.00.01 of the LSAM:

```./install_agent add /usr/local/lsam-15.00.01 6100```

:::

:::info Note

The "add" option will not work for versions 05.20.01 or older since those versions prompt the user for inputs for some of the configuration settings (such as symbolic linking of the tmp directory and STDOUT/STDERR file capture for JORS). This was done starting with release 05.20.20 to allow for non-interactive (i.e., without any user's input) LSAM installation. The default action is to create a symbolic link of LSAM_ROOT/tmp to /tmp directory and enable STDOUT/STDERR file capture by JORS. The rational for doing a symbolic link to /tmp is that there is more ample disk space allocated there under the typical UNIX file system. If this is not the case, you can manually remove the symbolic link and create the tmp directory under LSAM_ROOT folder, as follows:

1. ```rm LSAM_ROOT/tmp```
2. ```mkdir LSAM_ROOT/tmp```
3. ```chmod 1777 LSAM_ROOT/tmp```

For proper operation of LSAM (e.g., SMAFT file transfer between different UNIX user's accounts), the tmp directory needs to have read/write/execute permission for everyone. The sticky bit ("t") is shown being set to avoid deletion of a folder by other users.

:::

### Verifying the Installation

You can check the output of the log file (```$INSTALL_LOG```) to check the status (success or failure) of the installation.

### Performing a Sudo Installation

The UNIX agent code was designed to be installed by a root account. If the installer does not have root privileges, the UNIX administrator must set up the user account to use the sudo command.

If properly configured, you can use the following steps to install:

1. Copy the install_agent script and lsamexe.tar file to a directory.
2. Perform the installation by prepending 'sudo' to the syntax, as in:

```sudo ./install_agent [upgrade | new | add]```


:::tip Example

The following example shows the syntax for installing a new version with the agent instance number 6000:

```sudo ./install_agent new /usr/local/lsam-new 6000```

:::