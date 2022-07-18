# file_check

The file_check utility checks if specified file(s) meet the requested criteria. The file_check utility is useful as a prerun job in OpCon when a job requires a specific file to meet some criteria before the job executes.

:::info Note

File_check returns the correct attributes (read, write, and execute) for the non-root UNIX user. For the root user, file_check will always return success for read, write, and execute (with some possible exceptions in Linux) attribute check.

:::

## Syntax

```
$SMA_BINDIR/file_check -a<erwx> [-e] –f<filename(s)> or - m<filename(s)>
[-s<#>] [-t<#>]
```

:::info Note

The environment variable ```$SMA_BINDIR``` is defined for use within OpCon jobs. If executed from a context other than an OpCon job, "```$SMA_BINDIR/```" must be replaced by the appropriate path.

:::

## Syntax Description for file_check

```-a<erwx>```: File attributes to check:

```e```: exists
```r```: read
```w```: write
```x```: execute

:::tip Example

The following example shows the command to check file attributes:

```$SMA_BINDIR/file_check –ae –f/home/john/datafile```

:::

```-e```: An optional argument to redirect filename(s) that match the specified criteria to STDOUT in environment variable format. The environment variable format is not standard format.

:::tip Example

The following example shows the both the variable and standard formats:

Variable Format: ```SMA_VAR_#=/usr/local/lsam/bin/genericpgm```

Standard Format: ```/usr/local/lsam/bin/genericpgm```

:::

```-f```: List of file(s) to check with exact filename(s). If checking multiple files, separate the files with commas (,).

:::tip Example

The following examples shows the command for checking file names:

```
$SMA_BINDIR/file_check –ae
-f /home/john/datafile1,/home/john/datafile2
```

:::

```-m```: List of filename pattern(s) to check. If not quoted, only the first file on the system with the pattern match is checked (comma delimited). User may specify how many files are checked within each pattern by specifying an optional number followed by a colon (:).

:::tip Example

The following example shows the command for checking filename patterns:

```-m "/dir/subdir/pattern","1:/anotherdir/subdir/pattern"```

:::

```-s```: An optional argument to further define the file criterion by specifying the minimum size (in bytes) of the file(s).

```-t```: An optional argument to further define the file criterion by specifying the minimum age (in seconds) of the file(s).

:::info Note

All files specified are compared to the attribute (```-a```), size (```-s```), and age (```-t```) criteria. If any of the files fail to meet the criteria, file check exits with a non-zero exit code.

:::

## file_check Exit Codes


### 0  

All criteria were met 

### 100

Invalid access attributes (-a) argument passed 

### 101

No files were specified to check with the -f and/or –m parameters 

### 102

* User does not have the required access attributes (-a) to the file(s) specified 
* Requested file(s) do not exist
* Requested file(s) reside on an un-mounted file system

### 103 

* User does not have access to the directory (or directories) specified by the match (-m) parameter
* Requested directory (or directories) do not exist
* Requested directory (or directories) reside on an un-mounted file system 

### 104 

The requested file(s) do not meet the size (-s) criteria 

### 105 

The requested file(s) do not meet the age (-t) criteria 