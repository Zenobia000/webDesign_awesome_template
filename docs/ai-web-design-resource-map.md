# AI 時代的網站設計資源地圖

> 從靈感、UI 元件、3D 動效到字體與配色。
> 互動版：[`atlas/index.html`](../atlas/index.html)　懶人包：[`quick-start.md`](./quick-start.md)

AI 讓「把網站做出來」變得很容易，也讓網站更容易長得一模一樣。

拉開差距的已經不是會不會寫 HTML、React 或 Tailwind CSS，而是有沒有一套自己的 **視覺參考系統（Visual Reference System）**：

- 去哪裡找版型
- 去哪裡拆 UX
- 去哪裡找元件
- 什麼東西值得交給 AI 重構
- 哪些視覺效果只適合拿來點綴

AI 最適合做「組裝與變形」，不適合憑空決定 Taste。

---

## 0. 八層模型

資源依用途拆成八層，由上往下越來越接近實作：

```
Inspiration → UX Pattern → UI Foundation → Expressive UI → Motion → 3D → Visual Assets → Design System
```

| 層 | 回答的問題 | 對應資源 |
|---|---|---|
| Inspiration | 這個網站可以長什麼樣子？ | Awwwards、Godly、Land-book、Lapa Ninja |
| UX Pattern | 使用者怎麼完成任務？ | Mobbin、SaaSFrame、Page Flows |
| UI Foundation | 基礎元件從哪來？ | shadcn/ui、Figma Community |
| Expressive UI | 品牌感與記憶點從哪來？ | 21st.dev、Aceternity UI、Magic UI |
| Motion | 東西怎麼動？ | Motion、GSAP、LottieFiles、Rive |
| 3D | 需要立體或 WebGL 嗎？ | Spline、Three.js Examples |
| Visual Assets | 照片、影片、字體 | Unsplash、Pexels、Typewolf、Google Fonts、Adobe Fonts |
| Design System | 顏色、對比、Token | Color Hunt、Canva Colors、Adobe Color、Realtime Colors、ColorZilla、Site Palette、CSS Peeper、OKLCH Picker、WebAIM |

---

## 1. 網站設計資源地圖

### 1.1 整站靈感（Inspiration）

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [Awwwards](https://www.awwwards.com/) | 高端品牌、藝術型網站、3D、互動敘事 | 找「可能性」，不要直接照抄 |
| [Godly](https://godly.website/) | 新潮 Web、Creative Developer、實驗性視覺 | Hero、轉場、特殊 Layout |
| [Land-book](https://land-book.com/) | 商業網站、Landing Page | 找實際可落地的排版 |
| [Lapa Ninja](https://www.lapa.ninja/) | Landing Page、完整長頁 | 研究 Hero → CTA → Footer 的敘事；收錄逾 7,300 個網站、15,000 張完整頁面截圖 |

### 1.2 產品 UX（UX Pattern）

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [Mobbin](https://mobbin.com/) | 真實產品 UI、Flow、Screen Pattern | 登入、Onboarding、Pricing、Dashboard 等流程；資料庫超過 62 萬個已上線畫面 |
| [SaaSFrame](https://www.saasframe.io/) | SaaS Landing、產品介面、Email Flow | B2B、AI SaaS、Dashboard；可切 desktop / mobile 與流程研究 |
| [Page Flows](https://pageflows.com/) | UX Interaction Flow | 看使用者怎麼一步步完成任務，而不只是單一畫面 |

### 1.3 基礎 UI 元件（UI Foundation）

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [shadcn/ui](https://ui.shadcn.com/) | Button、Dialog、Form、Table、Sidebar | React / Next.js 的 Design System 基底；元件直接進入自己的 codebase |
| [Figma Community](https://www.figma.com/community) | UI Kit、Wireframe、Design System | 從設計端取得正式元件與模板；也有 Material、Apple 等 UI Kits |

### 1.4 AI 原生與視覺型元件（Expressive UI）

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [21st.dev](https://21st.dev/) | Hero、Cards、Shader、Navbar、AI Chat UI | 適合 Claude Code / Codex / Cursor；元件同時提供 Code 與 Prompt，並支援 MCP |
| [Aceternity UI](https://ui.aceternity.com/) | 3D Card、Beam、Parallax、Spotlight、Globe | 快速做出高質感 Landing Page；React / Tailwind / Motion 元件與 Blocks |
| [Magic UI](https://magicui.design/) | Bento、Beam、Text Effect、Marquee、Particles | 比 Aceternity 更偏乾淨的 SaaS / AI Landing 視覺 |

### 1.5 動效（Motion）

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [Motion](https://motion.dev/) | Hover、Drag、Scroll、Micro-interaction | React 動效首選；文件特別支援 AI Agent 使用 |
| [GSAP](https://gsap.com/) | 高階 Scroll Animation、Pin、Timeline | Apple 式長頁、產品展示、Scroll storytelling |
| [LottieFiles](https://lottiefiles.com/) | Loader、Icon Animation、Illustration Motion | 輕量動態素材，網站與 App 都好整合 |
| [Rive](https://rive.app/) | Interactive Illustration、Mascot、互動動畫 | 支援 State Machine（狀態機），動畫能回應使用者操作 |

### 1.6 3D

| 網站 | 最適合找什麼 | 使用方式 |
|---|---|---|
| [Spline](https://spline.design/) | Hero 3D、Interactive Object、產品展示 | 非工程師也能快速產 3D；支援 2D/3D、AI Agent 與 MCP |
| [Three.js Examples](https://threejs.org/examples/) | WebGL、Shader、Particle、3D 世界 | 需要真正客製化時才進這層；官方範例本身就是大型技術參考庫 |

### 1.7 視覺素材（Visual Assets）

| 網站 | 類型 | 最適合找什麼 | 使用方式 |
|---|---|---|---|
| [Unsplash](https://unsplash.com/) | 照片 | 品牌 Hero、大圖、Lifestyle Photography | 可廣泛商用，但仍要確認人物、商標等權利 |
| [Pexels](https://www.pexels.com/) | 照片＋影片 | Landing Page 背景與影片 | 背景影片特別好用 |
| [Typewolf](https://www.typewolf.com/) | 字體靈感 | 真實網站字體、Font Pairing | 研究別人怎麼把字體放進品牌 |
| [Google Fonts](https://fonts.google.com/) | 免費 Web Font | 開源字體 | 安全、載入容易 |
| [Adobe Fonts](https://fonts.adobe.com/) | 商業字體 | 高質感字體 | Adobe 訂閱生態，Web Project 可直接用 |

### 1.8 配色與無障礙（Design System）

| 網站 | 用途 | 使用方式 |
|---|---|---|
| [Color Hunt](https://colorhunt.co/) | 快速找配色 | 最快的 Moodboard；有 UI Palette 分類 |
| [Canva Colors](https://www.canva.com/colors/) | 圖片抽色、Color Wheel | 非設計師最好上手 |
| [Adobe Color](https://color.adobe.com/) | Color Harmony、圖片抽色 | 系統化建立品牌色 |
| [Realtime Colors](https://www.realtimecolors.com/) | 實際測配色 | 直接把 Palette 套在網站上看 |
| [ColorZilla](https://www.colorzilla.com/chrome/) | 吸網站顏色 | Eyedropper、整頁 Color Analyzer |
| [Site Palette](https://palette.site/) | 一鍵抽整站 Palette | 分析整頁並匯出色盤 |
| [CSS Peeper](https://csspeeper.com/) | 拆 Design DNA | 一次看到 Color、Font、Spacing、Asset |
| [OKLCH Picker](https://oklch.com/) | 色彩工程 | 系統化建立色階，做 Design Token |
| [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Accessibility | 一般文字 WCAG AA 至少 4.5:1 |

---

## 2. 配色要設計的是角色，不是五個 HEX

常見流程：Pinterest → 找一張圖 → 吸五個顏色 → 丟進網站。這適合找 Mood，不適合直接變成 Design System。

先決定 **色彩角色（Color Roles）**：

| Role | 功能 |
|---|---|
| Background | 整體 Canvas |
| Surface | Card、Panel、Navigation |
| Text Primary | 主文字 |
| Text Muted | 次要說明 |
| Primary | 主要品牌行為與 CTA |
| Secondary | 次級資訊 |
| Accent | 少量視覺焦點 |
| Semantic | Success / Warning / Error / Info |
| Border | 元件層級與分隔 |

Realtime Colors 比 Color Hunt 多走一步的地方，是它逼你把顏色放回真實 UI。它的模型就是 Neutral Background / Text + Primary + Secondary + Accent。

### 2.1 Color Harmony 只是起點

| Harmony | 特性 |
|---|---|
| Monochromatic | 單一色相，不同明度與彩度 |
| Analogous | 鄰近色，視覺安靜 |
| Complementary | 色環相對兩端，天然高對比 |
| Split Complementary | 主色＋補色兩側，對比較柔和 |
| Triadic | 色環等分三色，活潑但難控制 |

### 2.2 在 UI 裡，Lightness 比 Hue 重要

同樣都是藍色，如果文字、Card、Background 的明度太接近，資訊階層照樣會消失。所以建立 Design Token 時，用 **OKLCH** 分開管理 Lightness、Chroma、Hue，會比 HSL 可靠。

### 2.3 Accessibility Gate

| 對象 | WCAG 2.2 AA 最低對比 |
|---|---|
| 一般文字 | 4.5 : 1 |
| 大型文字（≥ 24px，或 ≥ 18.66px 粗體） | 3 : 1 |

---

## 3. AI 時代的網站設計 Workflow

過去：

```
設計師 → Figma → 工程師 → Code
```

現在：

```
Reference → Design DNA → Design Token → Component Library → AI Agent → Visual QA
```

關鍵差異：**不要只丟 Screenshot 給 AI**。先把喜歡的網站拆成 Design DNA：

| 維度 | AI 應取得的資訊 |
|---|---|
| Layout | Grid、Container Width、Section Rhythm |
| Typography | Typeface、Scale、Weight、Line Height |
| Color | Background / Surface / Text / Accent |
| Shape | Radius、Border、Shadow |
| Density | Padding、Whitespace、Information Density |
| Imagery | Photo / Illustration / 3D / Editorial |
| Motion | Hover / Scroll / Transition / Parallax |
| Component | Navbar、Hero、Card、CTA、Footer |

拆完再讓 Claude Code、Codex、Cursor 這類 Agent 實作。

21st.dev 值得注意的原因也在這裡：元件同時提供 Code 與 Prompt，又能透過 MCP 讓 Agent 搜尋元件。Component Library 不再只是工程師的 Dependency，也會成為 AI 的「Taste Context」。

---

## 4. 不同網站風格的資源組合

| 風格 | Reference | 元件 | Motion / 3D | 字體 / 色彩 |
|---|---|---|---|---|
| Apple / 高級科技 | Awwwards + Land-book | shadcn | GSAP + Spline | Typewolf + Realtime Colors |
| AI SaaS | SaaSFrame + Mobbin | shadcn + Magic UI | Motion | Inter / Geist + OKLCH |
| Future / Cyber | Godly | Aceternity + 21st | Three.js / Shader | Dark Neutral + Neon Accent |
| Magazine / Editorial | Land-book + Typewolf | Custom Layout | 少量 Motion | Serif + Grotesk |
| Creative Portfolio | Awwwards + Godly | Custom | GSAP + Three.js | 高對比 Typography |
| 企業顧問 / B2B | Lapa + SaaSFrame | shadcn | 微動效即可 | Neutral + 單一 Accent |
| 教育 / 內容品牌 | Lapa + Land-book | shadcn + 少量 21st | Rive / Lottie | Editorial Typography |

### 80 / 15 / 5 法則

成熟的網站通常是：

| 比例 | 內容 |
|---|---|
| 80% | 穩定的資訊架構 |
| 15% | 品牌視覺 |
| 5% | 記憶點 |

3D、Glow、Parallax、Glass、Particle、Marquee、Gradient 全部放進去，結果不是高級，是 Demo Site。

---

## 5. 實戰 Stack

從零做一個有品牌感、又能讓 AI Coding 快速實作的網站，工具可以縮到這套：

| 環節 | 工具 |
|---|---|
| 視覺探索 | Land-book + Lapa Ninja + Godly |
| UX Research | Mobbin + SaaSFrame |
| Foundation | shadcn/ui |
| 高質感元件 | 21st.dev + Aceternity UI + Magic UI |
| Motion | Motion；需要大型 Scroll Storytelling 再上 GSAP |
| 3D | Spline；真的需要 Shader / WebGL 才用 Three.js |
| Typography | Typewolf → Google Fonts / Adobe Fonts |
| Color | Pinterest / Canva 找 Mood → Realtime Colors 驗證 → OKLCH 建 Token |
| Reverse Engineering | CSS Peeper + ColorZilla + Site Palette |
| Quality Gate | WebAIM + Responsive Test + Performance Test |

這樣 AI 不必從零「幻想設計」。你給它的是一句明確的指令：

> Layout 參考 A、Typography 參考 B、Hero Interaction 採 C、Component Architecture 用 D，但全部必須服從這一套 Design Token。

這就是 AI 時代的 Web Design Context Engineering。
