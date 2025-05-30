# paper_helper/strengths_and_weakness.py

from google.generativeai import GenerativeModel
import textwrap

model = GenerativeModel("gemini-1.5-flash")  # 可替換其他模型如 gemini-1.5-pro

def analyze_abstract_strengths_and_weaknesses(abstract: str) -> str:
    prompt = textwrap.dedent(f"""
    根據以下英文摘要，請用條列式列出這篇論文的優點（Strengths）與可能的缺點或限制（Weaknesses）。

    ===摘要開始===
    {abstract}
    ===摘要結束===

    請以以下格式回答：

    ## ✅ 優點
    - ...
    - ...

    ## ⚠️ 缺點 / 限制
    - ...
    - ...
    """)

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ 發生錯誤：{e}"
