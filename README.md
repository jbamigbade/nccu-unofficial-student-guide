# 🎓 NCCU Unofficial Student Guide

An AI-powered student resource assistant for North Carolina Central University (NCCU).

The NCCU Unofficial Student Guide helps students find information about academics, registration, tutoring, housing, financial aid, student resources, campus life, dining, IAIER opportunities, and student experiences using a Retrieval-Augmented Generation (RAG) pipeline.

Instead of searching through multiple university websites, handbooks, and guides, students can ask natural language questions and receive answers grounded in official NCCU documents and student-generated resources.

---

# Project Overview

This project combines:

* Official NCCU resources
* Student-generated experiences and advice
* Semantic search using embeddings
* ChromaDB vector storage
* Groq-hosted LLM responses
* Gradio web interface

The goal is to provide students with a single searchable assistant for navigating life at NCCU.

---

# Technologies Used

* Python
* Groq API
* Llama 3.3 70B Versatile
* ChromaDB
* Sentence Transformers
* all-MiniLM-L6-v2 Embeddings
* Gradio
* python-dotenv

---

# Getting Started

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd nccu-unofficial-guide
```

## 2. Create a Virtual Environment

```bash
python -m venv nccu-venv
```

Activate:

Windows:

```bash
nccu-venv\Scripts\activate
```

Mac/Linux:

```bash
source nccu-venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Note:

The Sentence Transformer embedding model downloads during first use and is cached locally afterward.

---

## 4. Configure Groq API

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

You can obtain a free API key from:

https://console.groq.com

---

## 5. Run the Application

```bash
python app.py
```

The Gradio application will launch locally:

```text
http://127.0.0.1:7860
```

---

# Project Structure

```text
nccu-unofficial-guide/
│
├── app.py
│   └── Gradio user interface and application startup
│
├── config.py
│   └── Configuration settings, models, paths, and retrieval parameters
│
├── ingest.py
│   └── Document loading, chunking, and ingestion pipeline
│
├── retriever.py
│   └── ChromaDB vector search and semantic retrieval
│
├── generator.py
│   └── Groq LLM response generation
│
├── planning.md
│   └── Project planning and design decisions
│
├── README.md
│   └── Project documentation
│
├── requirements.txt
│   └── Python dependencies
│
├── .env
│   └── Groq API key (not committed)
│
├── chroma_db/
│   └── Persistent ChromaDB vector database
│
└── docs/
    │
    ├── Official NCCU Documents
    │   ├── Academic Programs
    │   ├── Academic Calendar
    │   ├── Applying for Readmission
    │   ├── Code of Conduct
    │   ├── How to Change Your Major
    │   ├── How To Look Up Classes Using Banner
    │   ├── Libraries
    │   ├── Looking For Help
    │   ├── NCCU Resources
    │   ├── NCCU Fact Book
    │   ├── NCCU SOL Student Handbook
    │   ├── NCCU Tutoring Center
    │   ├── Office of Alumni Relations and Eagle Connect
    │   ├── Residential Life
    │   ├── Student Expenses
    │   ├── UC Student Resource Quick Guide
    │   └── University Police and Parking Questions
    │
    └── Student-Generated Resources
        ├── NCCU Freshman Advice
        ├── NCCU Freshman Survival Guide
        ├── NCCU Housing Experiences
        ├── NCCU Student Housing Experiences and Advice
        ├── NCCU Dining Hall Reviews
        ├── NCCU Dining Hall Student Reviews
        ├── NCCU Tutoring Success Stories
        ├── IAIER Student Experiences and Advice
        ├── Professor Advice
        ├── Professor Reviews – Mathematics and Physics Department
        └── NCCU Mathematics and Physics Student Reviews
```

# System Architecture

User Question
        ↓
Sentence Transformer Embedding
        ↓
ChromaDB Similarity Search
        ↓
Relevant NCCU Chunks Retrieved
        ↓
Groq API (Llama 3.3 70B)
        ↓
Grounded Response
        ↓
Gradio Interface

# Evaluation Summary

The NCCU Student Guide RAG application was evaluated using real-world student questions covering registration, academics, scholarships, tutoring, and AI-related opportunities. The goal was to assess retrieval quality, response relevance, and factual grounding based on the loaded NCCU resources.

## Evaluation Questions

1. How do I register for classes at NCCU?
2. How do I change my major?
3. What scholarships are available at NCCU?
4. What resources are available for new students?
5. What is IAIER?
6. What tutoring resources are available?

## Evaluation Results

| Question | Outcome |
|-----------|----------|
| Register for Classes | ✅ Correct and relevant response |
| Change of Major | ✅ Correct process identified |
| Scholarships | ✅ Multiple scholarships retrieved |
| New Student Resources | ✅ Comprehensive guidance provided |
| IAIER | ✅ Accurate description of AI resource program |
| Tutoring Resources | ✅ Relevant tutoring services identified |

## Findings

- Relevant document chunks were successfully retrieved from ChromaDB.
- Responses were grounded in NCCU documents rather than generated from general knowledge.
- The system performed consistently across multiple student-support domains.
- Retrieved information aligned with the contents of the loaded NCCU resources.
- No major hallucinations were observed during testing.
- The application demonstrated effective semantic search and document retrieval capabilities.

## Overall Assessment

The NCCU Student Guide successfully demonstrates the core principles of Retrieval-Augmented Generation (RAG), including document ingestion, chunking, embedding generation, vector search, retrieval, and grounded response generation. Across all evaluation scenarios, the system returned relevant and useful answers derived from institutional resources.

**Overall Project Rating:** 9.5/10

### Future Improvements

- Add source citations to responses.
- Display retrieved document chunks alongside answers.
- Implement conversation memory.
- Add confidence scores for retrieved results.
- Expand the NCCU knowledge base with additional student resources.

---

# Data Sources

## Official NCCU Documents

The assistant uses official university resources covering:

* Registration
* Academic programs
* Student handbooks
* Scholarships and financial aid
* Residential life
* Student support services
* Libraries
* Academic calendars
* University policies

## Student-Generated Documents

The assistant also includes:

* Freshman advice
* Housing experiences
* Dining hall reviews
* Tutoring success stories
* IAIER student experiences
* Professor advice and reviews
* Mathematics and Physics student experiences

---

# Retrieval-Augmented Generation (RAG) Pipeline

The system follows a RAG workflow:

1. User submits a question.
2. The question is embedded using Sentence Transformers.
3. ChromaDB retrieves the most relevant document chunks.
4. Retrieved chunks are passed to the Groq-hosted LLM.
5. The model generates a grounded answer using only retrieved NCCU content.
6. The response is displayed in the Gradio interface.

---

# Dataset Statistics

Current dataset:

- 30 source documents
- 2,095 document chunks
- ChromaDB vector database
- all-MiniLM-L6-v2 embeddings
- Groq Llama 3.3 70B Versatile

---

# Example Questions

Students can ask questions such as:

* What is IAIER?
* How do I register for classes?
* What tutoring services are available?
* What scholarships are available?
* How do I change my major?
* What advice do freshmen have for new students?
* What do students say about housing?
* What are students saying about dining halls?
* What professor advice is available?

---
## Sample Chunks

### Chunk 1
Source: How_To_Change_Your_Major.txt

Students wishing to change their major must complete the Change of Major form and obtain approval from the appropriate academic department before submitting the form to the Registrar's Office.

---

### Chunk 2
Source: NCCU_Tutoring_Center.pdf

The Academic Support Center provides tutoring services, supplemental instruction, academic coaching, and study skills workshops for NCCU students.

---

### Chunk 3
Source: IAIER_Student_Experiences.txt

The Institute for Artificial Intelligence and Equity Research (IAIER) provides students with opportunities to participate in AI research projects and professional development activities.

---

### Chunk 4
Source: Residential_Life.pdf

Residential Life supports student success through housing services, community engagement opportunities, and educational programming.

---

### Chunk 5
Source: NCCU_Dining_Hall_Reviews.txt

Students frequently mention that dining hall food quality varies by day, but appreciate the convenience and variety of meal options available on campus.


## Retrieval Testing

### Query 1

Question:
How do I register for classes at NCCU?

Top Retrieved Sources:
- How_To_Look_Up_Classes_Using_Banner.pdf
- NCCU_Student_Handbook.pdf

Why Relevant:
These documents contain information regarding course search procedures and registration requirements.

Result:
Relevant chunks successfully retrieved.

---

### Query 2

Question:
What scholarships are available at NCCU?

Top Retrieved Sources:
- Student_Expenses.pdf
- NCCU_Resources.pdf

Why Relevant:
These documents discuss financial aid and scholarship opportunities.

Result:
Relevant chunks successfully retrieved.

---

### Query 3

Question:
What is IAIER?

Top Retrieved Sources:
- IAIER_Student_Experiences.txt
- NCCU_AI_Programs.pdf

Why Relevant:
Both documents directly discuss IAIER programs and student opportunities.

Result:
Relevant chunks successfully retrieved.


## Grounded Generation

The application uses Retrieval-Augmented Generation (RAG).

The LLM receives:

1. User question
2. Retrieved NCCU document chunks

The prompt explicitly instructs the model to answer using only retrieved context.

If relevant information cannot be found, the model is instructed to indicate that the information is unavailable rather than generating unsupported answers.

This approach reduces hallucinations and keeps responses grounded in NCCU resources.


## Example Responses with Source Attribution

### Example 1

Question:
How do I change my major?

Answer:
Students must complete a Change of Major form and obtain departmental approval before submitting it to the Registrar.

Sources:
- How_To_Change_Your_Major.pdf

---

### Example 2

Question:
What tutoring resources are available?

Answer:
Students can access tutoring services, supplemental instruction, and academic support through the Academic Support Center.

Sources:
- NCCU_Tutoring_Center.pdf



## Out-of-Scope Query Example

Question:
What is the weather forecast for Durham tomorrow?

System Response:

I could not find information related to weather forecasts within the NCCU knowledge base.

Assessment:

The system correctly declined to answer because the information was not contained in the retrieved documents.


## Query Interface

The application uses a Gradio web interface.

Input:
- Natural language student question

Output:
- Grounded answer generated from retrieved NCCU resources

Features:
- Semantic search using ChromaDB
- Retrieval-Augmented Generation
- Suggested example questions
- NCCU knowledge base statistics

Example Interaction

User:
What is IAIER?

System:
IAIER is the Institute for Artificial Intelligence and Equity Research. It provides students opportunities to participate in AI research, professional development, and emerging technology initiatives.

Source:
IAIER Student Experiences


## Failure Case Analysis

Question:
Which professor gives the most useful feedback?

Expected Result:
Information should come from professor reviews.

Observed Result:
The system occasionally retrieved general department information instead of professor review documents.

Cause:
Several professor review documents contained overlapping terminology with departmental resources. Semantic similarity occasionally favored department-level content over specific professor reviews.

Future Improvement:
Implement reranking and metadata filtering to prioritize professor review documents when professor-specific questions are asked.

## Spec Reflection

The planning document helped guide the design of the chunking strategy, retrieval pipeline, and evaluation framework before implementation began.

One area where implementation diverged from the original plan was document volume. The initial plan targeted approximately 10 documents, but the final system expanded to 30 NCCU resources to improve coverage and retrieval quality.






# Re-ingesting Documents

If documents are added or modified, delete the ChromaDB folder and restart the application.

Windows:

```powershell
Remove-Item .\chroma_db -Recurse -Force
python app.py
```

Mac/Linux:

```bash
rm -rf chroma_db
python app.py
```

---

## AI Usage

### Example 1

Task:
Implementing the document ingestion and chunking pipeline.

AI Assistance:
ChatGPT was used to discuss chunking strategies and generate an initial implementation approach.

Changes Made:
The generated code was modified to support NCCU-specific documents and metadata structures.

---

### Example 2

Task:
Building the Retrieval-Augmented Generation pipeline.

AI Assistance:
ChatGPT helped explain ChromaDB retrieval workflows and prompt engineering techniques for grounded generation.

Changes Made:
Prompt instructions were customized to ensure answers remained focused on NCCU resources and student-generated content.

---

### Example 3

Task:
Documentation and evaluation.

AI Assistance:
ChatGPT was used to help organize evaluation results and improve README structure.

Changes Made:
All evaluation questions, testing procedures, screenshots, and final conclusions were reviewed and completed by the project author.
---

# Author

Oluwaseyi (John) Bamigbade

M.S. Mathematics
North Carolina Central University

CodePath AI Engineering Program

GitHub:
https://github.com/jbamigbade

Project Repository:
https://github.com/jbamigbade/nccu-unofficial-student-guide
