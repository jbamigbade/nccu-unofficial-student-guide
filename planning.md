# NCCU Unofficial Student Guide – Planning Document

## Project Title

NCCU Unofficial Student Guide

---

## Project Goal

The goal of this project is to build a Retrieval-Augmented Generation (RAG) system that helps students find useful information about North Carolina Central University (NCCU).

Many students rely on both official university resources and advice from other students. Official resources provide policies and procedures, while student experiences provide practical insights about housing, dining, tutoring, professors, and campus life.

This project combines both types of information into a single AI-powered assistant.

---

## Domain

The domain for this project is:

**North Carolina Central University (NCCU) student life, academic success, campus resources, and student experiences.**

The system is designed to answer questions related to:

* Registration
* Academic programs
* Student resources
* Financial aid
* Housing
* Dining
* Tutoring
* Campus life
* IAIER opportunities
* Freshman experiences
* Professor advice

---

## Intended Users

The primary users include:

* Current NCCU students
* Incoming freshmen
* Transfer students
* Prospective students
* Students interested in IAIER opportunities

---

## Dataset Statistics

- Total Documents: 30
- Total Chunks: 2,095
- Embedding Model: all-MiniLM-L6-v2
- Vector Database: ChromaDB
- LLM Provider: Groq
- Model: Llama 3.3 70B Versatile

---

## Data Sources

### Official NCCU Documents

The following official NCCU resources were collected:

1. Academic Programs
2. Applying for Readmission (Undergraduate)
3. UC Student Resource Quick Guide
4. NCCU SOL Student Handbook
5. NCCU Tutoring Center Boosting Student Success
6. How To Look Up Classes Using Banner
7. How To Change Your Major
8. NCCU Code of Conduct
9. Academic Calendar Fall 2025–Summer 2026
10. NCCU Fact Book
11. Libraries
12. Student Expenses
13. Residential Life
14. NCCU Resources
15. Looking for Help
16. University Police and Parking Questions
17. Office of Alumni Relations and Eagle Connect

### Student-Generated Documents

The following unofficial resources were created to capture student experiences:

1. NCCU Freshman Advice
2. NCCU Freshman Survival Guide
3. NCCU Housing Experiences
4. NCCU Student Housing Experiences and Advice
5. NCCU Dining Hall Reviews
6. NCCU Dining Hall Student Reviews
7. NCCU Tutoring Success Stories
8. IAIER Student Experiences and Advice
9. Professor Advice
10. Professor Reviews – Mathematics and Physics Department
11. NCCU Mathematics and Physics Student Reviews

---

## Why These Documents Were Selected

These documents provide both:

### Official Knowledge

Examples:

* Registration procedures
* Academic policies
* Housing information
* Financial aid information
* Student support services

### Student Knowledge

Examples:

* Housing experiences
* Dining hall reviews
* Tutoring experiences
* Freshman advice
* Professor recommendations
* IAIER experiences

This combination helps create a more realistic student-focused assistant.

---

## Chunking Strategy

Documents were split into smaller chunks before being embedded and stored in ChromaDB.

A total of 2,076 chunks were generated from the 28 NCCU source documents.

Reasons:

- Improves retrieval accuracy
- Allows retrieval of specific information
- Reduces irrelevant context
- Improves answer quality

Instead of retrieving entire documents, the system retrieves the most relevant chunks related to a user's question.

---

## Embedding Model

Embedding Model:

all-MiniLM-L6-v2

Reasons for selection:

* Lightweight
* Fast
* Good semantic search performance
* Works well with ChromaDB

The model converts text into vector embeddings used for similarity search.

---

## Vector Database

The project uses:

ChromaDB

ChromaDB stores:

* Embedded document chunks
* Chunk metadata
* Source information

This enables efficient retrieval of relevant content.

## Retrieval Strategy

When a question is submitted:

1. User enters a question.
2. The question is converted into an embedding.
3. ChromaDB performs similarity search.
4. The most relevant chunks are retrieved.
5. Retrieved chunks are passed to the Groq LLM.
6. The model generates a grounded response using retrieved context.

---

## System Architecture

```text
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
```

## LLM Used

Provider:

Groq

Model:

Llama-3.3-70B-Versatile

Reasons:

* Fast inference speed
* Strong reasoning ability
* Good performance for RAG applications

---

## Evaluation Plan

The system will be evaluated using representative student questions.

Example questions:

1. What is IAIER?
2. How do I register for classes?
3. What tutoring services are available?
4. What housing advice do students provide?
5. What freshman advice is available?
6. What do students say about mathematics professors?
7. What dining hall options are most popular?

For each question, results will be evaluated based on:

* Retrieval relevance
* Answer accuracy
* Grounding in documents
* Clarity of response

---
## Evaluation Results

The system was tested using representative NCCU student questions.

Questions tested:

1. What is IAIER?
2. How do I register for classes?
3. What tutoring services are available?
4. What housing advice do students provide?
5. What freshman advice is available?

Results:

- 5/5 questions successfully answered using retrieved NCCU documents.
- Responses were grounded in both official and student-generated resources.
- Retrieval quality was strongest for academic resources, student advice, and IAIER-related questions.

Evaluation Outcome:

The chatbot successfully answered both official NCCU information questions and student-experience questions, demonstrating effective retrieval across multiple document categories.
---

## Potential Challenges

### Retrieval Quality

Some questions may retrieve irrelevant chunks.

### Limited Student Data

Student-generated content is limited to the collected documents.

### Hallucination Risk

The language model may occasionally attempt to generate information not contained in retrieved documents.

### Document Diversity

Official documents and student-generated documents have different writing styles and levels of detail.

---

## Success Criteria

The project will be considered successful if:

* Students can ask natural language questions.
* Relevant NCCU information is retrieved.
* Responses remain grounded in source documents.
* The system accurately answers academic and student-life questions.
* Both official and student-generated knowledge are represented.

---

## Future Improvements

Future versions may include:

* Additional professor reviews
* Student club experiences
* Internship experiences
* Campus event information
* Source citations in responses
* Public deployment for NCCU students

---

## AI Usage

ChatGPT was used to assist with:

* Brainstorming
* Planning
* Documentation
* Debugging support
* Evaluation design

All implementation decisions, testing, and final project integration were completed by the project author.
