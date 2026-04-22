---
title: Formatting the Control File
description: "Guidelines and examples for formatting SMA FAD Control Files, including whitespace handling, comment syntax, and recommended layout for readability."
tags:
  - Procedural
  - Reference
  - System Administrator
  - Agents
---

# Formatting the Control File

**Theme:** Configure  
**Who Is It For?** System Administrator

## What is it?
Guidelines and examples for formatting SMA FAD Control Files, including whitespace handling, comment syntax, and recommended layout for readability.

The formatting of elements is not important to the daemon; however, SMA Technologies recommends the files be laid out for easiest readability. Carriage returns, line feeds, and non-significant spaces are optional and are ignored. Use a pound symbol (#) to "comment out" a line.

:::info Note 

Spaces in the data portion of an element are important and are considered part of the data for SMA FAD to interpret.
 
:::

- When creating a new Control File and you want to lay out elements across multiple lines so the configuration is easier to read and maintain.
- When you need to temporarily disable a specific line in a Control File — for example, to suppress an event or exclude a directory — without deleting the content.
- When troubleshooting a Control File and you want to isolate individual record blocks by commenting out lines to narrow the scope of active configuration.
- When reviewing or auditing a Control File and you want to confirm that spaces within data values are intentional, since non-significant whitespace is ignored but data-portion spaces are preserved.

:::tip Example 

The following example shows identical, valid sets of elements in a different layout:

```

<id1><elt1>a</elt1><elt2>b</elt2></id1>

- or -

<id1>
<elt1>a</elt1>
<elt2>b</elt2>
</id1>

```

:::

## How to implement it

Before editing a Control File, confirm the following:

- The Control File already exists in `LSAM_ROOT/fad/<SMA_LSAM_INSTANCE>/control/` or you are creating a new one in that directory.
- You have write access to the Control File location.
- You have identified which elements to lay out across multiple lines or which lines to comment out.

To apply formatting to a Control File, complete the following steps:

1. Open the Control File in a standard text editor (for example, vi).
2. Add carriage returns, line feeds, or spaces between elements as needed to improve readability. These characters are ignored by the daemon and do not affect processing.
3. To comment out a line, place a `#` as the first non-blank character on that line. The entire line is ignored by the daemon.
4. Verify that any spaces within data values — the content between opening and closing element tags — are intentional, as the daemon treats those spaces as part of the data.
5. Save the file.
6. Restart the daemon from the `<LSAM_Root_Directory>` directory by issuing `bin/stop_fad` followed by `bin/start_fad` so the updated Control File is recognized.

## Exception handling

**A commented-out line does not take effect after restart** → The `#` character must be the first non-blank character on the line. If the `#` is preceded by any spaces or tabs, the line is not treated as a comment and the daemon attempts to parse it. Review the line and ensure the `#` is in the first non-blank position.

**Spaces within a data value produce unexpected behavior** → Spaces inside element tags — for example, `<filemask> report.txt</filemask>` — are treated as part of the data value, not whitespace to be ignored. If the daemon is not matching the expected file or directory, open the Control File and confirm that no unintended leading or trailing spaces appear within data elements.