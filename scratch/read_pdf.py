import pypdf
import sys

pdf_path = r"C:\Users\Lucas Emanuel\Downloads\Telegram Desktop\02-Fundamentals 1 [@coursesatsale)]\02-Fundamentals 1 [@coursesatsale)]\01-Spacing, Interleaving and Retrieval(@coursesatsale)\1.2-Resource-Interleaving Table - iCanStudy.pdf"

try:
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n---PAGE BREAK---\n"
        
    with open("scratch_pdf_text.txt", "w", encoding="utf-8") as out:
        out.write(text)
    print("Successfully extracted text")
except Exception as e:
    print(f"Error: {e}")
