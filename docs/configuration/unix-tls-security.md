# UNIX TLS Security Procedures

When enabled, TLS (i.e., “use_TLS_SAM” parameter is set to '1' in lsam.conf file) allows secured communication between the agent and OpCon/SAM and JORS, and is supported since agent version 16.01. SMAFT TLS functionality is supported on versions greater than 19.1. Hence, with the new SMAFT_TLS feature, ensure that the “SMAFT TLS_socket” number is always different than the “SMAFT_socket” number in the lsam.conf file. Also notice that if “use_TLS_SAM” is enabled, SMAFT_socket (which doesn’t support TLS protocol) must be different than JORS_FT_socket, which uses TLS protocol to communicate with OpCon/SAM. If it is disabled, then JORS_FT_socket can be the same or different than the SMAFT_socket number. SMA Technologies recommends that all three sockets (SMAFT_socket, SMAFT_TLS_socket, and JORS_FT_socket) use different numbers to avoid possible conflicts.

The UNIX agent supports both trusted (signed by a trusted certificate authority – CA) and untrusted (self-signed) certificates. The agent performs the role of a TLS/SSL server (similar to a web server) and OpCon/SAM as the client (e.g., a web browser).

For trusted certificates (e.g., signed by Verisign), the user can simply import it into the agent and configure the lsam.conf file to point to that certificate.

For self-signed certificates, besides configuring the lsam.conf file to point to it, the user must also import that file into the OpCon/SAM machine.

It is the responsibility of the user to monitor the certificates' expiration dates. When the certificate expires communication between the agent and OpCon could stop (future versions will provide a script to monitor expiration dates and warn the users ahead of time via email).

To ease certificate management it is recommended that the user uses a wildcard certificate. Refer to this article for additional details:

[What is a Wildcard SSL Certificate?](https://www.godaddy.com/help/what-is-a-wildcard-ssl-certificate-567)

## Lsam.conf File Changes

Four new entries are added under TCP/IP configuration parameters:

* Use ```_TLS_SAM 1 // 0``` to disable, anything else to enable.
* Lsam_pem_file ```/usr/dt/mycert.pem //``` points to the public certificate file.
* Lsam_private_key_file ```/usr/dt/mycert.pem // ```points to the private key file (may be the same as public certificate file).
* Netcom_pem_file (none // reserved for future use)

In the above example, file /usr/dt/mycert.pem contains both the public certificate and private key.

Netcom_pem_file is reserved for future use and its purpose is intended for the agent to authenticate OpCon/SAM.

### create_cert and show_cert

Two new commands (create_cert and show_cert) are added to lsam. They are shown below:

```

[root@redhat5as 1014]/usr/dt/main# bin/lsam5000

Usage: lsam5000 <option>

--option--

SMASUP

command

config

config_check

create_cert [certificate validity date (default=365, max=3650)]

delete_logs

dumptracking

kill_jobs

log_break

refresh

restart [newlog]

show_cert certificate_file

start [newlog]

start_fad

status

stop

stop_fad

version

```

For example, users could issue the following command to create a self-signed wildcard certificate that:

* Is valid for 10 years,

* Combines both the private key and public certificate into one file with .pem format and,

* Generates a certificate file with .pfx format for importing into OpCon/SAM machine via mmc, for example.

On a Windows machine, use IIS Manager to create a server certificate.

### Common Name

The most important configuration to configure is the “Common Name” field. By using wildcard ```*smausa.com``` in this field, we can make use of this one certificate file for all the servers that end with domain name “smausa.com”. In other words, there is no need to generate a unique certificate for each server.

```

bin/lsam5000 create_cert 3650

Generating self-signed certificate redhat5as.pem valid for 3650 days

Generating a 2048 bit RSA private key

..........................................................+++

...+++

writing new private key to 'redhat5as.pem'

```

### Distinguished Name

At this point, you will be asked to enter information that will be incorporated into your certificate request. What you are about to enter is what is called a Distinguished Name or a 'DN'.

There are quite a few fields, but some may be left blank. For some fields there will be a default value. If you enter the value '.', the field will be left blank.

```

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

### User Friendly Certificate Format

The following command can be used to display the certificate in a user’s friendly format:

```

bin/lsam5000 show_cert redhat5as.pem

Certificate:

Data:

Version: 3 (0x2)

Serial Number:

e5:c1:38:13:65:4e:8f:47

Signature Algorithm: sha256WithRSAEncryption

Issuer: C=US, ST=TX, L=Kingwood, O=SMA Technologies, OU=Engineering,

CN=*.smausa.com/emailAddress=support@smatechnologies.com

Validity

Not Before: Oct 14 20:18:11 2016 GMT

Not After : Oct 12 20:18:11 2026 GMT

Subject: C=US, ST=TX, L=Kingwood, O=SMA Technologies, OU=Engineering,

CN=*.smausa.com/emailAddress=support@smatechnologies.com

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

 

-----BEGIN CERTIFICATE-----

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

-----END CERTIFICATE-----

```