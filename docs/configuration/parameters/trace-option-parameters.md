# Trace Option Parameters

The following parameters reference the trace settings for troubleshooting the UNIX LSAM.

:::caution

Always leave the following flags set to zero unless otherwise instructed by SMA Technologies. Specifying non-zero values may result in creation of very large trace files as well as erratic behavior.

:::

### DISP_trace

**Default Value**: 0

**Description**:

* Enables/Disables tracing of communication and processing steps from the LSAM (via process 'sma_disp') to the SAM.
* If set to zero, tracing does not occur.
* If set to non-zero, tracing occurs.
* Trace file name is "sma_disp.trace".

### LSAM_trace

**Default Value**: 0

**Description**:

* Enables/Disables tracing of communication and processing steps internal to the LSAM, specifically, the process named 'sma_lsam'.
* If set to zero, tracing does not occur.
* If set to non-zero, tracing.
* Trace file name is "sma_lsam.trace".

### JORS_FT_trace

**Default Value**: 0

**Description**:

* Enables/Disables tracing of communication and processing steps related to JORS and SMAFT activities.
* If set to zero, tracing does not occur.
* If set to non-zero, tracing occurs.
* Trace file name is "sma_JORS.trace" for the JORS and FT Server, and "SMAFTAgent.trace" for the FT Agent.

### RM_trace

**Default Value**: 0

**Description**:

* Enables/Disables tracing of communication and processing steps related to Resource Monitor (SMA_RM) activities.
* If set to zero, tracing does not occur.
* If set to non-zero, tracing occurs.
* Trace file name is "sma_RM.trace".

### FAD_trace

**Default Value**: 0

**Description**:

* Enables/Disables tracing of communication and processing steps related to the File Activity Daemon (FAD) activities.
* If set to zero, tracing does not occur.
* If set to non-zero, tracing occurs.
* Trace setting applies to all FAD processes started with the LSAM.
* Trace file name is "sma_FAD.trace".


