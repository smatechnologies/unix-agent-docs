# TCP/IP Configuration Parameters

## Configuration Parameters

The following parameters reference the TCP/IP settings for communication between the LSAM and SMANetCom.


### allowed_sam_ip_address_1

**Default Value**: Any

**Description**:

* Determines if communication from SMANetCom to the LSAM is restricted to one or more TCP/IP addresses.
* If ANY is specified, the LSAM accepts communication from any SMANetCom.
* If a specific TCP/IP address is defined (e.g., 126.40.90.231), the LSAM only accepts SMANetCom communication from the specified address.
* The LSAM refuses a connection if communication is attempted from another address.
* This definition enhances communication security.
* If multiple SAMs are on a network, this address ensures the LSAM is only accepting messages from the intended SMANetCom.

### allowed_sam_ip_address_2

**Default Value**: unused

**Description**:

Same as address_1 explanation.

### allowed_sam_ip_address_3

**Default Value**: unused

**Description**:

Same as address_1 explanation.

### allowed_sam_ip_address_4

**Default Value**: unused

**Description**:

Same as address_1 explanation.

### allowed_sam_ip_address_5

**Default Value**: unused

**Description**:

Same as address_1 explanation.

### bound_NIC_adapter_ip

**Default Value**: default

**Description**:

* Defines the desired TCP/IP address to bind to.
* This must be a valid TCP/IP address for this machine.

### use_TLS_SAM

**Default Value**: 0

**Description**:

* Determines if communication from SMANetCom to the LSAM is using TLS.
* When enabling TLS, ensure that the JORS and SMAFT ports are not configured to use the same port number in the lsam.config file.
* If set to zero, TLS is disabled.
* If set to non-zero, TLS is enabled.


### lsam_pem_file

**Default Value**: none

**Description**:

Defines the absolute path of the public certificate file.

### lsam_private_key_file

**Default Value**: none

**Description**:

Defines the absolute path of the private key file (the path may be the same as the public certificate file).

### netcom_pem_file

**Default Value**: none

**Description**:

Reserved for future use.