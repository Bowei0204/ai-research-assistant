import os
import streamlit as st

NOTES_DIR = os.path.join("output", "paper_notes")

st.set_page_config(page_title="📂 歷史筆記管理", layout="wide")
st.title("📂 歷史筆記管理")

if not os.path.exists(NOTES_DIR):
    st.warning("❌ 尚未產生任何筆記")
else:
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    files.sort(reverse=True)

    if not files:
        st.info("🔍 尚未找到任何筆記檔案。")
    else:
        selected_file = st.selectbox("請選擇要查看的筆記：", files)

        with open(os.path.join(NOTES_DIR, selected_file), "r", encoding="utf-8") as f:
            content = f.read()

        st.markdown("---")
        st.markdown(content)
print("🪵 偵測到筆記檔案：", files)
