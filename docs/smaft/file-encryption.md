# File Encryption

By default, the SMA File Transfer (SMAFT) Server does not encrypt the Source File prior to its transfer to the Agent. Two additional options are available: PREFERRED and REQUIRED. If PREFERRED is selected, the file is transferred without encryption if the Server and Agent are unable to negotiate a compatible method of encrypting the file. If REQUIRED is selected and if an encryption method cannot be negotiated, the transfer is not performed and the job fails.

By default, the SMA File Transfer (SMAFT) Server does not encrypt the Source File prior to its transfer to the Agent. Two additional options are available: PREFERRED and REQUIRED. If PREFERRED is selected, the file is transferred without encryption if the Server and Agent are unable to negotiate a compatible method of encrypting the file. If REQUIRED is selected and if an encryption method cannot be negotiated, the transfer is not performed and the job fails.

During the LSAM installation, the LSAM is configured with support for all available encryption capabilities as outlined below. Each installation of the LSAM may subsequently be configured for encryption in SMAFT jobs (refer to [Updating the SMA File Transfer (SMAFT) Control Script)](/configuration/updating-smaft-control-script). Encryption support applies to both Server and Agent for an LSAM.

Configuring encryption support involves entering a string of one or more comma-separated numbers. A simple zero disables encryption. If no encryption support is enabled, all SMAFT jobs which reference the LSAM (as either Source machine or Destination machine) FAIL(s) if encryption is REQUIRED or FAIL-PREFERRED.

Configuration changes take effect immediately in the Agent; however, the LSAM must either be restarted or refreshed for the changes to become effective in the Server.

The UNIX LSAM supports three encryption algorithms in two modes of operation with two-variants per mode, for a total of fifteen (15) capabilities (not all possible combinations are used):

* Algorithms (in increasing order of security)
    * 1: DES
    * 2: 3DES (Triple-DES)
    * 3: AES-128

* Modes (in increasing order of security)
    * 100: ECB
    * 200: CBC

* Variants
    * 10000: CTS (increases security)
    * 20000: Bitstring-padding (no effect on security)

A supported capability is the **sum** of an algorithm, mode, and variant. For example, to specify AES-128 operating in CBC-CTS enter 10203 (3 + 200 + 10000).

Algorithms: DES is now considered to be too insecure for most uses. 3DES still offers a reasonable level of security. AES is the new standard adopted by the United States government and is expected to offer a high level of security for the foreseeable future.

Modes: ECB (Electronic CodeBook) has the undesirable feature of allowing multiple instances of plaintext to be revealed in the ciphertext. The plaintext itself is not revealed, only that a pattern exists. CBC (Cipher Block Chaining) keeps patterns in the plaintext from appearing in the ciphertext.

Variants: All three algorithms chop the plain text into equally-sized blocks for encryption. CTS (Ciphertext Stealing) makes it so the ciphertext is not always a multiple of the algorithm's block size, thus hiding this information from eavesdroppers. When CTS is not being used, the final block must be expanded to the required size. The default method is to determine how many bytes need to be added (minimum of 1) to the final block of plain text and then add that many bytes of that value. For example, if the final block of plain text is "wxyz" and the algorithm is 3DES (which has a block size of 8), 4 bytes need to be added to the plain text, which will be "wxyz4444" after padding, where 4 indicates text added to allow encryption. After decryption, the final byte of the decrypted text is inspected to see how many bytes must be removed to recover the plain text. For Bitstring-padding, a 1-bit is added to the plain text, and then enough 0-bits to fill-out the block. After decryption, the plain text will be searched from the end for the first 1-bit; it and the rest of the block will then be discarded to recover the plain text. Since UNIX does not support bit-length files, the Agent will pad the recovered plain text with enough 0-bits to fill the final byte of the file as it writes it to disk. 

Supported capabilities may be listed in any order. When UNIX is the Source machine, the Server sends the Agent the supported capabilities in the order listed (during configuration). From those capabilities supported by the Server, the Agent decides what algorithm, mode, and variant to use. The Agent may or may not take into account the order in which the Server lists its supported capabilities. Although the UNIX Agent does not use the order for its determination, other Agents may. SMA Technologies recommends configuring supported capabilities in priority order.

When UNIX is the Destination machine; the Agent determines the algorithm, mode, and variant to be used for encrypting the file by searching its supported capabilities list against the Server's list of supported capabilities. The search is from left to right for the first match to a capability supported by the Server.

Including all encryption capabilities currently available with the UNIX LSAM, the default supported capabilities list is:

```

10203,20203,203,10202,20202,202,20103,103,20102,102,10201,20201,201,20101,101

```
 

This string translates to:

```

AES‑128/CBC‑CTS, AES‑128/CBC‑Bitstring AES‑128/CBC, 3DES‑CBC‑CTS, 3DES‑CBC‑Bitstring, 3DES‑CBC, AES‑128/ECB, AES‑128/ECB‑Bitstring, 3DES/ECB, 3DES/ECB‑Bitstring, DES/CBC‑CTS, DES/CBC‑Bitstring, DES/CBC, DES/ECB‑Bitstring, DES/ECB 

```

Many factors, some of which were noted above in the discussion of algorithms, modes, and variants, go into the determination of which combinations offer the highest security. SMA Technologies makes no claim that the default order of precedence listed above offers the best level of security in all situations. LSAM Administrators must configure the supported capabilities and the capabilities' precedence according to their organization's security policies. Unless their organization's security policies require otherwise, SMA Technologies recommends that all supported capabilities be configured (in whatever precedence order is desired) to allow the greatest opportunity for completion cross-platform file transfers using encryption.

In the default configuration listed above, SMA Technologies applies a higher precedence to 3DES/CBC than to AES-128/ECB, although AES‑128 is a more secure algorithm than 3DES. Reducing security risk, 3DES/CBC is preferable because of the ECB property of patterns of plaintext being evident in the ciphertext to eavesdroppers. The difference in the levels of security between 3DES and DES is too great to give DES/CBC a higher precedence than 3DES/ECB.