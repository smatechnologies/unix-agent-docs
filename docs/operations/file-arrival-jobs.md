---
sidebar_label: 'File Arrival Jobs'
title: File Arrival Jobs
description: "Reference for the Unix Agent File Arrival job type, which monitors a directory for files matching a pattern and reports success when a matching, stable file is found within a defined time window."
tags:
  - Reference
  - System Administrator
  - Agents
---

# File Arrival jobs

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
The File Arrival job type monitors a directory for files matching a defined pattern and reports success when a matching, stable file is found within a defined time window.

A File Arrival job replaces polling scripts that check for the existence of a file before triggering downstream processing. The agent monitors the target directory directly, waits for a matching file to stop changing (stabilize), and reports the result back to OpCon. Dependent jobs do not start until the File Arrival job finishes with a success status.

- Use a File Arrival job when a downstream OpCon job must wait for a file to be delivered before it can run.
- Use a File Arrival job when a file may arrive at irregular times within a known daily window and you want OpCon to start processing as soon as the file is ready.
- Use a File Arrival job when you need to verify that a file has fully landed (stabilized) rather than just appeared — for example, when a large file is being written incrementally.
- Use a File Arrival job when files may land in subdirectories under a root drop location and you need a recursive search.

## How it works

1. The agent receives the File Arrival job definition from OpCon, including the directory path, file pattern, time window, and stabilization time.
2. The agent begins monitoring the specified directory for files that match the pattern.
3. When a matching file is found, the agent verifies that:
   - The file's creation date falls within the defined time window (start time offset and end time offset from the schedule date).
   - The file remains unchanged for at least the configured stabilization time, confirming it is fully written.
   - The job's run-as user has read permission on the file.
4. When all conditions are met, the agent reports success to the SAM and records the matched filename.
5. If no matching file is found before the end time, the agent reports a failure.

## Job definition parameters

These parameters are configured in OpCon's job definition for the UNIX machine when the job action is set to **File Arrival**:

| Parameter | Description |
|---|---|
| **Directory path / file pattern** | The directory to monitor. May include wildcards in the filename component to match a pattern (for example, `/data/inbound/feed_*.csv`). |
| **Start time offset** | The number of hours after midnight of the schedule date when monitoring begins. A value of `0` starts monitoring at midnight. |
| **End time offset** | The number of hours after midnight of the schedule date when monitoring ends. The job fails if no file is found by this time. |
| **Stabilization time** | The number of seconds a matching file must remain unchanged before the agent considers it fully written and reports success. Use a non-zero value when files are delivered by an ongoing write process. |
| **Search subdirectories** | When set, the agent recursively searches subdirectories under the specified path in addition to the directory itself. |

:::info Note

The file pattern supports wildcards. The file's creation timestamp is compared against the schedule date and offset window — files created before the start offset or after the end offset are not considered valid matches.

:::

## Exit codes

| Code | Condition |
|---|---|
| `0` | Success — a matching, stable file was found within the time window and the run-as user has read permission. |
| `1` | No matching file was found within the time window, or a matching file was found but the run-as user does not have read permission on it. |
| `2` | The specified directory does not exist or is not accessible. The system error is captured and reported in the agent log. |
| `3` | A file matching the pattern was found, but its creation date falls outside the defined time window. |
| `4` | Internal system error. |
| `-1` | Generic error, or the end time is earlier than the start time in the job definition. |
| `128 + signal` | The job was terminated by a system signal (for example, `SIGKILL` produces exit code `137`). |

:::info Note

When a File Arrival job succeeds, OpCon populates the following Job Instance properties with the matched file's details. These can be referenced in downstream jobs using the `[[JI.$ARRIVED FILE NAME]]` token syntax:

| Property | Value |
|---|---|
| `JI.$ARRIVED FILE NAME` | Full path and file name (e.g., `/data/inbound/feed_20240506.csv`) |
| `JI.$ARRIVED SHORT FILE NAME` | File name and extension only (e.g., `feed_20240506.csv`) |
| `JI.$ARRIVED BASE FILE NAME` | File name without extension (e.g., `feed_20240506`) |
| `JI.$ARRIVED FILE EXTENSION` | Extension only (e.g., `.csv`) |
| `JI.$ARRIVED FILE PATH` | Directory path only (e.g., `/data/inbound`) |

:::

## Exception handling

**File Arrival job fails with exit code `2`** — The directory path specified in the job definition does not exist on the agent machine, or the run-as user does not have access to it. — Verify that the directory exists and that the user the job runs as has read and execute permissions on the path.

**File Arrival job fails with exit code `1` after the time window expires** — No file matching the pattern was placed in the directory before the end time offset. — Confirm that the upstream process that delivers the file ran successfully. Consider widening the time window or adjusting the end time offset if the delivery schedule varies.

**File Arrival job succeeds but immediately — the stabilization time is 0** — When stabilization time is `0`, the agent reports success as soon as a matching file appears, even if it is still being written. — Set stabilization time to a value (in seconds) that exceeds the typical time the upstream process takes to finish writing the file.

**File Arrival job fails with exit code `3`** — A file matching the pattern exists, but it was created outside the defined window. — The file may be a leftover from a previous day's run. Verify that the upstream process created the file on the expected schedule date and adjust the time window offsets if needed.

## Glossary

**Stabilization time** — The number of seconds a matching file must remain unchanged (no size or modification change) before the File Arrival job considers it fully delivered and reports success.

**Time window** — The range of valid file arrival times, defined as start and end offsets in hours from midnight of the OpCon schedule date. Files created outside this range are not accepted as valid matches.

**File pattern** — The filename portion of the monitored path, which may include wildcard characters to match multiple files. The agent reports success on the first file it finds that satisfies all criteria.
