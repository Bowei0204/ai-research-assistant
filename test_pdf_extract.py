#test_pdf_extract.py
from pdf_tools.downloader import download_arxiv_pdf
from pdf_tools.extractor import extract_sections_from_pdf
from paper_helper.strengths_and_weakness import analyze_abstract_strengths_and_weaknesses

arxiv_id = "2505.17917"
pdf_path = download_arxiv_pdf(arxiv_id)
sections = extract_sections_from_pdf(pdf_path)

abstract = sections.get("Abstract", "")
if abstract:
    result = analyze_abstract_strengths_and_weaknesses(abstract)
    print(result)
else:
    print("❗ 找不到 Abstract 段落")
