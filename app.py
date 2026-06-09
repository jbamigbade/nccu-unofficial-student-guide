import gradio as gr

from ingest import load_documents, chunk_document
from retriever import embed_and_store, retrieve, get_collection
from generator import generate_response


documents = load_documents()
DOC_COUNT = len(documents)
CHUNK_COUNT = 2095


def run_ingestion():
    collection = get_collection()

    if collection.count() > 0:
        print(
            f"Vector store already populated "
            f"({collection.count()} chunks). Skipping ingestion."
        )
        print("To re-ingest, delete the ./chroma_db folder and restart.")
        return

    print("Ingesting NCCU documents...")

    documents = load_documents()
    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc["text"], doc["source"])
        all_chunks.extend(chunks)

    if all_chunks:
        embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print("No chunks produced. Check your docs folder and ingest.py.")


def chat(message, history):
    if not message.strip():
        return ""

    retrieved = retrieve(message)
    return generate_response(message, retrieved, history)


with gr.Blocks(
    title="Unofficial NCCU Student Guide",
    css="""
    .gradio-container {
        max-width: 1500px !important;
        margin: auto !important;
    }

    #main-chatbot {
        height: 600px !important;
    }

    textarea {
        font-size: 0.95rem !important;
    }
    """
) as demo:

    gr.HTML("""
        <div style="text-align:center; padding:1.25rem 0 0.5rem;">
            <h1 style="font-size:2rem; font-weight:700; color:#6b0f1a; margin:0;">
                🦅 Unofficial NCCU Student Guide
            </h1>

            <p style="color:#6b7280; font-size:1rem; margin:0.4rem 0 0;">
                Ask questions about academics, registration, scholarships, housing,
                tutoring, student life, and AI opportunities at NCCU.
            </p>
        </div>
    """)

    with gr.Row():

        with gr.Column(scale=3):

            gr.ChatInterface(
                fn=chat,

                chatbot=gr.Chatbot(
                    elem_id="main-chatbot",
                    height=600,
                    placeholder="Ask an NCCU question to get started 🦅"
                ),

                textbox=gr.Textbox(
                    placeholder='e.g. "How do I register for classes at NCCU?"',
                    container=False,
                    scale=7,
                ),

                examples=[
                    "What is IAIER?",
                    "Who is Dr. Sung-Sik Kwon?",
                    "How do I change my major?",
                    "How do I contact Academic Advising?",
                    "How do I register for classes at NCCU?",
                    "What scholarships are available at NCCU?",
                    "What tutoring resources are available?",
                    "What does Residential Life provide?",
                    "What student organizations are available?",
                    "How do you select your classes each semester?",
                    "What factors do you consider when choosing classes?",
                    "What resources are available for first-year students?",
                    "Can you tell me about the Mathematics and Physics Department at NCCU?",
                    "What is the most important advice you would give to students taking a course with Dr. Sung-Sik Kwon, and why?",
                    "Can you share your thoughts on the professors, courses, and academic environment in the Mathematics and Physics Department?",
                ],

                cache_examples=False,
            )

        with gr.Column(scale=1, min_width=320):

            gr.HTML(f"""
                <div style="
                    background:#fff7ed;
                    border:1px solid #fed7aa;
                    border-radius:10px;
                    padding:1rem;
                    margin-top:0.5rem;
                ">

                    <p style="
                        font-size:0.8rem;
                        font-weight:700;
                        color:#7f1d1d;
                        margin:0 0 0.75rem;
                        letter-spacing:0.05em;
                    ">
                        📚 NCCU KNOWLEDGE BASE
                    </p>

                    <div style="
                        background:white;
                        border:1px solid #fed7aa;
                        border-radius:8px;
                        padding:0.75rem;
                        margin-bottom:0.75rem;
                    ">
                        <p style="font-size:0.9rem; color:#7c2d12; margin:0 0 0.4rem;">
                            📄 <strong>{DOC_COUNT} NCCU Documents Indexed</strong>
                        </p>

                        <p style="font-size:0.9rem; color:#7c2d12; margin:0;">
                            🔍 <strong>{CHUNK_COUNT} Searchable Knowledge Chunks</strong>
                        </p>
                    </div>

                    <p style="
                        font-size:0.78rem;
                        font-weight:700;
                        color:#7f1d1d;
                        margin:0 0 0.4rem;
                    ">
                        KNOWLEDGE AREAS
                    </p>

                    <ul style="
                        font-size:0.84rem;
                        color:#7c2d12;
                        list-style:none;
                        padding:0;
                        margin:0;
                        line-height:1.8;
                    ">
                        <li>🎓 Academic Programs</li>
                        <li>📝 Registration & Advising</li>
                        <li>🏠 Housing & Residential Life</li>
                        <li>💰 Scholarships & Financial Aid</li>
                        <li>📚 Tutoring & Academic Support</li>
                        <li>🤖 IAIER & AI Resources</li>
                        <li>🏫 Campus Life</li>
                        <li>📌 Student Resource Guides</li>
                        <li>🍽️ Dining & Student Experiences</li>
                        <li>⚖️ University Policies</li>
                    </ul>

                    <hr style="
                        border:none;
                        border-top:1px solid #fed7aa;
                        margin:0.75rem 0;
                    ">

                    <p style="
                        font-size:0.75rem;
                        color:#9a3412;
                        margin:0;
                        line-height:1.5;
                    ">
                        🚀 AI-Powered Student Assistant

                        Built with RAG, ChromaDB, Sentence Transformers, and Groq Llama 3.3.
                    </p>

                </div>
            """)


if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("   Unofficial NCCU Student Guide — Starting Up")
    print("=" * 60 + "\n")

    run_ingestion()

    demo.launch()