# 發哥公式日報交件（可攜）

## 目標
平日早上把蛟龍取水 digest 交到：**發哥公式 bot 對話** + **Discord #daily-report**。Alice 聊天只留一句。

## 防失敗原則
1. **優先交件**：若 `/workspace/dragon-water/candidates.csv` 已是當日／最近交易日結果，直接格式化，勿先重掃。
2. Digest ≤ ~500 字；完整報告寫 `out/daily-report.md`。
3. Discord：`scripts/investing/notify_discord.py --file …`（讀 `DISCORD_WEBHOOK_DAILY_REPORT`）。
4. 任一步失敗：短路徑重試一次；仍失敗要明示，不可靜默。

## 補跑指令（本機）
```bash
# 有 candidates 時只交件
python3 scripts/investing/format_daily_report.py -i out/daily-report-input.json -o out/daily-report.md
python3 scripts/investing/notify_discord.py --file out/daily-digest-YYYY-MM-DD.txt
# 再請發哥公式 bot 把 digest SendToUser
```
