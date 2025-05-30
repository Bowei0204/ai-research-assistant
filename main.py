#main.py
import streamlit as st
from paper_helper.arxiv_fetcher import fetch_arxiv_metadata
from paper_helper.translator import translate_text
from paper_helper.markdown_writer import save_markdown
from paper_helper.strengths_and_weakness import analyze_abstract_strengths_and_weaknesses  # ✅ NEW
import os

st.set_page_config(page_title="AI 技術研究助手", layout="wide")
st.title("AI 技術研究助手")

arxiv_input = st.text_input("請輸入 arXiv 論文連結或 ID：")

if arxiv_input:
    with st.spinner("正在取得論文資料..."):
        metadata = fetch_arxiv_metadata(arxiv_input)

    if metadata:
        st.success("成功取得論文資料！")

        st.subheader("📄 論文資訊")
        st.markdown(f"**標題：** {metadata['title']}")
        st.markdown(f"**作者：** {metadata['authors']}")
        st.markdown(f"**發表日期：** {metadata['published']}")
        st.markdown("---")

        st.subheader("🧠 Abstract（原文）")
        st.markdown(metadata['abstract'])

        st.subheader("🌏 Abstract（繁體中文翻譯）")
        translated = translate_text(metadata['abstract'])
        st.markdown(translated)

        # ✅ 優缺點分析
        st.subheader("📋 優點與限制分析")
        with st.spinner("分析中..."):
            sw_result = analyze_abstract_strengths_and_weaknesses(metadata['abstract'])
        st.markdown(sw_result)

        if st.button("💾 匯出 Markdown 筆記"):
            filepath = save_markdown(
                metadata['title'],
                metadata['authors'],
                metadata['published'],
                metadata['abstract'],
                translated,
                arxiv_input.strip(),
                strengths_weakness=sw_result  # ✅ 傳入優缺點內容
            )
            st.success("✅ 筆記已儲存！")
            st.markdown(f"📂 [點我下載筆記 📄]({filepath})")
            print(f"🗂 儲存完整路徑：{os.path.abspath(filepath)}")
            

    else:
        st.error("❌ 無法取得論文資料，請確認 arXiv ID 是否正確。")
