# Automatic Startup Configuration for the LSAM

To ensure that the LSAM automatically starts and stops, create a symbolic link from the LSAM Control Script (e.g., lsam3100) to the system's init.d directory. Then make symbolic links from the init.d link to the rc<#>.d directories.

:::info Note

To ensure that the LSAM automatically starts and stops, create a symbolic link from the LSAM Control Script (e.g., lsam3100) to the system's init.d directory. Then make symbolic links from the init.d link to the rc<#>.d directories.

:::

When creating the links to the rc<#>.d directories, appropriately place the LSAM in the sort order. This order should cause the LSAM to be one of the last items started and one of the first items stopped.

:::warning

If the LSAM startup is not one of the final steps in the system boot sequence, erratic behavior may result. If this erratic behavior disappears with a manual restart of the LSAM, move the LSAM startup further down in the system's boot sequence.

:::


:::tip Example

The following example shows the commands, on a Solaris machine, to automatically stop and start the lsam3100 control script if the machine is booted in multi-user mode.

```
ln -s /usr/local/lsam/bin/lsam3100 /etc/init.d/lsam3100

ln -s /etc/init.d/lsam3100 /etc/rc2.d/K02lsam3100

ln -s /etc/init.d/lsam3100 /etc/rc2.d/S98lsam310
```

:::