# maintain_ofiles

The maintain_ofiles program prevents the accumulation of outdated job-related files. This program deletes files older than the specified number of days. It specifically deletes: job output files, job tracking files, and anything within the LSAM's tmp directory. For example, if the program's parameter indicates 10 days should be kept, it removes any job-related file older than midnight of 10 days ago.

:::tip Example

If the command is issued at 10:21 AM on Oct 20th with the number of days to retain specified as 10, all files older than 12:00 AM of Oct 10th are deleted.

:::

SMA Technologies recommends scheduling this program in OpCon and running the job daily or weekly to remove job-related files older than the configured days to retain. The default number of days to retain is 3.

:::info Note

This program will also delete any SMA Resource Monitor (SMA_RM) log files which are older than the specified number of days.

:::

## Syntax

```$SMA_BINDIR/maintain_ofiles <number of days to retain>```

:::info Note

The environment variable ```$SMA_BINDIR``` is defined for use within OpCon jobs. If executed from a context other than an OpCon job, "```$SMA_BINDIR/```" must be replaced by the appropriate path.

:::



