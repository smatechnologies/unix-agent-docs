# get_errno

The get_errno program translates the numeric error indicator (returned by UNIX system calls) into meaningful text. Text includes the standard symbolic constant # defined for the error and a brief description. Output is written to STDOUT. 

Additionally, if run as an OpCon job, the utility writes to the Enterprise Manager in the Detailed Job Messages field in the Job Information screen>Configuration Tab>Operations Related Information Tab. For additional information, refer to [Job Information](https://help.smatechnologies.com/opcon/core/Files/UI/Enterprise-Manager/Job-Information) in the Enterprise Manager online help.

## Syntax

```get_errno error_number```

```error_number``` is the numeric error indicator

:::info Note

 If executed from within a user's OpCon job, "```$SMA_BINDIR/```" must be preface the command (e.g., "```$SMA_BINDIR/get_errno error_number```").

:::

:::tip Example

The following example shows the use of get_errno for retrieving two error codes.

```
# get_errno 75

75 [EISCONN] - Socket is already connected

# get_errno 77

77 [ESHUTDOWN] - Can't send after socket shutdown
```

:::

:::tip Example

The following example shows get_errno clarifying error information on different systems. Note, although the error numbers differ, they are the same error.

```
AIX# get_errno 79

79 [ECONNREFUSED] - Connection refused

...

HP-UX$ get_errno 239

239 [ECONNREFUSED] - Connection refused
```

:::

:::tip Example

The following example shows get_errno within an OpCon job retrieving detailed exist status information on a command. The command returns the UNIX error number (i.e., errno) as its exit value.

```
...

$HOME/some_command p1 p2 p3 pn

$SMA_BINDIR/get_errno $?

...
```

:::