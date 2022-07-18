# Updating the SMA File Transfer (SMAFT) Control Script

The SMA File Transfer (SMAFT) Control Script contains several variables necessary for the proper operation of SMAFT jobs. Since the installation script "install_lsam" easily creates a new UNIX LSAM (and updates the SMAFT Control Script), further modification of the SMAFT Control Script is not necessary. If changes need to be made, proceed as directed below under "Editing the SMAFT Control Script".

:::info Note

If the SMAFT Control Script should ever be deleted, the execution of the LSAM Control Script creates a new one.

:::

## SMA File Transfer Control Script Variables

### LSAM_ROOT

**Default**: None

**Description**:

Must match definition for ```LSAM_ROOT``` in the LSAM Control Script.

### SAM_SOCKET

**Default**: None

**Description**:

Must match definition for ```SAM_SOCKET``` in LSAM Control Script.

### SMA_LSAM_INSTANCE

**Default**: None

**Description**:

Must match definition for ```SMA_LSAM_INSTANCE``` in LSAM Control Script.

### PATH

**Default**: None

**Description**: 

* Includes the path to the LSAM bin directory, and to the 'tar' and 'gzip' compression utilities if installed on the system.
* Should match the definition for ```PATH``` in LSAM Control Script.
* Do not modify this file if only modifying the PATH variable. Modify the LSAM Control Script instead. For information on editing the LSAM Control Script, refer to [Updating the LSAM Control Script](updating-lsam-control-script).


## Editing the SMAFT Control Script

With an ASCII editor, modify the SMAFT Control Script to set the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, and ```PATH``` variables to the preferred values.

:::info Note

Modifying the SMAFT Control Script is optional. The installation procedures have set default values.

:::

:::tip Example

The following example shows an excerpt from the SMAFT Control Script defining values for the ```LSAM_ROOT```, ```SAM_SOCKET```, ```SMA_LSAM_INSTANCE```, and ```PATH variables```.

*\*The wrapping of the text in this example does not indicate the location of a carriage return; the ↵ indicates the location of a carriage return.*

```
LSAM_ROOT=/usr/local/lsam; export LSAM_ROOT ↵
SAM_SOCKET=3100; export SAM_SOCKET ↵
SMA_LSAM_INSTANCE=prod; export SMA_LSAM_INSTANCE ↵
PATH=/usr/bin:/usr/sbin:/sbin:/usr/local/lsam/bin:/usr/bin:/usr/contrib/bin; export PATH ↵
```

:::