# NCCU Student Guide RAG Application – Evaluation Report

## Project Overview
This project is an AI-powered Retrieval-Augmented Generation (RAG) application designed to answer questions about NCCU student resources using institutional documents.

**Technology Stack**
- Python
- Gradio
- ChromaDB
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)
- Groq LLM API

---

# Evaluation Methodology

The application was evaluated using six representative student-support questions.

| Test # | Question |
|----------|----------|
| 1 | How do I register for classes at NCCU? |
| 2 | How do I change my major? |
| 3 | What scholarships are available at NCCU? |
| 4 | What resources are available for new students? |
| 5 | What is IAIER? |
| 6 | What tutoring resources are available? |

---

# Results

## Question 1: Class Registration

**User Question**
> How do I register for classes at NCCU?

### Evaluation
- Relevant answer returned.
- Response references registration timing and advising resources.
- Information is generally useful for incoming students.

### Score
| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 4/5 |
| Completeness | 4/5 |

---

## Question 2: Change of Major

**User Question**
> How do I change my major?

### Evaluation
- System correctly identifies advisor consultation as the first step.
- Provides a high-level process.
- Could be improved by citing specific forms, departments, or links.

### Score

| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 4/5 |
| Completeness | 3/5 |

---

## Question 3: Scholarships

**User Question**
> What scholarships are available at NCCU?

### Evaluation
- Multiple scholarship opportunities were identified.
- Includes institutional and state-supported programs.
- Demonstrates successful retrieval from scholarship documents.

### Score

| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 5/5 |
| Completeness | 4/5 |

---

## Question 4: New Student Resources

**User Question**
> What resources are available for new students?

### Evaluation
- Provides several useful recommendations.
- Mentions tutoring, advising, orientation, student organizations, and campus events.
- Well-rounded answer for first-year students.

### Score

| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 4/5 |
| Completeness | 5/5 |

---

## Question 5: IAIER

**User Question**
> What is IAIER?

### Evaluation
- Correctly describes IAIER as an AI and professional development resource.
- Highlights networking, technical growth, and student engagement.
- Demonstrates retrieval from AI-related NCCU resources.

### Score

| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 5/5 |
| Completeness | 4/5 |

---

## Question 6: Tutoring Resources

**User Question**
> What tutoring resources are available?

### Evaluation
- Correctly identifies tutoring services and academic coaching.
- Includes support services and tutoring success programs.
- Useful and actionable response.

### Score

| Metric | Rating |
|----------|----------|
| Relevance | 5/5 |
| Accuracy | 5/5 |
| Completeness | 4/5 |

---

# Overall Evaluation Summary

| Category | Score |
|----------|----------|
| Average Relevance | 5.0/5 |
| Average Accuracy | 4.5/5 |
| Average Completeness | 4.0/5 |

### Strengths
- Consistently retrieves relevant NCCU information.
- Produces coherent natural-language responses.
- Covers multiple student-support domains.
- Demonstrates successful document grounding.

### Areas for Improvement
- Add source citations in responses.
- Display retrieved document chunks.
- Improve procedural answers with step-by-step instructions.
- Add confidence scores and document references.
- Expand document collection for broader coverage.

---

# Conclusion

The NCCU Student Guide RAG application successfully answers student-focused questions using institution-specific documents. Testing across six representative scenarios demonstrated strong relevance and good factual grounding. The system is suitable as an informational assistant for students and provides a solid foundation for future enhancements such as citation tracking, source transparency, and expanded document coverage.
