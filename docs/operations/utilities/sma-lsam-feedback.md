# sma_LSAM_feedback

The sma_LSAM_feedback utility instructs the LSAM to send a message to be displayed for a job's "LSAM Feedback" or "Detailed Job Messages" (depends on job type) field of the Job Configuration. One entry will be created for each use of "sma_LSAM_feedback". 

Note that this should not be used in the place of regular job output files to log job execution data, as indiscriminate use can quickly result in large amounts of data getting added to the OpCon database – its primary use is intended to be for the LSAM to communicate non-job-specific error conditions to SAM.

## Syntax

```$SMA_BINDIR/sma_LSAM_feedback "Message"```


:::tip Example

The following example shows a script using the sma_LSAM_feedback utility to send a message to be displayed in the Enterprise Manager.

```
. . .

$SMA_BINDIR/sma_LSAM_feedback "Unable to open PRD file"

. . .
```

:::