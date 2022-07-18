# Dispatcher Configuration Parameters

The following parameters reference the dispatcher setting for the LSAM's internal communication.

### msg_timeout_in_seconds

**Default Value**: 600

**Description**:

* Defines the timeout in seconds for the LSAM to wait for a message from SMANetCom.
* If the timeout is exceeded, the dispatcher closes and reopens the TCP/IP socket.