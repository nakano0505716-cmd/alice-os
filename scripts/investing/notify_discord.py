#!/usr/bin/env python3
"""Post a markdown/text daily report to Discord webhook. Dual-delivery companion to bot chat."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def load_webhook() -> str:
    env = os.environ.get("DISCORD_WEBHOOK_DAILY_REPORT", "").strip()
    if env:
        return env
    for path in (
        Path("/home/box/.config/alice-os/discord.env"),
        Path(__file__).resolve().parents[2] / ".env",
    ):
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("DISCORD_WEBHOOK_DAILY_REPORT=") and not line.endswith("="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("DISCORD_WEBHOOK_DAILY_REPORT not set")


def post(content: str, username: str = "Alice · 發哥公式") -> None:
    # Discord limit ~2000 chars per message
    chunks = []
    while content:
        chunks.append(content[:1900])
        content = content[1900:]
    url = load_webhook()
    for i, chunk in enumerate(chunks):
        payload = {"content": chunk, "username": username}
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "AliceOS/1.0"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status not in (200, 204):
                    raise SystemExit(f"Discord HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            raise SystemExit(f"Discord HTTP {e.code}: {body}") from e


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--file", type=Path, help="Read message from file")
    p.add_argument("--text", help="Inline message text")
    args = p.parse_args()
    if args.file:
        text = args.file.read_text(encoding="utf-8")
    elif args.text:
        text = args.text
    else:
        text = sys.stdin.read()
    text = text.strip()
    if not text:
        raise SystemExit("empty message")
    post(text)
    print("ok", file=sys.stderr)


if __name__ == "__main__":
    main()
