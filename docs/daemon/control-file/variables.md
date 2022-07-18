# Variables


The SMA FAD supports several variables in the event strings. Before sending the event string to the SAM for processing, SMA FAD replaces the variables with their current values. The following variables retrieve values from the ```<filemask>``` element in the associated record block:

* ```%FULLNAME%```: Full path and filename
* ```%PATHNAME%```: Path name of the file's location, excluding the last slash (/)
* ```%FILENAME%```: The file name alone
* ```%FILEROOT%```: Part of the filename up to but excluding the last dot (.)
* ```%FILEEXT%```: The end of the filename beginning after the last dot (.)

:::info Note 

All tokens are case sensitive.

:::

## FAD Condition Variables

* CREATE: Checks to see if a file has been created since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not grown in the last MINTIMETOWAIT seconds. FAD will execute the associated event(s) once the file has stopped changing size.
* DELETE: Checks to see if a file has been deleted since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not been in existence in the last MINTIMETOWAIT seconds. FAD will execute the associated event(s) once the file has ceased to exist.
* GROWTH: Checks to see if a file has had new bytes written to the file since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that no bytes have been written in the last MINTIMETOWAIT seconds. FAD will execute the associated event(s) once the file has stopped changing size.
* SHRINK: Checks to see if a file has become smaller since the last check. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not grown smaller in the last MINTIMETOWAIT seconds. FAD will execute the associated event(s) once the file has stopped changing size.
* ABSOLUTE: Checks to see if a file has exactly the specified number of bytes. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has grown/shrunk to the specified number of bytes after MINTIMETOWAIT seconds. FAD will execute the associated event(s) once the file has reached the specified size.
* MODIFY: Checks to see if a file has been modified. When combined with MINTIMETOWAIT parameter, FAD will verify that the file has not been modified in the last MINTIMETOWAIT seconds. FAD will execute the associated event(s) once modifications to the file have stopped.