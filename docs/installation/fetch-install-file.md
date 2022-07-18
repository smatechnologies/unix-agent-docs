# Fetching LSAM Installation File

Regardless of whether the installation is new or an upgrade, the installation procedure is initiated by placing the LSAM Installation File into "/tmp" on the target machine. The OpCon installation media contains the binary tar file for the LSAM. If the UNIX machine has a DVD-ROM drive, copy the file directly from the DVD; otherwise, FTP the file (in binary mode) from a networked machine to the UNIX machine.

## Option 1: Copy the File

1. Create a "```/tmp```" directory on the UNIX machine if it does not already exist.
2. Insert the OpCon installation media in the machine.
3. Copy the LSAM tar file from the OpCon installation media to ```/tmp```.
    * Use file path: ```<media>/Install/LSAM/ UNIX LSAM/15.00.xx/<platform>```
4. Copy the install_agent script file from the OpCon/xps installation media to ```/tmp```.

:::info Note

The LSAM tar file name varies depending both on the UNIX platform type and on the operating system version.

::: 

:::tip Example

The following example shows the commands for copying the ```HP-UX 11_00.tar``` file to ```/tmp```:

```
cd "DVD-ROM/Install/LSAM/UNIX LSAM/15.00.xx/HP-UX/"
cp 11_00.tar /tmp
```

::: 

## Option 2: FTP the File

The file transfer installation procedure uses the basic FTP program distributed with the Windows Operating System. If using another FTP program, be sure to set the transfer type to binary.

1. Create a "```/tmp```" directory on the UNIX machine if it does not already exist.
2. Insert the OpCon installation media in a Windows machine with a network connection to the UNIX machine.
3. Use menu path: Start > Run.
4. Enter cmd to open a command window.
5. Change the directory to the location of the tar file on the installation media. Use the following syntax:
```cd<media>\Install\LSAM\ UNIX LSAM\15.00.xx\<platform>```

:::tip Example

The following example shows the command for navigating to the HP-UX directory on the OpCon DVD on drive letter E:

```cd e:\Install\LSAM\UNIX LSAM\15.00.xx\HP-UX```

:::

6. Enter the FTP command with the TCP/IP address of the target UNIX machine. Use the following syntax:

```ftp <Machine Name>```

:::tip Example

The following example shows the syntax for the FTP command to FTP to a machine called "jupiter":

```ftp jupiter```

:::

7. Enter the appropriate user for the FTP session (this may not be 'root', as 'root' is often disallowed for FTP for security reasons).
8. At the Password prompt, enter the appropriate password.
9. Enter bin to set the transfer type to binary.
10. Make the target directory to be "/tmp" with the following command: cd /tmp. Put the LSAM tar file into /tmp. Use the following syntax:

```put<OS Version>.tar```

:::info Note

The LSAM tar file name varies depending both on the UNIX platform type and on the operating system version.

:::


:::tip Example

The following example shows the command for putting the HP-UX 11_00.tar file into the target directory ("```/tmp```"):

```put 11_00.tar```

:::

11. Enter bye or quit to exit the FTP program.

