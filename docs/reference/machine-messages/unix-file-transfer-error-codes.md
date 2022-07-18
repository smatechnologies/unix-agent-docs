# UNIX File Transfer Error Codes

File transfer errors received by STDOUT/STDERR may be viewed in the Enterprise Manager's Job Output Retrieval System (JORS). The messages in this section are output by the UNIX Agent and Server; messages output by a non-UNIX Agent or Server will be different, and the user is referred to the documentation for the appropriate LSAM.

## UNIX SMAFT Exit Codes

| Exit Code | Description |
| --------- | ----------- |
| 0	| Success; The job finished OK |
| 1	| Internal system error such as fork, memory or space failure, etc. |
| 2	| Invalid SMAFT OpCon Job Definition parameters |
| 3	| Received an error from peer (i.e., the other end) |
| 4	| Network or file Read error | 
| 5	| Network or file Write error |
| 6	| Encryption error | 
| 7	| Decryption error | 
| 8	| Compression error | 
| 9	| Decompression error | 
| 10 | TAR error | 
| 11 | SMAFT protocol header error | 
| 12 | User's permission/access error | 
| 13 | File operation error | 
| 14 | Disk space error | 
| 15 | Error in prepping source file for transfer | 
| 16 | Error in post-processing destination file |

