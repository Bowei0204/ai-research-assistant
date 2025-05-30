# paper_helper/translator.py
from deep_translator import GoogleTranslator

def translate_text(text, source_lang="en", target_lang="zh-TW"):
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        return f"[翻譯失敗] {e}"
