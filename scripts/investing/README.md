# scripts/investing

可攜腳本：不依賴 Grok Bot，stdlib 即可跑。

## format_daily_report.py

讀 `example_input.json`（或 `--input`），寫出 `out/daily-report.md`（相對 **repo 根目錄**）。

```bash
# 在 repo 根目錄
python3 scripts/investing/format_daily_report.py

# 或指定路徑
python3 scripts/investing/format_daily_report.py \
  --input scripts/investing/example_input.json \
  --output out/daily-report.md
```

無需網路、無第三方套件。


## Discord notify (dual delivery)

```bash
# requires DISCORD_WEBHOOK_DAILY_REPORT in .env or env
python3 scripts/investing/notify_discord.py --file out/daily-report.md
```

Daily report should go to Discord **and** the 發哥公式 bot chat.
