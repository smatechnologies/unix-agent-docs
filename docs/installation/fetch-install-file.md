---
title: Fetching agent Installation File
description: "Step-by-step procedures for placing the Unix Agent installation tar file onto the target UNIX machine via DVD copy or FTP transfer."
tags:
  - Procedural
  - System Administrator
  - Installation
---

# Fetching agent installation file

**Theme:** Build  
**Who Is It For?** System Administrator

## What is it?
Step-by-step procedures for placing the Unix Agent installation tar file onto the target UNIX machine via DVD copy or FTP transfer.

Use this procedure in the following situations:

- When the UNIX machine has a DVD-ROM drive and the OpCon installation media is available locally, to copy the tar file directly from the DVD.
- When the UNIX machine does not have a DVD-ROM drive but has a network connection to a Windows machine that holds the installation media, to transfer the tar file to the UNIX machine using FTP.

Regardless of whether the installation is new or an upgrade, the installation procedure is initiated by placing the agent Installation File into "/tmp" on the target machine. The OpCon installation media contains the binary tar file for the agent. If the UNIX machine has a DVD-ROM drive, copy the file directly from the DVD; otherwise, FTP the file (in binary mode) from a networked machine to the UNIX machine.

## Option 1: Copy the file

To copy the installation file from OpCon installation media, complete the following steps:

1. Create a "```/tmp```" directory on the UNIX machine if it does not already exist.
2. Insert the OpCon installation media in the machine.
3. Copy the agent tar file from the OpCon installation media to ```/tmp```.
    * Use file path: ```<media>/Install/LSAM/ UNIX LSAM/15.00.xx/<platform>```
4. Copy the install_agent script file from the OpCon/xps installation media to ```/tmp```.

:::info Note

The agent tar file name varies depending both on the UNIX platform type and on the operating system version.

::: 

:::tip Example

The following example shows the commands for copying the ```HP-UX 11_00.tar``` file to ```/tmp```:

```
cd "DVD-ROM/Install/LSAM/UNIX LSAM/15.00.xx/HP-UX/"
cp 11_00.tar /tmp
```

::: 

The file is copied to ```/tmp``` on the UNIX machine.

## Option 2: FTP the file

The file transfer installation procedure uses the basic FTP program distributed with the Windows Operating System. If using another FTP program, be sure to set the transfer type to binary.

To transfer the installation file using FTP, complete the following steps:

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
10. Make the target directory "/tmp" with the following command: cd /tmp.
11. Put the agent tar file into /tmp. Use the following syntax:

```put<OS Version>.tar```

:::info Note

The LSAM tar file name varies depending both on the UNIX platform type and on the operating system version.

:::


:::tip Example

The following example shows the command for putting the HP-UX 11_00.tar file into the target directory ("```/tmp```"):

```put 11_00.tar```

:::

12. Enter bye or quit to exit the FTP program.

The agent installation file is transferred to ```/tmp``` on the UNIX machine.

## Exception handling

**FTP connection is refused or the login fails for the root account** — Root is often disallowed for FTP sessions for security reasons. — Use a non-root account that has FTP access to log in and transfer the file, as noted in step 7 of the FTP procedure.

**File is transferred but the installation fails to extract correctly** — The tar file was transferred in ASCII mode instead of binary mode, which corrupts the binary content. — Re-transfer the file after setting the FTP transfer type to binary by entering `bin` at the FTP prompt before issuing the `put` command.

**The install_agent script cannot locate the tar file or behaves unexpectedly** — More than one `.tar` file is present in the working directory. The install_agent script searches for a single file with the `.tar` extension rather than a specific filename. — Remove any extra `.tar` files from the working directory before running the installation script, leaving only the agent binary tar file.
