# sma_status

The sma_status utility sends a message for the Enterprise Manager to display after the OpCon status message. The message's maximum is twenty-characters. Without warning the user, the LSAM truncates messages longer than the maximum.

## Syntax

```$SMA_BINDIR/sma_status "<message>"```

:::info Note

The environment variable $SMA_BINDIR is defined for use within OpCon jobs. If executed from a context other than an OpCon job, "$SMA_BINDIR/" must be replaced by the appropriate path.

The job status posted by this command remains in the Enterprise Manager until the job status changes or the job terminates.

:::

:::tip Example

The following example shows a script using the sma_status utility. The script sends a message when each step of the job begins processing.

```

#!/bin/sh

# Job status in Enterprise Manager currently shows "Job Running:Pid = pid"

$SMA_BINDIR/sma_status "Starting Step 1"

# Job status in Enterprise Manager now shows "Job Running:Starting Step 1"

do_step 1

$SMA_BINDIR/sma_status "Starting Step 2"

do_step 2

# Job status in Enterprise Manager now shows "Job Running:Starting Step 2"

```

:::