---
sidebar_label: 'FAD Parameters'
title: FAD Parameters
description: "Reference for the Unix Agent FAD parameter that controls whether the File Activity Detection monitor detects files created while the agent was down."
tags:
  - Reference
  - System Administrator
  - Agents
---

# FAD parameters

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?

Reference for the Unix Agent FAD parameter that controls whether the File Activity Detection monitor detects files created while the agent was down.

The following parameters reference the FAD setting for the Unix Agent. This setting controls whether the File Activity Detection monitor detects files that were created while the agent or FAD was down.

## When would you use it?

- When configuring File Activity Detection (FAD) startup behavior
- When determining whether FAD should process files created during agent downtime

### fad_mon_start

**Default Value**: 0

**Description**:

* When set to zero, FAD will detect files created after the agent or FAD have started.
* When set to one, FAD will detect files that were created when the agent or FAD were down.



