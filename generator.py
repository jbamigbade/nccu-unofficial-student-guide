from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = Groq(api_key=GROQ_API_KEY)


def generate_response(query, retrieved_chunks, history=None):
    """
    Generate a grounded, natural answer from retrieved NCCU document chunks
    with conversational memory.
    """

    if not retrieved_chunks:
        return (
            "I could not find that information in the loaded NCCU documents. "
            "Try rephrasing your question."
        )

    context = "\n\n".join(
        [
            f"Source: {chunk.get('source', chunk.get('game', 'NCCU Document'))}\n"
            f"Content: {chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    conversation_history = ""

    if history:
        for user_msg, assistant_msg in history[-4:]:
            conversation_history += f"Student: {user_msg}\n"
            conversation_history += f"Guide: {assistant_msg}\n\n"

    prompt = f"""
You are the Unofficial NCCU Student Guide.

Answer the student's question using ONLY the NCCU context below.

Important rules:
- Give one clear, natural, student-friendly answer.
- Use the conversation history to understand follow-up questions like "he", "they", "that class", "that office", or "what should I do next?"
- Do NOT list each retrieved chunk separately.
- Do NOT use the word "Game".
- Do NOT use the word "Rule".
- Do NOT mention board games or rule books.
- Do NOT start the answer with "Source:".
- Combine relevant information into a helpful paragraph.
- If useful, mention the source naturally, such as "According to the UC Student Resource Quick Guide..."
- If the answer is not supported by the context, say:
  "I could not find that information in the loaded NCCU documents."

CONVERSATION HISTORY:
{conversation_history}

NCCU CONTEXT:
{context}

CURRENT QUESTION:
{query}

ANSWER:
"""

    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful NCCU student guide. "
                    "Answer only from the provided NCCU context. "
                    "Use conversation history only to understand references, not to invent facts. "
                    "Do not make up information. "
                    "Never use the words Game, Rule, board game, or rule books."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content