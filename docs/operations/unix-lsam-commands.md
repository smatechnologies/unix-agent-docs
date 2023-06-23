# UNIX LSAM Commands

The LSAM Control Script ```<LSAM root path>/bin/lsam<SAM_Socket Number>``` accepts many parameters to support the various LSAM commands. The parameters below reference a list of all supported LSAM commands and descriptions.

## Commands and Short Descriptions


| LSAM Command | Short Description |
| ------------ | ----------------- |
| ```lsam<SAM_Socket> command '<Event String>'``` | Send an OpCon event back to the SAM through the sma_disp process |
| ```lsam<SAM_Socket> config``` | Modify the LSAM configuration file |
| ```lsam<SAM_Socket> config_check``` | Verify the integrity of the LSAM's configuration file |
| ```lsam<SAM_Socket> create_cert [certificate validity date]``` | Create a self-signed certificate for the date specified |
| ```lsam<SAM_Socket> delete_logs``` | Delete all but the current log files and error files |
| ```lsam<SAM_Socket> dumptracking``` | Display the contents of LSAM's tracking file on the console |
| ```lsam<SAM_Socket> kill_jobs``` | Terminate any running jobs |
| ```lsam<SAM_Socket> log_break``` | Insert a date/time-stamped divider into the LSAM's current log file and error file |
| ```lsam<SAM_Socket> refresh``` | Cause the LSAM to reread the configuration file |
| ```lsam<SAM_Socket> restart [newlog]``` | Stops and then starts the LSAM - Specifying the newlog parameter causes the LSAM to archive and save the current logfile and errfile and create a new logfile and errfile |
| ```lsam<SAM_Socket> show_cert certificate_file``` | Displays the certificate in a user-friendly format |
| ```lsam<SAM_Socket> SMASUP``` | Gather troubleshooting information into a compressed file |
| ```lsam<SAM_Socket> start [newlog]``` | Start the LSAM. Specifying the newlog parameter causes the LSAM to archive and save the current logfile and errfile and create a new logfile and errfile |
| ```lsam<SAM_Socket> start_fad``` | Start the lsam_fad process(es) |
| ```lsam<SAM_Socket> status``` | Check if the LSAM's primary processes are running |
| ```lsam<SAM_Socket> stop``` | Stop the LSAM |
| ```lsam<SAM_Socket> stop_fad``` | Stop the lsam_fad process(es) |
| ```lsam<SAM_Socket> version``` | Display the version of the LSAM |


### lsam command

The lsam command sends an OpCon event back to the SAM through the sma_disp process. Execute this command from the command line or from within a script. For a list of valid OpCon Events, refer to Introduction in the OpCon Events online help.

When entering the event, either do not include the dollar sign (```$```) at the beginning of the event, or enclose the event in single quotes as shown below in the syntax. Although a dollar sign is required for OpCon events, the UNIX shell tries to process a dollar sign as a variable if it is not quoted. The sma_command program automatically inserts the dollar sign when it receives the event string. Additionally, if OpCon tokens are in an un-quoted event, escape (```\```) the dollar sign as shown in the example below.

#### Syntax

```lsam<SAM_Socket> command '<event string>,<User Login ID>,<Events Password>'```

:::tip Example

The following example shows an excerpt from a sample script attempting to release a job called Ujob2 on schedule UNIXSched for the current date.

The wrapping of the text in this example does not indicate the location of a carriage return; the ↵ indicates the location of a carriage return.

```
lsam3100 command

JOB:RELEASE,[[\$DATE]],UnixSched,Ujob2,batchuser,batchpasswd ↵
```

:::

### lsam config

The config command starts an interactive LSAM configuration program. Use file path: ```<LSAM root path>/config/<SMA_LSAM_INSTANCE>/lsam.conf```. For information on LSAM Configuration, refer to UNIX LSAM Configuration.

#### Syntax

```lsam<SAM_Socket> config```

### lsam config_check

The config_check command verifies the integrity of the LSAM configuration file. SMA Technologies recommends executing this command if the LSAM configuration file is manually modified.

If errors exist in the configuration file, the command prints the erroneous line to the screen.
If errors do not exist in the configuration file, the command outputs text indicating the command completed successfully.
Syntax
```lsam<SAM_Socket> config_check [-p]```

```-p```: An optional argument to print all lines of the configuration file to the screen.

### lsam create_cert

The create_cert command creates a self-signed certificate valid for the certificate validity date specified, or the default 365 days when left blank. It also creates a ```PKCS#12``` format file for exporting to the Windows OpCon server.

#### Syntax

```lsam<SAM_Socket> create_cert [certificate validity date (default=365, max=3650)]```


:::tip Example

```
lsam5000 create_cert 3650

Generating self-signed certificate redhat5as.pem valid for 3650 days

Generating a 2048 bit RSA private key

..........................................................+++

...+++

writing new private key to 'redhat5as.pem'

___________________________________________________________________________

You are about to be asked to enter information that will be incorporated

into your certificate request.

What you are about to enter is what is called a Distinguished Name or a DN.

There are quite a few fields but you can leave some blank

For some fields there will be a default value,

If you enter '.', the field will be left blank.

___________________________________________________________________________

Country Name (2 letter code) [GB]:US

State or Province Name (full name) [Berkshire]:TX

Locality Name (eg, city) [Newbury]:Kingwood

Organization Name (eg, company) [My Company Ltd]:SMA Technologies

Organizational Unit Name (eg, section) []:Engineering

Common Name (eg, your name or your server's hostname) []:*.smausa.com

Email Address []:support@smatechnologies.com

redhat5as.pem successfully created.

 

Exporting redhat5as.pem to Windows format PKCS#12 file redhat5as.pfx

Enter Export Password:

Verifying - Enter Export Password:

redhat5as.pfx successfully created.
```

:::

### lsam _delete_logs

The delete_logs command removes all but the current log file and error files. For the LSAM to automatically maintain its logs, create a script containing the delete_logs command, and create and schedule the maintenance job through OpCon.

#### Syntax

```lsam<SAM_Socket> delete_logs```

### lsam dumptracking

The dumptracking command reads the LSAM's job tracking directory and displays the contents on the console of each job tracking file found. No data is lost by running this command.

#### Syntax

```lsam<SAM_Socket> dumptracking```

### lsam kill_jobs

The kill_jobs command terminates any running jobs. This command may be used when the LSAM is active or inactive; however, logging of a job killed occurs only when LSAM is active. Once SAM receives the job status update from the LSAM, the Enterprise Manager displays the status "Failed: Killed by Sys Admin" for all killed jobs. If the LSAM is inactive when the job is killed, the job's status is updated when an LSAM is restarted.

#### Syntax

```lsam<SAM_Socket> kill_jobs```

### lsam log_break

The log_break command writes a line of asterisks (*) in the log file to delimit entries in the log file.

#### Syntax

```lsam<SAM_Socket> log_break```

### lsam refresh

The refresh command causes the LSAM to reread the configuration file following modification. To modify the configuration, run the LSAM Configuration program. For information on LSAM configuration, refer to [UNIX LSAM Configuration](../configuration/unix-lsam-configuration). After saving the changes to the LSAM configuration file, execute the refresh command for the LSAM to recognize the changes.

:::info Note

This command only refreshes the LSAM processes "sma_lsam" and "sma_JORS", and the SMAFT Agent. If configuration changes affect other LSAM processes (e.g., "sma_fad"), restart the LSAM.

:::

#### Syntax

```lsam<SAM_Socket> refresh```

### lsam restart

The restart command systematically stops all of the LSAM processes, then executes the sma_log, sma_lsam, sma_disp, sma_cronmon, sma_filein, and sma_JORS processes to bring the LSAM to a fully operational status.

#### Syntax

```lsam<SAM_Socket> restart```

### lsam show_cert certificate_file

The show_cert command can be used to display the certificate in a user-friendly format.

#### Syntax

```lsam<SAM_Socket> show_cert certificate_file```

:::tip Example

```
lsam5000 show_cert /usr/jsmith/main/redhat5as.pem

Certificate:

Data:

Version: 3 (0x2)

Serial Number:

e5:c1:38:13:65:4e:8f:47

Signature Algorithm: sha256WithRSAEncryption

Issuer: C=US, ST=TX, L=Kingwood, O=SMA Technologies, OU=Engineering, CN=*.smausa.com/emailAddress=support@smatechnologies.com

Validity

Not Before: Oct 14 20:18:11 2016 GMT

Not After : Oct 12 20:18:11 2026 GMT

Subject: C=US, ST=TX, L=Kingwood, O=SMA Technologies, OU=Engineering, CN=*.smausa.com/emailAddress=support@smatechnologies.com

Subject Public Key Info:

Public Key Algorithm: rsaEncryption

RSA Public Key: (2048 bit)

Modulus (2048 bit):

00:ea:59:7e:b5:3b:7e:b2:a3:f9:ce:ef:79:f3:38:

a4:a0:4a:31:e0:ff:84:97:1d:cd:27:33:79:47:63:

92:92:74:48:d3:71:0e:1c:8e:e0:0c:48:7b:fd:3b:

af:cb:e0:fa:ae:b6:3a:21:bb:cb:b0:5c:1b:7e:e2:

72:0d:86:be:48:aa:4d:a5:02:28:b3:e0:3f:d9:a8:

46:7e:ca:29:ba:4c:9e:60:45:13:0e:d9:04:6b:42:

4a:c1:ff:62:4d:b8:e9:5c:72:18:2c:b0:67:52:d0:

c7:6b:3a:d6:b2:6e:2e:b0:33:77:d5:30:a2:a5:1e:

21:42:2d:31:b8:04:37:bb:b9:aa:70:3e:44:d0:39:

50:13:67:02:82:de:64:d3:bb:69:bd:4f:05:4f:ab:

1a:81:3c:cf:b7:0f:5d:9c:e3:66:6f:d1:80:ed:96:

21:70:cb:1d:5b:40:b9:d9:fe:f8:cf:5f:6e:3d:52:

fb:61:f5:f4:e7:52:81:fe:08:ec:72:1e:64:6d:34:

7b:c6:c3:f6:e8:40:a9:8d:a4:76:fc:f3:5c:11:38:

75:17:62:9f:70:46:fc:6d:dc:d9:6e:70:da:d2:35:

93:cf:61:37:bf:fe:b2:a2:e1:78:6a:ee:8b:31:51:

9f:ac:c9:d1:35:e1:9c:a8:c2:36:42:ff:1d:8c:5b:

93:ed

Exponent: 65537 (0x10001)

X509v3 extensions:

X509v3 Subject Key Identifier:

27:D7:19:77:05:CA:F8:60:32:B9:24:A9:69:32:F9:2E:E8:AB:A6:AD

X509v3 Authority Key Identifier:

keyid:27:D7:19:77:05:CA:F8:60:32:B9:24:A9:69:32:F9:2E:E8:AB:A6:AD

DirName:/C=US/ST=TX/L=Kingwood/O=SMA Technologies/OU=Engineering/CN=*.smausa.com/emailAddress=support@smatechnologies.com

serial:E5:C1:38:13:65:4E:8F:47

 

X509v3 Basic Constraints:

CA:TRUE

Signature Algorithm: sha256WithRSAEncryption

07:f7:7a:eb:69:89:48:5f:26:4a:03:de:57:17:be:3a:b1:b0:

27:d0:3e:2c:7b:74:1e:c3:cb:e4:d4:32:13:f6:84:35:9a:24:

8a:46:64:16:06:c4:17:7b:bf:64:1d:22:3c:d1:27:92:68:eb:

10:4f:a6:b5:33:27:cc:f0:a9:9c:a0:01:78:30:e9:c7:7d:04:

bb:b3:3e:e8:89:83:7e:23:10:1f:69:df:81:ab:63:ae:a6:42:

b8:12:ca:72:e6:68:e5:39:09:f5:78:dc:36:55:b2:b5:e1:60:

ed:65:5c:e6:91:6f:c4:5d:88:51:8c:7d:2c:83:d8:14:f1:94:

01:da:b6:97:5c:02:d3:65:74:70:91:95:ab:ec:3e:4a:d8:33:

b9:a2:2b:ed:9c:ce:af:dd:59:18:f9:4a:98:7e:25:cb:5a:1a:

b1:70:5e:c4:8d:4d:80:f4:21:9b:6a:76:c7:e0:5b:8c:f2:d1:

6d:11:d2:94:e0:de:eb:ce:52:aa:d6:02:4f:2d:29:c4:b8:7e:

ab:8c:a8:ec:38:82:80:22:4d:99:1d:22:f9:7c:ad:6d:51:fe:

a5:ac:8a:9d:32:af:13:5d:83:a9:b9:b7:62:de:a2:1a:4d:d0:

68:93:30:62:87:4b:99:67:41:a7:51:b4:34:f9:50:07:c1:d2:

2c:a0:02:73

----BEGIN CERTIFICATE----

MIIEnjCCA4agAwIBAgIJAOXBOBNlTo9HMA0GCSqGSIb3DQEBCwUAMIGQMQswCQYD

VQQGEwJVUzELMAkGA1UECBMCVFgxETAPBgNVBAcTCEtpbmd3b29kMQwwCgYDVQQK

EwNTTUExFDASBgNVBAsTC0VuZ2luZWVyaW5nMRUwEwYDVQQDDAwqLnNtYXVzYS5j

b20xJjAkBgkqhkiG9w0BCQEWF3N1cHBvcnRAc21hc29sdXRpb25zLml0MB4XDTE2

MTAxNDIwMTgxMVoXDTI2MTAxMjIwMTgxMVowgZAxCzAJBgNVBAYTAlVTMQswCQYD

VQQIEwJUWDERMA8GA1UEBxMIS2luZ3dvb2QxDDAKBgNVBAoTA1NNQTEUMBIGA1UE

CxMLRW5naW5lZXJpbmcxFTATBgNVBAMMDCouc21hdXNhLmNvbTEmMCQGCSqGSIb3

DQEJARYXc3VwcG9ydEBzbWFzb2x1dGlvbnMuaXQwggEiMA0GCSqGSIb3DQEBAQUA

A4IBDwAwggEKAoIBAQDqWX61O36yo/nO73nzOKSgSjHg/4SXHc0nM3lHY5KSdEjT

cQ4cjuAMSHv9O6/L4Pqutjohu8uwXBt+4nINhr5Iqk2lAiiz4D/ZqEZ+yim6TJ5g

RRMO2QRrQkrB/2JNuOlcchgssGdS0MdrOtaybi6wM3fVMKKlHiFCLTG4BDe7uapw

PkTQOVATZwKC3mTTu2m9TwVPqxqBPM+3D12c42Zv0YDtliFwyx1bQLnZ/vjPX249

Uvth9fTnUoH+COxyHmRtNHvGw/boQKmNpHb881wROHUXYp9wRvxt3NlucNrSNZPP

YTe//rKi4Xhq7osxUZ+sydE14ZyowjZC/x2MW5PtAgMBAAGjgfgwgfUwHQYDVR0O

BBYEFCfXGXcFyvhgMrkkqWky+S7oq6atMIHFBgNVHSMEgb0wgbqAFCfXGXcFyvhg

MrkkqWky+S7oq6atoYGWpIGTMIGQMQswCQYDVQQGEwJVUzELMAkGA1UECBMCVFgx

ETAPBgNVBAcTCEtpbmd3b29kMQwwCgYDVQQKEwNTTUExFDASBgNVBAsTC0VuZ2lu

ZWVyaW5nMRUwEwYDVQQDDAwqLnNtYXVzYS5jb20xJjAkBgkqhkiG9w0BCQEWF3N1

cHBvcnRAc21hc29sdXRpb25zLml0ggkA5cE4E2VOj0cwDAYDVR0TBAUwAwEB/zAN

BgkqhkiG9w0BAQsFAAOCAQEAB/d662mJSF8mSgPeVxe+OrGwJ9A+LHt0HsPL5NQy

E/aENZokikZkFgbEF3u/ZB0iPNEnkmjrEE+mtTMnzPCpnKABeDDpx30Eu7M+6ImD

fiMQH2nfgatjrqZCuBLKcuZo5TkJ9XjcNlWyteFg7WVc5pFvxF2IUYx9LIPYFPGU

Adq2l1wC02V0cJGVq+w+StgzuaIr7ZzOr91ZGPlKmH4ly1oasXBexI1NgPQhm2p2

x+BbjPLRbRHSlODe685SqtYCTy0pxLh+q4yo7DiCgCJNmR0i+XytbVH+payKnTKv

E12Dqbm3Yt6iGk3QaJMwYodLmWdBp1G0NPlQB8HSLKACcw==

----END CERTIFICATE----
```

:::

### lsam SMASUP

The command places all troubleshooting information in a compressed tar file in the ```<LSAM root path>``` directory. The SMASUP command gathers the following troubleshooting information:

* Environmental variables
* System configuration (i.e., hostname, uname)
* Resource usage (i.e., df, netstat)
* The output of the lsam status command
* The LSAM_output file
* All log files and error files
* All trace files
* Contents of all configuration files

#### Syntax

```lsam<SAM_Socket> SMASUP```

### lsam start

The start command systematically executes the sma_log, sma_lsam, sma_disp, sma_cronmon, sma_filein, and sma_JORS processes to bring the LSAM to a fully operational status.

#### Syntax

```lsam<SAM_Socket> start```


### lsam start_fad

The start_fad command starts the SMA File Activity Detection Daemon(s) (SMA FAD). SMA FAD monitors directories specified for any relevant changes and forwards defined OpCon events to the SAM. For information on the SMA File Activity Detection Daemon, refer to [SMA File Activity Detection Daemon](../daemon/file-activity-detection-daemon).

#### Syntax

```lsam<SAM_Socket> start_fad```

### lsam status

The status command displays currently active LSAM components and LSAM-initiated processes.

#### Syntax

```lsam<SAM_Socket> status```

### lsam stop

The stop command systematically stops all of the LSAM processes.

#### Syntax

```lsam<SAM_Socket> stop```

### lsam stop_fad

The stop_fad command stops the SMA File Activity Detection Daemon(s) (SMA FAD). For information on the SMA File Activity Detection Daemon, refer to [SMA File Activity Detection Daemon](../daemon/file-activity-detection-daemon).

#### Syntax

```lsam<SAM_Socket> stop_fad```

### lsam version

The version command displays the version of the LSAM installed on the specified socket.

#### Syntax

```lsam<SAM_Socket> version```

