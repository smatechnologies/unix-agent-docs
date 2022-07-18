# STDERR - Processing Errors

:::info Note

 Occurrence of an error doesn't necessarily (but usually does) mean that a job is aborted. If the job does complete successfully, it may indicate some marginal operating conditions in need of attention.

:::

### Source File [file] does not exist	
**Origination**: FTServer

The Source File does not exist.

### Source File [file] is empty	

**Origination**: FTServer

The Source File contains no data (i.e., its length is zero).

### Could not open Temp File [file] (indicator)
### Could not open FT Directory lock [file] (indicator)

**Origination**: FTServer or FTAgent

* The indicated file could not be opened for processing.
* The indicator field provides the specific reason.

### Could not open OLD Destination File [file] (indicator) 
### Could not open APPEND-TO Destination File [file] (indicator)

**Origination**: FTAgent

* The indicated file could not be opened for processing.
* The indicator field provides the specific reason.

### Could not create FT Directory [directory] (indicator) 
### Could not create Temp Directory [directory] (indicator) 
### Could not create /tmp [directory] (indicator)

**Origination**: FTServer or FTAgent

* The indicated directory could not be created for processing.
* The indicator field provides the specific reason.

### Could not fseek Temp File [file] (indicator) 
### Could not fseek FT Directory [directory] (indicator)

**Origination**: FTServer or FTAgent

The indicated object could not be positioned for processing.
The indicator field provides the specific reason.

### Could not rename Temp. FT Directory [from] to [to] (indicator)	

**Origination**: FTServer or FTAgent

* The indicated directory could not be renamed for processing.
* The indicator field provides the specific reason.

### Could not rename Source File [from] to [to] (indicator)	

**Origination**: FTServer

* The indicated file could not be renamed for processing.
* The indicator field provides the specific reason.

### Could not rename [from] to [to] (indicator) 
### Could not rename unTAR'd [un-TAR] to Temp [temp] (indicator)

**Origination**: FTAgent

* The indicated file could not be renamed for processing.
* The indicator field provides the specific reason.

### Could not get size of Temp File [file] (indicator)	

**Origination**: FTServer

* The size of the indicated file could not be determined.
* The indicator field provides the specific reason.

### Could not get size of Partial File [file] (indicator) 
### Could not get size of APPEND-TO Destination File [file] (indicator)

**Origination**: FTAgent

* The size of the indicated file could not be determined.
* The indicator field provides the specific reason.

### Could not get file info for Source File [file] (indicator)

**Origination**: FTServer

* The statistics (e.g., size, date, etc.) for the Source File could not be obtained.
* The indicator field provides the specific reason.

### Tag [tag] is not specified

**Origination**: FTServer or FTAgent

The indicated XML tag was missing.

### End tag [tag] is not specified	

**Origination**: FTServer or FTAgent

The associated ending tag for the indicated XML tag was missing.

### Value for Tag [tag] is not specified

**Origination**: FTServer or FTAgent

No value was supplied for the indicated XML tag.

### Could not fork() for [operation] (indicator)

**Origination**: FTServer or FTAgent

* The indicated operation could not be performed due to inability to execute a fork() call.
* The indicator field provides the specific reason.

### Could not wait() for [operation] (indicator)

**Origination**: FTServer or FTAgent

* The indicated operation could not be performed due to inability to execute a wait() call.
* The indicator field provides the specific reason.

### Processing error in [operation] (indicator)

**Origination**: FTServer or FTAgent

The indicated operation could not be performed due to the reason pointed to by the indicator field.

### Max attempts at sending message exceeded

**Origination**: FTServer or FTAgent

The maximum number of attempts to send a message was reached.

### Max Wait Time to receive message has elapsed

**Origination**: FTServer or FTAgent

The maximum time allowed for reception of a message was reached.

### Receive was not successful (indicator)

**Origination**: FTServer or FTAgent

* Reception of a message failed.
* The indicator field provides the specific reason.

### Send unsuccessful (indicator)

**Origination**: FTServer or FTAgent

* A message could not be sent.
* The indicator field provides the specific reason.

### Could not set buffer size  
### Could not set buffer size for sending

**Origination**: FTServer or FTAgent

The communications channel could not be initialized.

### Send failed for ACK	

**Origination**: FTServer or FTAgent

An attempt to ACK (i.e., acknowledge) a message failed.

### Mis-match between received & expected CRC	

**Origination**: FTServer or FTAgent

The received message was incomprehensible.

### Received invalid message

**Origination**: FTServer or FTAgent

The received message was not expected.

### RCV Queue full	

**Origination**: FTServer or FTAgent

The queue is full because a processing error occurred.

### Error in FT Directory format	

**Origination**: FTServer or FTAgent

The file which maps Source and Destination files to temporary files for processing is corrupted.

### Could not lock FT Directory [directory] (indicator)	

**Origination**: FTServer or FTAgent

* The file which maps Source and Destination files to temporary files for processing could not be locked for exclusive use.
* The indicator field provides the specific reason.

### Incorrect number of parameters	

**Origination**: FTAgent

FTAgent received the wrong number of startup parameters from the LSAM.

### Unknown host name [computer]	

**Origination**: FTAgent

FTAgent was unable to locate the indicated computer on the network while trying to connect to the FTServer.

### Error connecting to [computer] (indicator)	

**Origination**: FTAgent

* FTAgent was unable to connect to the FTServer located on the indicated computer.
* The indicator field provides the specific reason.

### Could not get host name (indicator)	

**Origination**: FTAgent

* FTAgent was unable to retrieve its own host name to send to FTServer.
* The indicator field provides the specific reason.

### FTServer process prematurely terminated	

**Origination**: FTAgent

FTAgent has lost communications with FTServer.

### Could not set GID to [groupID] to check file access
### Could not set UID to [userID] to check file access

**Origination**: FTServer

FTServer could not set the GID/UID as indicated to determine if the user has access to the Source File.

### Error reading Temp File [file]
### Error writing Temp File [file]	

**Origination**: FTServer or FTAgent

The temporary file could not be read/written.

### Error writing file data (Indicator)	

**Origination**: FTAgent

* FTAgent could not save data as packets arrived from FTServer.
* The indicator field provides the specific reason.

### Could not move Temp File [temp] to Destination File [dest] (indicator)	

**Origination**: FTAgent

* FTAgent could not make a temporary file into a permanent Destination File.
* The indicator field provides the specific reason.

### Unable to get environment variable [SMA_JOBNAME]
### Unable to send message (indicator)

**Origination**: FTAgent

* FTAgent could not send job status information to the SAM.
* The indicator field provides the specific reason.

### Could not process zero-length Source File [machine]file	

**Origination**: FTAgent

FTAgent could not create a zero-length destination file to match the zero-length source file, or could not update the timestamp of the destination file when "append" was specified.

### Invalid length of file for FIXED-length records	

**Origination**: FTAgent

The length of the received file was not as expected, when the user specified that the file be saved in a record-oriented format (by pre-pending a '=' to the destination file name).

### Invalid RECORD-LENGTH indicator	

**Origination**: FTAgent

The data format from the FTServer was not as expected, when the user specified that the file be saved in a record-oriented format (by pre-pending a '=' to the destination file name).

### Missing/Invalid ```<RecordFormat>``` in XML-header	

**Origination**: FTAgent

The data format from the FTServer was not as expected, when the user specified that the file be saved in a record-oriented format (by pre-pending a '=' to the destination file name).

### Invalid ```<RecordSep> [RS]``` in XML-header	

**Origination**: FTAgent

The data format from the FTServer was not as expected, when the user specified that the file be saved in a record-oriented format (by pre-pending a '=' to the destination file name). RS indicates the erroneous data.

### XFER RECORDS and bad/missing Index File [%s]	

**Origination**: FTServer

The user specified that the file be sent in a record-oriented format (by pre-pending a '=' to the source file name), and the associated index file (which contains the record structure) could not be found or was corrupted. The most likely cause for a missing index file is either that the source file was not previously saved by the FTAgent as a record-oriented destination file, or that the index file was accidentally deleted. A native, stream format, file cannot be sent as a record-oriented file unless it is first transferred to itself/another file/another UNIX system as a record-oriented destination file.