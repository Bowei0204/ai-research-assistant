# paper_helper/markdown_writer.py
import os
import re
from datetime import datetime
from paper_helper.strengths_and_weakness import analyze_abstract_strengths_and_weaknesses

def save_markdown(title, authors, published, abstract_en, abstract_zh, arxiv_id, strengths_weakness=None):
    cleaned_title = title.replace('\n', ' ').replace('\r', ' ').strip()
    safe_title = re.sub(r'[\\/:*?"<>|]', '', cleaned_title)[:80].replace(' ', '_')
    filename = f"{published}_{safe_title}.md"
    filepath = os.path.join("output", "paper_notes", filename)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # 自動優缺點分析
    strengths_weakness_text = analyze_abstract_strengths_and_weaknesses(abstract_en) if abstract_en else "[無法產生優缺點分析]"

    content = f"""
# 📄 {title}

- **作者**：{authors}
- **發表日期**：{published}
- **arXiv ID**：{arxiv_id}

---

## 🧠 Abstract（英文）

{abstract_en if abstract_en else '[無資料]'}

## 🌏 Abstract（繁體翻譯）

{abstract_zh if abstract_zh else '[翻譯失敗或無資料]'}

---

{strengths_weakness_text}

---
（由 AI 技術研究助手自動產生）
"""

    print("🚀 Markdown 寫入內容如下：")
    print(content)
    print(f"🗂 儲存完整路徑：{os.path.abspath(filepath)}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath
