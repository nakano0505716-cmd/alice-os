# 投資部（Investment Department）

Alice OS 第一個落地部門。

## 組成

| Agent | Prompt |
|-------|--------|
| Investing Manager | `prompts/departments/investing-manager.md` |
| US / TW / ETF / Macro | `prompts/departments/*-agent.md` |
| 發哥公式／蛟龍取水 | `prompts/departments/fage-formula.md` + `formulas/dragon-water.md` |

## 本目錄

- `watchlist.example.yaml` — 追蹤清單範本（複製為 `watchlist.yaml`，勿 commit 真實私密持倉若不想公開）  
- `report-templates/` — 每日報告與警報骨架  
- `schedules/daily-report.yaml` — 部門排程意圖  
- `formulas/dragon-water.md` — 量化規則  

## 腳本

`scripts/investing/format_daily_report.py`：stdlib only，讀 example JSON → `out/daily-report.md`。

## Discord

見 `notifications/discord-channels.md`。
