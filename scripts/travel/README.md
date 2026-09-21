# scripts/travel

可攜腳本佔位：規格在 repo；執行層（Grok Bot 或其他 runtime）負責實際抓價與通知。

目標：不依賴單一 Bot；stdlib / 明確依賴即可在 repo 外跑。

## 規劃中

| 腳本（未來） | 用途 |
|--------------|------|
| `collect_flight_prices.py` | 依 watchlist 抓機票觀察價 |
| `collect_lodging.py` | 住宿空房／價位快照 |
| `format_price_watch.py` | 讀 JSON → `out/travel-price-watch.md` |
| `notify_discord.py` | 複用 `DISCORD_WEBHOOK_DAILY_REPORT`，或未來 `DISCORD_WEBHOOK_TRAVEL` |

## 通知意圖

- **V0**：Discord `#daily-report` webhook（與投資部共用）
- **未來**：專用 travel webhook + bot chat；大幅跌價可進 `#alerts`

## 本地驗證（待 stub 落地後）

```bash
# 在 repo 根目錄
python3 scripts/travel/format_price_watch.py \
  --input scripts/travel/example_input.json \
  --output out/travel-price-watch.md
```

Secrets 放 `.env`（見根目錄 `.env.example`）；永不 commit webhook URL。
