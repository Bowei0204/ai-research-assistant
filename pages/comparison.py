# pages/comparison.py
import streamlit as st
import os
import re
import pandas as pd

# 📂 歷史筆記資料夾
NOTE_DIR = "output/paper_notes"

# 讀取所有 Markdown 檔案
def load_note_files():
    return [f for f in os.listdir(NOTE_DIR) if f.endswith(".md")]

# 從檔案中提取欄位
def extract_note_info(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    def extract(pattern, default=""):
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        return match.group(1).strip() if match else default

    title = extract(r"# 📄 (.+)")
    authors = extract(r"\*\*作者\*\*：(.+)")
    abstract = extract(r"## 🧠 Abstract（英文）\n\n(.+?)(?=\n##|\n---|\Z)")
    pros_cons = extract(r"(## ✅ 優點.+?## ⚠️ 缺點 / 限制.+?)(?=\n#+|\n---|\Z)")

    # 根據 radio 選項做簡單過濾
    if view_option == "只看優點":
        pros_cons = re.search(r"## ✅ 優點\s*(.*?)(?=\n##|$)", pros_cons, re.DOTALL)
        pros_cons = pros_cons.group(1).strip() if pros_cons else "[找不到優點]"
    elif view_option == "只看缺點":
        pros_cons = re.search(r"## ⚠️ 缺點.+?\n(.*?)(?=\n##|$)", pros_cons, re.DOTALL)
        pros_cons = pros_cons.group(1).strip() if pros_cons else "[找不到缺點]"


    return {
        "標題": title,
        "作者": authors,
        "方法摘要": abstract,
        "優點與限制": pros_cons
    }

# 🌟 Streamlit UI
st.set_page_config(page_title="技術比較表產生器", layout="wide")
st.title("📊 技術比較表產生器")

note_files = load_note_files()

if not note_files:
    st.warning("⚠️ 尚無任何筆記，請先產生論文筆記。")
    st.stop()

selected_files = st.multiselect("📂 選擇要比較的論文筆記：", note_files)
# ✅ 額外過濾選項
view_option = st.radio("📋 顯示內容選擇：", ["全部", "只看優點", "只看缺點"], horizontal=True)


if selected_files:
    data = []
    for fname in selected_files:
        path = os.path.join(NOTE_DIR, fname)
        data.append(extract_note_info(path))

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    if st.button("📥 匯出比較表 (Markdown)"):
        md_output = "# 技術比較表"
        for i, row in df.iterrows():
            md_output += f"## {row['標題']}"
            md_output += f"- **作者**：{row['作者']}"
            md_output += f"- **方法摘要**：{row['方法摘要']}"
            md_output += f"- **優點**：{row['優點']}"
            md_output += f"- **缺點**：{row['缺點']}"

        output_path = os.path.join("output", "comparison_table.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_output)
        st.success(f"✅ 已匯出為 Markdown 檔案！路徑：{output_path}")
