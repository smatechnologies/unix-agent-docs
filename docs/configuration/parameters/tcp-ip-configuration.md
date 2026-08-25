---
sidebar_label: 'TCP/IP Configuration Parameters'
title: TCP/IP Configuration Parameters
description: "Reference for Unix Agent TCP/IP configuration parameters, including allowed SMANetCom IP addresses, NIC binding, and TLS certificate settings."
tags:
  - Reference
  - System Administrator
  - Agents
---

# TCP/IP configuration parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for Unix Agent TCP/IP configuration parameters, including allowed SMANetCom IP addresses, NIC binding, and TLS certificate settings.

- When restricting which SMANetCom IP addresses are allowed to connect to the agent
- When binding the agent to a specific network interface card (NIC)
- When enabling or configuring TLS encryption for agent communication

## Configuration parameters

The following parameters reference the TCP/IP settings for communication between the agent and SMANetCom. These settings control allowed SMANetCom IP addresses, NIC binding, and TLS certificate configuration.


### allowed_sam_ip_address_1

**Default Value**: Any

**Description**:

* Determines if communication from SMANetCom to the agent is restricted to one or more TCP/IP addresses.
* If `any` is specified, the agent accepts communication from any SMANetCom.
* If a specific TCP/IP address is defined (e.g., 126.40.90.231), the agent only accepts SMANetCom communication from the specified address.
* The agent refuses a connection if communication is attempted from another address.
* This definition enhances communication security.
* If multiple SAMs are on a network, this address ensures the agent is only accepting messages from the intended SMANetCom.

### allowed_sam_ip_address_2

**Default Value**: unused

**Description**:

* Specifies a second IP address from which SMANetCom communication is permitted.
* When set to a specific TCP/IP address, the agent accepts connections from that address in addition to those permitted by `allowed_sam_ip_address_1`.
* Leave unused if only one SMANetCom address requires whitelisting.

### allowed_sam_ip_address_3

**Default Value**: unused

**Description**:

* Specifies a third IP address from which SMANetCom communication is permitted.
* When set to a specific TCP/IP address, the agent accepts connections from that address in addition to those permitted by `allowed_sam_ip_address_1` and `allowed_sam_ip_address_2`.
* Leave unused if fewer than three SMANetCom addresses require whitelisting.

### allowed_sam_ip_address_4

**Default Value**: unused

**Description**:

* Specifies a fourth IP address from which SMANetCom communication is permitted.
* When set to a specific TCP/IP address, the agent accepts connections from that address in addition to those already permitted.
* Leave unused if fewer than four SMANetCom addresses require whitelisting.

### allowed_sam_ip_address_5

**Default Value**: unused

**Description**:

* Specifies a fifth IP address from which SMANetCom communication is permitted.
* When set to a specific TCP/IP address, the agent accepts connections from that address in addition to those already permitted.
* Leave unused if fewer than five SMANetCom addresses require whitelisting.
* The agent supports a maximum of five whitelisted SMANetCom IP addresses (`allowed_sam_ip_address_1` through `allowed_sam_ip_address_5`).

### bound_NIC_adapter_ip

**Default Value**: default

**Description**:

* Defines the desired TCP/IP address to bind to.
* This must be a valid TCP/IP address for this machine.

### use_TLS_SAM

**Default Value**: 0

**Description**:

* Determines if communication from SMANetCom to the agent is using TLS.
* When enabling TLS, ensure that the JORS and SMAFT ports are not configured to use the same port number in the lsam.conf file.
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

### restrict_SAM_port_single_connection

**Default Value**: 0

**Description**:

* Rejects a new connection attempt from SMANetCom when a connection on the SAM port is already active.
* If set to zero, multiple connection attempts on the SAM port are allowed.
* If set to one, only one connection at a time is accepted on the SAM port; subsequent attempts are rejected until the current connection closes.

:::info Note

Added in agent version 26.0.0 (OCAG-7).

:::

### apply_sam_ip_whitelist_to_all_ports

**Default Value**: 0

**Description**:

* Extends the `allowed_sam_ip_address_*` whitelist enforcement to all agent ports, not only the base SAM port.
* If set to zero, whitelist filtering applies only to the base SAM communication port.
* If set to one, whitelist filtering applies to all ports the agent listens on.

:::info Note

Added in agent version 26.0.0 (OCAG-16).

:::

### bind_localhost_DISP

**Default Value**: 0

**Description**:

* Binds the dispatcher (DISP) socket to the localhost interface only.
* If set to zero, the socket binds to the address specified by `bound_NIC_adapter_ip` or the default interface.
* If set to one, the socket binds to `127.0.0.1` (localhost), restricting connections to the local machine.

### bind_localhost_LSAM

**Default Value**: 0

**Description**:

* Binds the LSAM job-submission socket to the localhost interface only.
* If set to zero, the socket uses the default or `bound_NIC_adapter_ip` address.
* If set to one, the socket binds to `127.0.0.1`.

### bind_localhost_JOB_STATUS

**Default Value**: 0

**Description**:

* Binds the job status reporting socket to the localhost interface only.
* If set to zero, the socket uses the default or `bound_NIC_adapter_ip` address.
* If set to one, the socket binds to `127.0.0.1`.

### bind_localhost_ALT_JOB_STATUS

**Default Value**: 1

**Description**:

* Binds the alternate job status socket to the localhost interface only.
* If set to zero, the socket uses the default or `bound_NIC_adapter_ip` address.
* If set to one (the default), the socket binds to `127.0.0.1`.

### bind_localhost_LOGGING

**Default Value**: 0

**Description**:

* Binds the logging socket to the localhost interface only.
* If set to zero, the socket uses the default or `bound_NIC_adapter_ip` address.
* If set to one, the socket binds to `127.0.0.1`.

### bind_localhost_JOB_LOGGING

**Default Value**: 0

**Description**:

* Binds the job logging socket to the localhost interface only.
* If set to zero, the socket uses the default or `bound_NIC_adapter_ip` address.
* If set to one, the socket binds to `127.0.0.1`.

:::info Note

The `bind_localhost_*` per-socket localhost binding flags were added in agent version 26.0.0 (OCAG-767). Each flag independently controls whether that socket is restricted to localhost.

:::