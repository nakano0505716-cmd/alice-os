# ✈️ Travel Price Watch — {{date}}

時區：Asia/Taipei (UTC+8)｜來源：Alice Travel Manager

━━━━━━━━━━━━━━━━━━━━

## 總覽

| trip_id | 路線 | 機票狀態 | 住宿狀態 | 一句話 |
|---------|------|----------|----------|--------|
| {{trip_id}} | {{route}} | {{flight_light}} | {{lodging_light}} | {{summary}} |

圖例：🔴 需立刻處理｜🟡 值得關注（跌價／好窗口）｜🟢 無明顯變化

━━━━━━━━━━━━━━━━━━━━

## 機票快照

- 去程：{{depart_date}}｜回程：{{return_date}}
- 艙等：{{cabin}}
- 目前觀察價：{{current_price}} {{currency}}
- 門檻 `max_price`：{{max_price}} {{currency}}
- 較上次：{{price_delta}}

{{flight_notes}}

━━━━━━━━━━━━━━━━━━━━

## 住宿快照

- 區域：{{lodging_area}}
- 入住／退房：{{lodging_checkin}} → {{lodging_checkout}}
- 空房／價位：{{lodging_status}}

{{lodging_notes}}

━━━━━━━━━━━━━━━━━━━━

## ⭐ 今日亮點（只列有用的）

1. {{top_1}}
2. {{top_2}}

━━━━━━━━━━━━━━━━━━━━

## 💡 Travel Manager 結論

**{{manager_conclusion}}**

下次檢查：{{next_check}}
