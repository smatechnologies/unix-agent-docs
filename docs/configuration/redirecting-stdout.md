# Redirecting STDOUT

If the parameter ```path_to_su``` is set to Yes, redirecting ```STDOUT``` in the start image received from the Enterprise Manager will work fine.

If the parameter ```path_to_su``` is set to No, redirecting ```STDOUT``` must take place within a script. Because of its design, the LSAM does not correctly interpret a redirection character (>) in a Start Image received from the Enterprise Manager. Each script must contain the code to redirect ```STDOUT```, or a wrapper script can receive each script and handle the redirection. If the output is not redirected, it will be sent to the ```LSAM_output``` file, ```LSAM_output_<SAM_socket>``` in the LSAM root directory.

SMA Technologies provides a generic script ```captureSTDOUT``` that redirects ```STDOUT``` for any script. The ```captureSTDOUT``` script resides in the ```<LSAM root path>/bin``` directory. This script is a working template, and is open to modification by a system programmer to contain more detailed information. The template is for use with the Korn shell; therefore, be sure to adjust the script according to the shell in use.

For information on analyzing standard out to determine exit conditions, refer to [sma_ppscript](sma-ppscript).

## Syntax

```<path>/captureSTDOUT <path to output file> <path to script>```

The ```<path>``` points to the LSAM "```bin/```" directory (e.g., "```/usr/local/lsam/bin```").

:::tip Example

An example UNIX job has the following characteristics:

The job to execute has the following path: ```/usr/local/payroll/timecalc```
The standard output from the job goes to the following file: ```/usr/local/payroll/finished/timecalc.datetime.```
Assuming the ```captureSTDOUT``` file is in the LSAM ```/bin``` directory, the Start Image and Parameters on the UNIX Details screen (in the Enterprise Manager's Job Master) for the above job would contain the following:

Start Image: ```/usr/local/lsam/bin/captureSTDOUT```

Parameters: ```/usr/local/payroll/finished/timecalc.datetime/usr/local/payroll/timecalc```

:::

For more information, refer to [UNIX Job Details](unix-job-details) in the Concepts online help.