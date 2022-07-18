# sma_ppscript

The sma_ppscript utility provides an alternative method to the Job Details screen's "Failure Criteria" for determining a job's success or failure. A Job's executable invokes sma_ppscript telling the LSAM the job needs post-processing with a user-supplied analysis script. 

When the job finishes, the LSAM executes the script. After analysis, the script returns a zero for success and a non-zero value for failure. The LSAM simply returns the success or failure of the job without specific details; however, the script may call the utility sma_status to provide further details to the Enterprise Manager.

## Syntax

```$SMA_BINDIR/sma_ppscript <script_command>```

:::info Note

The environment variable $SMA_BINDIR is defined for use within OpCon jobs. If executed from a context other than an OpCon job, "$SMA_BINDIR/" must be replaced by the appropriate path.

:::

## Analysis Script

To create an Analysis Script, write a shell script (or compiled program) to do the analysis. It may take any start parameters desired, and has the pathnames of the job's redirected STDOUT and STDERR files appended to the user-supplied list of start parameters. The script/program may do whatever it wishes to determine success or failure, to be indicated by its exit status.

:::info Note

If the LSAM is not configured to redirect STDOUT and/or STDERR to files, the script sees "NONE" for the/each pathname.

:::

:::tip Example

The following example shows the analysis script "/usr/home/john/check_ls" which uses the LSAM file_check utility. The script determines whether the job's redirected STDOUT exists and is of sufficient length. If so, the script exits with a zero; otherwise, the script returns a non-zero value.

```

#!/bin/sh

# $1 -- status text to display in Enterprise Manager

# $2 -- minimum acceptable file size

# $3 –- pathname of redirected STDOUT

# $4 -– pathname of redirected STDERR (not used!)

$SMA_BINDIR/sma_status $1

sleep 10

# Does STDOUT exist and at least $2 bytes long?

$SMA_BINDIR/file_check –ae -f $3 –s $2

exit $?

```

:::

## Invocation of the Analysis Script

Insert sma_ppscript into the job's executable for invocation of analysis script. Once the analysis script has been written, embed the command "$SMA_BINDIR/sma_ppscript ```<script_command>```" anywhere within the job's top-level script/program. For example, assuming the script is named "/usr/home/john/check_results", "$SMA_BINDIR/sma_ppscript /usr/home/john/check_results 1 a".

:::tip Example

This is the job which requires post-processing by "/usr/home/john/check_results":

```

#!/bin/sh

$SMA_BINDIR/sma_status "Registering script"

$SMA_BINDIR/sma_ppscript /usr/home/john/check_ls Checking 50

sleep 10

$SMA_BINDIR/sma_status "Listing stuff"

ls –l /usr/home/john/stuff

sleep 10

```

:::