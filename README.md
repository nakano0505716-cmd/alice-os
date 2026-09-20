# Alice Private AI OS

**Alice** 是使用者的私人 AI 作業系統（Private AI OS）：總管協調各部門專家、排程產出每日摘要與警報，並把通知送到手機——不必綁死在單一聊天 App。

> 像 Jarvis 之於 Tony Stark，Alice 是你的私人 AI 管家、情報中心與 AI 團隊管理者。

## Portability（不可妥協）

| 角色 | 定位 |
|------|------|
| **本 Repository** | **Source of truth**（規格、prompts、模板、公式、腳本） |
| **Grok Bot Alice** | 目前的 **execution layer**（編排、例行、專屬 bots） |

Grok Bot 必須讀寫本 repo 內的產物。問任何新功能前先問：

> **如果明天 Grok Bot 消失，這套能否靠「本 repo + scheduler + notifier」繼續跑？**

詳見 [PORTABILITY.md](./PORTABILITY.md)、[ARCHITECTURE.md](./ARCHITECTURE.md)。

## 目前優先：投資部 V1

專家：美股 / 台股 / ETF / 宏觀（+ **發哥公式／蛟龍取水** 技術篩選）

輸出：每日投資報告 + 緊急警報

通知目標（Discord）：`#us-stock` `#tw-stock` `#etf` `#macro` `#alerts` `#daily-report`

## 目錄一覽

```
alice-os/
├── README.md / ARCHITECTURE.md / PORTABILITY.md
├── docs/design-chatgpt-share.md
├── prompts/                    # Alice 與部門 agent 人設
├── departments/investing/      # watchlist、報告模板、公式、排程描述
├── scripts/investing/          # 可離線跑的格式化 stub
├── schedules/                  # 全域排程意圖
├── notifications/              # Discord / LINE 通道設計
├── .env.example
└── .gitignore
```

## 快速驗證 stub（無需網路、stdlib only）

```bash
cd /workspace/alice-os   # 或本機 clone 後的根目錄
python3 scripts/investing/format_daily_report.py
# → 寫出 out/daily-report.md
```

## 領域藍圖（可擴充）

投資 | 記帳 | 日文 | 旅遊 | 遊戲 | 購物 | 保健 | 工作 |（未來：運動…）

每個部門必須可再拆 **Sub-department → Agents**。

## 免責

本 repo 內篩選規則與報告範例僅供個人研究；**非投資建議**。
