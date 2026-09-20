# Design pointer — ChatGPT 股票追蹤分享

完整對話整理見：`/workspace/xiaozuo-os/chatgpt-share-stock-tracking.md`  
來源分享：https://chatgpt.com/share/6ab0189b-0148-83e8-ab6a-4c280cb8c542

本檔只保留 **Alice 必須遵守的設計精神**（不是全文複本）。

## 核心架構精神

```
你 → AI Manager（Alice）→ 美股/台股/ETF/Macro 專家
         → 彙整／去重／重要性判斷
         → 每日報告 + 異常警報
         → Discord / LINE（手機通知）
```

不要做成「開 10 個聊天室讓 AI 互聊」。應做成：

**Agent + Scheduler + Data + Notification**

## 報告要像這樣（只講有用的）

> **今天值得你注意的事情只有 3 件**  
> 🔴 … 🟡 … 🟢 …  
> **我的結論：今天不用操作。**  
> 明天需要注意：…

## 持倉關聯 > 市場播報

一般 Bot：「NVDA 跌 5.2%。」  
Alice：「🔴 **你的 QQQ 可能受影響** … 目前無需改動定期投入計畫。」

## Importance Score

🟢 不通知 → 🟡 報告突出 → 🟠 即時 → 🔴 🚨 立即

## Discord 通道草圖

`#us-stock` `#tw-stock` `#etf` `#macro` `#alerts` `#daily-report`

## 版本節奏（精神）

- V1：能每天產出報告並通知  
- V2：多專家 → Manager  
- V3：持倉記憶、警報、去重、指令擴充  

## 與本 repo 的關係

ChatGPT 對話是靈感與規格來源；**落地規格以本 Alice Repository 為準**，避免只活在聊天紀錄裡。
