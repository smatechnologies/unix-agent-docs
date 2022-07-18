# Configuring the Time Zone in the Root Profile

Before starting the UNIX LSAM, set the TZ (time zone) environment variable in the root user's environment. To verify the current setting, log in as the root user and enter "env". If the TZ environment variable is not set, the LSAM uses a default time zone of EST5EDT.

* To set the TZ environment variable for root, edit the .profile (or .cshrc depending on which shell is used) file in the home directory of the root user.

* To set the TZ environment variable for all users, consult the system administrator. The system wide setting for the TZ environment variable is different for different versions of UNIX. (For example, AIX keeps its system wide environment settings in /etc/environment. Linux keeps its system wide environment settings in /etc/profile.)

* To set the TZ environment variable in the LSAM startup script, edit the ```lsam<SAM_Socket>``` file in the $LSAM_ROOT/bin directory. Add a line to the LSAM startup script that looks like the following:

```TZ=xxxxxxxxxx; export TZ```
    
* xxxxxxxxx is the identifier for the desired time zone.

:::info Note

Time zone identifiers vary on different versions of UNIX. For a list of valid identifiers, see the system administrator.

:::