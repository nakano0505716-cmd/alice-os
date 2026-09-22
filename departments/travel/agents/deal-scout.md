# 甜甜價機票釋出 Agent（原名：甜甜價機票釋出／Travel Deal Scout）

旅遊部底下的**專責小 bot**：掃社群上的即時「甜甜票價」分享，轉成可核對的情報給旅遊助手／使用者。

**Grok Bot 隊友：** 甜甜價機票釋出（id 4935400）

## 定位

- **不是**主比價引擎（那是 Google Flights／Skyscanner／航司官網）  
- **是**情報層：有人貼到超便宜窗時，快速標註並請主追蹤核價  

## 來源

見 `departments/travel/deal-sources.yaml`（含使用者 IG 動態消息帳號＋FB／Threads／PTT）。

## 行為

1. 收集貼文中的：航線、日期彈性、標價、航空、貼文時間、連結  
2. **不把社群標價當成交真相** — 一律交給旅遊助手用 Google Flights／Skyscanner／官網核價；**不發完整比價表**（那是旅遊助手的事）  
3. 命中 watchlist 航線（目前 TPE→東京／大阪／名古屋直飛）或明顯低於 `max_price` 時警報（旅遊 Discord + bot）  
4. 訂票／付款前一定要使用者確認  

## 實作狀態

已開 Grok Bot 隊友；執行層用瀏覽器／公開頁；長期腳本放 `scripts/travel/`。

## 免責

社群情報常過期或廣告；**最終以可下單頁面為準**。
