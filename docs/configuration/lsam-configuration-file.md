# LSAM Configuration File

## Modify the Configuration File

1. Log in to the UNIX system as root.
2. Change the directory to the LSAM's bin directory. Use the following syntax: ```cd $LSAM_ROOT/bin```.

:::tip Example

The following example shows the syntax for getting to the LSAM's bin directory, assuming that ```$LSAM_ROOT``` is ```/usr/local/lsam```:

```cd /usr/local/lsam/bin```

:::

3. Start the LSAM configuration program. Use the following syntax: ```./lsam<SAM_Socket> config```

:::tip Example

The following example shows the syntax for starting the LSAM configuration program. The LSAM's SAM Socket number (```<SAM_Socket>```) is 3100:

```./lsam3100 config```

:::

4. Select an option from the menu and make any necessary modifications to the displayed values. For complete information on the lsam.conf settings, refer to the [TCP/IP Configuration Parameters](tcp-ip-configuration) tables.
5. Repeat step 3 until all LSAM options are set correctly.
6. Enter s to save the configuration changes.
7. Enter q to quit the configuration program.
8. If the LSAM was running when performing step 3, refresh the LSAM after saving the configuration file. For information on refreshing the LSAM, refer to [lsam refresh](lsam-refresh).