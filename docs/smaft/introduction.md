# SMAFT - Introduction

The SMA File Transfer (SMAFT) system reliably transfers files across multiple platforms via an OpCon job. Like file transfer protocol (ftp), SMAFT supports file compression and encryption but ensures that the file transfer completes before processing subsequent dependent jobs. SMAFT can support file transfers larger than two gigabytes as long as the underlying OS supports this feature. SMA Technologies does not recommend enabling encryption or compression for files larger than one gigabyte.

SMAFT supports Version 2 of the SMAFT specification. This allows the user to select Start Transfer On Source Machine in the Enterprise Manager definition screen. The Delete Source File option is not supported and should always be set to "No."

The receiving (Agent) and sending (Server) components are installed with FT-enabled LSAMs (e.g., the UNIX LSAM). The Source and Destination machines must have these components for a file transfer.

After receiving instructions from the LSAM on the Destination machine, the Agent (also on the Destination machine) and Server (on the Source machine) determine the best method for transporting the file. After negotiating the file transfer settings with the Server, the Agent requests the file. The Server retrieves the file and sends it to the Agent according to the Agent's instructions.

The LSAM will perform file transfer using the open standard SFTP between UNIX LSAMs when the user has configured the LSAM Configuration Parameter "sftp_port" to a non-zero value. If, for whatever reason the transfer failed, the LSAM will fallback to using SMAFT to perform the transfer.

When the LSAM is installed, the user has the option of choosing to use the /TMP partition or to use a TMP area in the same partition as the LSAM. File transfers may require anywhere from two to three times the size of the file being transferred in /TMP or TMP workspace designated when the LSAM was installed.