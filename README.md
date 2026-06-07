# Japan Trip 2026 · 9 月

家族日本 11 日遊行程表(2026/9/24 – 10/4)。

- **線上版本**: https://edgar0119.github.io/japan-trip-2026-09/
- **路線**: 桃機 → 京都(OMO5 三條, 3 晚)→ 金澤(Dormy Inn)→ 新穗高 / 西穂山荘 → …(規劃中)
- **適用**: 手機優先(`max-width: 560px`)
- **GitHub Pages 部署**: push 到 `main` 即可自動部署

## 檔案結構

| 路徑 | 用途 |
|---|---|
| `index.html` | 行程表(~50KB,外部圖片) |
| `images/` | 部署用的優化圖片(commit) |
| `photos/` | 原圖儲存區,不 commit(`.gitignore`) |
| `scripts/extract-images.py` | 一次性遷移腳本(base64 → 外部) |
| `netlify.toml` | (歷史遺留,目前主要用 GitHub Pages) |

## 加新圖片的工作流

1. 把優化過的 JPEG 直接放進 `images/`(建議 longest-side ≤ 1400,quality 75–80)
2. 在 `index.html` 用 `<img src="images/foo.jpg">` 引用即可,**不要再用 base64**
3. `git add images/foo.jpg index.html && git commit && git push`
4. GitHub Pages 約 30 秒後上線

## 設計來源

完整 design system 沿用 [`japan-trip-2026`](../japan-trip-2026) (5/19–5/31 立山黑部・富士五湖・東京 13 日遊)。
詳細元件 reference 看那邊的 `HANDOFF.md`。

## 本地預覽

```bash
python3 -m http.server 8080
# 開 http://localhost:8080
```

## TODO

- [x] 確認 Day 1–5 路線(京都 / 金澤 / 西穂山荘)
- [ ] 填 9/29 之後行程
- [ ] 確認回程班機
- [ ] 啟用天氣 badge(目前各天 `data-empty`,複製 5 月版 `scripts/update-weather.py` 跑一次即可)
