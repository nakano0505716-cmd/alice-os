# Schedules

全域／跨部門排程意圖。執行器（Grok Bot routine、cron、GitHub Actions、n8n…）負責真正觸發；**本目錄只描述「要做什麼、何時做」**。

## 約定

- 時區預設 **Asia/Taipei (UTC+8)**  
- 部門細部排程也可放在 `departments/<name>/schedules/`  
- 變更排程必須 commit 進本 repo（portability）

## 目前

| ID | 說明 | 詳細 |
|----|------|------|
| investing-daily-report | 平日 20:00 投資日報 | `departments/investing/schedules/daily-report.yaml` |

## 未來示例（未啟用）

- 盤中警報輪詢（高 importance → `#alerts`）  
- 保健服用提醒、旅遊票價 watchlist 等其他部門
