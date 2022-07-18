# genericpgm

The genericpgm program sleeps for the requested time (default 10 seconds) and then exits with the requested exit code (default zero [0]) and signal disposition (default zero [0]). Valid UNIX exit codes are restricted to the range -127 to 127.

## Syntax

```genericpgm [-e#] [-s#] [-t#]```

* ```-e#```: An optional argument to set the exit code.
* ```-s#```: An optional argument to set the signal disposition.
* ```-t#```: An optional argument to set the sleep time in seconds.