---
sidebar_label: 'sma_cronmon'
title: sma_cronmon — Cron Monitor
description: "Reference for the sma_cronmon component, which monitors the system cron log for user-defined search strings and forwards matching OpCon events to the SAM."
tags:
  - Reference
  - System Administrator
  - Agents
---

# sma_cronmon — Cron monitor

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
The sma_cronmon component monitors the system cron log for user-defined search strings and forwards matching OpCon events to the SAM.

The cron monitor allows the Unix Agent to react to cron-activated processes by watching the system cron log. When a configured search string matches an entry in the cron log, sma_cronmon forwards a paired OpCon event to the SAM through the sma_disp process.

- Use sma_cronmon when you need OpCon to react to a cron job that fires on a schedule you cannot or prefer not to replicate inside OpCon.
- Use sma_cronmon when a cron job produces a predictable log entry and you want to trigger a downstream OpCon job, threshold update, or console alert in response.
- sma_cronmon is optional. If cron-based event triggering is not required, leave it deactivated. For instructions on deactivating optional components, refer to [Deactivating agent Components](../../reference/system-modification/deactivating-lsam-components).

## Configuration file

sma_cronmon reads all cron search strings and events from the `cronmon.conf` file located at:

```
<LSAM_ROOT>/config/<SMA_LSAM_INSTANCE>/cronmon.conf
```

Each line in `cronmon.conf` pairs a regular expression search string with an OpCon event string using the `#e#` separator:

```
<regular expression search string>#e#<event string>
```

:::info Note

An event file placed in the MSGIN directory can only contain one event. The same constraint does not apply to `cronmon.conf` — multiple search/event pairs may appear, one per line.

:::

## Cron log locations

sma_cronmon searches for the cron log in the following locations, in order:

1. `/var/log/cron`
2. `/var/cron/log`
3. `/var/adm/cron/log`

The first location that exists is used. If none of these paths exist on your system, sma_cronmon cannot monitor the cron log.

## cronmon.conf syntax

Each line uses the format:

```
<regular expression search string>#e#<event string>
```

| Field | Description |
|---|---|
| `<regular expression search string>` | A POSIX regular expression matched against each new line written to the cron log |
| `#e#` | Literal separator between the search string and the event string |
| `<event string>` | A valid OpCon event string, including user login ID and event password, forwarded to the SAM when the search string matches |

:::tip Example

The following `cronmon.conf` file defines two entries. The first triggers a threshold update when `/dev/null` appears in the cron log. The second triggers a different threshold update when `jobtest` appears.

```
/dev/null#e#$THRESHOLD:SET,thresholdnull,1
jobtest#e#$THRESHOLD:SET,findtest,3
```

:::

For a complete list of valid OpCon event strings, refer to [OpCon Events — Introduction](https://help.smatechnologies.com/opcon/core/events/introduction) in the OpCon online help.

## How sma_cronmon works

1. On startup, sma_cronmon reads `cronmon.conf` to load all search/event pairs.
2. sma_cronmon monitors the cron log file for new entries.
3. When a new cron log entry is written, sma_cronmon tests it against each regular expression in `cronmon.conf`.
4. When a match is found, the paired event string is passed to the sma_disp process.
5. sma_disp forwards the event to the SAM.

:::info Note

sma_cronmon is an optional component. It starts automatically when the agent starts if `cronmon.conf` is present and the component is not deactivated. For instructions on starting and stopping the agent, refer to [Operating the agent](../operating-the-lsam).

:::

## Exception handling

**sma_cronmon starts but no events are forwarded to the SAM** — The regular expression in `cronmon.conf` does not match the format of entries in the cron log on this system. — Review the actual cron log to confirm the exact text produced by the cron job, then adjust the regular expression to match. Use a simple literal substring first to confirm the match before adding regex metacharacters.

**sma_cronmon does not start** — The cron log does not exist in any of the three search locations (`/var/log/cron`, `/var/cron/log`, `/var/adm/cron/log`). — Confirm the cron log location on your system and create a symbolic link at one of the expected paths if necessary.

**Events are forwarded but SAM rejects them** — The event string in `cronmon.conf` is not formatted as a valid OpCon event, or the user login ID or event password is incorrect. — Verify the event syntax against the OpCon Events documentation. Confirm that the user login ID and event password embedded in the event string are valid.

## Glossary

**cronmon.conf** — The configuration file for sma_cronmon, located in `<LSAM_ROOT>/config/<SMA_LSAM_INSTANCE>/`. Each line pairs a POSIX regular expression with an OpCon event string using the `#e#` separator.

**sma_cronmon** — The optional Unix Agent daemon that monitors the system cron log and forwards configured OpCon events to the SAM when a matching cron log entry is detected.
