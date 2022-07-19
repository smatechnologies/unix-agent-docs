# Updating the LSAM Control Script

The LSAM Control Script contains several variables necessary for the proper processing of LSAM commands and of LSAM components. Since the installation script "install_lsam" easily creates a new UNIX LSAM (and updates the LSAM Control Script), further modification of the LSAM Control Script is not necessary. For information on the install_lsam script, refer to [install_lsam](/operations/utilities/install-lsam). SMA Technologies recommends confirming that the following variables are set to the correct values for the environment after executing install_lsam. If changes need to be made, proceed as directed below under "Editing the LSAM Control Script."

## LSAM Control Script Variables

### LSAM_ROOT

**Default**: /usr/local/lsam

**Description**:

The location of the symbolic link to the LSAM's installation directory.

### SAM_SOCKET

**Default**: 3100

**Description**:

* The LSAM communicates with SMANetCom through this socket number.
* The Machine definition in the Enterprise Manager must contain this socket number.

### SMA_LSAM_INSTANCE

**Default**: ```$SAM_SOCKET```

**Description**:

Allows for descriptive pathnames which are not tied to a specific SAM Socket number. ```$SAM_SOCKET``` can be changed without having to copy and move LSAM configuration and job tracking files.

### SMA_LOG_DIRECTORY

**Default**: ```$LSAM_ROOT/log/$SMA_LSAM_INSTANCE```

**Description**:

The LSAM writes its log files and error files to this path.

### PATH

**Description**:

* Includes the path to the LSAM "bin" directory.
* Includes the path(s) to the 'tar' and 'gzip' compression utilities if installed on the system.

## Editing the LSAM Control Script

:::info Note

Modifying the LSAM Control Script is optional. The installation procedures have set default values.

:::

With an ASCII editor, modify the LSAM Control Script to set the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, ```SMA_LOG_DIRECTORY```, and ```PATH``` variables to the preferred values.

:::tip Example

The following example shows an excerpt from the LSAM Control Script defining values for the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, ```SMA_LOG_DIRECTORY```, and ```PATH``` variables.


*\*The wrapping of the text in this example does not indicate the location of a carriage return; the ↵ indicates the location of a carriage return.*


```
LSAM_ROOT=/usr/local/lsam; export LSAM_ROOT ↵

SAM_SOCKET=3100; export SAM_SOCKET ↵

SMA_LSAM_INSTANCE=prod; export SMA_LSAM_INSTANCE ↵

SMA_LOG_DIRECTORY=$LSAM_ROOT/log/$SMA_LSAM_INSTANCE; export SMA_LOG_DIRECTORY ↵

PATH=/usr/bin:/usr/sbin:/sbin:/usr/local/lsam/bin:/usr/bin:/usr/contrib/bin; export

PATH ↵
```

:::

### Add/Remove Path to Compression Utilities

If you add or remove the path to the 'tar' or 'gzip' utilities from the PATH variable, you'll need to further modify the control script.

1. Scroll under the line "These 0 – 2 lines for creation of FTAgent script...".
2. For the tar utility:
    * If adding the tar utility path, add a line "#got_tar".
    * If removing the tar utility path, delete the line "#got_tar".
3. For the gzip utility:
    * If adding the gzip utility path, add a line "#got_gzip".
    * If removing the gzip utility path, delete the line "#got_gzip".
4. If the SMA File Transfer (SMAFT) Control Script has not been manually updated, delete it.

    ```rm SMAFTScript<SAM_Socket>```

    * Issue an LSAM 'status' command (refer to [lsam status](/operations/unix-lsam-commands#lsam-status)) to automatically update the PATH statement in the SMAFT Control Script.

    ```lsam<SAM_Socket> status```

    \- or -

    * Manually edit the ```PATH``` definition within the SMA File Transfer Control Script to match the new settings.


:::tip Example

The following example shows the bottom of an LSAM Control Script if the ```PATH``` variable contained the path to 'tar' but not the path to 'gzip':

```
#################-#-#-#-###################
These 0-2 lines for creation of FTAgent script...
#got_tar
#################-#-#-#-###################
```

:::