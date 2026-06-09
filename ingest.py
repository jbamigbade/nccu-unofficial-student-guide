import os
import pdfplumber
from config import DOCS_PATH


def load_pdf(filepath):
    text = ""

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n\n"

    return text


def load_documents():
    """Load .txt and .pdf documents from the docs folder."""
    documents = []

    for filename in sorted(os.listdir(DOCS_PATH)):
        filepath = os.path.join(DOCS_PATH, filename)

        if filename.lower().endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

        elif filename.lower().endswith(".pdf"):
            text = load_pdf(filepath)

        else:
            continue

        if not text.strip():
            continue

        document_name = filename.rsplit(".", 1)[0].replace("_", " ").title()

        documents.append({
            "source": document_name,
            "filename": filename,
            "text": text,
        })

    print(f"Loaded {len(documents)} document(s): {[d['source'] for d in documents]}")
    return documents


def chunk_document(text, source_name):
    chunk_size = 500
    overlap = 100
    min_length = 80

    chunks = []
    prefix = source_name.lower().replace(" ", "_")
    counter = 0
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "source": source_name,
                "chunk_id": f"{prefix}_{counter}",
            })
            counter += 1

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_documents()

    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc["text"], doc["source"])
        all_chunks.extend(chunks)

    print(f"Created {len(all_chunks)} chunks.")

    for chunk in all_chunks[:5]:
        print("\n--- SAMPLE CHUNK ---")
        print(chunk["source"])
        print(chunk["text"][:500])
