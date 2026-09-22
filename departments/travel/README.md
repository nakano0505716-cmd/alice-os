# 旅遊部（Travel Department）

追蹤日本（及一般）行程的機票與住宿價格／空房；價格下跌或出現好訂位窗口時警報。

## 組成

| Agent | Prompt | 職責 |
|-------|--------|------|
| 旅遊助手（Travel Manager） | `prompts/departments/travel-manager.md` | 航線 watchlist 比價與住宿追蹤 |
| 甜甜價機票釋出（已開 bot；原名甜甜價機票釋出） | `prompts/departments/travel-deal-scout.md` | Threads／Facebook 等社群即時甜甜票價情報 |

## 機票資訊來源（優先序）

1. **Google Flights** — 比價主來源  
2. **Skyscanner** — 交叉比價／日曆視圖  
3. **航空公司官網**（長榮／華航／星宇、ANA／JAL 等）— 確認艙等、行李、最終價  
4. Web 搜尋 — 只作交叉檢查，不當唯一報價  

**禁止捏造價格。** 單一截圖不當長期真相；追蹤要重查。

## 住宿資訊來源（優先序）

1. Booking.com / Hotels.com（或指定通路）  
2. Airbnb（整套房）  
3. 品牌／飯店官網（促銷核對）

## 本目錄

- `watchlist.example.yaml` — 行程追蹤清單範本（複製為 `watchlist.yaml`；**勿把真實個資／訂位密鑰 commit**）
- `report-templates/price-watch.md` — 每日價格監控報告骨架
- `schedules/daily-watch.yaml` — 平日早上台北時間檢查意圖
- `agents/deal-scout.md` — 社群甜價小 bot 規格（Threads／FB）
- `deal-sources.yaml` — 公開甜價來源清單
- `watchlist.yaml` — 本機追蹤清單（gitignore；範本見 example）

## Discord

- 旅遊警報：`DISCORD_WEBHOOK_TRAVEL`（與投資 `#daily-report` 分開）  
- 雙軌：旅遊助手對話 + 旅遊 Discord  

## Portability

規格與範本住在本 repo；**Grok Bot = execution layer**。換執行器不必重寫規則。
