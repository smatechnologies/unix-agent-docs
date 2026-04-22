---
sidebar_label: 'Dispatcher Configuration Parameters'
title: Dispatcher Configuration Parameters
description: "Reference for Unix Agent dispatcher configuration parameters, including the message timeout setting that controls TCP/IP socket behavior when SMANetCom communication is delayed."
tags:
  - Reference
  - System Administrator
  - Agents
---

# Dispatcher configuration parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for Unix Agent dispatcher configuration parameters, including the message timeout setting that controls TCP/IP socket behavior when SMANetCom communication is delayed.

The following parameters reference the dispatcher setting for the agent's internal communication. This setting controls the timeout behavior of the TCP/IP socket when SMANetCom communication is delayed.

- When troubleshooting communication issues related to the agent dropping or resetting TCP/IP socket connections

### msg_timeout_in_seconds

**Default Value**: 600

**Description**:

* Defines the timeout in seconds for the agent to wait for a message from SMANetCom.
* If the timeout is exceeded, the dispatcher closes and reopens the TCP/IP socket.
