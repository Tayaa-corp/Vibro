#!/usr/bin/env python3
"""PreToolUse hook: block writes to protected paths and content that looks like a secret.

Claude Code sends the tool call as JSON on stdin. Exit code 2 blocks the call and
the message on stderr is shown to the model so it can correct itself.
"""

import json
import os
import re
import sys

PROTECTED_PREFIXES = ("data/",)

SECRET_PATTERNS = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key"),
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"), "GitHub token"),
    (re.compile(r"sk-[A-Za-z0-9_-]{20,}"), "API key"),
    (
        re.compile(
            r"(?i)\b(password|passwd|secret|api[_-]?key|token)\b\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"
        ),
        "hard-coded credential",
    ),
]


def block(reason: str) -> None:
    print(f"Blocked by .claude/hooks/guard.py: {reason}", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    event = json.load(sys.stdin)
    tool_input = event.get("tool_input", {})

    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    rel = os.path.relpath(os.path.abspath(path), project_dir) if path else ""

    if any(rel.startswith(prefix) for prefix in PROTECTED_PREFIXES):
        block(f"{rel} is client data and is read-only. Copy it into a test fixture instead.")

    chunks = [tool_input.get("content", ""), tool_input.get("new_string", ""), tool_input.get("new_source", "")]
    chunks += [edit.get("new_string", "") for edit in tool_input.get("edits", [])]
    text = "\n".join(c for c in chunks if c)

    for pattern, label in SECRET_PATTERNS:
        if pattern.search(text):
            block(f"content looks like a {label}. Read secrets from the environment or the vault, never from code.")

    sys.exit(0)


if __name__ == "__main__":
    main()
