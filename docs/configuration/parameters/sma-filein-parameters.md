---
sidebar_label: 'sma_filein Parameters'
title: sma_filein Parameters
description: "Reference for the Unix Agent sma_filein parameter that defines the sleep interval between checks of the MSGIN directory."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_filein parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Reference for the Unix Agent sma_filein parameter that defines the sleep interval between checks of the MSGIN directory.

The following parameters reference the sma_filein setting for the sleep time. This setting controls how frequently the agent checks the MSGIN directory for incoming messages.

### sma_filein_sleep_time

**Default Value**: 5

**Description**:

* Defines the number of seconds for the process sma_filein to wait between checks of the MSGIN directory.
* The value for this parameter must be numeric and greater than zero.


