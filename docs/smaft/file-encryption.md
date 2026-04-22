---
title: File Encryption
description: "SMAFT supports optional file encryption using DES, 3DES, and AES-128 algorithms in ECB and CBC modes, configurable per agent installation as PREFERRED or REQUIRED."
tags:
  - Conceptual
  - Reference
  - System Administrator
  - Agents
---

# File Encryption

**Theme:** Overview  
**Who Is It For?** System Administrator

## What is it?
SMAFT supports optional file encryption using DES, 3DES, and AES-128 algorithms in ECB and CBC modes, configurable per agent installation as PREFERRED or REQUIRED.

By default, the SMA File Transfer (SMAFT) Server does not encrypt the Source File prior to its transfer to the Agent. Two additional options are available: PREFERRED and REQUIRED. If PREFERRED is selected, the file is transferred without encryption if the Server and Agent are unable to negotiate a compatible method of encrypting the file. If REQUIRED is selected and if an encryption method cannot be negotiated, the transfer is not performed and the job fails.

During the agent installation, the installation script configures the agent with support for all available encryption capabilities as outlined below. You can subsequently configure each installation of the agent for encryption in SMAFT jobs (refer to [Updating the SMA File Transfer (SMAFT) Control Script)](../configuration/updating-smaft-control-script). Encryption support applies to both Server and Agent for an agent.

Configuring encryption support involves entering a string of one or more comma-separated numbers. A simple zero disables encryption. If no encryption support is enabled, all SMAFT jobs which reference the agent (as either Source machine or Destination machine) FAIL(s) if encryption is REQUIRED or FAIL-PREFERRED.

Configuration changes take effect immediately in the Agent; however, the agent must either be restarted or refreshed for the changes to become effective in the Server.

The Unix Agent supports three encryption algorithms in two modes of operation with two-variants per mode, for a total of fifteen (15) capabilities (not all possible combinations are used):

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

Including all encryption capabilities currently available with the Unix Agent, the default supported capabilities list is:

```

10203,20203,203,10202,20202,202,20103,103,20102,102,10201,20201,201,20101,101

```
 

This string translates to:

```

AES‑128/CBC‑CTS, AES‑128/CBC‑Bitstring AES‑128/CBC, 3DES‑CBC‑CTS, 3DES‑CBC‑Bitstring, 3DES‑CBC, AES‑128/ECB, AES‑128/ECB‑Bitstring, 3DES/ECB, 3DES/ECB‑Bitstring, DES/CBC‑CTS, DES/CBC‑Bitstring, DES/CBC, DES/ECB‑Bitstring, DES/ECB 

```

Many factors, some of which were noted above in the discussion of algorithms, modes, and variants, go into the determination of which combinations offer the highest security. SMA Technologies makes no claim that the default order of precedence listed above offers the best level of security in all situations. agent Administrators must configure the supported capabilities and the capabilities' precedence according to their organization's security policies. Unless their organization's security policies require otherwise, SMA Technologies recommends that you configure all supported capabilities (in whatever precedence order is desired) to allow the greatest opportunity for completion cross-platform file transfers using encryption.

In the default configuration listed above, SMA Technologies applies a higher precedence to 3DES/CBC than to AES-128/ECB, although AES‑128 is a more secure algorithm than 3DES. Reducing security risk, 3DES/CBC is preferable because of the ECB property of patterns of plaintext being evident in the ciphertext to eavesdroppers. The difference in the levels of security between 3DES and DES is too great to give DES/CBC a higher precedence than 3DES/ECB.

- Enable encryption when organizational security policies require that file contents be protected in transit.
- Configure supported capabilities in priority order — for example, listing AES-128 combinations before 3DES and DES — to ensure the most secure available algorithm is selected first during negotiation.

## Algorithm comparison

The following table describes the supported algorithms, modes, and their security characteristics as documented for the Unix Agent.

| Algorithm | Description | Security level | Notes |
|---|---|---|---|
| DES | Data Encryption Standard; numeric code 1 | Low — now considered too insecure for most uses | Use only where legacy interoperability requires it. |
| 3DES | Triple-DES; numeric code 2 | Moderate — still offers a reasonable level of security | Acceptable where AES is not available on the remote platform. |
| AES-128 | Advanced Encryption Standard, 128-bit key; numeric code 3 | High — the new standard adopted by the United States government, expected to offer a high level of security for the foreseeable future | Recommended algorithm where supported. |
| ECB mode | Electronic CodeBook; numeric code 100 | Lower — allows multiple instances of plaintext to be revealed in the ciphertext (the plaintext itself is not revealed, only that a pattern exists) | Avoid when pattern concealment is required. |
| CBC mode | Cipher Block Chaining; numeric code 200 | Higher — keeps patterns in the plaintext from appearing in the ciphertext | Preferred mode for most transfers. |
| CTS variant | Ciphertext Stealing; numeric code 10000 | Increases security — makes ciphertext length not always a multiple of the algorithm's block size, hiding this information from eavesdroppers | Add to an algorithm + mode sum to enable. |
| Bitstring-padding variant | Bitstring padding; numeric code 20000 | No effect on security | Alternative to the default padding method; pads with a 1-bit followed by 0-bits. |

A supported capability code is the sum of one algorithm code, one mode code, and one variant code. For example, AES-128/CBC-CTS = 3 + 200 + 10000 = 10203.

## Examples

An agent is configured with encryption REQUIRED, and the supported capabilities list is set to the default:

```

10203,20203,203,10202,20202,202,20103,103,20102,102,10201,20201,201,20101,101

```

When UNIX is the Destination machine, the Agent searches this list from left to right for the first capability that the Server also supports. In this configuration, the Agent attempts AES-128/CBC-CTS (10203) first. If the Server supports AES-128/CBC-CTS, the file is encrypted using AES-128 operating in CBC mode with Ciphertext Stealing. If the Server does not support that combination, the Agent moves to the next entry (AES-128/CBC-Bitstring, 20203), and so on. If no match is found and encryption is REQUIRED, the transfer is not performed and the job fails.

## Glossary

**Supported capability** — A numeric code representing a specific combination of encryption algorithm, mode, and variant supported by an agent installation. The code is the sum of one algorithm value (1 = DES, 2 = 3DES, 3 = AES-128), one mode value (100 = ECB, 200 = CBC), and one variant value (10000 = CTS, 20000 = Bitstring-padding). For example, AES-128/CBC-CTS = 3 + 200 + 10000 = 10203.

**CBC (Cipher Block Chaining)** — An encryption mode, identified by numeric code 200, that keeps patterns in the plaintext from appearing in the ciphertext by chaining each encrypted block to the previous one. Preferred over ECB for most transfers because ECB allows repeated plaintext patterns to be visible in the ciphertext.