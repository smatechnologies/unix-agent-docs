---
sidebar_label: 'Configuration'
title: Unix Agent configuration
description: "Overview of the configuration steps required to set up the Unix Agent, including the control script, configuration file, and root profile."
tags:
  - Conceptual
  - System Administrator
  - Agents
---

Agent configuration includes modification of the agent Control Script, modification of the agent configuration file, and configuration of the root profile. For information on configuring the agent Control Script, refer to [Updating the agent Control Script](updating-lsam-control-script). The initial execution of the agent configuration program, which is automatically run during the agent installation, creates the Unix Agent configuration file lsam.conf. The lsam.conf resides in directory "```$LSAM_ROOT/config/<SMA_LSAM_INSTANCE>/```". Except as noted in section "Hidden agent Configuration Parameters", do not directly modify lsam.conf. Use the agent configuration program to make all modifications to the agent's configuration. For more information on Hidden agent Configuration Parameters, refer to [Hidden agent Configuration Parameters](../configuration/parameters/hidden-parameters).

Beyond the core configuration file, you can configure TLS-secured communication between the agent and OpCon/SAM, define black list and white list rules to control which users are permitted to run jobs, run multiple independent agent instances on a single machine, and configure the agent to start and stop automatically during system boot and shutdown.

:::info Note

Do not directly modify lsam.conf. Use the agent configuration program to make all modifications to the agent's configuration.

:::

## When would you use it?

Refer to this page when:

- You are setting up the Unix Agent for the first time and need to understand which configuration areas to address and in what order.
- You are troubleshooting a configuration issue and need to identify which file or program controls a specific behavior, such as TLS security, user access rules, or time zone settings.
- You are planning to run multiple agent instances on a single machine and need an overview of all configuration components before diving into individual procedures.

## Why would you use it?

- Agent configuration spans multiple files and programs; a single overview helps you locate the correct configuration area without searching through unrelated documentation.
- Understanding the relationship between the agent Control Script, `lsam.conf`, and supplementary configuration areas (TLS, security, multiple instances, automatic startup) reduces the risk of applying changes in the wrong file or the wrong order.

## Configuration areas

| Area | What it controls | Primary file | Where to go |
|---|---|---|---|
| Agent configuration file | Core job-handling parameters (maximum concurrent jobs, user impersonation method, health monitoring, job statistics, and privilege settings) | `lsam.conf` | [Agent configuration file](./lsam-configuration-file.md) |
| Agent configuration parameters | Detailed reference for all parameters stored in `lsam.conf`, including `max_number_of_jobs_to_run`, `allowed_privileged_runs`, `monitor_LSAM_health`, and `LSAM_0_255` | `lsam.conf` | [Agent configuration parameters](./parameters/lsam-configuration-parameters.md) |
| TLS security | Encrypted communication between the agent and OpCon/SAM and JORS; certificate creation and `lsam.conf` entries for `use_TLS_SAM`, `lsam_pem_file`, and `lsam_private_key_file` | `lsam.conf` | [UNIX TLS security](./unix-tls-security.md) |
| Security configuration | Black list and white list rules that control which users (by gid/uid) are permitted to run regular and file transfer jobs | `lsam.conf` | [Security configuration options](./security-configuration-options.md) |
| Running multiple agents | Environment variables and installation steps for running multiple agent instances simultaneously on one machine, each with its own `$SAM_SOCKET` and `$SMA_LSAM_INSTANCE` | N/A | [Running multiple agents](./running-multiple-lsams.md) |
| Automatic startup | Symbolic links to `init.d` and `rc<#>.d` directories that cause the agent to start and stop automatically during system boot and shutdown | OS init scripts | [Automatic startup configuration](./automatic-startup-configuration.md) |

## Examples

:::tip Example

A Unix Agent installation uses the following configuration structure:

- The agent Control Script (`lsam3100`) is located in `$LSAM_ROOT/bin/` and sets `LSAM_ROOT=/usr/local/lsam`, `SAM_SOCKET=3100`, and `SMA_LSAM_INSTANCE=prod`.
- The `lsam.conf` file resides in `$LSAM_ROOT/config/prod/` and is managed exclusively through the agent configuration program.
- TLS is enabled by setting `use_TLS_SAM=1` and providing `lsam_pem_file` and `lsam_private_key_file` paths in `lsam.conf`.
- A black list entry in `lsam.conf` prevents the root user (uid=0) from running regular jobs through the agent.

:::

:::tip Example

A site running two agent instances on a single host uses separate control scripts (`lsam3100` for general users and `lsam3200` for critical jobs), each with its own `SMA_LSAM_INSTANCE` value (`general` and `critical`). The corresponding `lsam.conf` files reside in `$LSAM_ROOT/config/general/` and `$LSAM_ROOT/config/critical/` respectively.

:::

## Glossary

**agent Control Script** — The shell script (for example, `lsam3100`) located in `$LSAM_ROOT/bin/` that sets environment variables and starts, stops, and reports the status of the agent. It is created by the `install_lsam` script and should not be manually edited unless adjusting variable values after installation.

**agent configuration program** — The interactive program used to create and modify `lsam.conf`. It is automatically run during installation and is the only supported method for changing configuration parameters stored in `lsam.conf`.

**lsam.conf** — The agent configuration file stored in `$LSAM_ROOT/config/<SMA_LSAM_INSTANCE>/`. It stores all core job-handling, security, and TLS parameters for the agent. It must not be edited directly; use the agent configuration program instead.

**$LSAM_ROOT** — An environment variable that specifies the root directory of the agent's installation, containing the `bin/`, `config/`, and `log/` subdirectories.

**$SMA_LSAM_INSTANCE** — An environment variable that identifies the instance-specific subdirectory within `$LSAM_ROOT/config/` where the agent's configuration and data files reside. It allows multiple agent instances to coexist under the same `$LSAM_ROOT`.
