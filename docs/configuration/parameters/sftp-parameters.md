# SFTP Parameters

The following parameters reference the SFTP setting for the UNIX LSAM.

### sftp_port

**Default Value**: 0

**Description**: 
	
* Enables (non-zero value)/Disables (0 value) the use of SFTP for file transfer.
* Standard SFTP uses port 22.

:::info Note 

This value must match the configured SSH port being used.

:::

* The SFTP component of SSH must be configured and enabled.
* When set, the LSAM attempts first to use SFTP for file transfer.
* If using SFTP for file transfer should fail, the LSAM will fallback to using SMAFT.
