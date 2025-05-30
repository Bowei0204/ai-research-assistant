# pdf_tools/downloader.py
import os
import requests

def download_arxiv_pdf(arxiv_id: str, save_dir: str = "pdf_files") -> str:
    os.makedirs(save_dir, exist_ok=True)
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    filepath = os.path.join(save_dir, f"{arxiv_id}.pdf")

    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ PDF 已下載：{filepath}")
        return filepath
    else:
        raise Exception(f"❌ 無法下載 PDF（arXiv ID: {arxiv_id}），狀態碼：{response.status_code}")

