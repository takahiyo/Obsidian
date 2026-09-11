# 📚 スクラップ MOC (Map of Content)

> 💡 **全自動追従中（Dataview）**: この目次ノートはリアルタイムに自動更新されています。
> ノートを新規追加・削除・編集すると、手動作業ゼロで一覧やリンク集計が全自動反映されます。

---

## 🔍 リアルタイム検索 & カテゴリマップ (完全自動分類集計)

```dataviewjs
const { MarkdownRenderer } = require("obsidian");

const pages = dv.pages('"Notion/倉庫/スクラップ"').where(p => p.file.name !== "スクラップ MOC");

const authorMap = {};
const circleMap = {};
const tagMap = {};

const linkRegex = /\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]/g;

for (let p of pages) {
    if (!p.file || !p.file.path) continue;
    const content = await dv.io.load(p.file.path);
    if (!content) continue;
    
    const lines = content.split('\n');
    for (let line of lines) {
        let matchCategory = null;
        if (line.includes("**作者**")) {
            matchCategory = authorMap;
        } else if (line.includes("**サークル**")) {
            matchCategory = circleMap;
        } else if (line.includes("**ジャンル・タグ**") || line.includes("**ジャンル**") || line.includes("**タグ**")) {
            matchCategory = tagMap;
        }
        
        if (matchCategory) {
            let match;
            linkRegex.lastIndex = 0;
            while ((match = linkRegex.exec(line)) !== null) {
                const target = match[1].trim();
                if (!target) continue;
                if (!matchCategory[target]) matchCategory[target] = [];
                if (!matchCategory[target].some(item => item.path === p.file.path)) {
                    matchCategory[target].push({ name: p.file.name, path: p.file.path });
                }
            }
        }
    }
}

// リアルタイム検索バーの生成
const searchContainer = dv.el("div", "");
const input = document.createElement("input");
input.type = "text";
input.placeholder = "🔍 作者名・サークル名・タグ名・作品名でリアルタイム絞り込み...";
input.style.cssText = "width: 100%; padding: 10px 14px; margin-bottom: 16px; border-radius: 8px; border: 1px solid var(--background-modifier-border); background: var(--background-primary); color: var(--text-normal); font-size: 14px; outline: none;";
searchContainer.appendChild(input);

const resultContainer = dv.el("div", "");

async function renderAll(query) {
    resultContainer.empty();
    const q = query.toLowerCase();
    
    function buildCategoryMd(title, map, emoji) {
        const sorted = Object.keys(map).sort((a, b) => map[b].length - map[a].length);
        let categoryLines = [];
        
        for (let key of sorted) {
            const keyMatches = !q || key.toLowerCase().includes(q);
            
            const matchingWorks = map[key].filter(item => {
                if (!q) return true;
                if (keyMatches) return true;
                return item.name.toLowerCase().includes(q);
            });
            
            if (matchingWorks.length === 0) continue;
            
            const worksStr = matchingWorks.map(item => `[[${item.name}]]`).join(", ");
            categoryLines.push(`- **[[${key}]]** (${matchingWorks.length}作品) ➔ ${worksStr}`);
        }
        
        if (categoryLines.length === 0) return "";
        
        return `### ${emoji} ${title}\n` + categoryLines.join("\n") + "\n\n";
    }
    
    let fullMd = "";
    fullMd += buildCategoryMd("作者一覧", authorMap, "👤");
    fullMd += buildCategoryMd("サークル一覧", circleMap, "👥");
    fullMd += buildCategoryMd("ジャンル・タグ一覧", tagMap, "🏷️");
    
    if (!fullMd.trim()) {
        fullMd = "*(該当する作者・タグ・作品が見つかりませんでした)*";
    }
    
    const tempEl = document.createElement("div");
    resultContainer.appendChild(tempEl);
    await MarkdownRenderer.renderMarkdown(fullMd, tempEl, dv.current().file.path, dv.component);
}

input.addEventListener("input", (e) => renderAll(e.target.value.trim()));
renderAll("");
```

---

## 📑 全作品インデックス (50音順 / 完全自動更新)

```dataview
LIST
FROM "Notion/倉庫/スクラップ"
WHERE file.name != "スクラップ MOC"
SORT file.name ASC
```

---

## 🔗 作品・関連リンク全表 (完全自動更新)

```dataview
TABLE file.outlinks AS "関連リンク・タグ"
FROM "Notion/倉庫/スクラップ"
WHERE file.name != "スクラップ MOC"
SORT file.name ASC
```
