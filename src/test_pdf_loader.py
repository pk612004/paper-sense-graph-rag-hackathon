from pdf_loader import load_all_pdfs

pdf_dir = "../data" 
texts = load_all_pdfs(pdf_dir)

for filename, text in texts.items():
    print(f"\n📄 {filename}:\n{'-'*40}\n{text[:1000]}...") 
