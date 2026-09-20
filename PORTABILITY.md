# Portability — Non-negotiable

Alice 可以換大腦、換執行器；**不能把規格只活在某一個 Bot 裡**。

## 兩層分工

1. **Source of truth**＝使用者擁有的 **Alice Repository**（本目錄；之後 push 到 GitHub/Origin）。  
2. **Execution layer**＝目前的 **Grok Bot Alice**（orchestrator、routines、specialist bots）。它必須讀寫本 repo 內的 artifacts。

> **Grok Bot = execution layer；本 repo = source of truth。**

## Department 交付物（portable）

每個部門應包含：

| 路徑 | 內容 |
|------|------|
| `prompts/` | Agent 人設與 Manager 規則 |
| `departments/<name>/` | watchlists、report templates、alert rules、formulas |
| `schedules/` | cron／意圖描述（人類可讀，執行器可解析） |
| `scripts/` | collectors & formatters——**可在 Grok Bot 外執行** |

## 新功能檢查清單

加功能前先問：

> **If Grok Bot disappeared tomorrow, can this still run from the repo + a scheduler + a notifier?**

若答案是「不行、規則只在聊天記憶裡」→ **先寫進本 repo 再實作**。

## 通知獨立化

- V0：聊天室內通知可接受  
- 目標：Discord / LINE webhook 等獨立通道（見 `notifications/`）  
- Notification Engine 抽象化；Provider 可插拔  

## Secrets

- 永不 commit API keys / webhook URL / tokens  
- 使用 `.env`（本機／執行器），範本見 `.env.example`  
- `.gitignore` 已排除 `.env`、`out/` 等  

## 可替換執行器

理論上任何能讀本 repo 的 runtime 都可接上：Grok Bot、Codex cloud、GitHub Actions、VPS cron、n8n……  
換執行器時改的是 **誰跑**，不是 **規則住哪裡**。
