# Discord 通道草圖

目標伺服器內建議頻道（與 ChatGPT 設計精神一致）：

| Channel | 用途 |
|---------|------|
| `#us-stock` | 美股專家細節與標的動態 |
| `#tw-stock` | 台股專家細節、籌碼／新聞、蛟龍台股清單 |
| `#etf` | ETF 視角（資金流、成分影響） |
| `#macro` | Fed／CPI／宏觀 |
| `#alerts` | 🟠–🔴 即時警報（持倉相關優先） |
| `#daily-report` | 🤖 每日投資報告總包（紅綠燈 + Manager 結論） |

## 每日報告貼文骨架

```text
20:00
🤖 Daily Investment Report
━━━━━━━━━━━━━━
🇺🇸 美股 …
🇹🇼 台股 …
📊 ETF …
🌎 宏觀 …
⭐ 今日最重要：…
💡 AI Manager：…
```

## 警報貼文骨架

```text
🚨 URGENT
標的／事件 …
重要性：🔴
是否影響持倉：是／否
建議：先觀察，不因單一事件追價。
```

Webhook 變數名稱見 repo 根目錄 `.env.example`（勿把真實 URL commit 進來）。
