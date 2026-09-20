#!/usr/bin/env python3
"""Format Alice investing daily report from JSON. Stdlib only; no network."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def repo_root() -> Path:
    # scripts/investing/this_file → repo root = parents[2]
    return Path(__file__).resolve().parents[2]


def fmt_dw_line(item: dict, market: str) -> str:
    sym = item.get("symbol", "?")
    name = item.get("name", "")
    score = item.get("score", "")
    vol = item.get("vol_contr", "")
    gain = item.get("prior_gain_pct", "")
    dist = item.get("dist_ma60_pct", "")
    macd = "MACD水上金叉" if item.get("macd_golden_above_zero") else ""
    note = item.get("note", "")
    parts = [
        f"**{sym}**" + (f" ({name})" if name else ""),
        f"score={score}",
        f"vol_contr={vol}",
        f"prior_gain={gain}%",
        f"dist_MA60={dist:+.1f}%" if isinstance(dist, (int, float)) else f"dist_MA60={dist}",
    ]
    if macd:
        parts.append(macd)
    line = ", ".join(parts)
    if market == "TW" and "close" in item:
        close = item["close"]
        line += f" | close=NT${close} | 1股≈NT${round(close)} | 10股≈NT${round(close * 10):,}"
    if note:
        line += f" — {note}"
    return f"- {line}"


def build_dragon_block(dw: dict | None) -> str:
    if not dw:
        return "_今日未跑蛟龍取水掃描。_"
    lines = [f"As-of: **{dw.get('as_of', 'n/a')}**", "", "### 🇹🇼 台股（零股友善優先）"]
    tw = dw.get("tw_odd_lot") or []
    if not tw:
        lines.append("_無_")
    else:
        for it in tw:
            lines.append(fmt_dw_line(it, "TW"))
    lines.extend(["", "### 🇺🇸 美股（全部命中摘要）"])
    us = dw.get("us_all") or []
    if not us:
        lines.append("_無_")
    else:
        for it in us:
            lines.append(fmt_dw_line(it, "US"))
    lines.append("")
    lines.append("_Pattern-match screen only; not investment advice._")
    return "\n".join(lines)


def render(data: dict) -> str:
    tops = data.get("top_items") or []
    while len(tops) < 3:
        tops.append("（無）")
    top_lines = "\n".join(f"{i}. {t}" for i, t in enumerate(tops[:3], 1))
    body = f"""# 📊 Daily Investment Report — {data.get('date', '')}

時區：{data.get('timezone', 'Asia/Taipei')} (UTC+8)｜來源：Alice Investing Manager

━━━━━━━━━━━━━━━━━━━━

## 總覽（紅綠燈）

| 區塊 | 狀態 | 一句話 |
|------|------|--------|
| 🇺🇸 美股 | {data.get('us_light', '🟢')} | {data.get('us_summary', '')} |
| 🇹🇼 台股 | {data.get('tw_light', '🟢')} | {data.get('tw_summary', '')} |
| 📊 ETF | {data.get('etf_light', '🟢')} | {data.get('etf_summary', '')} |
| 🌎 宏觀 | {data.get('macro_light', '🟢')} | {data.get('macro_summary', '')} |

圖例：🔴 必須注意｜🟡 值得關注｜🟢 無需處理

━━━━━━━━━━━━━━━━━━━━

## ⭐ 今日最重要（只列有用的）

{top_lines}

━━━━━━━━━━━━━━━━━━━━

## 持倉／Watchlist 關聯

{data.get('holdings_impact', '_未設定_')}

━━━━━━━━━━━━━━━━━━━━

## 🐉 蛟龍取水掃描（若有）

{build_dragon_block(data.get('dragon_water'))}

━━━━━━━━━━━━━━━━━━━━

## 💡 Alice／Investment Manager 結論

**{data.get('manager_conclusion', '')}**

明天留意：{data.get('tomorrow_watch', '')}
"""
    return body.rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    root = repo_root()
    default_in = root / "scripts" / "investing" / "example_input.json"
    default_out = root / "out" / "daily-report.md"

    p = argparse.ArgumentParser(description="Format Alice daily investment report (stdlib only).")
    p.add_argument("--input", "-i", type=Path, default=default_in)
    p.add_argument("--output", "-o", type=Path, default=default_out)
    args = p.parse_args(argv)

    if not args.input.is_file():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 1

    data = json.loads(args.input.read_text(encoding="utf-8"))
    text = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
