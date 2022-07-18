# Control File

The Control File contains all the parameters the daemon needs to monitor the directories and initiate the SAM external events. As a single ASCII text file, the Control File is configurable with standard editors (e.g., vi). The Control File has the following characteristics:

* The Control File resides in the following directory: ```LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/```. The filename has a limit of 63 characters (excluding the pathname).
* The Control File consists of blocks of records that are processed one at a time.
* The Control File is an XML type file, and all the elements are defined within their tags.
* A "#" sign as the first non-blank character on a line comments out the whole line.
* Multiple Control Files can exist in the control directory.
    * Each Control File identifies a unique instance of the file activity detection daemon.
    * Each Control File also serves as a configuration file for the associated instance of the daemon.
    * Using the Control File names as identifiers, the FAD daemon startup script (like the LSAM startup script) starts one instance of the daemon for each file in the control directory.

:::info Note

For most sites, a single instance of the SMA FAD is sufficient; nevertheless, multiple instances of SMA FAD can monitor different directories at different intervals.

:::

* The LSAM must be restarted before modifications take effect, or after the new control file has been copied into the Control Directory. Issue a bin/stop_fad command followed by a bin/start_fad command from the ```<LSAM _Root_Directory>``` directory.