# 網站設計快速啟動懶人包

> 完整版：[`ai-web-design-resource-map.md`](./ai-web-design-resource-map.md)　互動版：[`atlas/index.html`](../atlas/index.html)

## 三條大原則

1. **AI 負責組裝與變形，Taste 由你決定。** 給 AI 參考來源和規則，不要讓它從零幻想。
2. **80 / 15 / 5。** 80% 穩定資訊架構、15% 品牌視覺、5% 記憶點。炫技效果最多挑一個。
3. **先拆 Design DNA，再寫 Code。** 只丟 Screenshot，AI 只能猜。

---

## 六步上手

| 步驟 | 要做的事 | 工具 | 產出 |
|---|---|---|---|
| 1. Reference | 找 3–5 個喜歡的網站，各自標註「要它的哪一點」 | Land-book、Lapa Ninja、Godly、Mobbin | 參考清單 |
| 2. Design DNA | 把每個參考拆成 8 個維度 | CSS Peeper、ColorZilla、Site Palette | DNA 表 |
| 3. Design Token | 定色彩角色、字級、間距、圓角 | Realtime Colors、OKLCH Picker、Typewolf | `tokens.css` |
| 4. Component | 選元件底座，加 1–2 個記憶點元件 | shadcn/ui、21st.dev、Magic UI、Aceternity UI | 元件清單 |
| 5. AI Agent | 用 Context Prompt 下指令 | Claude Code、Codex、Cursor（+ 21st MCP） | 頁面原型 |
| 6. Visual QA | 對比、響應式、效能 | WebAIM、DevTools、Lighthouse | 上線檢查表 |

### 每一步用到哪幾層

| 步驟 | L1 Inspiration | L2 UX | L3 Foundation | L4 Expressive | L5 Motion | L6 3D | L7 Assets | L8 System |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1. Reference | ● | ● | | | | | | |
| 2. Design DNA | | | | | | | | ● |
| 3. Design Token | | | | | | | ● | ● |
| 4. Component | | | ● | ● | ● | ● | | |
| 5. AI Agent | | | | ● | | ● | | |
| 6. Visual QA | | | | | | | | ● |

---

## Design DNA 八個維度（拆站速查）

| 維度 | 要抄下來的東西 | 範例寫法 |
|---|---|---|
| Layout | Grid、Container Width、Section Rhythm | 12 col / max 1200px / section 間距 120px |
| Typography | Typeface、Scale、Weight、Line Height | H1 56/1.05 600，Body 17/1.6 400 |
| Color | Background / Surface / Text / Accent | 見下方色彩角色 |
| Shape | Radius、Border、Shadow | radius 12，1px border，無陰影 |
| Density | Padding、Whitespace、資訊密度 | card padding 24，鬆 |
| Imagery | Photo / Illustration / 3D / Editorial | 產品 3D render，無人物照 |
| Motion | Hover / Scroll / Transition / Parallax | hover 上浮 2px / 150ms |
| Component | Navbar、Hero、Card、CTA、Footer | 置中 Hero + Bento Feature |

---

## 配色：先定角色再挑色

| Role | 用途 | 檢查 |
|---|---|---|
| Background | 整體 Canvas | — |
| Surface | Card、Panel、Nav | 與 Background 要有可辨識的明度差 |
| Text Primary | 主文字 | 對 Background ≥ 4.5:1 |
| Text Muted | 次要說明 | 對 Surface ≥ 4.5:1 |
| Primary | CTA、品牌行為 | 按鈕文字對 Primary ≥ 4.5:1 |
| Secondary | 次級資訊 | — |
| Accent | 少量焦點 | 用量控制在畫面 5% 以內 |
| Semantic | Success / Warning / Error / Info | 不要跟 Accent 撞色 |
| Border | 分隔與層級 | — |

流程：**Pinterest / Canva 找 Mood → Realtime Colors 套在真實 UI 上驗證 → OKLCH 建 Token → WebAIM 檢查。**

技巧：看 **Lightness** 不看 Hue。Text、Surface、Background 三者明度拉開，階層就出來了。

---

## 技巧清單

- 參考網站只拿「一個點」：A 的 Layout、B 的字體、C 的 Hero 互動。整站照抄就是抄襲。
- 元件底座選一個就好（shadcn/ui），視覺元件只是點綴。
- 動效先用 Motion；只有長頁 Scroll Storytelling 才上 GSAP。
- 3D 先用 Spline；真的需要 Shader / WebGL 才碰 Three.js。
- 圖片用 Unsplash / Pexels 前，確認人物與商標權利。
- 字體先去 Typewolf 看真實網站怎麼配，再到 Google Fonts / Adobe Fonts 取用。
- 看到喜歡的網站：CSS Peeper 拆字體與間距，Site Palette 抽整站色，ColorZilla 補單色。
- 上線前一定跑 WebAIM：一般文字 4.5:1，大字 3:1。

### Demo Site 警報

下面這些同一頁出現三個以上，就該刪：

`3D` `Glow` `Parallax` `Glass` `Particle` `Marquee` `Gradient`

---

## 實戰 Stack

| 環節 | 工具 |
|---|---|
| 視覺探索 | Land-book + Lapa Ninja + Godly |
| UX Research | Mobbin + SaaSFrame |
| Foundation | shadcn/ui |
| 高質感元件 | 21st.dev + Aceternity UI + Magic UI |
| Motion | Motion（大型 Scroll Storytelling 再上 GSAP） |
| 3D | Spline（需要 Shader / WebGL 才用 Three.js） |
| Typography | Typewolf → Google Fonts / Adobe Fonts |
| Color | Pinterest / Canva → Realtime Colors → OKLCH |
| Reverse Engineering | CSS Peeper + ColorZilla + Site Palette |
| Quality Gate | WebAIM + Responsive Test + Performance Test |

---

## 風格配方速查

| 風格 | Reference | 元件 | Motion / 3D | 字體 / 色彩 |
|---|---|---|---|---|
| Apple / 高級科技 | Awwwards + Land-book | shadcn | GSAP + Spline | Typewolf + Realtime Colors |
| AI SaaS | SaaSFrame + Mobbin | shadcn + Magic UI | Motion | Inter / Geist + OKLCH |
| Future / Cyber | Godly | Aceternity + 21st | Three.js / Shader | Dark Neutral + Neon Accent |
| Magazine / Editorial | Land-book + Typewolf | Custom Layout | 少量 Motion | Serif + Grotesk |
| Creative Portfolio | Awwwards + Godly | Custom | GSAP + Three.js | 高對比 Typography |
| 企業顧問 / B2B | Lapa + SaaSFrame | shadcn | 微動效 | Neutral + 單一 Accent |
| 教育 / 內容品牌 | Lapa + Land-book | shadcn + 少量 21st | Rive / Lottie | Editorial Typography |

---

## Context Prompt 範本

把下面這段貼給 Claude Code / Codex / Cursor，替換 `{}`：

```text
你要實作一個 {網站類型} 的 {頁面名稱}。

參考來源（只取指定的部分，不要整站照抄）：
- Layout 參考 {A}：{要的點，例如 12 欄、置中 Hero、Section 間距 120px}
- Typography 參考 {B}：{字體與字級}
- Hero Interaction 採 {C}：{互動描述}
- Component Architecture 用 {D}（例如 shadcn/ui）

Design Token（全部元件必須服從，不得新增顏色）：
--bg: {}; --surface: {}; --text: {}; --muted: {};
--primary: {}; --on-primary: {}; --accent: {}; --border: {};
radius: {}; spacing scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96

限制：
- 記憶點只有一個：{例如 Hero 的 3D 物件}，其餘維持穩定資訊架構
- 文字對比符合 WCAG AA（一般文字 4.5:1）
- 支援 375px 手機寬度，不得水平捲動
```
