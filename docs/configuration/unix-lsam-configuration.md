---
sidebar_label: 'Configuration'
---

LSAM configuration includes modification of the LSAM Control Script, modification of the LSAM configuration file, and configuration of the root profile. For information on configuring the LSAM Control Script, refer to [Updating the LSAM Control Script](updating-lsam-control-script). The initial execution of the LSAM configuration program, which is automatically executed during the LSAM installation, creates the UNIX LSAM configuration file lsam.conf. The lsam.conf resides in directory "```$LSAM_ROOT/config/<SMA_LSAM_INSTANCE>/```". Except as noted in section "Hidden LSAM Configuration Parameters", lsam.conf should not be directly modified, i.e., all modifications to the LSAM's configuration should be made with the LSAM configuration program. For more information on Hidden LSAM Configuration Parameters, refer to [Hidden LSAM Configuration Parameters](../configuration/parameters/hidden-parameters).

:::info Note

The lsam.conf should not be directly modified, i.e., all modifications to the LSAM's configuration should be made with the LSAM configuration program.

:::