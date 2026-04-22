---
title: Legacy Installation
description: "Step-by-step procedures for performing a new or upgrade Unix Agent installation using the legacy manual method."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Legacy installation

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?
Step-by-step procedures for performing a new or upgrade Unix Agent installation using the legacy manual method.

:::info Note

The procedures in this section describe the legacy method for installing the Unix Agent. For the preferred method, refer to [Preferred Installation Procedures](../installation/preferred-installation).

:::

Use the legacy installation method in the following situations:

- When the Unix Agent version being installed is older than 05.20.30, because the install_agent script used by the preferred method is only included in version 05.20.30 or later.
- When the "add" option of the preferred installation is unavailable because the target agent version is 05.20.01 or older, as those versions require interactive input during configuration that the install_agent script cannot provide.

## When the preferred installation is not available

The preferred installation method requires the install_agent script, which is included in the Unix Agent image starting with version 05.20.30. If you are installing a version earlier than 05.20.30, or if the script is otherwise unavailable on the target machine, use the legacy procedures described on this page to manually create the installation directory, establish symbolic links, extract the tar file, set file ownership, and run the install_lsam script.

This section describes how to install the Unix Agent using the legacy method. The type of installation that you require will determine what steps you must take.

## Preparing for a new agent installation

When performing a new installation, the procedure for 'Setting up the agent Installation Directory' will:

* Create the agent installation directory.
* Create a symbolic link from the agent installation directory to the agent root directory.

### Set up the agent installation directory

To set up the agent installation directory for a new installation, complete the following steps:

1. Create the agent installation directory. Use the following syntax:

```mkdir /usr/local/lsam<version>```

:::tip Example

The following example shows the syntax for creating an LSAM installation directory for LSAM version 4.01:

```mkdir /usr/local/lsam-4.01```

:::

2. Create a symbolic link from the new agent installation directory to the agent root directory with the following syntax:

```ln –s <LSAM installation directory> <LSAM root directory>```

:::tip Example

The following example shows the syntax for creating a symbolic link from the new LSAM installation directory to the LSAM root directory:

```ln -s /usr/local/lsam-4.01 /usr/local/lsam```

:::

The agent installation directory is created and linked.

## Preparing for an upgrade agent installation

When performing an upgrade installation, the following procedure for 'Setting Up the agent Installation Directory' will:

* Create the agent installation directory.
* Change the agent root directory symbolic link to point to the new agent installation directory.
* Ensure that existing users' jobs will continue to run.

### Set up the agent installation directory

To set up the agent installation directory for an upgrade installation, complete the following steps:

1. STOP the Unix Agent communication in OpCon Enterprise Manager (make sure all running jobs complete first).
2. STOP the Unix Agent processes on the UNIX machine.
3. Create the agent installation directory. Use the following syntax:

```mkdir /usr/local/lsam<version>```

:::tip Example

The following example shows the syntax for creating an LSAM installation directory for LSAM version 4.01:

```mkdir /usr/local/lsam-4.01```

:::

4. Remove the symbolic link from the old agent installation directory (e.g., usr/local/lsam-3.06/) with the following syntax:

```rm <LSAM root directory>```

:::tip Example

The following example shows the syntax for an installation upgrade:

```rm /usr/local/lsam```

:::

5. Create a symbolic link from the new agent installation directory to the agent root directory with the following syntax:

```ln –s <LSAM installation directory> <LSAM root directory>```

:::tip Example

The following example shows the syntax for creating a symbolic link from the new LSAM installation directory to the LSAM root directory:

```ln -s /usr/local/lsam-4.01 /usr/local/lsam```

:::

The agent installation directory is updated and linked to the new version.

### Update the job scripts

Users may need to modify their job scripts. Scripts need to be modified if they rely on the environment variable $PATH to resolve the location of any agent utilities when calling them, if they rely on the SAM Socket number (or environment variable $SAM_SOCKET), or if they rely on a hard-coded location. The environment variable $SMA_BINDIR is defined for use within OpCon jobs and contains the path pointing to agent utilities. This path may vary across different instances of the agent. Update any calls to a utility which may exist in job scripts.

If run from a context other than a user job (e.g., a disk-monitoring utility that wishes to spawn an OpCon event) "```$SMA_BINDIR/```" must be replaced by whatever is appropriate.

:::tip Example

If a script issues a job-status message via the command:

```sma_status "Starting Phase 1"```

- or -

```/usr/local/lsam/sma_status "Starting Phase 1"```

They should change the command to read:

```$SMA_BINDIR/sma_startus "Starting Phase 1"```

:::

## Installing the LSAM

Whether performing a new install or an upgrade, the following procedure:

* Installs the LSAM with the default configuration.
* Allows review and revision of the LSAM's configuration.

### Install the UNIX LSAM

To install the UNIX LSAM, complete the following steps:

1. Go to the LSAM root directory with the following syntax:

:::tip Example 

The following example shows the command for navigating to the LSAM root directory:

```cd /usr/local/lsam```

:::

2. Retrieve the agent tar file from /tmp with the following syntax (note the '.' at the end is part of the command):

```mv /tmp/<LSAM tar file>```

:::tip Example

The following example shows the command for retrieving the 11_00.tar file from /tmp:

```mv /tmp/<version>.tar.```

:::

3. The following example shows the command for retrieving the 11_00.tar file from /tmp:

```mv /tmp/<version>.tar.```

:::tip Example

The following example shows the command for extracting the 11_00.tar file on an HP-UX machine:

```tar xvf <version>.tar.```

:::

4. Change the ownership of the files in the bin directory to root with the following syntax:

```chown 0 bin/*```

5. Change the group of the bin directory to root with the following syntax:

```chgrp 0 bin/*```

6. Configure the new agent by running the "install_lsam" script:

```./bin/install_lsam `pwd`<SAM_Socket> <LSAM_instance>```

* (Optional) ```<SAM_Socket> ```is a parameter that you can define to identify the TCP/IP socket number the LSAM instance will use. If multiple LSAMs will be installed on the same machine to the same parent directory, be sure to specify this parameter.

* (Optional) ```<LSAM_instance> ```is a parameter that you can define to identify the name of the LSAM instance. This setting is useful for defining distinctly different operating environments (e.g., Production versus Development environments). Do not specify this parameter if fail-over LSAMs will be installed.

:::info Note

 If planning to install fail-over LSAMs, SMA Technologies recommends specifying the same ```<LSAM root directory>``` and ```<SAM_socket>```, but omitting the ```<LSAM_instance>``` parameter from the install_lsam command on each machine involved in the fail-over configuration.

:::

:::info Note

Use the UNIX "pwd" command in back-quotes (`) as the ```<LSAM root directory>```.

:::

:::tip Example 

The following example shows the command for setting the SAM Socket Number to 3100 and the LSAM Instance identifier to "prod":

```bin/install_lsam `pwd` 3100 prod```

:::

:::info Note

The installation process generates and runs the ```lsam<SAM_Socket>``` script (e.g., lsam3100). The script searches for the tar and gzip compression utilities on the system. If the search is unsuccessful, the script prompts you for the utilities' location(s) or instructs you to edit the agent configuration file. If the search is successful, the scripts run the agent configuration program to set the SMAFT compression_support parameter and STDOUT/STDERR file capture (for use with the JORS).

:::

7. If installing on Linux, AIX, HP-UX, or Solaris, create the symbolic links to the start up directory so the agent will start automatically when the machine is rebooted. Use the following syntax:

```bin/ install_lsam_service `pwd` <SAM _Socket>```

:::tip Example

The following example shows the command for creating the symbolic links for startup of an LSAM using SAM Socket number 3100:

```bin/install_lsam_service `pwd` 3100```

:::

8. Start the agent Configuration program to verify the JORS and SMAFT parameters defined in step 6, and to modify any other values as may be necessary. For information on configuring the agent, refer to [Unix Agent Configuration](../configuration/unix-lsam-configuration). Use the following syntax:

```bin/lsam<SAM_Socket> config```

:::tip Example

The following example shows the command for starting the configuration program for the LSAM using SAM Socket number 3100:

```bin/lsam3100 config```

:::

* View and modify relevant configuration parameters.
* Enter ```s``` to save the file.
* Enter ```q``` to quit the configuration program.

The LSAM is installed and configured.

## Exception handling

**The install_lsam script prompts for the location of tar or gzip utilities** — The installation process searches for the tar and gzip compression utilities on the system. If the search is unsuccessful, the script cannot automatically determine the utility paths. — Supply the full path to each utility when prompted, or edit the agent configuration file to specify the correct locations as directed by the script.

**Ownership or permission errors after extracting the tar file** — The files in the bin directory may not be owned by root after extraction, which prevents the agent from performing user impersonation. — Run `chown 0 bin/*` to set ownership to root and `chgrp 0 bin/*` to set the group to root, as shown in steps 4 and 5 of the installation procedure.

**The agent fails to start and displays `error while loading shared libraries`** — The SSL or Crypto library version the agent was built against is not present in the system library path. — Run `ldconfig -p | grep libssl` to locate the installed SSL library version, then create a symbolic link from the expected version name to the installed version. Repeat the same steps using `libcrypto` in place of `libssl`. See [Installation Requirements](../installation/requirements) for the complete procedure.
