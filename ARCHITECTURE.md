# Alice — Architecture

Design authority：使用者 ChatGPT 分享 + 架構圖（2026-09-20/21）+ 本 repo 為 source of truth。

## Goal

Private AI OS：Manager 協調 specialist departments；scheduled tasks 產出 daily digests 與 alerts；通知到達手機，不必綁死單一 chat app。

## Product layers

```
Alice (OS)
  AI Router → Astra/ChatGPT primary / Gemini secondary / future plugins
  Departments → Sub-departments → Agents
  Watchlist + Memory
  Tasks → Scheduler → Notification (chat now → Discord/LINE later)
  Codex / cloud agents = Alice Engineer（把規格蓋進本 repo）
```

## Core modules（憲法級）

1. **AI Manager（Alice）** — 唯一主要入口  
2. **Memory** — 長期偏好、持倉、心法  
3. **Agents** — 部門專家  
4. **Watchlist** — 跨部門「幫我長期注意」  
5. **Tasks** — 一次性工作  
6. **Scheduler** — 何時自動跑  
7. **Notification** — 何時找使用者（Importance Score）  
8. **Model Router** — Primary / Secondary / Plugin，不寫死單一廠商  

## Portability（NON-NEGOTIABLE）

見 [PORTABILITY.md](./PORTABILITY.md)。摘要：

- 本 **Alice Repository** = source of truth  
- **Grok Bot** = 目前 execution layer，必須 sync 回本 repo  
- 每個 Department 以 portable artifacts 交付：`prompts/`、`departments/<name>/`、`schedules/`、`scripts/`

## Domains

投資 | 記帳 | 日文 | 旅遊 | 遊戲 | 購物 | 保健 | 工作 |（可追加，例如運動）

## Investment Department V1（先做）

```
💰 投資部
├── 🇺🇸 美股 Agent
├── 🇹🇼 台股 Agent
├── 📊 ETF Agent
├── 🌎 Macro Agent
└── 🔎 選股策略
    └── 🐉 發哥公式／蛟龍取水（見 departments/investing/formulas/）
```

輸出：

- Daily Investment Report（紅綠燈、只講重要的、Manager 結論）  
- Urgent alerts（持倉相關、高重要性）

Discord 通道草圖：`#us-stock` `#tw-stock` `#etf` `#macro` `#alerts` `#daily-report`

## Runtime vs Engineering

| Track | 內容 |
|-------|------|
| **Runtime（現在）** | Grok Bot：Alice + teammate bots + routines，規格持續寫回本 repo |
| **Engineering** | GitHub → 本 repo → Codex/cloud agent：Backend → DB → Agent framework → Watchlist → API → Web UI → tests → deploy |

## Notification importance（設計精神）

| 等級 | 行為 |
|------|------|
| 🟢 1–2 | 不即時通知 / 僅進每日報告 |
| 🟡 3 | 每日報告突出 |
| 🟠 4 | Discord 即時 |
| 🔴 5 | 🚨 立即通知 |

報告精神：**今天值得注意的只有 N 件** + **Manager 結論**（例如「今天不用操作」）。
