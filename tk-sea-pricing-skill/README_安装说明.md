# TikTok Shop 东南亚定价计算器 — 安装说明

这是一个 Claude Code 的 Skill，帮你算 TikTok Shop 东南亚五国（马来西亚/菲律宾/泰国/越南/新加坡）的商品定价、利润和毛利率。

## 怎么装

1. 解压本压缩包，得到 `tk-sea-pricing` 文件夹（确保文件夹名就叫 `tk-sea-pricing`）。
2. 把整个文件夹放到你的 Claude Code skills 目录：
   - macOS / Linux：`~/.claude/skills/tk-sea-pricing`
   - Windows：`C:\Users\你的用户名\.claude\skills\tk-sea-pricing`
3. 重启 Claude Code（或新开一个会话）。

装好后，目录结构应该是：
```
~/.claude/skills/tk-sea-pricing/
├── SKILL.md
├── README_安装说明.md
├── references/
│   ├── formulas.md
│   ├── logistics.md
│   ├── verified-rates.md
│   ├── *.pdf（官方佣金费率存档）
│   └── data/
│       ├── 东南亚跨境物流运费价格表.xlsx
│       └── 海外仓价卡汇总260515.xlsx
└── scripts/read_xlsx.py
```

## 怎么用

直接跟 Claude 说话即可，例如：
- “帮我算一下这个产品在马来西亚 TK 上能赚多少”
- “TK 东南亚定价，菲律宾，成本 8 块”
- “算一下毛利率”

Claude 会自动收集必填项（售价、成本、重量、物流方式等），实时核验汇率，再出一张完整的利润明细表。

## 注意事项（数据时效）

- **物流价表**：包内自带，版本为 2024/4/15（马来西亚 sheet）。如官方调价，请用新价表替换 `references/data/` 下的对应文件。
- **佣金/手续费/税率**：部分为参考表快照值，可能过时；Skill 会在计算时尽量联网核验，并对未核验项明确标注。
- 利润测算**不含货损/退货成本**，请自行按退货率再打折评估。

—— 自用工具，分享请保留本说明。
