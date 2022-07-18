# STDOUT Error Codes

## Original Destination File [dest] backed-up to [backup]

**Origination**: FTAgent

Per the job's "Overwrite" option, the FTAgent backed up the Destination File prior to starting the file transfer.

## Original Destination File [file] did not exist to back-up

**Origination**: FTAgent

At the job's startup, no Destination File existed to backup.

## Could not change default access permissions for Destination File [dest]

**Origination**: FTAgent

Following the transfer of a new Destination file, the new file's access privileges could not be changed from the system-dependent default to:

* Full access by owner
* Read access by group
* No access by others

:::info Note 

If the Destination File existed before the file transfer, the file transfer does not modify its access permissions.

:::

## \[src_machine]src_file --> [dest_mach]dest_file

**Origination**: FTAgent

* Displays the results of the file transfer.
* The Destination File was created or overwritten.
* Shown if the job's "Overwrite" option specified appending, but the Destination File did not exist prior to the file transfer.

## \[src_machine]src_file appended --> [dest_mach]dest_file

**Origination**: FTAgent

* Displays the results of the file transfer.
* The Source File was appended to the Destination File.

## File transfer successfully completed

**Origination**: FTAgent

The job ran to completion.

## File transfer did not complete!

**Origination**: FTAgent

* The job did not run to completion. The file may or may not have been transferred.
* Refer to the job's STDERR output for details of what went wrong.