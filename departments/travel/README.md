# 旅遊部（Travel Department）

追蹤日本（及一般）行程的機票與住宿價格／空房；價格下跌或出現好訂位窗口時警報。

## 組成

| Agent | Prompt |
|-------|--------|
| Travel Manager | `prompts/departments/travel-manager.md` |

## 本目錄

- `watchlist.example.yaml` — 行程追蹤清單範本（複製為 `watchlist.yaml`；**勿把真實個資／訂位密鑰 commit**）
- `report-templates/price-watch.md` — 每日價格監控報告骨架
- `schedules/daily-watch.yaml` — 平日早上台北時間檢查意圖

## 職責範圍

- 機票：起訖機場、去程／回程日期、艙等、`max_price`
- 住宿：區域、入住／退房日、空房與價位
- 警報：價格跌破門檻、好訂位／好價窗口

## 腳本

`scripts/travel/` — collectors / formatters 佔位（規格在 repo；執行由 Grok Bot 或其他 runtime）

## Discord

目前可複用 `#daily-report` webhook；未來可加專用 travel webhook + bot chat。見 `notifications/discord-channels.md`。

## Portability

規格與範本住在本 repo；**Grok Bot = execution layer**。換執行器不必重寫規則。
