# File Compression

Both the UNIX SMA File Transfer (SMAFT) Agent and Server support file compression using the UNIX "tar" and "gzip" utilities. By default, the Server does not compress the Source File prior to its transfer to the Agent. Two additional options are available: PREFERRED and REQUIRED. If PREFERRED is selected, the file is transferred without compression if the Server and Agent are unable to negotiate a compatible compression method. If REQUIRED is selected and if a compression method cannot be negotiated, the transfer is not performed and the job fails.

:::info Note 

Although the "tar" utility may process multiple files, an OpCon File Transfer job can only transfer a single file.

:::

During the LSAM installation, the installation script searches the system for the "tar" and "gzip" utilities and sets compression support accordingly. Each installation of the LSAM may subsequently be configured for compression during file transfer. Compression settings apply to both Server and Agent for an LSAM. If compression support is not enabled, all SMAFT jobs which reference the LSAM (as either Source machine or Destination machine) fail if compression is REQUIRED or FAIL-PREFERRED. 

Configuration changes take effect immediately in the Agent; however, the LSAM must either be restarted or refreshed for the changes to become effective in the Server.