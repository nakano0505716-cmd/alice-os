# Notifications

Notification Engine 抽象：同一事件可送 ChatGPT 聊天（V0）、Discord、LINE…

## 原則

- Importance Score 決定是否即時打擾（見 ARCHITECTURE.md）  
- Daily digest ≠ Urgent alert  
- Webhook URL／tokens 只放環境變數，見 `.env.example`  
- 通道設計見 `discord-channels.md`

## V0 → V1

| 階段 | Provider |
|------|----------|
| V0 | 聊天室內（執行層轉述） |
| V1 | Discord webhooks（建議優先） |
| Later | LINE Messaging API、Email、Push |
