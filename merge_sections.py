"""
merge_sections.py

Merges "## When would you use it?" and "## Why would you use it?" sections
INTO the "## What is it?" section across all Markdown files in docs/.

Rules:
- Only merges the exact headings above (not "## When would you use this section?" etc.)
- When bullets come first, Why bullets second, after the prose body
- Removes the When/Why headings entirely
- Protects content inside fenced code blocks
- Cleans up triple+ consecutive blank lines
- Preserves utf-8 encoding
"""

import os
import re
import sys

DOCS_DIR = r"C:\Users\rweesner\Documents\GitHub\unix-agent-docs\docs"

TARGET_WHAT = "## What is it?"
TARGET_WHEN = "## When would you use it?"
TARGET_WHY  = "## Why would you use it?"


def parse_segments(lines):
    """
    Parse lines into segments: list of (heading, body_lines).
    The first segment may have heading=None (front matter / content before first ##).
    Respects fenced code blocks — ## inside them is NOT treated as a heading.
    """
    segments = []
    current_heading = None
    current_body = []
    in_fence = False
    # Match a true fence line: optional leading spaces, then ``` or ~~~,
    # followed by an optional language tag — NOT an inline snippet that opens
    # AND closes on the same line (e.g. ```code```).
    fence_open_pattern = re.compile(r"^(\s*)(```|~~~)([^`~]*)$")

    for line in lines:
        stripped = line.rstrip("\n")
        if fence_open_pattern.match(stripped):
            in_fence = not in_fence

        if not in_fence and line.startswith("## "):
            # Save previous segment
            segments.append((current_heading, current_body))
            current_heading = line.rstrip("\n")
            current_body = []
        else:
            current_body.append(line)

    # Save last segment
    segments.append((current_heading, current_body))
    return segments


def strip_blank_edges(body_lines):
    """Remove leading and trailing blank lines from a list of lines."""
    lines = list(body_lines)
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    return lines


def rebuild_lines(segments):
    """Reconstruct the full file lines from segments."""
    out = []
    for heading, body in segments:
        if heading is not None:
            out.append(heading + "\n")
        out.extend(body)
    return out


def collapse_blank_lines(lines):
    """Replace 3+ consecutive blank lines with exactly 2."""
    result = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    return result


def merge_file(filepath):
    """
    Process a single file. Returns True if the file was modified, False otherwise.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        original_lines = f.readlines()

    segments = parse_segments(original_lines)

    # Find indices of the three target sections
    what_idx = when_idx = why_idx = None
    for i, (heading, _) in enumerate(segments):
        if heading == TARGET_WHAT:
            what_idx = i
        elif heading == TARGET_WHEN:
            when_idx = i
        elif heading == TARGET_WHY:
            why_idx = i

    # Nothing to do if What is missing, or both When and Why are absent
    if what_idx is None or (when_idx is None and why_idx is None):
        return False

    # Build the merged What body
    what_heading, what_body = segments[what_idx]
    prose = strip_blank_edges(what_body)

    extra_bullets = []
    if when_idx is not None:
        when_bullets = strip_blank_edges(segments[when_idx][1])
        if when_bullets:
            extra_bullets.extend(when_bullets)

    if why_idx is not None:
        why_bullets = strip_blank_edges(segments[why_idx][1])
        if why_bullets:
            if extra_bullets:
                extra_bullets.append("\n")  # blank line separator between blocks
            extra_bullets.extend(why_bullets)

    # Compose the new What body
    if prose and extra_bullets:
        new_what_body = prose + ["\n"] + extra_bullets + ["\n"]
    elif prose:
        new_what_body = prose + ["\n"]
    else:
        new_what_body = extra_bullets + ["\n"]

    # Build a new segment list, skipping When/Why, replacing What body
    new_segments = []
    skip_indices = set(filter(lambda x: x is not None, [when_idx, why_idx]))
    for i, (heading, body) in enumerate(segments):
        if i in skip_indices:
            continue
        if i == what_idx:
            new_segments.append((heading, new_what_body))
        else:
            new_segments.append((heading, body))

    new_lines = rebuild_lines(new_segments)
    new_lines = collapse_blank_lines(new_lines)

    # Only write if content actually changed
    if new_lines == original_lines:
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return True


def main():
    modified = []
    for root, dirs, files in os.walk(DOCS_DIR):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for filename in sorted(files):
            if not filename.lower().endswith(".md"):
                continue
            filepath = os.path.join(root, filename)
            if merge_file(filepath):
                rel = os.path.relpath(filepath, DOCS_DIR)
                modified.append(rel)

    print(f"Files modified: {len(modified)}")
    for rel in modified:
        print(f"  {rel}")


if __name__ == "__main__":
    main()
